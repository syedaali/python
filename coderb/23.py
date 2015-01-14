__author__ = 'syedaali'

'''
Using the Python language, have the function DashInsert(str) insert
dashes ('-') between each two odd numbers in str.
For example: if str is 454793 the output should be 4547-9-3.
Don't count zero as an odd number.
'''


def DashInsert(num):

    a = map(int, list(str(num)))

    for i in xrange(len(a)-1, 0, -1):
        if a[i-1] & 1 and a[i] & 1:
            a = a[:i] + ['-'] + a[i:]
    return ''.join(map(str, a))


print DashInsert('12357')