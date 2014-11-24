# purpose: to demonstrate how to process a list last item differently
# print a space between list item

__author__ = 'syedaali'


mylist = ['a','b','c','d']

for letter in mylist:
  if letter == mylist[-1]:
    print letter
    exit()
  print letter + " ",
