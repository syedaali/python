__author__ = 'syedaali'

'''
Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

'''

import string

s = raw_input('enter: ')

letters = 0
digits = 0

for word in s:
    if word.isalpha():
        letters += 1
    elif word.isdigit():
        digits += 1

print 'Letter {}'.format(letters)
print 'Digits {}'.format(digits)