'''
Using the Python language, have the function DistinctList(arr) take the array
of numbers stored in arr and determine the total number of duplicate entries.
For example if the input is [1, 2, 2, 2, 3] then your program should output 2
because there are two duplicates of one of the elements.

'''

def DistinctList(arr):

    d = {}
    counter = 0

    for item in arr:
        if not item in d:
           d[item] = 1
        else:
            d[item] += 1

    for key in d.keys():
        if d[key] >= 2:
            counter += d[key]-1

    return counter

# keep this function call here
# to see how to enter arguments in Python scroll down
print DistinctList([0,-2,-2,5,5,5])


def DistinctList(arr):
  return len(arr)-len(list(set(arr)))


# keep this function call here
# to see how to enter arguments in Python scroll down
print DistinctList(raw_input())