__author__ = 'syedaali'

'''
Write a function char_freq() that takes a string and
builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
'''

import collections


def char_freq(a_string):
    d = collections.defaultdict(int)
    for item in a_string:
        d[item] += 1

    for k, v in sorted(d.iteritems(), key=lambda x: x[1], reverse=True):
        print k, v

s = 'abbabcbdbabdbdbabababcbcbab'

char_freq(s)
