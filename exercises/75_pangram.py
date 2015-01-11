__author__ = 'syedaali'

'''
A pangram is a sentence that contains all the letters of the English
alphabet at least once, for example: The quick brown fox jumps over the l
azy dog. Your task here is to write a function to check a sentence to see
if it is a pangram or not.
'''

import re
import string

s = set('abcdefghijklmnopqrstuvwxyz')

sentence = 'The quick browns fox jumps over the lazy dog'

sentence = sentence.lower()

sentence = re.sub('\s+','',sentence)

function = lambda x: x not in string.punctuation

sentence = filter(function,sentence)

sentence= set(sentence)

if sentence - s:
    print 'no'
else:
    print 'yes'
