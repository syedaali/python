__author__ = 'syedaali'

'''
Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

import sys
import signal


def handler(a_signal, stack):
    print 'bye'
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

# method 1
s = sys.argv[1]
s = s.upper()
print s

# method 2
x = [x.upper() for x in s]
print ''.join(x)

# method 3
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print sentence

# method 4
# while True:
#    s = raw_input('enter string: ')
#    print s.upper()
