# purpose: to demonstrate use of Python modules
# given an input file called 'infile.txt', find the top 10 most
# commonly occuring words and print them out

author__ = 'syedaali'

import re
import collections

words = re.findall(r'\w+', open('infile.txt').read().lower())

print collections.Counter(words).most_common(10)

