__author__ = 'syedaali'

'''
calculator
'''
import re

s = raw_input('Enter numbers to add: ')

s.rstrip('\n')

s = s.replace(' ', '')

print 's is {}'.format(s)

print 's is of type {}'.format(type(s))

print eval(s)
