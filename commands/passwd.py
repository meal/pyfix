import sys, os
import MySQLdb
import settings
#import urwid

def help():
    print "Change password for username given"
    print "Syntax: ./pyfix.py passwd <username>"


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
            
            passwd = raw_input("New password: \n")
            passwd2 = raw_input("Confirm password: \n")
            
            
            if passwd == passwd2 :
                c.execute("""UPDATE mailbox set password = %s WHERE username=%s""", ( passwd, user))
                
                print "\n"
