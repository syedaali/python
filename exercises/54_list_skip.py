__author__ = 'syedaali'

'''
Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 7 (every 6 will be followed
by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2])  5
sum67([1, 2, 2, 6, 99, 99, 7])  5
sum67([1, 1, 6, 7, 2])  4
'''

add = True


def sum67(nums):
        state = 0
        s = 0
        for n in nums:
                if state == 0:
                        if n == 6:
                                state = 1
                        else:
                                s += n
                else:
                        if n == 7:
                                state = 0
        return s

print sum67([1, 2, 2, 6, 99, 99, 7])
print sum67([1, 2, 2])
print sum67([1, 1, 6, 7, 2])
print sum67([2, 7, 6, 2, 6, 7, 2, 7])
