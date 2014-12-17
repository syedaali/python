__author__ = 'syedaali'

'''
Define a function sum() and a function multiply()
that sums and multiplies (respectively) all the
numbers in a list of numbers. For example,
sum([1, 2, 3, 4]) should return 10, and
multiply([1, 2, 3, 4]) should return 24.
'''


def mysum(a_list):
    s = 0
    for item in a_list:
        s += item
    return s


def multiply(a_list):
    s = 1
    for item in a_list:
        s *= item
    return s

# another way of writing mysum and multiply


def asum(a_list):
    return reduce(lambda x, y: x + y, a_list)


def amultiply(a_list):
    return reduce(lambda x, y: x * y, a_list)

a = [1, 2, 3, 4]


print mysum(a)
print asum(a)
print multiply(a)
print amultiply(a)
