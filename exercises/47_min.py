__author__ = 'syedaali'

'''
The Smallest Number in a Circular List in Python
'''

alist = [22, 52, 66, 82, 5, 8, 12, 19]

def mymin(alist):
    min_num = alist[0]
    for item  in alist:
        if item < min_num:
            min_num = item

    return min_num

print mymin(alist)
