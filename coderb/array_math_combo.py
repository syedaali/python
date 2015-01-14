__author__ = 'syedaali'

'''
Have the function ArrayAdditionI(arr) take the array of numbers stored
in arr and return the string true if any combination of numbers in the
array can be added up to equal the largest number in the array, otherwise
return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3]
the output should return true because 4 + 6 + 10 + 3 = 23. The array will
not be empty, will not contain all the same elements, and may contain
negative numbers.
'''
import itertools

def ArrayAddition(arr):

    max_num = max(arr)
    index = arr.index(max_num)
    arr.pop(index)
    for i in range(2,len(arr)+1):
        for x in itertools.combinations(arr,i):
            if sum(x)==max_num:
                return 'true'
    return 'false'

print ArrayAddition([3,5,-1,8,12])