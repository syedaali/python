__author__ = 'syedaali'

'''
Given two strings, return True if either of
the strings appears at the very end of the
other string, ignoring upper/lower case
differences (in other words, the computation
should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc')  True
end_other('AbC', 'HiaBc')  True
end_other('abc', 'abXabc')  True

'''


def end_other(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1.endswith(s2) or s2.endswith(s1):
        return True
    return False

print end_other('Hiabc', 'abc')
print end_other('AbC', 'HiaBc')
print end_other('abc', 'abXabc')



# another way of doing the same as above
