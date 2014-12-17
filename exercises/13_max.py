__author__ = 'syedaali'

'''
Write a function max_in_list() that takes a
list of numbers and returns the largest one.
'''


def max_in_list(l):
    n = sorted(l, reverse=True)
    return n[0]

print max_in_list([100, 99, 4, 6, 8, 34, 65, 999])
