from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['suitmedia@202.67.10.2']
env.password = 'Palat1no'
env.passwords = {
    'suitmedia@202.67.10.2': 'Palat1no'
}
env.activate = 'workon mysite'
APPPATH = '/home/suitmedia/ivan/mysite'


def test():
    with settings(warn_only=True):
        result = local('python manage.py test api', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def commit():
    local("git add -p && git commit")


def commit_all(message=''):
    local("cd ..")
    local("git add -A && git commit -m '%s'" % message)
    local("git push origin master")


def push():
    local("git push")


def prepare_deploy():
    test()
    commit()
    push()


def syncdb():
    with cd(APPPATH):
        run('python manage.py syncdb')


def collectstatic():
    with cd(APPPATH):
        run('python manage.py collectstatic')


def migrate():
    with cd(env.directory):
        with prefix(env.activate):
            run('python manage.py migrate')
            run("sudo supervisorctl restart mysite")


def update():
    with cd(APPPATH):
        run("git pull")
        run("sudo supervisorctl restart mysite")


def deploy():
    code_dir = '/home/suitmedia/ivan/mysite'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/ivanelian/mysite.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("cd mysite")
        run("sudo supervisorctl restart mysite")
