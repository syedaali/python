__author__ = 'syedaali'

'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print
the first half values in one line and the last half values in one line.
'''

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

half = len(t) / 2

print t[:5]
print t[5:]
