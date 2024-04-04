#!/usr/bin/env python3
"""Fabric script to generate a .tgz archive from the contents of web_static"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of web_static"""
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive path
        now = datetime.now()
        archive_path = "versions/web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S"))

        # Compress the contents of the web_static folder
        local("tar -czvf {} web_static".format(archive_path))

        # Check if the archive was created successfully
        if os.path.exists(archive_path):
            return archive_path
        else:
            return None
    except Exception as e:
        return None
