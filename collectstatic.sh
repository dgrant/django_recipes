#!/bin/sh
/home/david/public_html/django/django_recipes/public/env/bin/python /home/david/public_html/django/django_recipes/public/manage.py collectstatic --settings=django_recipes.settings.production --noinput --link --clear
