#!/usr/bin/python3
"""a script that deletes out of date archives using the function
do_clean"""
from fabric.api import local, put, run, env
import os
env.hosts = ['34.227.101.5', '52.91.116.255']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'
env.password = None


def do_clean(number=0):
    """deletes out of date archives"""
    
