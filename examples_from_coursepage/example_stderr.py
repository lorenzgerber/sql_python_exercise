# A simple example which shows how to write to standard error.
# Stephen J. Hener 21 February 2014

from __future__ import print_function

import sys

print("Hello Stderr!", file=sys.stderr)
