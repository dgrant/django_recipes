mysqldump -u$1 -p$1 --add-drop-table --no-data $1 | grep ^DROP | mysql -u$1 -p$1 $1
