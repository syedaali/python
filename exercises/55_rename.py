__author__ = 'syedaali'

'''
Given an array of ints, return True if the array contains a 2 next to a
2 somewhere.


has22([1, 2, 2])  True
has22([1, 2, 1, 2]) False
has22([2, 1, 2]) False

'''


def has22(l):
    for index, num in enumerate(l):
        if num == 2:
            if index + 1 == len(l):
                return False
            if l[index + 1] == 2:
                return True
    return False

print has22([1, 2, 2])
print has22([1, 2, 1, 2])
print has22([2, 1, 2])
