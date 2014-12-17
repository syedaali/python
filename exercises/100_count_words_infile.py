__author__ = 'syedaali'

# count all words in  a file


import string
import collections

infile = 'infile.txt'

# have to use defaultdict for auto-incrementing value based on key

d = collections.defaultdict(int)

function = lambda x: x not in string.punctuation

with open(infile, mode='r') as f:
    for line in f:

        # remove all punctuation
        clean_line = filter(function, line)

        # lower case all, since This is the same as this
        lower_line = clean_line.lower()

        # split line into words and add to dictionary
        for words in lower_line.split():
            d[words] += 1


for k, v in sorted(d.iteritems(), key=lambda x: x[1], reverse=True):
    print k, v
