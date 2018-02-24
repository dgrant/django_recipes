from fabric.api import run, env, cd, shell_env, execute

from fabric.network import ssh

ssh.util.log_to_file("paramiko.log", 10)

env.hosts = ['linode']
env.use_ssh_config = True
ROOT='/home/david/public_html/django/django_recipes/public'

def restart():
    with cd(ROOT):
        run('touch ../../django_recipes.ini')

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
        run('sed -e "s/home=.*/home=$(pipenv --venv)/g" -i.bak ../../django_recipes.ini')
        run("cat ../../django_recipes.ini")
