__author__ = 'syedaali'

'''
Reverse a file, shows 3 methods.
Method 1 and 2 both read the entire file in memory.
Method 3 reads one character at a time, and is therefore not subject to out
of memory errors due to reading large files.
Comment out method 1 and method 2 and use method 3.
'''

'''
EASY WAY
Linux has 'tac' command which reverses a file, be smart and use that :)
'''
filename = 'input.txt'

'''
METHOD 1
Simple way is to read the entire file in memory and print it backwards.
'''


for line in reversed(open(filename).readlines()):
    print line.rstrip()

'''
METHOD 2
same way as above, but makes the code more readable, and handles errors
better when it comes to opening file
'''

with open(filename,'r') as f:
    for line in reversed(f.readlines()):
        print line,

'''
METHOD 3
Start from end of file and read one character at a time
'''

import os


def reverse_line(filename):
    with open(filename) as afile:
        afile.seek(0, os.SEEK_END)
        position = afile.tell()
        line = ''
        while position >= 0:
            afile.seek(position)
            next_char = afile.read(1)
            if next_char == "\n":
                yield line[::-1]
                line = ''
            else:
                line += next_char
            position -= 1
        yield line[::-1]


counter = 0
for aline in reverse_line(filename):
    if counter == 0:
        counter += 1
        continue
    print aline
