#!/bin/sh
#python ./manage.py runfcgi daemonize=true host=127.0.0.1 port=8080

# Replace these three settings.
PROJDIR="/home/david/public_html/recipes.davidgrant.ca/public"
PIDFILE="$PROJDIR/django_recipes.pid"
#SOCKET="$PROJDIR/mysite.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

#exec /usr/bin/env - \
#  PYTHONPATH="../python:.." \
./manage.py runfcgi pidfile=$PIDFILE daemonize=true method=threaded host=127.0.0.1 port=8080
#./manage.py runfcgi pidfile=$PIDFILE socket=/home/david/recipes.sock daemonize=true method=threaded
