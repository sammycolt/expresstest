from django.db.models import QuerySet
from rest_framework import viewsets, generics

from .models import Note, User, QuizTest, QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz, AnswerByUser, \
    QuizResults, QuestionToResult
from .enums import UniUser
from .serializers import NoteSerializer, UserSerializer, QuizTestSerializer,\
    QuizQuestionSerializer, QuizAnswerSerializer, AnswerToQuestionSerializer, \
    UserToQuizSerializer, QuizQuestionStudentSerializer, QuizTestStudentSerializer, \
    AnswerByUserSerializer, QuizResultsSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('universityuser')
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all().select_related('universityuser')
    serializer_class = UserSerializer

class QuizTestViewSet(viewsets.ModelViewSet):
    queryset = QuizTest.objects.all()
    serializer_class = QuizTestSerializer

    def get_serializer_class(self):
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return QuizTestSerializer
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            return QuizTestStudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return queryset.filter(author_id=self.request.user.id)
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            return queryset.filter(readers__id=self.request.user.id)

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('universityuser').filter(universityuser__type=UniUser.STUDENT.value)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return queryset

class QuizTestDetails(generics.RetrieveAPIView):
    queryset = QuizTest.objects.all()

    def get_serializer_class(self):
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return QuizTestSerializer
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            return QuizTestStudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return queryset.filter(author_id=self.request.user.id)
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            return queryset.filter(readers__id=self.request.user.id)

class QuizAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

    # def get_serializer_class(self):
    #     if self.request.user.universityuser.type == UniUser.TEACHER.value:
    #         return QuizQuestionSerializer
    #     elif self.request.user.universityuser.type == UniUser.STUDENT.value:
    #         return QuizQuestionStudentSerializer

class QuizQuestionDetails(generics.RetrieveAPIView):
    queryset = QuizQuestion.objects.all()

    def get_serializer_class(self):
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            return QuizQuestionSerializer
        elif self.request.user.universityuser.type == UniUser.STUDENT.value:
            return QuizQuestionStudentSerializer

class AnswerToQauestionVS(viewsets.ModelViewSet):
    queryset = AnswerToQuestion.objects.all()
    serializer_class = AnswerToQuestionSerializer

class UserToQuizVS(viewsets.ModelViewSet):
    queryset = UserToQuiz.objects.all()
    serializer_class = UserToQuizSerializer

class AnswerByUserViewSet(viewsets.ModelViewSet):
    queryset = AnswerByUser.objects.all()
    serializer_class = AnswerByUserSerializer

    def create(self, request, *args, **kwargs):
        resp = super().create(request, *args, **kwargs)
        answer = resp.data['answer']
        user = resp.data['user']
        # print(resp.data)
        abu = AnswerByUser.objects.filter(answer_id=answer, user_id=user)[0]
        resp.data['id'] = abu.id
        # print(abu.answer.questions.filter(answer_id=answer)[0].question.id)
        resp.data['question'] = abu.answer.questions.filter(answer_id=answer)[0].question.id
        # print(abu.answer.questions.all()[0].id)
        return resp

    def destroy(self, request, *args, **kwargs):
        id = kwargs['pk']
        abu = AnswerByUser.objects.get(id=id)
        # print(abu.answer, abu.user)
        question = abu.answer.questions.filter(answer_id=abu.answer)[0].question
        quiz = question.quiz
        user = abu.user
        results = QuizResults.objects.filter(user_id=user.id, quiz_id=quiz.id)

        if abu.answer.is_correct:
            if results.count():
                result = results[0]
                if question in result.correct_questions.all():
                    QuestionToResult.objects.filter(question_id=question.id, result_id=result.id).delete()
                    result.total_score -= question.score
                    result.save()
        else:
            print('Kek')
        return super().destroy(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.universityuser.type == UniUser.TEACHER.value:
    #         return queryset.filter(answer__question__quiz__author_id=self.request.user.id)
    #     elif self.request.user.universityuser.type == UniUser.STUDENT.value:
    #         return queryset.filter(user_id=self.request.user.id)


class UserQuizResultsViewSet(viewsets.ModelViewSet):
    queryset = QuizResults.objects.all()
    serializer_class = QuizResultsSerializer