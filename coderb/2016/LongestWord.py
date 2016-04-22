'''
Have the function LongestWord(sen) take the sen parameter being passed and
 return the largest word in the string. If there are two or more words that
  are the same length, return the first word from the string with that length.
  Ignore punctuation and assume sen will not be empty.
'''


def LongestWord(sen):

    punctations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_sen = ''
    max_lenght = 0

    for character in sen:
        if character not in punctations:
            new_sen += character

    for word in new_sen.split():
        if len(word) > max_lenght:
            largest_word = word

    return largest_word

print LongestWord('a ab abc abcd!')