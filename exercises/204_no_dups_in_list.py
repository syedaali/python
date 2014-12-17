__author__ = 'syedaali'

'''
With a given list [12,24,35,24,88,120,155,88,120,155],
write a program to print this list after removing all
duplicate values with original order reserved.


Hints:
Use set() to store a number of values without duplicate.
'''

import collections

l = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

d = collections.OrderedDict.fromkeys(l)

ml = list(d)

print type(ml)

print ml
