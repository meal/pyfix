import sys, os
import MySQLdb
import settings
#import urwid

def help():
    print "Search chained/looped aliases"
    print "Syntax: ./pyfix.py loopsearch <username>"


def execute():
    if 3 != len(sys.argv):
        help()
    else:
        
        
        conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
        c=conn.cursor ()

        username = sys.argv[2] 

        c.execute("""SELECT goto from alias WHERE address=%s""", (username,))
        
        

        
        print "\n"
