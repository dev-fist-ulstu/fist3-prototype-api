from django.conf import settings

class DocumentErrors:
    DOC_TYPE_IS_NOT_ACTIVE = {
        "ru": "Данный тип документа выведен из оборота."
    }
    DOC_MAX_TAGS_ERROR= {
        "ru": f"Максимальное число тегов для одной записи: {settings.MAX_TAGS_PER_ENTITY}."
    }
    DOC_TAGS_NOT_PRESENTED = {
        "ru": "Необходимо добавить хотя бы 1 тег."
    }
    
class AuthenticationErrors:
    USER_NOT_FOUND_OR_PASSWORD_INVALID = {
        "ru": "Неверный логин или пароль."
    }
    EMAIL_TOKEN_LIFETIME_ENDED_NEED_REPEAT_REGISTRATION = {
        "ru": "Ошибка подтверждения регистрации. Пожалуйста, пройдите процедуру регистрации через 30 минут. "
              "В случае возникновения повторной ошибки, пожалуйста, свяжитесь со службой поддержки!"
    }
    NEED_RESIGN_IN_APP = {
        "ru": "Нужно перезайти в приложение."
    }