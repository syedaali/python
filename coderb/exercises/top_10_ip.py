'''
print the top 10 most occuring IP's in an apache log file
'''

fh = open ("log.txt",'r')

for line in fh:
    print line

