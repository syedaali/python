__author__ = 'syedaali'

'''
Using the Python language, have the function SecondGreatLow(arr)
take the array of numbers stored in arr and return the second lowest
and second greatest numbers, respectively, separated by a space.
For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98.
The array will not be empty and will contain at least 2 numbers. It can
get tricky if there's just two numbers!

'''

def SecondGreatLow(arr):

    if len(arr) == 2:
        return '{} {}'.format(max(arr), min(arr))

    amax = max(arr)
    arr = [ x for x in arr if x != amax]

    amin   = min(arr)
    arr = filter(lambda x: x!=amin, arr)

    amax = max(arr)
    amin = min(arr)


    return '{} {}'.format(amin, amax)


print SecondGreatLow([80,80])

'''
    nums = sorted(set(arr))
    if len(nums) < 2:
        nums += nums
    return '%d %d' % (nums[1], nums[-2])
'''

