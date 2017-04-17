#!/bin/sh
pyenv uninstall -f django-recipes-3.6.1
pyenv virtualenv 3.6.1 django-recipes-3.6.1
pip install -r requirements.txt
