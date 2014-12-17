__author__ = 'syedaali'

'''
Please write a program using generator to print the numbers which can be
 divisible by 5 and 7 between 0 and n in comma separated form while n is
 input by console.

'''

n = raw_input('enter n: ')


def gen(b):
    for number in range(0, b):
        if number % 5 == 0 and number % 7 == 0:
            print number

gen(int(n))
