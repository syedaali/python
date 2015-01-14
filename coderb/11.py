__author__ = 'syedaali'

'''
count vowels in a string
'''

def VowelCount(str):
    return len([x for x in str if x.lower() in ('aeiou')])

print VowelCount('hello')

#METHOD 2

str = 'hello'

print sum([1 for ch in str if ch.lower() in 'aeiou'])