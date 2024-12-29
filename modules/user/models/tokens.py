from django.db import models

from core.direct_sql_worker.server_time import get_server_time_now
from modules.user.models.user import UserCustom


class AccessTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)
    token_created_dt = models.DateTimeField(default=get_server_time_now)

    class Meta:
        db_table = "session\".\"access_tokens"


class RefreshTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)
    access = models.OneToOneField(AccessTokens, on_delete=models.CASCADE)
    token_created_dt = models.DateTimeField(default=get_server_time_now)

    class Meta:
        db_table = "session\".\"refresh_tokens"
