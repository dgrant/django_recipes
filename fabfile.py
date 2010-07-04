from fabric.api import *
from fabric.context_managers import cd
import os

svn_url = 'http://django-recipes.googlecode.com/svn/branches/pip'
PIP_PATH ='/usr/bin/pip'
CURR_DIR = os.path.abspath(os.path.split(__file__)[0])

def dev():
    env.config = 'dev'
    env.hosts = ['david@localhost']
    env.root_dir = os.path.join(CURR_DIR, '..')
    env.show = ['debug']

def local():
    env.config = 'local'
    env.hosts = ['david@localhost']
    env.root_dir = 'test-pip'
    env.show = ['debug']
    env.svn = 'svn export ' + (svn_url) + ' src'

def prod():
    env.config = 'prod'
    env.hosts = ['david@slice:55555']
    env.root_dir = 'django-recipes-deploy'
    env.user = "david"
    env.key_filename = ["/home/david/.ssh/id_dsa"]
    env.show = ['debug']
    env.svn = 'svn export ' + (svn_url) + ' src'

def __prereqcheck():
    require('hosts', provided_by=[local,slice])
    require('root_dir', provided_by=[local,slice])

def clean():
    run('rm -rf %(root_dir)s' % env)

def setup():
    __prereqcheck()
    sudo('apt-get update')
    sudo('apt-get install python-setuptools subversion')
    sudo('easy_install -U virtualenv')
    sudo('easy_install -U pip')

def virtualenv():
    __prereqcheck()
    run('mkdir -p %(root_dir)s' % env)
    with cd('%(root_dir)s' % env):
        run('rm -rf env')
        run('mkdir --parents ~/.pipcache')
        run('virtualenv --distribute --no-site-packages env')

def deploy():
    __prereqcheck()
    with cd('%(root_dir)s' % env):
        if env.config != 'dev':
            run('rm -rf src')
            run('%(svn)s' % env)
        run('%(pip_path)s -E env install --upgrade -r src/requirements.txt --download-cache=~/.pipcache' % {'pip_path': PIP_PATH})
