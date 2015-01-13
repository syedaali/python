__author__ = 'syedaali'


def PrimeTime(num):
    if num < 1:
        return 'false'
    else:
        for i in range(2,num):
            if num % i == 0:
                return 'false'
        else:
            return 'true'

for i in range(1,10):
    print '{} prime check {}'.format(i,PrimeTime(i))