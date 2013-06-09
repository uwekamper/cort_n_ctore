from __future__ import with_statement
from fabric.api import env
from fabric.api import run,sudo, local, settings, abort, cd, prefix
from fabric.contrib.project import upload_project
from fabric.contrib.files import exists
from fabric.operations import put
from fabric.contrib.console import confirm
from fabric.contrib import django

code_dir = '/home/uk/cort_n_ctore'
virtualenv = 'virtualenv'

def create_environment():
    # TODO: Install packages with pacman
    # sudo('apt-get install libjpeg-dev libjpeg-turbo8 libjpeg-turbo8-dev '
    #      'zlib1g-dev libfreetype6 libfreetype6-dev')

    run('mkdir -p %s' % code_dir)
    put('requirements.txt', code_dir)
    put('start_gunicorn.sh', code_dir)

    with cd(code_dir):
        run('chmod +x start_gunicorn.sh')
        run('%s --distribute --no-site-packages .' % virtualenv)
        run('source bin/activate; easy_install -U distribute')
        run('source bin/activate; pip install -r requirements.txt')
        run('mkdir -p static')
        run('mkdir -p media')

def copy_project():
    """
    """
    local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
    with cd(code_dir):
        put('templates', code_dir)
        put('cort_n_ctore', code_dir)
        run("find . -name '*.pyc' -print0|xargs -0 rm")

def init_project():
    """
    Initialize Django and the database
    """
    with cd(code_dir):
        with prefix('source bin/activate'):
            run('DJANGO_SETTINGS_MODULE=cort_n_ctore.settings_deploy python cort_n_ctore/manage.py syncdb')
            run('DJANGO_SETTINGS_MODULE=cort_n_ctore.settings_deploy python cort_n_ctore/manage.py migrate')
            run('DJANGO_SETTINGS_MODULE=cort_n_ctore.settings_deploy python cort_n_ctore/manage.py collectstatic --noinput')

def restart():
    sudo('/etc/init.d/cort_n_ctore restart')
    sudo('/etc/init.d/nginx restart')


def deploy():
    create_environment()
    copy_project()
    init_project()
    # restart()
