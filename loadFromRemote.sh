#!/bin/bash
ssh -p 55555 david@slice mysqldump -urecipes_django -precipes_django recipes_django | mysql -urecipes_django -precipes_django recipes_django
