__author__ = 'syedaali'

'''
By using list comprehension, please write a program to print the list after
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''

l = [12, 24, 35, 70, 88, 120, 155]

print [x for (i, x) in enumerate(l) if i not in (0, 4, 5)]
