mysqldump -urecipes_django -precipes_django --add-drop-table --no-data recipes_django | grep ^DROP | mysql -urecipes_django -precipes_django recipes_django
