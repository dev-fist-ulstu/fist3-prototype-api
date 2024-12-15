from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response

from core.exception import ClientException, ServerException
from modules.user.serializers import PasswordChangeSerializer, ConfirmPasswordChangeSerializer

User = get_user_model()

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def restore_password_step1(request: Request):
    serializer = PasswordChangeSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    candidates = User.objects.filter(
        email=serializer.validated_data.get("email"))
    if len(candidates) == 1:
        serializer.instance = candidates[0]
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    raise ServerException()


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def restore_password_step2(request: Request):
    serializer = ConfirmPasswordChangeSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    candidates = User.objects.filter(
        token_password_change=serializer.validated_data.get("token"))
    if len(candidates) == 1:
        serializer.instance = candidates[0]
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    raise ServerException()