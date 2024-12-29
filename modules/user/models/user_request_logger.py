from django.contrib.auth import get_user_model
from django.db import models
from modules.user.models.abstract_model import BaseUserInformation

User = get_user_model()

class UserRequestLogger(BaseUserInformation):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "user\".\"request_logs"