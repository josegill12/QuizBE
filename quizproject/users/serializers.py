from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models
from rest_framework import serializers, viewsets

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username')
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'email')
        exclude = ('password')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email')
        exclude = ('password')


class UserProfileviewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserProfileSerializer
    exclude = ('password')
   