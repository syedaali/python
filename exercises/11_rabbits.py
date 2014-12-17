__author__ = 'syedaali'

'''
Define a function generate_n_chars() that takes an integer n
and a character c and returns a string, n characters long,
consisting only of c:s. For example, generate_n_chars(5,"x")
should return the string "xxxxx". (Python is unusual in that
you can actually write an expression 5 * "x" that will
evaluate to "xxxxx". For the sake of the exercise you
should ignore that the problem can be solved in this manner.)
'''


def generate_n_chars(i, c):
    s = ''
    for item in range(0, i, 1):
        s += c
    return s

print generate_n_chars(5, 'a')
