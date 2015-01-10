__author__ = 'syedaali'

'''
Leap years occur according to the following formula: a leap year is divisible
 by four, but not by one hundred, unless it is divisible by four hundred.
 For example, 1992, 1996, and 2000 are leap years, but 1993 and 1900 are not.
  The next leap year that falls on a century will be 2400.
'''

def is_leap(year):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        return True


while True:
    s = raw_input()
    s = int(s)
    if is_leap(s):
        print 'y'
    else:
        print 'n'

