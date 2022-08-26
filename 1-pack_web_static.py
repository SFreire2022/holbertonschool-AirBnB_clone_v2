#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
from os.path import getsize, exists
from os import mkdir


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
        local('sudo tar -czvf {}.tgz web_static'.format(file_))
        fname = '{}.tgz'.format(file_)
        print('web_static packed: {} -> {}Bytes'.
              format(fname, getsize(fname)))
    except Exception:
        return None
