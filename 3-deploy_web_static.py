#!/usr/bin/python3
"""creates and distributes an archive to my servers"""


import datetime
from fabric.api import local, put, run, env
import os
env.hosts = ['34.227.101.5', '52.91.116.255']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'
env.password = None

def do_pack():
    """compress the webstatic folder into a .tgz file"""
    try:
        local("mkdir -p versions")
        day = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(day)
        local("tar -czvf {} web_static".format(filename))
        return filename
    except FileNotFoundError:
        return None

def do_deploy(archive_path):
    """distributes an archive to my webservers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        unarchived = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}'.format(path, unarchived))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, unarchived))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, unarchived))
        run('rm -rf {0}{1}/web_static/'.format(path, unarchived))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{} /data/web_static/current'.format(path, unarchived))
        print("New version deployed!")
        return True
    except FileNotFoundError:
        False

def deploy():
    """creates and distributes an archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
