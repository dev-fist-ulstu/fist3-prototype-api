from django.db import models

from modules.user.models.abstract_model import BaseUserInformation


class UserAccessRecovery(BaseUserInformation):
    code_password = models.CharField(max_length=1024, verbose_name="Токен для замены пароля",
                                     null=True, blank=True, default=None)
    code_password_valid_to_dt = models.DateTimeField(verbose_name="Действителен до",
                                                     null=True, blank=True)

    class Meta:
        db_table = "user\".\"access_recovery"
