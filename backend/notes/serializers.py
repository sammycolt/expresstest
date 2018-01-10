from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


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
    # id = serializers.Field(source='user.id')
    # username = serializers.CharField(source='user.username')
    # email = serializers.CharField(source='user.email')
    # password = serializers.CharField(source='user.password')
    type = serializers.CharField(source='universityuser.type')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'type')

    # def create(self, attrs):
    #     user = User.objects.create_user(username=attrs['user']['username'], email=attrs['user']['email'],
    #                                     password=attrs['user']['password'])
    #     return UniversityUser(user=user, type=attrs['type'])

    # def restore_object(self, attrs, instance=None):
    #     """
    #     Given a dictionary of deserialized field values, either update
    #     an existing model instance, or create a new model instance.
    #     """
    #     if instance is not None:
    #         instance.user.email = attrs.get('user.email', instance.user.email)
    #         instance.ban_status = attrs.get('ban_status', instance.ban_status)
    #         instance.user.password = attrs.get('user.password', instance.user.password)
    #         return instance
    #
    #     user = User.objects.create_user(username=attrs.get('user.username'), email=attrs.get('user.email'),
    #                                     password=attrs.get('user.password'))
    #     return UniversityUser(user=user)
