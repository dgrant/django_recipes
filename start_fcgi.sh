#!/bin/sh
. ./env.sh

OLDDIR=`pwd`
cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

env/bin/python src/manage.py runfcgi pidfile=$PIDFILE daemonize=true method=threaded host=127.0.0.1 port=8080
cd $OLDDIR
