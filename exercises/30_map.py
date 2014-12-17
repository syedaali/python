__author__ = 'syedaali'

'''
Write a program which can map() to make a list whose elements are square
of numbers between 1 and 20 (both included).
'''


def func(i):
    return i ** 2

# method 1
print map(func, range(1, 21))

# method 2
print map(lambda x: x ** 2, range(1, 21))

# method 3
print [x ** 2 for x in range(1, 21)]
