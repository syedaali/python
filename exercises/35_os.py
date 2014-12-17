__author__ = 'syedaali'

'''
print file size of input file
'''

import os
import sys

infile = raw_input('enter file name: ')
print 'path in bytes is {0}'.format(os.path.getsize(infile))
