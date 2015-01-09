__author__ = 'syedaali'

'''
Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''


l = raw_input("enter: ")

l = list(l)

def function(l):
    if l != ',':
        return True

print filter(function,l)

print filter(function,tuple(l))


