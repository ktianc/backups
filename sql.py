from fabric.api import *

import sys
import os
import time

env.password=""
env.user=""
env.port=22
env.key_filename=""

now = time.strftime("%y%m%d%H",time.localtime())

def sql_backups(sql_name,remote_dir):
	with cd("/usr/local/sql_backup/"):
		run("mysqldump -u root -p Gy64100124 {0} > {0}-{1}.sql".format(sql_name,now))
	    get("/usr/local/sql_backup/{0}-{1}.sql".format(sql_name,now),"/usr/local/nginx/html/backups/remote_dir/")
	    run("rm -rf {0}-{1}.sql".format(sql_name,now))