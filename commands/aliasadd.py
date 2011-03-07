import sys, os
import MySQLdb
import settings


def help():
    print "Add alias"
    print "Syntax: ./pyfix.py aliasadd <address> <destination> "


def execute():

    if 3 != len(sys.argv):
        help()
    else:
        conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
        c=conn.cursor ()
        
        address = sys.argv[2]
        
        c.execute("""SELECT * FROM alias WHERE address=%s""", (address,))
        c.fetchone()
        if c.rowcount == 1 :
            print "Alias already exists, sorry. \n"
        else:
            
            address =  sys.argv[2]
                
            goto = sys.argv[3]   
                
            c.execute("""INSERT INTO alias (address, goto) VALUES (%s, %s)""", ( address, goto))
                
                
            print "\n"
