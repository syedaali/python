'''
You will be given an array of several arrays that each contain integers and
 your goal is to write a function that will sum up all the numbers in all
 the arrays. For example, if the input is [[3, 2], [1], [4, 12]] then
 your program should output 22 because 3 + 2 + 1 + 4 + 12 = 22.
'''

my_list = [[3, 2], [1], [4, 12]]
my_sum = 0

for sub_list in my_list:
    for item in sub_list:
        my_sum = my_sum + item

print my_sum

