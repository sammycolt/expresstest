from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import JWTSerializer


from .models import Note, UniversityUser, User, QuizTest, \
    QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz, \
    AnswerByUser


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
    answers = QuizAnswerSerializer(many=True, read_only=True)
    class Meta:
        model = QuizQuestion
        fields = ('id', 'quiz', 'text', 'answers')

class QuizTestSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(many=True, read_only=True)
    readers = UserSerializer(many=True, read_only=True)
    class Meta:
        model = QuizTest
        fields = ('id', 'title', 'author', 'questions', 'readers')

class QuizAnswerStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAnswer
        fields = ('id', 'answer_text')


class QuizQuestionStudentSerializer(serializers.ModelSerializer):
    answers = QuizAnswerStudentSerializer(many=True, read_only=True)
    class Meta:
        model = QuizQuestion
        fields = ('id', 'quiz', 'text', 'answers')

class QuizTestStudentSerializer(serializers.ModelSerializer):
    questions = QuizQuestionStudentSerializer(many=True, read_only=True)
    readers = UserSerializer(many=True, read_only=True)
    class Meta:
        model = QuizTest
        fields = ('id', 'title', 'author', 'questions', 'readers')

class AnswerToQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerToQuestion
        fields = ('answer', 'question')


class UserToQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToQuiz
        fields = ('quiz', 'user')


class AnswerByUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerByUser
        fields = ('answer', 'user')

def jwt_token_payload_handler(token, user, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


