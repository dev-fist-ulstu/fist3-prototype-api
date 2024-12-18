CREATE SCHEMA IF NOT EXISTS "session";
CREATE SCHEMA IF NOT EXISTS "user";
CREATE SCHEMA IF NOT EXISTS "document";

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('USER', 1);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('LECTURER', 2);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('SUPPORT', 10);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('MODERATOR', 15);

INSERT INTO "user"."roles" (name, permission_level)
VALUES ('ADMIN', 10000);

INSERT INTO "document"."document_type" (doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only, is_accept_for_files, is_need_approve, is_active_type)
VALUES ('news')