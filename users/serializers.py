from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password', 'avatar')