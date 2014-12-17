__author__ = 'syedaali'

'''
Python has 3 types of parameters passed to a function:
1. named
2. optional
3. positional
This script demonstrates each of them.
'''


def namedp(**p):
    for k, v in p.iteritems():
        print k, v


def optionalp(y, z, x=0):
    print x + y + z


def positionalp(*p):
    for item in p:
        print item

namedp(x=1, y=2, z=3)

optionalp(y=1, z=2)

positionalp(1, 2, 3)
