INSERT INTO prs_role (name, permission_level)
VALUES ('USER', 1);

INSERT INTO prs_role (name, permission_level)
VALUES ('LECTURER', 2);

INSERT INTO prs_role (name, permission_level)
VALUES ('SUPPORT', 10);

INSERT INTO prs_role (name, permission_level)
VALUES ('MODERATOR', 15);

INSERT INTO prs_role (name, permission_level)
VALUES ('ADMIN', 10000);


-- В doc_type засунуть: направления, кафедры, преподаватели, лаборанты, вопросы и ответы (либо разделить, либо всё одно)
-- Это можно сделать в apps.py в изначальном (fist3_prototype_api)
class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from .models import MyModel

        initial_data = [
            {"field1": "value1", "field2": "value2"},
            {"field1": "value3", "field2": "value4"},
        ]

        for data in initial_data:
            try:
                MyModel.objects.get_or_create(**data)
            except IntegrityError:
                # Обработка ошибок, если необходимо
                pass