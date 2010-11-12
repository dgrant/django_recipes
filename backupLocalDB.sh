#!/bin/bash
mysqldump -urecipes_django -precipes_django recipes_django > backups/django_recipes_localhost_`eval date +%Y%m%d_%H%M%S`.sql
