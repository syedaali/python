__author__ = 'syedaali'

'''
This program will print out the top 10 most eventful times in Apache HTTPD
log file. The format it expects the log to be in is:
1.1.1.1 - - [28/Dec/2014:03:21:08 +0000] "GET /index.html HTTP/1.0" 200 \
15 "-" "-"
Most eventful times refers to the time that most events occurred in.
'''

import re
import collections

adict = collections.defaultdict(int)

p = re.compile(
    r"""(?P<ip>\d+\.\d+\.\d+\.\d+)\s+
        (?P<username>-)\s+
        (?P<TZ>-)\s+
        (?P<TS>\[.*?\])\s+
        (?P<rest>.*)""",re.VERBOSE)

with open('access_log', 'r') as f:
    for line in f:
        match = re.search(p, line)
        adict[match.group('TS')] += 1

counter = 0
for k,v in sorted(adict.iteritems(),key=lambda  x:x[1],reverse=True):
    counter += 1
    if counter == 10:
        break
    print k,v
