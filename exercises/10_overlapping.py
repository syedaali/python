__author__ = 'syedaali'

'''
Define a function overlapping() that takes two lists
and returns True if they have at least one member in
common, False otherwise. For the sake of the
exercise, you should (also) write it using two nested for-loops.
'''


def overlapping(l1, l2):
    for outer in l1:
        for inner in l2:
            print 'checking outer {} and inner {}'.format(outer, inner)
            if outer == inner:
                return True
    return False

print overlapping([1, 2, 3], [4, 5, 6, 1])
