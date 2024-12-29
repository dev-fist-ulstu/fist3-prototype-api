CREATE SCHEMA IF NOT EXISTS "session";
CREATE SCHEMA IF NOT EXISTS "user";
CREATE SCHEMA IF NOT EXISTS "document";

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('USER', 10);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('LECTURER', 20);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('SUPPORT', 30);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('MODERATOR', 40);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('ADMIN', 10000);

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'news'
    , 'Новость'
    , true
    , true
    , true
    , false
    , true
    , false
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'resume'
    , 'Резюме пользователей для поиска работы'
    , false
    , false
    , true
    , false
    , true
    , true
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'vacancy'
    , 'Вакансии работодателей'
    , false
    , false
    , true
    , false
    , true
    , true
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'idea'
    , 'Идеи пользователей для улучшения портала или структурного подразделения (включая кафедры, факультет, кабинет и так далее)'
    , true
    , true
    , true
    , false
    , true
    , true
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'course'
    , 'Курсы для обучения студентов'
    , true
    , true
    , true
    , false
    , true
    , true
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'structure_department'
    , 'Курсы для обучения студентов'
    , true
    , true
    , true
    , false
    , true
    , true
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'question'
    , 'Вопросы, заданные пользователями портала'
    , false
    , false
    , true
    , false
    , true
    , true
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'answer_on_question'
    , 'Ответы на заданные вопросы'
    , false
    , false
    , false
    , false
    , true
    , false
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

INSERT INTO "document"."document_type" (
    doc_type
    , description
    , is_accept_for_comments
    , is_accept_for_reactions
    , is_accept_for_tags
    , is_admin_level_only
    , is_accept_for_files
    , is_need_approve
    , is_active_type
)
VALUES (
    'questionnaire'
    , 'Опрос среди пользователей портала'
    , true
    , true
    , true
    , false
    , true
    , false
    , true
)
ON CONFLICT (doc_type) DO NOTHING;

-- документы
-- news, resume, vacancy, idea, course, structure, questions, answer_on_question, questionnaire (опросы)