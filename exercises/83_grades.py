__author__ = 'syedaali'


'''
read grades from grades file and sort
format of grades file is :
2:58,1-32,5;14
delimiter is comma
'''

with open('grades.txt','r') as f:
    for line in f:
        line = line.rstrip('\n')
        g_list = line.split(',')
        for index,score in enumerate(g_list):
            score = score.replace(':','.').replace('-','.').replace(';','.')
            g_list[index] = score

print sorted(g_list)