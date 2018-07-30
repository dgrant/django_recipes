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

def env():
    with cd(ROOT):
        run('pipenv install')
        pipenv_env_dir = run('pipenv --venv')
        pipenv_env_dir = pipenv_env_dir.replace('/', '\\/')
        sudo("sed -e 's/home=.*/home={0}/g' -i.bak {1}".format(pipenv_env_dir, INI_FILE))
        run("cat " + INI_FILE)
