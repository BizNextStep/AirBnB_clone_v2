#!/usr/bin/env python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, put, run
import os

# Set the user and hosts
env.user = 'ubuntu'
env.hosts = ['xx-web-01', 'xx-web-02']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_name)[0]

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
    except Exception as e:
        return False

