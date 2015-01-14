__author__ = 'syedaali'

'''
Using the Python language, have the function SimpleSymbols(str) take
 the str parameter being passed and determine if it is an acceptable
  sequence by either returning the string true or false. The str
   parameter will be composed of + and = symbols with several letters
   between them (ie. ++d+===+c++==a) and for the string to be true each
   letter must be surrounded by a + symbol. So the string to the left
    would be false. The string will not be empty and will have at least one letter.
Input = "+d+=3=+s+"Output = "true"
Input = "f++d+"Output = "false"
'''

def SimpleSymbols(str):

    if len(str) < 2:
        return 'false'

    if str[0].isalpha() or str[-1].isalpha():
        return 'false'

    for i,c in enumerate(str):
        if c.isalpha():
            if str[i-1] == '+' and str[i+1] == '+':
                t = 'true'
            else:
                return 'false'
    return t

str = '+d+=3=+s+'
print SimpleSymbols(str)

# method 2

if str[0].isalpha() or str[-1].isalpha():
    print 'false'

for i in xrange(1, len(str)-1):
    if str[i].isalpha() and (not str[i-1] == '+' or not str[i+1] == '+'):
        print 'false'
print 'true'