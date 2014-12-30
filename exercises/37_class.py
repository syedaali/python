__author__ = 'syedaali'

'''
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

man = Celsius()
man.temperature = 100
print man.to_fahrenheit()
'''


class Celsius:

    def __init__(self):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print "Getting value"
        return self._temperature

    @temperature.setter
