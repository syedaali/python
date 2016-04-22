'''
import sys

FILE = 'log.txt'

with open(FILE,'r') as fh:
    while EOFError:
        byte = fh.read(1)
        if byte == '':
            exit()
        sys.stdout.write(byte)

fh.close()
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
    for qline in readlines_reverse('log.txt'):
        print qline

