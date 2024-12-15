from django.db import models


class Role(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=32)
    permission_level = models.IntegerField(verbose_name="Уровень доступа")
    role_description = models.TextField(verbose_name="Описание роли", null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "user\".\"roles"
        ordering = ["permission_level"]
