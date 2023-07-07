#!/usr/bin/python3
"""
    Fabric script that creates and distributes an archive
    on my web servers, using deploy function
"""
from fabric.api import *
from fabric.operations import run, put, sudo, local
from datetime import datetime
import os

def do_pack():
    """
        generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
