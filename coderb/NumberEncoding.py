'''
Using the Python language, have the function NumberEncoding(str) take the str
parameter and encode the message according to the following rule: encode
every letter into its corresponding numbered position in the alphabet.
Symbols and spaces will also be used in the input. For example: if
str is "af5c a#!" then your program should return 1653 1#!.
'''

d = {}
counter = 1

from string import ascii_lowercase
for c in ascii_lowercase:
    d[c] = counter
    counter += 1

def NumberEncoding(mystr):
    ret_str = ''
    for char in mystr:
        if char in d:
            ret_str += str(d[char])
        else:
            ret_str += char
    return ret_str

print NumberEncoding(raw_input())
