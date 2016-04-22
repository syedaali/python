'''
Have the function SimpleSymbols(str) take the str parameter being passed and
determine if it is an acceptable sequence by either returning the string true
or false. The str parameter will be composed of + and = symbols with several
letters between them (ie. ++d+===+c++==a) and for the string to be true each
letter must be surrounded by a + symbol. So the string to the left would be
false. The string will not be empty and will have at least one letter.

'''

def SimpleSymbols(str):

  if str[0].isalpha() or str[-1].isalpha():
    return 'false'

  for i in xrange(1, len(str)-1):
    if str[i].isalpha() and (not str[i-1] == '+' or not str[i+1] == '+'):
      return 'false'
  return 'true'



print SimpleSymbols('+H++===+a')
