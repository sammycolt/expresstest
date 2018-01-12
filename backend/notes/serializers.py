from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import JWTSerializer


from .models import Note, UniversityUser, User, USER_CHOICES


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


def jwt_token_payload_handler(user, request=None):
    return {
        'user': UserSerializer(user, context={'request': request}).data
    }


