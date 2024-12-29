import random

from django.conf import settings

from django.contrib.auth.hashers import check_password
from rest_framework.request import Request

from core.direct_sql_worker.server_time import get_server_time_now


def get_refresh_dict(value: str = ""):
    return {
        "key": "refresh",
        "value": value,
        "httponly": True,
        "expires": settings.JWT_REFRESH_LIFETIME + get_server_time_now(),
        "samesite": "Lax"
    }


def check_password_by_request(request: Request) -> bool:
    password = request.data.get("checkPassword")
    return password and check_password(password, request.user.password)


def generate_code_confirmation() -> str:
    code_length = 6
    digit = str(random.randint(0, 999999))
    if len(digit) < code_length:
        lead_zeros = (code_length - len(digit)) * "0"
        digit = lead_zeros + digit
    return digit
