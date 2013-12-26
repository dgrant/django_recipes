#!/bin/bash
mysqldump -urecipes_django -precipes_django recipes_django | ssh -C david@slice mysql -urecipes_django -precipes_django recipes_django
