from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `django_site` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `domain` varchar(100) NOT NULL,
        `name` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `django_site`;
"""])
