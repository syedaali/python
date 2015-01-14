__author__ = 'syedaali'

'''
Using the Python language, have the function SwapCase(str) take the str
parameter and swap the case of each character. For example: if str
is "Hello World" the output should be hELLO wORLD. Let numbers and
symbols stay the way they are.
'''

def SwapCase(s):

    n = ''
    for c in s:
        if c.isalpha():
            if c.islower():
                n += c.upper()
            elif c.isupper():
                n += c.lower()
        else:
            n += c
    return n

# another way of doing the same
# return ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in str])

print SwapCase('Hello2 World!')
