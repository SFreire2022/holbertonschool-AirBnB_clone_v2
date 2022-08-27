#!/usr/bin/python3
"""
Fabfile to delete outdated archives,
locally and remote in both servers
If number is 0 or 1, keeps only the most recent archive.
If number is 2, keeps the most and second-most recent archives
"""
from os import listdir
from fabric.api import local, env, lcd, cd


env.hosts = ['3.91.220.140', '54.221.177.99']


def do_clean(number=0):
    """
    Delete outdated archives.
    Keep the number of archives recived as argument.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(listdir('versions'))
    [archives.pop() for i in range(number)]
    with lcd('versions'):
        [local('rm ./{}'.format(a)) for a in archives]

    with cd('/data/web_static/releases'):
        archives = run('ls -tr').split()
        archives = [a for a in archives if 'web_static_' in a]
        [archives.pop() for i in range(number)]
        [run('rm -rf ./{}'.format(a)) for a in archives]
