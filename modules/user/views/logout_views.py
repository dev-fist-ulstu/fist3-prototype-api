from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response

from core.utils.esia import get_refresh_dict
from modules.user.models import AccessTokens

@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def logout(request: Request):
    AccessTokens.objects.get(token=request.auth.token).delete()
    response = Response(status=status.HTTP_204_NO_CONTENT)
    response.set_cookie(**get_refresh_dict())
    return response


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def logout_all(request: Request):
    AccessTokens.objects.filter(user_id=request.user.id).delete()
    response = Response(status=status.HTTP_204_NO_CONTENT)
    response.set_cookie(**get_refresh_dict())
    return response