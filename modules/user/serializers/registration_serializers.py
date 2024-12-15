import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.email import send_email_template
from core.utils.esia import generate_code_confirmation
from ..models import Role

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        role = Role.objects.get(name="USER")
        user.role = role
        code = generate_code_confirmation()
        user.code_email = code
        user.code_email_dt = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=15)
        user.save()
        send_email_template([user.email],
                            "Подтверждение адреса электронной почты",
                            "confirm-registration.html",
                            {"code": code})
        return user

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name", "middle_name"]

class ConfirmRegistrationSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.code_email = None
        instance.code_email_dt = None
        instance.is_active = True
        instance.is_confirmed_email = True
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ["code_email", "email"]