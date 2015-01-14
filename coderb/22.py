__author__ = 'syedaali'

'''
Using the Python language, have the function PrimeTime(num) take
the num parameter being passed and return the string true if the
parameter is a prime number, otherwise return the string false.
The range will be between 1 and 2^16.

'''

def PrimeTime(num):
    if num < 1:
        return 'false'
    else:
        for i in range(2,num):
            if num % i == 0:
                return 'false'
        else:
            return 'true'

print PrimeTime(1)