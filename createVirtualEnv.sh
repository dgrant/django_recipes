#!/bin/sh
rm -rf env.bak
mv env env.bak
sudo easy_install pip
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
virtualenv --distribute --no-site-packages env
env/bin/pip install --download-cache=~/.pip-cache -r requirements.txt
