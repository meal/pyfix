import sys, os
import MySQLdb
import settings

def help():
    print "Lists users"
    print "Syntax: ./pyfix.py list"


def execute():

    conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
    c=conn.cursor ()
    c.execute("""SELECT * from mailbox""")
    info = c.fetchall()

    while (1):
        row = c.fetchone()
        if row == None:
            break

        print "%s, %s" % (row[0], row[1])
