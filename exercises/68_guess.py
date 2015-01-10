__author__ = 'syedaali'

'''
The computer will pick a number between 1 and 100. (You can choose any
high number you want.) The purpose of the game is to guess the number
the computer picked in as few guesses as possible.
'''

import random
import sys

n = random.randrange(0,101)

def guess(u):
    if u == n:
        return True
    elif u > n:
        return 'too high'
    elif u < n:
        return 'too low'

tries = 1

while True:
    u = raw_input('guess a number: ')
    u = int(u)
    result = guess(u)
    if result == True :
        print 'You guessed it in {} tries!'.format(tries)
        sys.exit(0)
    else:
        print result
    tries += 1