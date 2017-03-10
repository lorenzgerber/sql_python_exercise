#!/usr/bin/python
# For invoking this script from the command line using Python3
# change the first line to #!/usr/bin/python3.
# This directive does nothing if the script is called as an argument
# of the Python interpreter.

# A basic program which connects to an ODBC database.
# This illustrates using modules for repeated operations
# and simple parameter changes.
# The ODBC database name must be described in the ODBC configuration file.
# ~/.odbc.ini under Unix/Linux.
# Stephen J. Hegner 21 February 2014.

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

# Import the connection functions.
import my_odbc_connect

# Uncomment to verify the system version.
print(sys.version_info)

# Choose the way to connect:
# nopwd = dbname only; pwd = dbname+username+pwd; cmdln = from command line.
connection1=my_odbc_connect.establish_connection("cmdln")

my_odbc_connect.close_connection(connection1)
