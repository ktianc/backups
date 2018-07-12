from fabric.api import *

import os
import sys
import time

env.password=""
env.user=""
env.port=22
env.key_filename=""

now = time.strftime("%y%m%d%H",time.localtime())

def apache_backups(file_dir,remote_dir):
   
    with cd("/var/www/html"):
        run("zip -r {0}-{1}.zip {0}".format(file_dir,now))
        get("/var/www/html/{0}-{1}.zip".format(file_dir,now),"/usr/local/nginx/html/backups/{0}/".format(remote_dir))
        run("mv {0}-{1}.zip /tmp")