#!/bin/sh
pipenv run ./manage.py test --settings=django_recipes.settings.test
