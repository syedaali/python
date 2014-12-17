__author__ = 'syedaali'

'''
Please write a program to generate all sentences where subject is in
["I", "You"] and verb is in ["Play", "Love"] and the object is in
["Hockey","Football"].

'''

import itertools

a = ["I", "You"]
b = ["Play", "Love"]
c = ["Hockey", "Football"]

for item in list(itertools.product(a, b, c)):
        print ' '.join(item)
