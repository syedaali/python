'''
Have the function LetterChanges(str) take the str parameter being passed and
modify it using the following algorithm. Replace every letter in the string
with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally
return this modified string.

Use the Parameter Testing feature in the box below to test your code with
different arguments.

'''

def LetterChanges(str):
    new_str = ''

    for character in str:
        if character.isalpha():
            new_str += chr(ord(character) + 1)

    upper_case_str = ''.join([x.upper() if x in 'aeiou' else x for x in
                              new_str])

    return upper_case_str

print LetterChanges('abcd')