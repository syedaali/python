__author__ = 'syedaali'

# Write a function that takes a character (i.e. a string of length 1) and
# returns True if it is a vowel, False otherwise.


def is_vowel(c):
    vowels = 'aeiou'
    if c in vowels:
        return True
    else:
        return False

print is_vowel('a')

'''
# Another way of doing the same thing

def check_vowel(s):
    vowels = 'aeiou'
    for letter in vowels:
        if letter == s:
            return True
    return False

print check_vowel('b')
'''
