__author__ = 'syedaali'

'''
give a num 'n', sum upto that number

'''
n = 12

sum = 0

for item in range(0,n+1):
    sum += item

print sum

# method 2

def mysum(n):
    if n == 0:
        return 0
    else:
        n += mysum(n-1)
    return n

print mysum(n)