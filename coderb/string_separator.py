__author__ = 'syedaali'

'''
Have the function ABCheck(str) take the str parameter being
passed and return the string true if the characters a and b
are separated by exactly 3 places anywhere in the string at
least once (ie. "lane borrowed" would result in true because
there is exactly three characters between a and b).
Otherwise return the string false.
'''

def ABCheck(str):

    for i in xrange(0, len(str)-4):
            if str[i] == 'a' and str[i+4] == 'b':
                return 'true'
    return 'false'



print ABCheck('abccccazzzb')