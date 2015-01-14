__author__ = 'syedaali'

import collections
l = [1,2,2,3,4,5,5,5,6]
c = collections.Counter(l)
for k,v in c.iteritems():
    print '{} occurs {} time(s)'.format(k,v)
