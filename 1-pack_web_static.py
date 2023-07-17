#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive
    from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """ Generates a .tgz archive"""

    try:
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year,now.month, now.day, now.hour, now.minute,now.second)
        local("mkdir -p versions")
        local("tar -czvf versions/{} web_static".format(archive_name))

        archive_path ="versions/{}".format(archive_name)
        archive_size = local("du -sh {}".format(archive_path),capture=True).split()[0]
        print("{} packed: {} -> {}Bytes".format(archive_path, archive_size, archive_size))
        return archive_path
    except:
        return None
