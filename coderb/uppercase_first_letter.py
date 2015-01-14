__author__ = 'syedaali'

'''
Using the Python language, have the function LetterCapitalize(str)
take the str parameter being passed and capitalize the first letter
 of each word. Words will be separated by only one space.

'''

s = 'oxford comma'

def LetterCapitalize(s):
    words_list = []
    new_s = []

    words_list = s.split()
    for word in words_list:
        word = word[0:1].upper() + word[1:]
        new_s.append(word)
    return ' '.join(new_s)

print LetterCapitalize(s)


# method 2

print ' '.join([word[0].upper()+word[1:] for word in s.split()])

print ' '.join([x[0].upper()+x[1:] for x in s.split()])