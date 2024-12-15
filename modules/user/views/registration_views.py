from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response

from core.error_messages import AuthenticationErrors
from core.exception import ClientException, ServerException
from modules.user.serializers import RegistrationSerializer, ConfirmRegistrationSerializer

User = get_user_model()

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def register_step_1(request: Request):
    data = RegistrationSerializer(data=request.data)
    if not data.is_valid():
        raise ClientException(data.errors)
    data.save()
    return Response(data.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def register_step_2(request: Request):
    """Этап подтверждения почты при регистрации

    Ошибка возникает в случае, если клиент не был найден по причине истёкшего срока жизни токена
    """
    code = request.data.get("code")
    id_from_request = request.data.get("id")
    candidates = User.objects.filter(code_email=code, id=id_from_request)
    if len(candidates) == 1:
        user = candidates[0]
        serializer = ConfirmRegistrationSerializer(
            user, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ServerException()
        serializer.save()
        return Response(status=204)
    raise ClientException(AuthenticationErrors.EMAIL_TOKEN_LIFETIME_ENDED_NEED_REPEAT_REGISTRATION,
                          status.HTTP_400_BAD_REQUEST)