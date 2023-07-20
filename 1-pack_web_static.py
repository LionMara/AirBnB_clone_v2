#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive
    from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime
import time


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
