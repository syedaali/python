__author__ = 'syedaali'

'''
Question:
Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

'''

s = raw_input('enter words separated by comma: ')

s_list = s.split(',')

print ','.join(sorted(s_list))
