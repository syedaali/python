__author__ = 'syedaali'


'''
Using the Python language, have the function LetterCountI(str) take the
 str parameter being passed and return the first word with the greatest
 number of repeated letters. For example: "Today, is the greatest day ever!"
 should return greatest because it has 2 e's (and 2 t's) and it comes before
 ever which also has 2 e's. If there are no words with repeating letters
 return -1. Words will be separated by spaces.

'''

def LetterCountI(str):

    c_dict = {}
    for c in str:
        if not c.isalpha():
            continue
        c_dict[c] = str.count(c)

    k = c_dict.keys()
    v = c_dict.values()
    letter = k[v.index(max(v))]

    words_list = str.split()

    for word in words_list:
        if letter in word:
            return word

    return -1


print LetterCountI('I lied before')