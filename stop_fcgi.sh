#!/bin/sh
. ./env.sh
kill `cat $PIDFILE`
