__author__ = 'syedaali'

import os
import sys

# to get current path of modules
print os.environ.get('PYTHONPATH')

# get all environment variables
for k, v in os.environ.iteritems():
    print k, '=', v

# to add to path of modules
sys.path.append(r'/Users/syedaali/Documents')

# print in key, value format
keys = sys.modules.keys()
for k in keys:
    print k, '=', sys.modules.get(k)
