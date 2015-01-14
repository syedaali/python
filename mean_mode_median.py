__author__ = 'syedaali'

import numpy as np
import collections


def f_mean(l):
    return float(sum(l)/len(l))


def f_median(l):
    n = np.array(l)
    return round(np.mean(n),1)

def f_mode(l):

    # if list is unique, then there is no mode
    if len(l) == len(set(l)):
        return 'None'

    #create dictionary based on numbers of values of each
    c = collections.Counter(l)

    #return key of dict that has the max value
    #another way of doing c.most_common
    single = max(c.iterkeys(),key=lambda k: c[k])

    #get the key of the dups
    match = c[single]
    mlist = []
    for k,v in [(k,v) for k,v in c.iteritems() if v == match]:
        mlist.append(k)

    #return c.most_common(1)[0][0]
    return ','.join(map(str,mlist))

alist = [1,2,3,3,4,5,5]
print 'mean is {}'.format(f_mean(alist))
print 'median is {}'.format(f_median(alist))
print 'mode is {}'.format(f_mode(alist))