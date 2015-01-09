__author__ = 'syedaali'

'''

Write a program that accepts a sequence of whitespace separated words as
input and prints the words after removing all duplicate words and sorting
them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

from collections import OrderedDict

s = 'hello world and practice makes perfect and hello world again'

word_list = []

for word in s.split():
    if not word in word_list:
        word_list.append(word)

print sorted(word_list)
