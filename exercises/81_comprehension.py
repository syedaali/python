__author__ = 'syedaali'

'''
By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155].
'''

l = [12,24,35,24,88,120,155]

print [x for x in l if x != 24]

s = 'abcd'

s = s.replace('a','b')

print s