__author__ = 'syedaali'

'''
Please write a program to print the list after removing delete even
numbers in [5,6,77,45,22,12,24].

'''

l = [5, 6, 77, 45, 22, 12, 24]

# using filter
# print filter(lambda  x: True if x % 2 != 0 else False, l)

print [x for x in l if x % 2 != 0]
