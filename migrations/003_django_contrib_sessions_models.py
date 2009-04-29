from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `django_session` (
        `session_key` varchar(40) NOT NULL PRIMARY KEY,
        `session_data` longtext NOT NULL,
        `expire_date` datetime NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `django_session`;
"""])
