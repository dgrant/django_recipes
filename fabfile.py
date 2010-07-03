from fabric.api import *
from fabric.context_managers import cd

def local():
    env.hosts = ['david@localhost']
    env.root_dir = '~/svn/django-recipes-pip'

def slice():
    env.hosts = ['david@slice:55555']
    env.root_dir = ''
    env.user = "david"
    env.key_filename = ["/home/david/.ssh/id_dsa"]
    env.show = ['debug']

def setup():
    sudo('apt-get update')
    sudo('apt-get install python-setuptools')
    sudo('easy_install -U virtualenv')
    sudo('easy_install -U pip')

def virtualenv():
    with cd('%(root_dir)s' % env):
        run('rm -rf env')
        run('mkdir --parents ~/.pipcache')
        run('virtualenv --no-site-packages env')
        run('rm -f distribute*.tar.gz')
        run('pip -E env install -r requirements.txt --download-cache=~/.pipcache')
