__author__ = 'syedaali'

'''
Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape
where Shape's area is 0 by default.
'''


class Shape():

    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * 2

aSquare = Square(3)
print aSquare.area()
