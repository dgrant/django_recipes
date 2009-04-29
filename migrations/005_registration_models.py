from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `registration_registrationprofile` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL UNIQUE,
        `activation_key` varchar(40) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `registration_registrationprofile` ADD CONSTRAINT `user_id_refs_id_4c3fb6e0cecd7f3c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
"""], sql_down=["""
    DROP TABLE `registration_registrationprofile`;
"""])
