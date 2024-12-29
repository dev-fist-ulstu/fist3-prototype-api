import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.business_logic_layer.email import send_email_template
from core.direct_sql_worker.server_time import get_server_time_now
from core.utils.esia import generate_code_confirmation
from ..models import Role, RegistrationInformation

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name", "middle_name"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.role = Role.objects.get(name="USER")
        code_for_email_send = generate_code_confirmation()
        code_valid_dt = get_server_time_now() + datetime.timedelta(minutes=15)
        user.save()
        registration_info = RegistrationInformation.objects.create(user=user,
                                                                   code_email=code_for_email_send,
                                                                   code_email_valid_to_dt=code_valid_dt)
        registration_info.save()
        # send_email_template([user.email],
        #                     "Подтверждение адреса электронной почты",
        #                     "confirm-registration.html",
        #                     {"code": code_for_email_send})
        return user

    def to_representation(self, instance):
        data = super(RegistrationSerializer, self).to_representation(instance)
        data.pop("password")
        return data

class ConfirmRegistrationSerializer(serializers.Serializer):
    code_email = serializers.CharField(required=True)
    id = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        instance.is_active = True
        instance.is_confirmed_email = True
        instance.save()
        registration_info = RegistrationInformation.objects.get(user_id=instance.id)
        registration_info.code_email = None
        registration_info.code_email_valid_to_dt = None
        registration_info.save()
        return instance