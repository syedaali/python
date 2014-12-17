__author__ = 'syedaali'

'''
Return True if the given string contains an
appearance of "xyz" where the xyz is not
directly preceeded by a period (.).
So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') True
xyz_there('abc.xyz') False
xyz_there('xyz.abc') True
'''

import re


def xyz_there(s):
    if re.findall(r'(?<!\.)xyz', s):
        return True
    else:
        return False


print xyz_there('abcxyz')
print xyz_there('abc.xyz')
print xyz_there('xyz.abc')
