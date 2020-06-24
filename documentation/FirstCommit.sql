DROP TABLE IF EXISTS "Role";
DROP SEQUENCE IF EXISTS role_seq;
CREATE SEQUENCE role_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."Role" (
    "IdRole" integer DEFAULT nextval('role_seq') NOT NULL,
    "Name" character varying NOT NULL,
    "Key" character varying NOT NULL,
    CONSTRAINT "Role_IdRole" PRIMARY KEY ("IdRole")
) WITH (oids = false);

INSERT INTO "Role" ("IdRole", "Name", "Key") VALUES
(1,	'Administrador',	'ADMIN'),
(2,	'Manager',	'MANAGER');

DROP TABLE IF EXISTS "UserStatus";
DROP SEQUENCE IF EXISTS userstatus_seq;
CREATE SEQUENCE userstatus_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."UserStatus" (
    "IdUserStatus" integer DEFAULT nextval('userstatus_seq') NOT NULL,
    "Name" character varying NOT NULL,
    CONSTRAINT "UserStatus_IdUserStatus" PRIMARY KEY ("IdUserStatus")
) WITH (oids = false);

INSERT INTO "UserStatus" ("IdUserStatus", "Name") VALUES
(1,	'Activación pendiente'),
(2,	'Activo'),
(3,	'Suspendido'),
(4,	'Dado de baja');

DROP TABLE IF EXISTS "User";
DROP SEQUENCE IF EXISTS user_seq;
CREATE SEQUENCE user_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."User" (
    "IdUser" integer DEFAULT nextval('user_seq') NOT NULL,
    "IdRole" integer,
    "IdUserStatus" integer,
    "Email" character varying,
    "Password" character varying,
    "Guid" character(36),
    "Name" character varying,
    "Lastname" character varying,
    "Created" timestamp NOT NULL,
    "Updated" timestamp,
    "Deleted" timestamp,
    CONSTRAINT "User_IdUser" PRIMARY KEY ("IdUser"),
    CONSTRAINT "User_IdRole_fkey" FOREIGN KEY ("IdRole") REFERENCES "Role"("IdRole") ON UPDATE RESTRICT ON DELETE RESTRICT NOT DEFERRABLE,
    CONSTRAINT "User_IdUserStatus_fkey" FOREIGN KEY ("IdUserStatus") REFERENCES "UserStatus"("IdUserStatus") ON UPDATE RESTRICT ON DELETE RESTRICT NOT DEFERRABLE
) WITH (oids = false);

CREATE INDEX "User_IdRole" ON "public"."User" USING btree ("IdRole");

CREATE INDEX "User_IdUserStatus" ON "public"."User" USING btree ("IdUserStatus");
