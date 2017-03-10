#!/usr/bin/python
# A simple program which connects to an ODBC database
# and then executes a simple query with arguments 
# whose values are obtained interactively.
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
    
query = "SELECT LName, FName, MInit \
              FROM   Employee \
              WHERE  (((SELECT count(*) FROM Dependent WHERE SSN=ESSN) = ?) \
                     AND (Salary >= ?))"

def input_loop():
    flag = 1
    while flag==1:
        print("Enter q to terminate the loop.")
        dep_count = input("Otherwise, enter the number of dependents of the employee: ")
        if dep_count!="q":
            min_salary = input("Enter the minimum salary of the employee: ")
            process_query(dep_count,min_salary)
        else :
            flag = 0

def print_result(r):
    print("          %s %s %s." % (r[0], r[1], r[2]))

def process_query(d,n):
    # The arguments to a query follow the query string in the list of parameters.
    cursor1.execute(query,d,n)
    print("Employees with %s dependents and minimum salary $%s:" % (d,n))
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

#Choose the way to connect:
connection1 = my_odbc_connect.establish_connection("cmdln")

print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
input_loop()
print("")
my_odbc_cursor.close_cursor(cursor1)
print("")
my_odbc_connect.close_connection(connection1)


