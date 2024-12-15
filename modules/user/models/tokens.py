from django.db import models

from modules.user.models.user import UserCustom


class AccessTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)

    class Meta:
        db_table = "session\".\"access_tokens"


class RefreshTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)
    access = models.OneToOneField(AccessTokens, on_delete=models.CASCADE)

    class Meta:
        db_table = "session\".\"refresh_tokens"
