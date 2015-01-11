__author__ = 'syedaali'

'''
print top urls from http log file
format of log file is:
64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET \
/twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523

'''

import re
import collections

d = collections.defaultdict(int)

p = re.compile(r''' \"(?P<method>\w+)
                        (?P<url>.*)
                         (?P<version>HTTP.*)\"''',re.VERBOSE)

with open('http.txt','r') as f:
    for line in f:
        m = re.search(p,line)
        d[m.group('url')] += 1

for k,v in sorted(d.iteritems(),key=lambda x:x[1],reverse=True):
    print k,v
