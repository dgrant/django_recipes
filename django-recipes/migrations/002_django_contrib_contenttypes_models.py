from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `django_content_type` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(100) NOT NULL,
        `app_label` varchar(100) NOT NULL,
        `model` varchar(100) NOT NULL,
        UNIQUE (`app_label`, `model`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `django_content_type`;
"""])
