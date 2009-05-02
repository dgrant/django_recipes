from dmigrations.mysql import migrations as m
import datetime
migration = m.Migration(sql_up=["""
    CREATE TABLE `recipes_source` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(150) NOT NULL,
        `url` varchar(500) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `recipes_category` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(120) NOT NULL UNIQUE,
        `order_index` integer UNSIGNED,
        `slug` varchar(50) NOT NULL UNIQUE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `recipes_foodgroup` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(150) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `recipes_food` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(150) NOT NULL,
        `group_id` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `recipes_food` ADD CONSTRAINT `group_id_refs_id_47ae550f7b29cf1f` FOREIGN KEY (`group_id`) REFERENCES `recipes_foodgroup` (`id`);
""", """
    CREATE TABLE `recipes_prepmethod` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(60) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `recipes_photo` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `caption` varchar(200) NOT NULL,
        `recipe_id` integer NOT NULL,
        `image` varchar(100) NOT NULL,
        `keep` bool NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `recipes_recipe` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `title` varchar(50) NOT NULL,
        `summary` varchar(500) NOT NULL,
        `description` longtext NOT NULL,
        `slug` varchar(50) NOT NULL UNIQUE,
        `prep_time` varchar(100) NOT NULL,
        `ctime` datetime NOT NULL,
        `mtime` datetime NOT NULL,
        `category_id` integer NOT NULL,
        `tags` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `recipes_recipe` ADD CONSTRAINT `category_id_refs_id_67c4d79161a1ac99` FOREIGN KEY (`category_id`) REFERENCES `recipes_category` (`id`);
""", """
    ALTER TABLE `recipes_photo` ADD CONSTRAINT `recipe_id_refs_id_4facdcca2c0f3c2e` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`);
""", """
    CREATE TABLE `recipes_direction` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `text` longtext NOT NULL,
        `recipe_id` integer NOT NULL,
        `order` integer UNSIGNED
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `recipes_direction` ADD CONSTRAINT `recipe_id_refs_id_4ca31660f2f22585` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`);
""", """
    CREATE TABLE `recipes_unit` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(60) NOT NULL,
        `name_abbrev` varchar(60) NOT NULL,
        `plural` varchar(60) NOT NULL,
        `plural_abbrev` varchar(60) NOT NULL,
        `type` integer NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `recipes_ingredient` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `amount` double precision NOT NULL,
        `amountMax` double precision,
        `unit_id` integer,
        `recipe_id` integer NOT NULL,
        `food_id` integer NOT NULL,
        `prep_method_id` integer,
        `order_index` integer UNSIGNED,
        `direction_id` integer
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `recipes_ingredient` ADD CONSTRAINT `unit_id_refs_id_36e06e969f141ae6` FOREIGN KEY (`unit_id`) REFERENCES `recipes_unit` (`id`);
""", """
    ALTER TABLE `recipes_ingredient` ADD CONSTRAINT `recipe_id_refs_id_1fad087d5e1489a0` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`);
""", """
    ALTER TABLE `recipes_ingredient` ADD CONSTRAINT `food_id_refs_id_6cfc5050cfec02fc` FOREIGN KEY (`food_id`) REFERENCES `recipes_food` (`id`);
""", """
    ALTER TABLE `recipes_ingredient` ADD CONSTRAINT `direction_id_refs_id_1381270ec71efa6a` FOREIGN KEY (`direction_id`) REFERENCES `recipes_direction` (`id`);
""", """
    ALTER TABLE `recipes_ingredient` ADD CONSTRAINT `prep_method_id_refs_id_5f9eabd13618a9e8` FOREIGN KEY (`prep_method_id`) REFERENCES `recipes_prepmethod` (`id`);
""", """
    CREATE TABLE `recipes_recipe_sources` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `recipe_id` integer NOT NULL,
        `source_id` integer NOT NULL,
        UNIQUE (`recipe_id`, `source_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `recipes_recipe_sources` ADD CONSTRAINT `recipe_id_refs_id_167d36c176eeeb1c` FOREIGN KEY (`recipe_id`) REFERENCES `recipes_recipe` (`id`);
""", """
    ALTER TABLE `recipes_recipe_sources` ADD CONSTRAINT `source_id_refs_id_623c8e3a108f7393` FOREIGN KEY (`source_id`) REFERENCES `recipes_source` (`id`);
"""], sql_down=["""
    DROP TABLE `recipes_recipe_sources`;
""", """
    DROP TABLE `recipes_ingredient`;
""", """
    DROP TABLE `recipes_unit`;
""", """
    DROP TABLE `recipes_direction`;
""", """
    ALTER TABLE `recipes_photo` DROP FOREIGN KEY recipe_id_refs_id_4facdcca2c0f3c2e;
""", """
    DROP TABLE `recipes_recipe`;
""", """
    DROP TABLE `recipes_photo`;
""", """
    DROP TABLE `recipes_prepmethod`;
""", """
    DROP TABLE `recipes_food`;
""", """
    DROP TABLE `recipes_foodgroup`;
""", """
    DROP TABLE `recipes_category`;
""", """
    DROP TABLE `recipes_source`;
"""])
