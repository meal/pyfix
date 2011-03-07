import sys, os
import MySQLdb
import settings


def help():
    print "Deletes alias"
    print "Syntax: ./pyfix.py delalias <address>"


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
            print "Alias already exists. \n"
        else:
            
            confirm = raw_input("Are you sure? (Yes) \n")
           
            
            if confirm == "Yes" :
                c.execute("""DELETE from alias WHERE address=%s""", ( address,))
                
                print "\n"
