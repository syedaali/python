__author__ = 'syedaali'


'''
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.
'''


class Circle(object):

    def __init__(self, n):
        self.n = n

    def radius(self):
        return self.n * self.n

aCircle = Circle(5)

print aCircle.radius()
