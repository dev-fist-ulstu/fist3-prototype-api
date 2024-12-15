import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.email import send_email_template
from core.exception import ServerException
from core.utils.esia import generate_code_confirmation


class PasswordChangeSerializer(serializers.Serializer):
    email = serializers.CharField()

    def create(self, validated_data):
        raise ServerException()

    def update(self, instance, validated_data):
        code = generate_code_confirmation()
        instance.code_password = code
        instance.code_password_dt = datetime.datetime.utcnow()
        instance.save()
        send_email_template(
            [validated_data.get("email")],
            "Восстановление пароля",
            "password_forgot.html",
            {"code": code}
        )
        return instance


class ConfirmPasswordChangeSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        raise ServerException()

    def update(self, instance, validated_data):
        instance.code_password = None
        instance.code_password_dt = None
        instance.password = make_password(validated_data.get("password"))
        instance.save()
        return instance