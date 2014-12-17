__author__ = 'syedaali'

'''
Write a function to compute 5/0 and use try/except to catch the exceptions.

'''


def compute(a, b):
    try:
        ret = a / b
    except ZeroDivisionError, e:
        return e

print compute(5, 0)
