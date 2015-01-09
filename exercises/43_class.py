__author__ = 'syedaali'

'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

'''


class Mine(object):

    def __init__(self):
        self.a_string = ''

    def getString(self):
        self.a_string = raw_input('Enter string')

    def printString(self):
        print self.a_string.upper()

s = Mine()

s.getString()

s.printString()
