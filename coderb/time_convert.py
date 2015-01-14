__author__ = 'syedaali'

'''
Using the Python language, have the function TimeConvert(num)
take the num parameter being passed and return the number of
hours and minutes the parameter converts to
(ie. if num = 63 then the output should be 1:3).
Separate the number of hours and minutes with a colon.
'''

def TimeConvert(num):

    if num < 60:
        return '0' + ':' + str(num)

    if num % 60 == 0:
        hour = num / 60
        return str(hour) + ':' + '0'

    t = divmod(num,60)

    return str(t[0]) + ':' + str(t[1])


print TimeConvert(253)

# METHOD 2

num = 253

print ':'.join([str(num/60), str(num%60)])