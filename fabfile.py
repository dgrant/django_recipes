import re

from fabric.api import run, env, cd, shell_env, execute, sudo
from fabric.network import ssh

from functools import wraps



ssh.util.log_to_file("paramiko.log", 10)

env.hosts = ['linode']
env.use_ssh_config = True
ROOT='/home/david/public_html/django/django_recipes/public'

INI_FILE = '/etc/uwsgi/apps-available/django_recipes.ini'

def restart():
    with cd(ROOT):
        sudo('/etc/init.d/uwsgi restart')

def update():
    with cd(ROOT):
        run('git pull --rebase')

def schema():
    with cd(ROOT), shell_env(DJANGO_SETTINGS_MODULE='django_recipes.settings.production'):
        run('pipenv run ./manage.py migrate')

def backupdb():
    with cd(ROOT):
        run('./backupLocalDB.sh recipes_django')

def static():
    with cd(ROOT):
        run('pipenv run ./manage.py collectstatic --settings=django_recipes.settings.production --noinput --link --clear')

def deploy():
    execute(update)
    execute(env)
    execute(backupdb)
    execute(schema)
    execute(static)
    execute(restart)

ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')

def env():
    with cd(ROOT):
        run('pipenv --rm')
        run('pipenv --python 3.7')
        run('pipenv install')

        pipenv_env_dir = run('pipenv --bare --venv')
        print("pipenv_env_dir=",pipenv_env_dir)

        pipenv_env_dir = ansi_escape.sub("", pipenv_env_dir)
        print("pipenv_env_dir=",pipenv_env_dir)

        pipenv_env_dir = pipenv_env_dir.strip()
        print("pipenv_env_dir=",pipenv_env_dir)

        pipenv_env_dir = pipenv_env_dir.replace('/', '\\/')
        print("pipenv_env_dir=",pipenv_env_dir)

        sudo("sed -e 's/home=.*/home={0}/g' -i.bak {1}".format(pipenv_env_dir, INI_FILE))
        run("cat " + INI_FILE)
