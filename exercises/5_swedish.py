__author__ = 'syedaali'

'''
Write a function translate() that will translate
a text into Swedish for "robber's language".
That is, double every consonant and place an occurrence of "o"
in between. For example, translate("this is fun") should
return the string "tothohisos isos fofunon".
'''


def translate(s):
    consonants = 'bcdfghjklmnpqrstvwxz'
    return ''.join(l + 'o' + l if l in consonants else l for l in s)

s = 'this is fun'

print(translate(s))
