__author__ = 'syedaali'

'''
Write a program that will calculate the average word length of a text stored
in a file (i.e the sum of all the lengths of the word tokens in the text,
divided by the number of word tokens).
'''

len_list = []

with open('file.txt','r') as f:
    for line in f:
        word_list = line.split()
        for word in word_list:
            len_list.append(len(word))

average = sum(len_list)/len(len_list)
print average
