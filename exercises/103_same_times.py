__author__ = 'syedaali'

'''
Return True if the string "cat" and "dog"
appear the same number of times in the given string.

cat_dog('catdog') True
cat_dog('catcat') False
'''

import re

s0 = 'catdog'
s1 = 'catcat'
s2 = '1cat1catdogdog'


def cat_dog(s):
    cat = s.count('cat')
    dog = s.count('dog')
    if cat == dog:
        return True
    else:
        return False

print cat_dog(s0)
print cat_dog(s1)
print cat_dog(s2)
