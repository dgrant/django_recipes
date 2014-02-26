#!/bin/sh
rm -rf env
virtualenv --distribute --no-site-packages env
env/bin/pip install --download-cache=~/.pip-cache -r requirements.txt
