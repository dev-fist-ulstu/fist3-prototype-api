from django.contrib.auth.hashers import check_password
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response

from core.exception import ClientException, ServerException
from core.security.jwt import generate_jwt_pair, decode_jwt
from core.utils.esia import get_refresh_dict
from core.error_messages import AuthenticationErrors
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from ..models import UserCustom as User, AccessTokens, RefreshTokens
from ..serializers import AuthResponseSerializer, ConfirmPasswordChangeSerializer, PasswordChangeSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def authorize(request: Request):
    data = request.data
    try:
        candidate = User.objects.get(username=data.get(
            "username"), is_confirmed_email=True)
    except Exception as e:
        raise ClientException(AuthenticationErrors.USER_NOT_FOUND_OR_PASSWORD_INVALID,
                              status.HTTP_400_BAD_REQUEST)
    if check_password(data.get("password"), candidate.password):
        pair = generate_jwt_pair(candidate)
        response_data = {
            "access": pair.access.token,
            "user": candidate
        }
        response_cookie = get_refresh_dict(pair.refresh.token)
        response = Response(AuthResponseSerializer(response_data).data,
                            status=status.HTTP_200_OK)
        response.set_cookie(**response_cookie)
        return response
    raise ClientException(AuthenticationErrors.USER_NOT_FOUND_OR_PASSWORD_INVALID,
                          status.HTTP_400_BAD_REQUEST)
