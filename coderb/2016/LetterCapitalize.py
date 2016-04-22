'''
Have the function LetterCapitalize(str) take the str parameter being passed
and capitalize the first letter of each word. Words will be separated by only
one space.
'''

def LetterCapitalize(str):

    new_str = []

    for word in str.split():
        new_word = word[0:1].upper() + word[1::]
        new_str.append(new_word)

    return ' '.join(new_str)

print LetterCapitalize('hello dear how are you')