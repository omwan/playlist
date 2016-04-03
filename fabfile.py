from fabric.api import run, puts, warn, abort, task

from time import sleep

@task
def deploy():
    with cd('/opt/perfect_party/playlist/'):
        run('git pull origin master')
        sudo('supervisorctl stop ppp')
        sleep(5)
        sudo('supervisorctl start ppp')
