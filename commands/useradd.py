import sys, os
import MySQLdb
import settings


def help():
    print "Add user"
    print "Syntax: ./pyfix.py useradd <username> "


def execute():

    if 3 != len(sys.argv):
        help()
    else:
        conn = MySQLdb.connect(host=settings.DBHOST ,user=settings.DBUSER , passwd=settings.DBPASS, db=settings.DBNAME)
        c=conn.cursor ()
        
        username = sys.argv[2]
        
        c.execute("""SELECT * FROM mailbox WHERE username=%s""", (username,))
        c.fetchone()
        if c.rowcount == 1 :
            print "User already exists, sorry. \n"
        else:
            c.execute("""SELECT * from alias WHERE address=%s""", (username,))
            c.fetchone()
            if c.rowcount == 1:
                print "It's an alias, sorry. \n"
            else:
                
                username =  sys.argv[2]
                
                password = raw_input("Password: ")
                name = raw_input("Name: ")
                quota = raw_input("Quota: ")
                transport = raw_input("Transport: ")
                opis = raw_input("Description: ")
                
                
                c.execute("""INSERT INTO mailbox (username, password, name, quota, transport, opis, czas) VALUES (%s, %s, %s, %s, %s, %s, NOW())""", ( username, password, name, quota, transport, opis
                    ))
                
                
                print "\n"
