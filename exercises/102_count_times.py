__author__ = 'syedaali'

'''
Return the number of times that the
string "hi" appears anywhere in
the given string.
'''

import re

s = 'abc hi ho hi'
s1 = 'hithere bob, my name is alice, bye hi hehiho'


def count_hi(s):
    l = re.findall('hi', s)
    return len(l)

print count_hi(s1)
