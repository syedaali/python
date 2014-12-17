__author__ = 'syedaali'

'''
A pangram is a sentence that contains all the letters of the
English alphabet at least once, for example: The quick brown
fox jumps over the lazy dog. Your task here is to write a
function to check a sentence to see if it is a pangram or not.
'''

import re
import string

# Create a set for pangram
s = set('abcdefghijklmnopqrstuvwxyz')

# Input string
input_s = 'The quick brown fox jumps over the lazy dog'

# Convert to lowercase
input_s = input_s.lower()

# Remove all spaces
input_s = re.sub('\s+', '', input_s)

# We need to remove all punctuation
function = lambda x: x not in string.punctuation
input_s = filter(function, input_s)

# Convert input string to a set
input_s = set(input_s)

# Subtract input string from all leters, if set is empty, then it is a pangram
if not input_s - s:
    print 'is a pangram'
else:
    print 'is not a pangram'
