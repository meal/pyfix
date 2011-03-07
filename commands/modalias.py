import sys, os
import MySQLdb
import settings


def help():
    print "Modify alias"
    print "Syntax: ./pyfix.py modalias <address> <new destination> "


def execute():

    if 3 != len(sys.argv):
        help()
    else:
        conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
        c=conn.cursor ()
        
        address = sys.argv[2]
        
        c.execute("""SELECT * FROM alias WHERE address=%s""", (address,))
        c.fetchone()
        if c.rowcount == 0:
            print "No such alias, sorry. \n"
        else:
            
            address =  sys.argv[2]
                
            goto = sys.argv[3]   
                
            c.execute("""UPDATE alias set address=%s, goto=%s""", ( address, goto))
                
                
            print "\n"
