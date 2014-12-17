__author__ = 'syedaali'

'''
Please write a program which prints all permutations of [1,2,3]
'''

import itertools

l = [1, 2, 3]

ml = list(itertools.permutations(l))

for item in ml:
    print item,
