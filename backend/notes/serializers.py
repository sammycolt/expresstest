from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import JWTSerializer


from .models import Note, UniversityUser, User, QuizTest, \
    QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz, \
    AnswerByUser, QuizResults, AnswerToResult


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
        fields = ('id', 'quiz', 'text', 'answers', 'score')

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

    def save(self, **kwargs):
        abu = super().save(**kwargs)
        question = abu.answer.questions.all()[0].question
        quiz = question.quiz
        # print(abu.answer.questions.all()[0].question.quiz.id)
        # print(dir(abu.answer.quizquestion_set))
        quiz_results = QuizResults.objects.filter(quiz_id=quiz.id).filter(user_id=abu.user.id)
        if (quiz_results.count()):
            quiz_result = quiz_results[0]
            if abu.answer not in quiz_result.correct_answers.all():
                ans_to_res = AnswerToResult(answer=abu.answer, result=quiz_result)
                ans_to_res.save()
                quiz_result.total_score += question.score
                quiz_result.save()
        else:
            score = 0
            if abu.answer.is_correct:
                score = question.score
            new_result = QuizResults(user=abu.user, quiz=quiz, total_score=score)
            new_result.save()
            if abu.answer.is_correct:
                ans_to_res = AnswerToResult(answer=abu.answer, result=new_result)
                ans_to_res.save()
        return abu

class QuizResultsSerializer(serializers.ModelSerializer):
    correct_answers = QuizAnswerStudentSerializer(many=True, read_only=True)

    class Meta:
        model = QuizResults
        fields = ('user', 'quiz', 'correct_answers', 'total_score')



def jwt_token_payload_handler(token, user, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


