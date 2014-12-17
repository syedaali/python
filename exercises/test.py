import re

from numbers import Number

x = 5

if isinstance(x, Number):
    print 'y'


def namedf(**p):
    print 'my params are:'
    for k, v in p.iteritems():
        print k, v

namedf(x=1, y=2, z=3)


def mix_up(a, b):
    if len(a) or len(b) < 3:
        raise ValueError("length too small")
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    new_both = new_a + ' ' + new_b
    return new_both

try:
    print mix_up('mi', 'po')
except Exception, e:
    print e
