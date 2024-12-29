from django.contrib.auth import get_user_model
from django.db import models
from modules.user.models.abstract_model import BaseUserInformation

User = get_user_model()

class RegistrationInformation(BaseUserInformation):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code_email = models.TextField(verbose_name="Токен для подтверждения", null=True, blank=True, default=None)
    code_email_valid_to_dt = models.DateTimeField(verbose_name="Действителен до", null=True, blank=True)

    class Meta:
        db_table = "user\".\"registration_information"