__author__ = 'syedaali'

'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit
as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

s = raw_input()

s_list = []

for index in range(1, 5):
    s_list.append(s * index)

s_list = [int(x) for x in s_list]

print sum(s_list)
