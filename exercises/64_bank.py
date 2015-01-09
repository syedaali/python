__author__ = 'syedaali'

'''
Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as
 following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

d = []
w = []

with open('deposit.txt', 'r') as f:
    for line in f:
        action, amount = line.split()
        if action == 'D':
            d.append(int(amount))
        if action == 'W':
            w.append(int(amount))

print sum(d) - sum(w)
