__author__ = 'syedaali'

'''
Using the Python language, have the function DistinctList(arr)
take the array of numbers stored in arr and determine the total number
of duplicate entries. For example if the input is [1, 2, 2, 2, 3]
then your program should output 2 because there are two duplicates of
 one of the elements.

'''

import collections

def DistinctList(arr):

    counter = collections.Counter(arr)

    dups = []

    for k,v in counter.iteritems():
        if v > 1:
            dups.append(k)

    return ','.join(map(str,dups))

print DistinctList([1, 2, 2, 2, 3,3])