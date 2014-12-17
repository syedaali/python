__author__ = 'syedaali'

'''
Write a program that maps a list of unique words into a list of integers
representing the lengths of the corresponding words.
'''

import collections

list_of_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

d = collections.defaultdict(int)

for words in list_of_words:
    d[words] = len(words)

for k, v in sorted(d.iteritems(), key=lambda x: x[1], reverse=True):
    print k, v
