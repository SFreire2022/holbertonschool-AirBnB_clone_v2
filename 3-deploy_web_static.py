#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import getsize, exists
from os import mkdir


env.hosts = ['3.91.220.140', '54.221.177.99']


def do_deploy(archive_path):
    """
    Deploy the package tgz file to both servers
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except Exception:
        return False

def do_pack():
    """
    Packing project directory content into a versioned packages as .tgz
    """
    try:
        if not exists('versions'):
            mkdir('versions')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        print('Packing web_static to versions/web_static_{}.tgz'.
              format(timestamp))
        file_ = 'versions/web_static_{}'.format(timestamp)
        local('tar -czvf {}.tgz web_static'.format(file_))
        fname = '{}.tgz'.format(file_)
        print('web_static packed: {} -> {}Bytes'.
              format(fname, getsize(fname)))
        return fname
    except Exception:
        return None

def deploy():
    """
    Function to do_pack and do_deploy
    """
    archive_path = do_pack()
    result = do_deploy(archive_path)
    return result
