__author__ = 'syedaali'


def var_args(*args):
    print type(args)
    for x in args:
        print x


def var_kargs(**kwargs):
    print type(kwargs)
    for k, v, in kwargs.iteritems():
        print k, v


var_args(1, 2, 3)

var_kargs(a=1, b=2, c=3)
