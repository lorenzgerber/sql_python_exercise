# A simple program which connects to an ODBC database 
# and then executes a simple query
# which illustrates that null values are recaptured
# via the None value of Python.
# Stephen J. Hegner 15 June 2011.
# Modified for Python 3 compatibility 21 February 2014.

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

query = "SELECT LName, FName, MInit, SSN, Super_SSN FROM Employee"

def print_result(r):
    n_length = 25 - (len(r[0]) + len(r[1]) + 10)
    pad = "".join(" " for i in range(n_length))
    print("     %s %s. %s %s %s   %s" % (r[1], r[2], r[0], pad, r[3], r[4]))

def process_query():
    cursor1.execute(query)
    print("Employees and their bosses:")
    print("         Name                SSN        Boss ")
    n=0
    while 1:
        row = cursor1.fetchone()
        if not row:
            break
        n = n+1
        print_result(row)
    if n==0:
        print("No tuples matching the given query were found.")

print("")

# Choose the way to connect:
connection1 = my_odbc_connect.establish_connection("pwd")

print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
process_query()
print("")
my_odbc_cursor.close_cursor(cursor1)
print("")
my_odbc_connect.close_connection(connection1)


