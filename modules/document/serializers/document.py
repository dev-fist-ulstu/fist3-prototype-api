from ..models import Document, DocumentType
from rest_framework import serializers
from modules.user.serializers import UserSerializer


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    doc_type = DocumentTypeSerializer(many=False, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    liked_by_me = serializers.BooleanField(default=None)
    disliked_by_me = serializers.BooleanField(default=None)
    create_by = UserSerializer(many=False, read_only=True)
    update_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Document
        fields = "__all__"

    def get_likes_count(self, obj: Document):
        return obj.likes.count()

    def get_dislikes_count(self, obj: Document):
        return obj.dislikes.count()