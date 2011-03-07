import sys, os
import MySQLdb
import settings
#import urwid

def help():
    print "Search users (prints username and password)"
    print "Syntax: ./pyfix.py search <username>"


def execute():
    if 3 != len(sys.argv):
        help()
    else:
        
        
        conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
        c=conn.cursor ()

        username = sys.argv[2] 

        c.execute("""SELECT username,password,name from mailbox WHERE username LIKE %s""", ("%"+username+"%",))



        while (1):
            row = c.fetchone()
            if row == None:
                break

            bold = lambda x: "\033[1m%s\033[0;0m" % x


            print "%(label1)s  %(data1)s  %(label2)s  %(data2)s  %(label3)s  %(data3)s" % {
                'label1': bold('Login'),
                'data1': row[0],
                'label2': bold('Password'),
                'data2': row[1],
                'label3': bold('Name'),
                'data3': row[2]
                }

            print "\n"
