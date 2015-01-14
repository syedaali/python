__author__ = 'syedaali'

'''
return true if equal number of x and o, else return false
'''

def ExOh(str):
    x = sum([1 for c in str if c == 'x'])
    o = sum([1 for c in str if c == 'o'])
    if x == o:
        return 'true'
    else:
        return 'false'

print ExOh('xooxxo')

#METHOD 2

str = 'xoxoxoxox'

print "true" if str.count('x') == str.count('o') else "false"