from django.apps import AppConfig


class CardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.document'

    # def ready(self):
    #     from .models import MyModel
    #
    #     initial_data = [
    #         {"field1": "value1", "field2": "value2"},
    #         {"field1": "value3", "field2": "value4"},
    #     ]
    #
    #     for data in initial_data:
    #         try:
    #             MyModel.objects.get_or_create(**data)
    #         except IntegrityError:
    #             # Обработка ошибок, если необходимо
    #             pass
