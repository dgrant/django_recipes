#!/bin/bash
if [ $# -eq 0 ]
then
  echo "Missing database arg"
  exit 1
fi
mkdir -p backups
NAME=backups/$1_localhost_`eval date +%Y%m%d_%H%M%S`.sql
mysqldump -u$1 -p$1 $1 > $NAME
gzip $NAME
