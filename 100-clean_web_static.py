#!/usr/bin/env python3
"""Fabric script to delete out-of-date archives"""

from fabric.api import env, run, local
from datetime import datetime
from os.path import isfile
from operator import itemgetter

env.user = 'ubuntu'
env.hosts = ['xx-web-01', 'xx-web-02']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    try:
        number = int(number)
        if number < 0:
            return
    except ValueError:
        return

    number_to_keep = number + 1

    # Delete unnecessary archives in the versions folder
    local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}"
          .format(number_to_keep))

    # Get a list of all archives in /data/web_static/releases
    archive_list = run("ls -1t /data/web_static/releases/").split()

    # Keep only the archive names without extensions
    archive_list_no_ext = [archive.split('.')[0] for archive in archive_list]

    # Get the count of each archive name
    archive_counts = {archive: archive_list_no_ext.count(archive)
                      for archive in set(archive_list_no_ext)}

    # Sort the archive counts by value in descending order
    sorted_counts = sorted(archive_counts.items(), key=itemgetter(1),
                           reverse=True)

    # Get the archives to delete
    archives_to_delete = [archive[0] for archive in
                          sorted_counts[number_to_keep:]]

    # Delete unnecessary archives in /data/web_static/releases
    for archive in archives_to_delete:
        run("rm -rf /data/web_static/releases/{}".format(archive))

