from django.contrib.auth import get_user_model
from rest_framework import serializers
from .user_serializers import UserSerializer

User = get_user_model()


class AuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class AuthResponseSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=2048)
    user = UserSerializer()