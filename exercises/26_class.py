__author__ = 'syedaali'

'''
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.
'''


class Rectangle(object):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * 4

aRectangle = Rectangle(4)

print aRectangle.area()
