__author__ = 'syedaali'

'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
print this list after removing all duplicate values with original order
reserved.

'''

l = [12,24,35,24,88,120,155,88,120,155]

l = l[::-1]

s = set(l)

for item in s:
    print item,
