#!/usr/bin/env python3
"""Fabric script to create and distribute an archive to web servers"""

from fabric.api import env, run
from fabric.operations import local
from datetime import datetime
from os.path import isfile

env.user = 'ubuntu'
env.hosts = ['xx-web-01', 'xx-web-02']


def do_pack():
    """Creates a .tgz archive from the contents of web_static"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        file_name = "versions/web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S"))
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not isfile(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]

        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')

        # Uncompress the archive to /data/web_static/releases/
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_name, archive_no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Move contents to appropriate folder
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'
            .format(archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_no_ext))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create new symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_no_ext))

        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Full deployment"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

