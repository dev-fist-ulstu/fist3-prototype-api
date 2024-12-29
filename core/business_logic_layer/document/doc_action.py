import datetime
from core.exception import ClientException
from core.direct_sql_worker.server_time import get_server_time_now
from modules.document.models import Document, DocumentType, DocumentTags
from django.conf import settings
from core.error_messages import DocumentErrors


def get_document(doc_id: int) -> Document:
    """ Получить документ по id

    :param doc_id: id документа
    :return: Инстанс Document
    """
    return Document.objects.get(id=doc_id)


def register_tags(tags: list[str]) -> list:
    """ Регистрация тегов

    :param max_tags: Максимальное количество тегов
    :param tags: Список строк (тегов)
    :return: Список моделей тегов
    """
    added_tags = []
    cnt_tags = len(tags)
    if cnt_tags > settings.MAX_TAGS_PER_ENTITY:
        raise ClientException(DocumentErrors.DOC_MAX_TAGS_ERROR["ru"])
    for tag in tags:
        added_tags.append(DocumentTags.objects.get_or_create(name=tag)[0])
    return added_tags


def register_document(doc_type: str, data: dict, create_by: int, tags: list = None) -> Document:
    """ Регистрация документа в базе данных

    :param doc_type: Тип документа по DocumentType
    :param data: Дата из validated_data в формате dict
    :param create_by: ID инициатора создания документа
    :param tags: Список строк тегов (["Тег1", "Тег2"])
    :return: Инстанс Document
    """
    doc_type_model = DocumentType.objects.get(doc_type=doc_type)
    if not doc_type_model.is_active_type:
        raise ClientException(DocumentErrors.DOC_TYPE_IS_NOT_ACTIVE["ru"])
    if data.get("user"):
        data.pop("user")
    doc = Document.objects.create(doc_type_id=doc_type, json_data=data, create_by_id=create_by)
    if doc_type_model.is_accept_for_tags and tags is not None:
        registered_tags = register_tags(tags)
        doc.tags.set(registered_tags)
    elif tags is None:
        raise ClientException(DocumentErrors.DOC_TAGS_NOT_PRESENTED["ru"])
    if doc.doc_type.is_need_approve:
        doc.is_ready_for_publish = False
        doc.is_moderated = False
    doc.save()
    return doc


def update_document(doc: Document, data: dict, update_by: int, tags: list = None) -> Document:
    """ Обновление зарегестрированного документа

    :param doc: Инстанс Document
    :param data: Дата из validated_data в формате dict
    :param update_by: ID инициатора обновления документа
    :param tags: Список строк тегов (["Тег1", "Тег2"])
    :return: Инстанс Document
    """
    if not doc.doc_type.is_active_type:
        raise ClientException(DocumentErrors.DOC_TYPE_IS_NOT_ACTIVE["ru"])
    doc.update_by_id = update_by
    doc.json_data = data
    doc.update_at = get_server_time_now()
    if data.get("user"):
        data.pop("user")
    if doc.doc_type.is_accept_for_tags and tags is not None:
        registered_tags = register_tags(tags)
        doc.tags.set(registered_tags)
    if doc.doc_type.is_need_approve:
        doc.is_ready_for_publish = False
        doc.is_moderated = False
    doc.save()
    return doc


