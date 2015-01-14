__author__ = 'syedaali'

import numpy as np
import collections


def f_mean(l):
    return float(sum(l)/len(l))


def f_median(l):
    n = np.array(l)
    return np.mean(n)

def f_mode(l):

    # if list is unique, then there is no mode
    if len(l) == len(set(l)):
        return 'None'

    #create dictionary based on numbers of values of each
    c = collections.Counter(l)

    #return key of dict that has the max value
    single = max(c.iterkeys(),key=lambda k: c[k])

    return single

alist = [1,2,2,3,3,4,5]

print f_mean(alist)

print f_median(alist)

print f_mode(alist)