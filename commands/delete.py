import sys, os
import MySQLdb
import settings


def help():
    print "Deletes user"
    print "Syntax: ./pyfix.py delete <username>"


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
            
            confirm = raw_input("Are you sure? (Yes) \n")
           
            
            if confirm == "Yes" :
                c.execute("""DELETE from  mailbox WHERE username=%s""", ( user,))
                
                print "\n"
