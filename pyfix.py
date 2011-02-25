#!/usr/bin/env python

import MySQLdb
from configobj import ConfigObj
import sys

#
# mysql credentials in config file
#
#



config = ConfigObj(config.cfg)

dbhost = config['dbhost'
dbuser = config['dbuser']
dbpass = config['dbpass']
dbname = config['dbname']




conn = MySQLdb.connect(dbhost, dbuser, dbpass, dbname)

c = conn.cursor()


