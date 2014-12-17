__author__ = 'syedaali'

'''
shows the difference between match, search and findall

'''
import re

m = 'hi my name is bob'
s = 'hello there and hi bob'
f = 'hello and hi to my dear hi five friend hido'

print 'TRYING MATCH'
o = re.match(r'(?P<name>hi)', m)

if o:
    print True
    print o.group('name')
else:
    print False

print 'TRYING SEARCH'
o = re.search(r'hi', s)

if o:
    print True
    print o.group()
else:
    print False

print 'TRYING FINDALL'

o = re.findall(r'hi', f)

if o:
    print o
else:
    print False
