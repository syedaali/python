__author__ = 'syedaali'

'''
Please write a program to print the running time of execution of
"1+1" for 100 times.

'''

from timeit import Timer

t = Timer("for i in range(100): 1+1")

print t.timeit()
