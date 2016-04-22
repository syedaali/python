'''
Have the function SimpleAdding(num) add up all the numbers from 1 to num.
For the test cases, the parameter num will be any number from 1 to 1000.

'''

def SimpleAdding(num):

    my_sum = 0

    for num in xrange(1,num+1):
        my_sum += num

    return my_sum

print SimpleAdding(10)