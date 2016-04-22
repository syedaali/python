'''
You will be given 2 parameters: a low number, and high number. Your goal is
to print all numbers between low and high, and for each of these numbers
print whether or not the number is divisible by 3. If the number is
divisible by 3, print the word "div3" directly after the number.
'''

low_num = int(raw_input("Enter low number: "))
high_num = int(raw_input("Enter high number: "))

for number in xrange(low_num,high_num+1):
    print number,
    if (number % 3 == 0):
        print ' div3',
    print ""