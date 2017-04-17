#!/bin/bash
ssh -C david@linode mysqldump -urecipes_django -precipes_django recipes_django | mysql -urecipes_django -precipes_django recipes_django
