__author__ = 'syedaali'
'''
An alternade is a word in which its letters, taken
alternatively in a strict sequence, and used in the
same order as the original word, make up at least
two other words. All letters must be used, but the
smaller words are not necessarily of the same length.
For example, a word with seven letters where every
second letter is used will produce a four-letter word
and a three-letter word. Here are two examples:

  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".
Using the word list at
http://www.puzzlers.org/pub/wordlists/unixdict.txt,
write a program that goes through each word in the
list and tries to make two smaller words using every
second letter. The smaller words must also be members
of the list. Print the words to the screen in the above fashion.
'''

import requests

r = requests.get('http://www.puzzlers.org/pub/wordlists/unixdict.txt')

if r.raise_for_status:
    print 'got url'
else:
    print 'could not get url'

s = str(r.text)
s = s.split()
s = list(s)

word1 = ''
word2 = ''
words = []

for item in s:
    word1 += item[::2]
    word2 += item[1::2]
    print 'item {0} makes {1} and {2}'.format(item, word1, word2)
    if word1 in s:
        words.append(word1)
        print '{0} exists'.format(word1)
    if word2 in s:
        words.append(word2)
        print '{0} exists'.format(word2)

    word1 = ''
    word2 = ''
