from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import JWTSerializer


from .models import Note, UniversityUser, User, QuizTest, \
    QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz, \
    AnswerByUser, QuizResults, QuestionToResult


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
        fields = ('id', 'quiz', 'text', 'answers', 'score')

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
        fields = ('quiz', 'user', 'id')

    def save(self, **kwargs):
        user = self.validated_data['user']
        quiz = self.validated_data['quiz']

        users_to_quiz = UserToQuiz.objects.filter(user_id=user.id, quiz_id=quiz.id)
        if users_to_quiz.count():
            user_to_quiz = users_to_quiz[0]
        else:
            user_to_quiz = super().save(**kwargs)

        return user_to_quiz


class AnswerByUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerByUser
        fields = ('answer', 'user', 'id')


    def save(self, **kwargs):
        answer = self.validated_data['answer']
        user = self.validated_data['user']

        answers_by_user = AnswerByUser.objects.filter(answer_id=answer.id).filter(user_id=user.id)
        if answers_by_user.count():
            abu = answers_by_user[0]
        else:
            abu = super().save(**kwargs)


        question = abu.answer.questions.all()[0].question
        quiz = question.quiz
        quiz_results = QuizResults.objects.filter(quiz_id=quiz.id).filter(user_id=abu.user.id)

        answers_on_this_question_by_user = AnswerByUser.objects.filter(user_id=user.id). \
            filter(answer__questions__question_id=question.id)

        correct_answers_on_this_question_by_user = answers_on_this_question_by_user.filter(answer__is_correct=True)
        correct_answers_on_this_question = QuizQuestion.objects.filter(id=question.id). \
            filter(answers__is_correct=True)
        # for elem in correct_answers_on_this_question_by_user.all():
        #     print(elem)
        # print('Correct answers by user: ', correct_answers_on_this_question_by_user.count())

        if (quiz_results.count()):
            quiz_result = quiz_results[0]
            if answers_on_this_question_by_user.count() == correct_answers_on_this_question_by_user.count():
                if correct_answers_on_this_question_by_user.count() == correct_answers_on_this_question.count():
                    # print("!!1")
                    if question not in quiz_result.correct_questions.all():
                        ans_to_res = QuestionToResult(question=question, result=quiz_result)
                        ans_to_res.save()
                        quiz_result.total_score += question.score
                        quiz_result.save()
                else:
                    if question in quiz_result.correct_questions.all() :
                        QuestionToResult.objects.filter(result=quiz_result.id, question=question.id).delete()
                        quiz_result.total_score -= question.score
                        quiz_result.save()
            else:
                if question in quiz_result.correct_questions.all():
                    QuestionToResult.objects.filter(result=quiz_result.id, question=question.id).delete()
                    quiz_result.total_score -= question.score
                    quiz_result.save()
        else:
            score = 0
            if answers_on_this_question_by_user.count() == correct_answers_on_this_question_by_user.count():
                if correct_answers_on_this_question_by_user.count() == correct_answers_on_this_question.count():
                    score = question.score
                new_result = QuizResults(user=abu.user, quiz=quiz, total_score=score)
                new_result.save()
                if correct_answers_on_this_question_by_user.count() == correct_answers_on_this_question.count():
                    ans_to_res = QuestionToResult(question=question, result=new_result)
                    ans_to_res.save()

        return abu


class QuizResultsSerializer(serializers.ModelSerializer):
    correct_questions = QuizQuestionStudentSerializer(many=True, read_only=True)

    class Meta:
        model = QuizResults
        fields = ('id', 'user', 'quiz', 'correct_questions', 'total_score')



def jwt_token_payload_handler(token, user, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


