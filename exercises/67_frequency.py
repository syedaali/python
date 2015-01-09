__author__ = 'syedaali'

'''
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2

to:1
'''

import collections
s = raw_input()

s_list = s.split()

d = collections.defaultdict(int)

for words in s_list:
    d[words] += 1

for k,v in sorted(d.iteritems(),key=lambda x:x[0]):
    print '{}:{}'.format(k,v)