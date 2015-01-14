__author__ = 'syedaali'

'''
longest word in string

# METHOD 1

import string

s = 'hi there how arejjjjk youjkljk, blah di blah'
function = lambda  x:x not in string.punctuation
s = filter(function,s)

largest = ''
max_size = 0

for word in s.split():
    word_size = len(word)
    if word_size > max_size:
        max_size = word_size
        largest = word

print largest

'''

# METHOD 2

s = 'fun&!! time'

largest = ''
max_size = 0
new_s = ''

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for c in s:
    if c not in punctuations:
        new_s += c


for word in new_s.split():
    word_size = len(word)
    if word_size > max_size:
        max_size = word_size
        largest = word

print largest

'''

'''
#METHOD 3

sen = 'hi there bobby!'
inc = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sen = ''.join([ch for ch in sen if ch in inc])
largest = ''
largest_size = 0
words = sen.split()
for word in words:
    if len(word) > largest_size:
       largest = word
       largest_size = len(word)

print largest

