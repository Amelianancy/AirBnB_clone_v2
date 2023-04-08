#!/usr/bin/python3
"""a script that deletes out of date archives using the function
do_clean"""
do_deploy = __import__('3-deploy_web_static').do_deploy


def do_clean(number=0):
    """deletes out of date archives"""

