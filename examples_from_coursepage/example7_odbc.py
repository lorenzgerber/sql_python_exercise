# A simple program which connects to an ODBC database
# and then executes a simple insert query.
# Note that it is possible to recapture that the insert "failed" if it violates
# integrity constraints.
# It also illustrates that updates must be committed explicitly.
# Stephen J. Hegner 15 June 2011.
# Modified for Python 3 compatibility 21 February 2014.
# Modified to show how to insert NULL, 24 April 2016.

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

if  sys.version_info<(3,0,0):
        input = raw_input

import my_odbc_connect
import my_odbc_cursor

query = "Insert into Works_On values (?,?,?)"

def read_input():
    print("Type the fields of a tuple to insert into the works_on relation:")
    essn  = input("Enter the employee SSN: ")
    pno   = input("Enter the project number: ")
    hours = input("Enter the number of hours: ")
# Pyodbc uses None to represent SQL NULL:
    if hours.upper()=='NULL':
            hours=None
    return [essn,pno,hours]

def process_query():
    global success
    print("Executing the update.")
    cursor1 = connection1.cursor()
    arglist = read_input()
## Some gymnastics to accommodate both Python2 and Python3:
    try:
        cursor1.execute(query,arglist[0],arglist[1],arglist[2])
        print("The insertion executed successfully.")
        success=1
## Python version incompatibilty:
## Comment out the second line for Python2 and the first for Python3:
#    except pyodbc.IntegrityError, why:
    except pyodbc.IntegrityError as why:
        print("The update would violate an integrity constraint.")
        print("The reason is:", why)
        success=0

def commit_updates(c):
    print("Committing the updates.")
    c.commit()

print("")
connection1 = my_odbc_connect.establish_connection("pwd")
print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
process_query()
print("")
if success==1:
        commit_updates(connection1)
print("")
my_odbc_cursor.close_cursor(cursor1)
print("")
my_odbc_connect.close_connection(connection1)


