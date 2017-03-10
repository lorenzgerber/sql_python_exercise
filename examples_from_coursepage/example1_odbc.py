# A basic program which connects to an ODBC database using ident authentication.
# The ODBC database name must be described in the ODBC configuration file.
# ~/.odbc.ini under Unix/Linux.
# Stephen J. Hegner 15 June 2011.
# Modified for partial Python 3 compatibility 21 February 2014.

### This script has been tested with both Python2 and Python3
### under PostgreSQL and MySQL running on Debian 7 Linux.
### IMPORTANT: For PostgreSQL:
###      the ANSI driver psqlodbca.so must be used for Python2;
###      the Unicode driver psqlodbcw.so must be used for Python3.
### For other Linux distributions which use Unicode in the OS (e.g., Ubuntu)
### it may be necessary to use psqlodbcw.so for Python2 as well.
### For MySQL, the driver libmyodbc.so works for both Python2 and Python3.

import sys
import pyodbc

# Since Python3 replaces raw_input with just input
# this trick handles both Python2 and Python3.
if  sys.version_info<(3,0,0):
    input = raw_input

def establish_connection():
    odbc_db_name = input("Enter the ODBC database name: ")
    try:
        c = pyodbc.connect("DSN="+odbc_db_name)
    except:
        print("ODBC connection failed.")
    else:
        print("ODBC connection: %s" % c)
        return c

def close_connection(c):
    print("Closing the connection.")
    c.close()

connection1 = establish_connection()
close_connection(connection1)
