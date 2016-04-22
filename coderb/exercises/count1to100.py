'''
- Write a program that counts from 1 to 100. For each number, print a certain
 string if the number is evenly divisible by 6. Print a different string if
 the number is evenly divisible by 4. Print yet another string if the number
 is evenly divisible by 24. If none of these cases match, print the number.
'''

import os


def readlines_reverse(filename):
    with open(filename) as qfile:
        qfile.seek(0, os.SEEK_END)
        position = qfile.tell()
        line = ''
        while position >= 0:
            qfile.seek(position)
            next_char = qfile.read(1)
            if next_char == "\n":
                yield line[::-1]
                line = ''
            else:
                line += next_char
            position -= 1
        yield line[::-1]


if __name__ == '__main__':
    for qline in readlines_reverse(raw_input()):
        print qline