__author__ = 'syedaali'

'''
Define a procedure histogram() that takes a list of
integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
'''


def histogram(int_list):
    for integer in int_list:
        print '*' * integer

histogram([4, 5, 6])
