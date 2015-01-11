__author__ = 'syedaali'

'''
Please write a program which count and print the numbers of each character
in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

'''

s = 'abcdefgabc'
d = {}

for letter in s:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] += 1

for k,v in d.iteritems():
    print k,v