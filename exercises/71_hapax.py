__author__ = 'syedaali'

'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs
only once in either the written record of a language, the works of an author,
 or in a single text. Define a function that given the file name of a text
 will return all its hapaxes. Make sure your program ignores capitalization.
'''

import collections

d = collections.defaultdict(int)

with open('file','r') as f:
    for line in f:
        word_list = line.split()
        for item in word_list:
            d[item] += 1

for k,v in d.iteritems():
    if v == 1:
        print '{} occurs only once'.format(k)


