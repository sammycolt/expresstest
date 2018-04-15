from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import JWTSerializer


from .models import Note, UniversityUser, User, QuizTest, QuizAnswer, QuizQuestion, AnswerToQuestion


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'created_at')


class UserRegSer(RegisterSerializer):
    type = serializers.CharField(source='UniversityUser.type')

    class Meta:
        model = UniversityUser
        fields = ('id', 'username', 'email', 'password', 'type')

    def save(self, request):
        user_type = request.data['type']
        user = super().save(request)
        uni_user = UniversityUser(user=user, type=user_type)
        uni_user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='universityuser.type')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'type')

class QuizAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAnswer
        fields = ('id', 'answer_text', 'is_correct')

class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True)
    class Meta:
        model = QuizQuestion
        fields = ('id', 'quiz', 'text', 'answers')

class QuizTestSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(many=True)
    class Meta:
        model = QuizTest
        fields = ('id', 'title', 'author', 'questions')

class AnswerToQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerToQuestion
        fields = ('answer', 'question')



def jwt_token_payload_handler(user, request=None):
    return {
        'user': UserSerializer(user, context={'request': request}).data
    }


