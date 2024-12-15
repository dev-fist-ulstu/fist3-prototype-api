from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response

from core.error_messages import AuthenticationErrors
from core.exception import ClientException
from core.security.jwt import decode_jwt, generate_jwt_pair
from core.utils.esia import get_refresh_dict
from modules.user.models import RefreshTokens, AccessTokens


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def get_new_token_pair(request: Request):
    token = request.COOKIES.get("refresh")
    if token is None or token == '':
        raise ClientException(AuthenticationErrors.NEED_RESIGN_IN_APP,
                              status.HTTP_400_BAD_REQUEST)
    decoded_token = decode_jwt(token)
    if not decoded_token.is_valid:
        raise ClientException(AuthenticationErrors.NEED_RESIGN_IN_APP,
                              status.HTTP_401_UNAUTHORIZED)
    refresh_model = RefreshTokens.objects.get(token=decoded_token.token)
    new_pair = generate_jwt_pair(refresh_model.user)
    AccessTokens.objects.get(token=refresh_model.access.token).delete()
    response = Response({"access": new_pair.access.token},
                        status=status.HTTP_200_OK)
    response.set_cookie(**get_refresh_dict(new_pair.refresh.token))
    return response