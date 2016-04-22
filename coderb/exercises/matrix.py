'''
Write a python program that prints a 12x12 multiplication table matrix.
'''

for i in xrange(1,12):
    for j in xrange(1,12):
        print i,j

for row in range(1,12):
    for col in range(1,n+1):
        print(row*col, end="\t")
    print()

