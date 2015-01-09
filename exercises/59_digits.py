__author__ = 'syedaali'

'''
Write a program which accepts a sequence of comma separated 4 digit binary
 numbers as its input and then check whether they are divisible by 5 or not.
 The numbers that are divisible by 5 are to be printed in a comma separated
 sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

'''

s = raw_input('enter: ')

s_list = s.split(',')

a_list = []

for i,num in enumerate(s_list):
    i_num = int(num,2)
    print 'num is {}'.format(i_num)
    if i_num % 5 == 0:
        a_list.append(num)


print a_list