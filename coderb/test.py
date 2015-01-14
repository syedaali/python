__author__ = 'syedaali'

def PrimeTime(num):
    if num <= 1:
        return
    else:
        for i in range(2,num):
            if num % i == 0:
                return
        else:
            return num

for i in [1,2,3,4,5,6,7,8,9]:
    x = PrimeTime(i)
    if isinstance(x,int):
        print x,

