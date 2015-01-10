__author__ = 'syedaali'

'''
translate a string into ICAO format
'''

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}

s = raw_input('enter string-> ')

for letter in s:
    if letter in d:
        print d[letter],