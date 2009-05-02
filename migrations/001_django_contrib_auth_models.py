from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `auth_permission` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(50) NOT NULL,
        `content_type_id` integer NOT NULL,
        `codename` varchar(100) NOT NULL,
        UNIQUE (`content_type_id`, `codename`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `auth_group` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(80) NOT NULL UNIQUE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `auth_user` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `username` varchar(30) NOT NULL UNIQUE,
        `first_name` varchar(30) NOT NULL,
        `last_name` varchar(30) NOT NULL,
        `email` varchar(75) NOT NULL,
        `password` varchar(128) NOT NULL,
        `is_staff` bool NOT NULL,
        `is_active` bool NOT NULL,
        `is_superuser` bool NOT NULL,
        `last_login` datetime NOT NULL,
        `date_joined` datetime NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `auth_message` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL,
        `message` longtext NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_message` ADD CONSTRAINT `user_id_refs_id_7837edc69af0b65a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    CREATE TABLE `auth_group_permissions` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `group_id` integer NOT NULL,
        `permission_id` integer NOT NULL,
        UNIQUE (`group_id`, `permission_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `group_id_refs_id_2ccea4c93cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
""", """
    ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `permission_id_refs_id_4de83ca7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
""", """
    CREATE TABLE `auth_user_groups` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL,
        `group_id` integer NOT NULL,
        UNIQUE (`user_id`, `group_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_user_groups` ADD CONSTRAINT `user_id_refs_id_1993cb70831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    ALTER TABLE `auth_user_groups` ADD CONSTRAINT `group_id_refs_id_321a8efef0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
""", """
    CREATE TABLE `auth_user_user_permissions` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL,
        `permission_id` integer NOT NULL,
        UNIQUE (`user_id`, `permission_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `user_id_refs_id_166738bf2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `permission_id_refs_id_6d7fb3c2067e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
""", """
    -- The following references should be added but depend on non-existent tables:
""", """
    -- ALTER TABLE `auth_permission` ADD CONSTRAINT `content_type_id_refs_id_6bc81a32728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
"""], sql_down=["""
    DROP TABLE `auth_user_user_permissions`;
""", """
    DROP TABLE `auth_user_groups`;
""", """
    DROP TABLE `auth_group_permissions`;
""", """
    DROP TABLE `auth_message`;
""", """
    DROP TABLE `auth_user`;
""", """
    DROP TABLE `auth_group`;
""", """
    DROP TABLE `auth_permission`;
"""])
