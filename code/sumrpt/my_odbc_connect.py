# Python commands to open and close ODBC connections.
# Stephen J. Hegner 21 February 2014.
# Repaired to handle autocommit correctly 22.02.2015

import sys
import pyodbc
import getpass

if  sys.version_info<(3,0,0):
        input = raw_input

# Function to establish a connection:        
# Choose the first argument as one of:
# nopwd = prompt for database name only; use ident authorization.
# pwd = prompt for database name, user name, and password.
# cmdln = take arugments from the command line.
# The (optional) "other" argument adds additional arguments verbatim.
# The autocommit arguments must be "True" or "Yes" to enable autocommit.

def establish_connection(mode,other="",autocommit=""):
        if mode=="cmdln":
                odbc_db_name=sys.argv[1]
                odbc_user_name = sys.argv[2]
                if sys.argv[3] == "-p":
                        odbc_pwd = getpass.getpass("Enter the database password: ")
                else:
                        odbc_pwd = sys.argv[3]
        elif mode=="pwd":
                odbc_db_name = input("Enter the ODBC database name: ")
                odbc_user_name = input("Enter the database user ID: ")
                odbc_pwd = getpass.getpass("Enter the database password: ")
        elif mode=="nopwd":
                odbc_db_name = input("Enter the ODBC database name: ")
        if other=="":
                additional=other
        else:
                additional=";"+other
        try:
                odbc_db_name
        except NameError:
                print("Illegal mode")
        else:
                argstring="DSN="+odbc_db_name
        if 'odbc_user_name' in locals():
                argstring=argstring+";Uid="+odbc_user_name
        if 'odbc_pwd' in locals():
                argstring=argstring+";PWD="+odbc_pwd
        argstring=argstring+additional
        print("argument string = %s" % argstring)
        try:
                if autocommit in ["True", "Yes"]:
                        c = pyodbc.connect(argstring,autocommit=True)
                else:
                        c= pyodbc.connect(argstring)
        except:
                print("ODBC connection failed*.")
        else:
                print("ODBC connection: %s established." % c)
                return c
    
# Close the connection.    
def close_connection(c):
    c.close()
    print("Closing the connection.")

