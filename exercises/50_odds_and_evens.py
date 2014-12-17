__author__ = 'syedaali'

'''
Return the number of even ints in the
given array. Note: the % "mod" operator
computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4])  3
count_evens([2, 2, 0]) 3
count_evens([1, 3, 5]) 0
'''


def function(n):
    if n % 2 == 0:
        return True
    return False


def count_evens(l):
    s = filter(function, l)
    return len(s)

print count_evens([2, 1, 2, 3, 4])
print count_evens([2, 2, 0])
print count_evens([1, 3, 5])
