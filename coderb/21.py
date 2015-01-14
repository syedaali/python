__author__ = 'syedaali'

'''
Using the Python language, have the function DivisionStringified(num1,num2)
 take both parameters being passed, divide num1 by num2, and return the result
 as a string with properly formatted commas. If an answer is only 3 digits
 long, return the number with no commas (ie. 2 / 3 should output "1").
 For example: if num1 is 123456789 and num2 is 10000 the output
 should be "12,345".
'''
import math

def DivisionStringified(num1,num2):

   m = int(math.ceil(float(num1)/float(num2)))
   return "{:,}".format(m)


print DivisionStringified(101077282,21123)
