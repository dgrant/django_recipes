#!/bin/bash
ssh -C david@slice mysqldump -urecipes_django -precipes_django recipes_django | mysql -urecipes_django -precipes_django recipes_django
