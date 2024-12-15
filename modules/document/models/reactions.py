from django.contrib.auth import get_user_model
from django.db import models

from modules.document.models.document import Document

User = get_user_model()


class DocumentLikes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    documents = models.ManyToManyField(Document, related_name="likes")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "document\".\"likes"


class DocumentDislikes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    documents = models.ManyToManyField(Document, related_name="dislikes")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "document\".\"dislikes"