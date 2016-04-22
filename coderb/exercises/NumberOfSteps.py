'''
Suppose you want climb a staircase of N steps, and on each step you can
take either 1 or 2 steps. How many distinct ways are there to climb
the staircase?
'''

def count_steps(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2

    ans = count_steps(n-1) + count_steps(n-2)

    return ans

print count_steps(40)