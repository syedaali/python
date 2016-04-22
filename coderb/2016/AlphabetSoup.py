'''
Have the function AlphabetSoup(str) take the str string parameter being passed
and return the string with the letters in alphabetical order (ie. hello
becomes ehllo). Assume numbers and punctuation symbols will not be included
in the string.
'''

def AlphabetSoup(string):

    punctuations = '''!@#$%^&*()_~+{}:"<>?'''

    new_string = [x if x not in punctuations for x in string]

    print new_string

AlphabetSoup('hello123!!')
