from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `tagging_tag` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(50) NOT NULL UNIQUE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `tagging_taggeditem` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `tag_id` integer NOT NULL,
        `content_type_id` integer NOT NULL,
        `object_id` integer UNSIGNED NOT NULL,
        UNIQUE (`tag_id`, `content_type_id`, `object_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `tagging_taggeditem` ADD CONSTRAINT `tag_id_refs_id_4f74229f51000d` FOREIGN KEY (`tag_id`) REFERENCES `tagging_tag` (`id`);
""", """
    ALTER TABLE `tagging_taggeditem` ADD CONSTRAINT `content_type_id_refs_id_dcffa23f1f84eed` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
"""], sql_down=["""
    DROP TABLE `tagging_taggeditem`;
""", """
    DROP TABLE `tagging_tag`;
"""])
