# A simple program which connects to an ODBC database
# and then executes a simple update query.
# Note that it is not possible to recapture that the update "failed"
# if it simply results in no changes.
# It also illustrates that updates must be committed explicitly.
# Stephen J. Hegner 15 June 2011, 02 October 2011.
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

def commit_updates(c):
    print("Committing the updates")
    c.commit()

# Choose the way to connect.
connection1 = my_odbc_connect.establish_connection("pwd")
print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
arglist = read_input()
print("")
process_query()
print("")
print_result()
print("")
my_odbc_cursor.close_cursor(cursor1)
print("")
# Close without commit.
my_odbc_connect.close_connection(connection1)

print("Re-establish connection:")
# Choose the way to connect.
connection1 = my_odbc_connect.establish_connection("pwd")
print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
print("The result with no commit:")
print_result()
print("")
my_odbc_cursor.close_cursor(cursor1)
print("")
my_odbc_connect.close_connection(connection1)

print("Re-establish connection again:")
# Choose the way to connect.
connection1 = my_odbc_connect.establish_connection("pwd")
print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
print("Execute the query again.")
process_query()
print("")
print("This is the result of the update without a commit")
print_result()
print("")
print("This time, commit before closing.")
commit_updates(connection1)
print("")
my_odbc_cursor.close_cursor(cursor1)
print("")
my_odbc_connect.close_connection(connection1)

print("Re-establish connection again:")
# Choose the way to connect.
connection1 = my_odbc_connect.establish_connection("pwd")
print("")
cursor1 = my_odbc_cursor.establish_cursor(connection1)
print("")
print("Check the committed result:")
print_result()
print("")
my_odbc_cursor.close_cursor(cursor1)
print("")
my_odbc_connect.close_connection(connection1)
