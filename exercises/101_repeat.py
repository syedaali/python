__author__ = 'syedaali'

'''
Given a string, return a string where for every char in the
original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

'''

s = 'The world'


def double_char(s):
    y = ''
    for item in s:
        y += item * 2

    return y

print double_char(s)
