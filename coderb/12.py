__author__ = 'syedaali'

'''
count words in a string
'''

def WordCount(str):
    return sum([1 for x in str.split()])

print WordCount('hi there how are you')

#METHOD 2

str ='hi there how are you'

print len(str.split())