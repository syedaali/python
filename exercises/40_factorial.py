__author__ = 'syedaali'

'''
Write a program which can compute the factorial of a given numbers.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

input = raw_input("Enter number: ")
input = int(input)

print 'Factorial of {0} is '.format(factorial(input))