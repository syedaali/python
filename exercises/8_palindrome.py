__author__ = 'syedaali'

# identify a palindrome


def is_palindrome(s):
    if s == s[::-1]:
        return True

s = 'radar'

if is_palindrome(s):
    print 'yes'
