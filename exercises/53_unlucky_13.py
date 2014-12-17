__author__ = 'syedaali'

'''
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that
come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) 6
sum13([1, 1]) 2
sum13([1, 2, 2, 1, 13]) 6
'''


def sum13(l):
    total = 0
    if not l:
        return 0
    for nums in l:
        if nums == 13:
            print 'found 13, returning total {0}'.format(total)
            return total
        total += nums
    return total

print sum13([1, 2, 2, 1])
print sum13([1, 1])
print sum13([1, 2, 2, 1, 13])
print sum13([1, 2, 13, 2, 1, 13])
print sum13([])
