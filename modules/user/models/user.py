from django.contrib.auth.models import AbstractUser
from django.db import models

from core.business_logic_layer.filemanager.path_saver import user_image_upload_to
from modules.user.models.roles import Role


class UserCustom(AbstractUser):
    middle_name = models.CharField(max_length=32, verbose_name="Отчество", 
                                   default=None, blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", unique=True)
    is_confirmed_email = models.BooleanField(default=False, verbose_name="Почта подтверждена")
    image = models.ImageField(upload_to=user_image_upload_to, verbose_name="Аватар", 
                              blank=True, null=True, default="not-found.png")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", 
                             blank=True, null=True, default="Не указано")
    gender = models.CharField(max_length=6, default=None, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, default=None)

    REQUIRED_FIELDS = ["password", "email"]
    USERNAME_FIELD = "username"

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "user\".\"users"

    def save(self, *args, **kwargs):
        if self.pk is None:
            avatar = self.image
            self.avatar = None
            super().save(*args, **kwargs)
            self.avatar = avatar
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class UserAdditionalData(models.Model):
    user_id = models.OneToOneField(UserCustom, on_delete=models.CASCADE, primary_key=True)
    is_end_bachelor_degree = models.BooleanField(default=False)
    is_end_master_degree = models.BooleanField(default=False)
    is_end_specialist_degree = models.BooleanField(default=False)
    is_end_postgraduate_degree = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)

    class Meta:
        ordering = ["user_id"]
        verbose_name = "Дополнительные данные пользователя"
        verbose_name_plural = "Дополнительные данные пользователей"
        db_table = "user\".\"user_additional_data"

    def __str__(self):
        return self.user_id.username

class UserEducationInfo(models.Model):
    user_id = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    started_date = models.DateField(null=True, default=None)
    ended_date = models.DateField(null=True, default=None)
    education_name = models.CharField(max_length=500, blank=True, null=True, default=None)
    education_information = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "user\".\"education_information"


