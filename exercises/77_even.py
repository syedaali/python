__author__ = 'syedaali'

'''
Please write a program which accepts a string from console and print the
characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

'''

import sys
s = 'H1e2l3l4o5w6o7r8l9d'

#method 1
for index,letter in enumerate(s):
    if index % 2 == 0:
        sys.stdout.write(letter)

#method 2
print s[::2]