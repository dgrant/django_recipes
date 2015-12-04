#!/bin/sh
rm -rf env
virtualenv -p python2 --distribute --no-site-packages env
env/bin/pip install --download-cache=~/.pip-cache -r requirements.txt
