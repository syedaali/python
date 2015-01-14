__author__ = 'syedaali'

from datetime import datetime

s = '09:00am'
e = '10:00am'

try:
    dt_start = datetime.strptime(s,'%I:%M%p')
except ValueError:
    print 'did not work'

try:
    dt_end = datetime.strptime(e,'%I:%M%p')
except ValueError:
    print 'did not work'

daysdiff = (dt_end - dt_start).seconds

print daysdiff / 60




