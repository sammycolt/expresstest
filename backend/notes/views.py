from rest_framework import viewsets

from .models import Note, User
from .serializers import NoteSerializer, UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('universityuser')
    serializer_class = UserSerializer
