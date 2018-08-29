#!/bin/bash
ssh -C david@linode mysqldump -urecipes_django -precipes_django recipes_django recipes_category recipes_direction recipes_food recipes_foodgroup recipes_ingredient recipes_photo recipes_prepmethod recipes_recipe recipes_recipe_sources recipes_servingstring recipes_source recipes_unit > dump.sql
