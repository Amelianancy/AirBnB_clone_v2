#!/usr/bin/python3
"""A fabric script that generates a .tgz archive from the contents of
web_static folder"""


import datetime
from fabric.api import local
from os.path import isdir


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
