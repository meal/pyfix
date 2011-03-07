import sys, os
import MySQLdb
import settings


def help():
    print "Add domain"
    print "Syntax: ./pyfix.py domainadd <domain> <description>"


def execute():

    if 3 != len(sys.argv):
        help()
    else:
        conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
        c=conn.cursor ()
        
        domain = sys.argv[2]
        
        c.execute("""SELECT * FROM mailbox WHERE domain=%s""", (domain,))
        c.fetchone()
        if c.rowcount == 1 :
            print "Domain already exists, sorry. \n"
        else:
            

         description =  sys.argv[2]

                c.execute("""INSERT INTO domain (domain,description) VALUES (%s, %s)""", ( domain, description))
                
                print "\n"
