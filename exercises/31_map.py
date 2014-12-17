__author__ = 'syedaali'

'''
Write a program which can filter() to make a list whose elements are even
number between 1 and 20 (both included).
'''


print filter(lambda x: True if x % 2 == 0 else False, range(1, 21))
