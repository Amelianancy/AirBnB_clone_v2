#!/usr/bin/python3
"""creates and distributes an archive to my servers"""
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack


def deploy():
    """creates and distributes an archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
