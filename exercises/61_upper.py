__author__ = 'syedaali'

'''
Write a program that accepts a sentence and calculate the number of upper case
 letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

'''


s = raw_input('enter: ')

lower = 0
upper = 0

for c in s:
    if c.islower():
        lower += 1
    elif c.isupper():
        upper += 1

print 'upper case {}'.format(upper)
print 'lower case {}'.format(lower)
