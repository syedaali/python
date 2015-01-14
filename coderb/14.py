__author__ = 'syedaali'

'''
check for palindrome
'''

def Palindrome(str):
    str = str.replace(' ','')
    if str == str[::-1]:
        return 'true'
    return 'false'

print Palindrome('bob bob')