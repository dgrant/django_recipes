from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `django_admin_log` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `action_time` datetime NOT NULL,
        `user_id` integer NOT NULL,
        `content_type_id` integer,
        `object_id` longtext,
        `object_repr` varchar(200) NOT NULL,
        `action_flag` smallint UNSIGNED NOT NULL,
        `change_message` longtext NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `django_admin_log` ADD CONSTRAINT `user_id_refs_id_6bfddbd40c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    ALTER TABLE `django_admin_log` ADD CONSTRAINT `content_type_id_refs_id_5c269194288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
"""], sql_down=["""
    DROP TABLE `django_admin_log`;
"""])
