__author__ = 'syedaali'

'''
Please write a program which accepts a string from console and print it
in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir
'''

s = 'rise to vote sir'

if not isinstance(s, str):
    raise ValueError("input is not a string")

print s[::-1]
