__author__ = 'syedaali'

'''
Define a function which can generate and print a list where the values
are square of numbers between 1 and 20 (both included).
'''


def func():
    d = {}
    for number in range(1, 21):
        d[number] = number ** 2
    l = list(d.values())
    print l

func()
