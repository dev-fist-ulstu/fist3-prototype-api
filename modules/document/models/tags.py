from django.db import models

from modules.document.models.document import Document


class DocumentTags(models.Model):
    name = models.CharField(primary_key=True, max_length=32, unique=True)
    documents = models.ManyToManyField(Document, related_name="tags",)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "document\".\"tags"