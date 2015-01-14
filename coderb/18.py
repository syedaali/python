__author__ = 'syedaali'

'''
Using the Python language, have the function CountingMinutesI(str) take the
str parameter being passed which will be two times (each properly formatted
with a colon and am or pm) separated by a hyphen and return the total number
of minutes between the two times. The time will be in a 12 hour clock format.
For example: if str is 9:00am-10:00am then the output should be 60. If str is
1:00pm-11:00am the output should be 1320.
'''

def CountingMinutesI(str):

    s, e = str.split('-')

    from datetime import datetime, timedelta

    try:
        dt_start = datetime.strptime(s,'%H:%M%p')
    except ValueError:
        print 'did not work s'

    try:
        dt_end = datetime.strptime(e,'%H:%M%p')
    except ValueError:
        print 'did not work e'

    a = timedelta(dt_start)
    b = timedelta(dt_end)

    print a - b

    daysdiff = (dt_end - dt_start).seconds

    return daysdiff / 60


print CountingMinutesI('1:00pm-11:00am')