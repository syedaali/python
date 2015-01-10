__author__ = 'syedaali'

'''
An anagram is a type of word play, the result of rearranging the letters of a
word or phrase to produce a new word or phrase, using all the original
letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a d
ot in place. Write a Python program that, when started 1) randomly picks a
 word w from given list of words, 2) randomly permutes w (thus creating an
  anagram of w), 3) presents the anagram to the user, and 4) enters an
  interactive loop in which the user is invited to guess the original word.
  It may be a good idea to work with (say) colour words only.
'''

import random

ilist = [
    'red', 'brown', 'green', 'pink', 'purple', 'orange', 'white', 'blue'
]

d = {}

# randomize each word and store in dictionary
for word in ilist:
    sword = ''.join(sorted(word,key=lambda x: random.random()))
    d[sword] = word

val = random.sample(d.items(),1)

# using val[0][0] because val is a list with one element which is a tuple

while True:
    print val[0][0],
    s = raw_input(' guess-> ')
    s = s.rstrip('\n')
    if s == val[0][1]:
        print 'you guessed it'
        exit(0)
    else:
        print 'try again'

