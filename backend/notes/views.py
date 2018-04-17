from rest_framework import viewsets, generics

from .models import Note, User, QuizTest, QuizAnswer, QuizQuestion, AnswerToQuestion, UserToQuiz
from .enums import UniUser
from .serializers import NoteSerializer, UserSerializer, QuizTestSerializer,\
    QuizQuestionSerializer, QuizAnswerSerializer, AnswerToQuestionSerializer, \
    UserToQuizSerializer


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

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.universityuser.type == UniUser.TEACHER.value:
            print(self.request.user.universityuser.type)
            return queryset.filter(author_id=self.request.user.id)

class QuizTestDetails(generics.RetrieveAPIView):
    queryset = QuizTest.objects.all()
    serializer_class = QuizTestSerializer

class QuizAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer

class QuizQuestionViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

class QuizQuestionDetails(generics.RetrieveAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

class AnswerToQauestionVS(viewsets.ModelViewSet):
    queryset = AnswerToQuestion.objects.all()
    serializer_class = AnswerToQuestionSerializer

class UserToQuizVS(viewsets.ModelViewSet):
    queryset = UserToQuiz.objects.all()
    serializer_class = UserToQuizSerializer