__author__ = 'syedaali'

'''
Assuming that we have some email addresses in the "username@companyname.com"
format, please write program to print the company name of a given email
address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed
to be a console input.
'''


s = raw_input('enter email: ')

import re

p = re.compile('(?P<user>\w+)@(?P<company>\w+)\.(?P<tld>\w+)')

try:
    r = re.search(p, s)
except Exception, e:
    print 'no match found'

if r:
    print r.group('company')
