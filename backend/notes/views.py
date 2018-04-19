from django.db.models import QuerySet
from rest_framework import viewsets, generics

from .models import Note, User, QuizTest, QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz, AnswerByUser, QuizResults
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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.universityuser.type == UniUser.TEACHER.value:
    #         return queryset.filter(answer__question__quiz__author_id=self.request.user.id)
    #     elif self.request.user.universityuser.type == UniUser.STUDENT.value:
    #         return queryset.filter(user_id=self.request.user.id)

class UserQuizResultsViewSet(viewsets.ModelViewSet):
    queryset = QuizResults.objects.all()
    serializer_class = QuizResultsSerializer