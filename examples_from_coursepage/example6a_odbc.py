# A simple program which connects to an ODBC database
# and then executes a simple update query.
# It illustrates how to enable autocommit in pyodbc.
# Stephen J. Hegner 15 June 2011.
# Modified for Python 3 compatibility 21 February 2014.
# Repaired to handle autocommit correctly 22.02.2015

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

query = "UPDATE Works_On SET hours=? where ESSN=? and PNo=?"
queryp = "SELECT * FROM Works_On where ESSN=? and PNo=?"

def read_input():
    print("Type the changes to a tuple in the works_on relation:")
    essn  = input("Enter the employee SSN: ")
    pno   = input("Enter the project number: ")
    hours = input("Enter the number of hours: ")
    return [hours,essn,pno]

def process_query():
    print("Executing the update.")
    print(cursor1.execute(query,arglist[0],arglist[1],arglist[2]))

def print_result():
    cursor1.execute(queryp,arglist[1],arglist[2])
    print("The updated tuple is", cursor1.fetchone())

print("")
# Choose the way to connect.
connection1 = \
  my_odbc_connect.establish_connection("pwd",other="",autocommit="True")
print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
arglist = read_input()
print("")
process_query()
print("")
print_result()
print("")
my_odbc_connect.close_connection(connection1)
