__author__ = 'syedaali'

'''
Write a program that given a text file will create a new text file in
which all the lines from the original file are numbered from 1 to n
(where n is the number of lines in the file).
'''

line_num = 1

with open('infile','r') as f:
    with open('outfile','w') as w:
        for line in f:
            w.write('{} {}'.format(line_num,line))
            line_num += 1


