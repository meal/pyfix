import sys, os
import MySQLdb
import settings
#import urwid

def help():
    print "Change quota for username given"
    print "Syntax: ./pyfix.py quota <username>"


def execute():

    if 3 != len(sys.argv):
        help()
    else:
        conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
        c=conn.cursor ()
        
        user = sys.argv[2]
        
        c.execute("""SELECT * FROM mailbox WHERE username=%s""", (user,))
        c.fetchone()
        if c.rowcount == 0 :
            print "No such user found. Try again. \n"
        else:
            quota = raw_input("New quota: \n")

            c.execute("""UPDATE mailbox set quota = %s WHERE username=%s""", ( quota, user))
                
            print "\n"
