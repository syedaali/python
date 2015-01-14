__author__ = 'syedaali'

'''
Using the Python language, have the function LetterChanges(str) take the str
 parameter being passed and modify it using the following algorithm.
 Replace every letter in the string with the letter following it in the
 alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in
 this new string (a, e, i, o, u) and finally return this modified string.
'''

s = 'fun times'
n = ''

for c in s:
    if c.isalpha():
        n += chr(ord(c) + 1)
    else:
        n += c

print ''.join([x.upper() if x in 'aeiou' else x for x in n])