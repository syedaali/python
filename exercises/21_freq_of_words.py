__author__ = 'syedaali'

'''
Write a function char_freq() that takes a string and
builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
'''

import collections
import string
import re

a_string = 'hello, how are you today?'

# remove punctuation
function = lambda x: x not in string.punctuation
a_list = filter(function, a_string)

# remove space
a_list = re.sub('\s+', '', a_list)

counter = collections.Counter(a_list)

for k, v in sorted(counter.iteritems()):
    print k, v
