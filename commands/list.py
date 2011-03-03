import sys, os
import MySQLdb
import settings
#import urwid

def help():
    print "Lists users"
    print "Syntax: ./pyfix.py list"


def execute():

    conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
    c=conn.cursor ()
    c.execute("""SELECT * from mailbox""")



    while (1):
        row = c.fetchone()
        if row == None:
            break

        bold = lambda x: "\033[1m%s\033[0;0m" % x


        print "%(label1)s  %(data1)s  %(label2)s  %(data2)s  %(label3)s  %(data3)s  %(label4)s  %(data4)s  %(label5)s  %(data5)s   %(label6)s   %(data6)s   %(label7)s %(data7)s" % {
                'label1': bold('Login'),
                'data1': row[0],
                'label2': bold('Password'),
                'data2': row[1],
                'label3': bold('Name'),
                'data3': row[2],
                'label4': bold('Quota'),
                'data4': row[3],
                'label5': bold('Transport'),
                'data5': row[4],
                'label6': bold('Description'),
                'data6': row[5],
                'label7': bold('Created at'),
                'data7': row[6]
                }

        print "\n"
