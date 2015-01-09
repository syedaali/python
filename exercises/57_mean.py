__author__ = 'syedaali'

'''
Mean of a files 4th element
'''

num_list = []

with open('input.txt','r') as f:
    for line in f:
        a,b,c,d = line.split(',')
        num_list.append(float(d))

mean = sum(num_list)/len(num_list)

print mean


