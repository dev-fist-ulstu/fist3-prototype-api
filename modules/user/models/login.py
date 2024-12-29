from django.contrib.auth import get_user_model
from django.db import models

from core.constants import InformationPresentationTypes
from core.direct_sql_worker.server_time import get_server_time_now
from modules.user.models import AccessTokens, RefreshTokens
from modules.user.models.abstract_model import BaseUserInformation

User = get_user_model()

class UserLoginInformation(BaseUserInformation):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_success_login = models.BooleanField(default=True)
    login_attempt_counter = models.IntegerField(default=1, blank=True, null=True)
    logged_in_dt = models.DateTimeField(default=get_server_time_now)
    user_time_zone = models.TextField(blank=True, null=True)
    generated_access_token = models.ForeignKey(AccessTokens, on_delete=models.SET_NULL, blank=True, null=True)
    generated_refresh_token = models.ForeignKey(RefreshTokens, on_delete=models.SET_NULL, blank=True, null=True)
    is_active_session = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']
        db_table = "session\".\"login_information"