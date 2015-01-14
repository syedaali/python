__author__ = 'syedaali'

'''
Have the function ArithGeo(arr) take the array of numbers stored in arr
and return the string "Arithmetic" if the sequence follows an arithmetic
 pattern or return "Geometric" if it follows a geometric pattern.
 If the sequence doesn't follow either pattern return -1. An arithmetic
 sequence is one where the difference between each of the numbers is
 consistent, where as in a geometric sequence, each term after the first
 is multiplied by some constant or common ratio. Arithmetic example:
 [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers
 may be entered as parameters, 0 will not be entered, and no array will
 contain all the same elements.
'''

def ArithGeo(alist):

    #build a list that contains the differences in numbers
    diff_list = [alist[i+1] - alist[i] for i in range(len(alist)-1)]

    #for each item in diff list, check if they are the same
    if all(diff_list[0] == x for x in diff_list):
        return  'Arithmetic'

    #check for geometric
    ratio = alist[1]/float(alist[0])
    for i in range(1, len(alist)):
        if alist[i]/float(alist[i-1]) != ratio:
            return -1
    return 'Geometric'

print ArithGeo([2,4,16,24])

print ArithGeo([5,10,15])

print ArithGeo([1,2,3,4])

print ArithGeo([2,6,18,54])

'''
   #METHOD 1
    #if len(set(diff_list)) == 1:
    #    return 'Arithmetic'
    #METHOD 2
'''