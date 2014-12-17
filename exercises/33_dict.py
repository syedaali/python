__author__ = 'syedaali'

'''
Define a function which can print a dictionary where the keys are
numbers between 1 and 3 (both included) and the values are square of keys.
'''


def func():
    d = {}
    for number in range(1, 4):
        d[number] = number ** 2
    return d

for k, v in func().iteritems():
    print k, v
