#!/bin/bash
mkdir -p backups
mysqldump -u$1 -p$1 $1 > backups/$1_localhost_`eval date +%Y%m%d_%H%M%S`.sql
