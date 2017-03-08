#!/bin/sh
out='temp.sql'

echo "SET FOREIGN_KEY_CHECKS = 0;" > $out
mysqldump -u$1 -p$1 --add-drop-table --no-data $1 | grep ^DROP >> $out
echo "SET FOREIGN_KEY_CHECKS = 1;" >> $out
mysql -u$1 -p$1 $1 < $out

rm $out
