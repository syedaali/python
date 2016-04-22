'''
Using the Python language, have the function ChangingSequence(arr) take the
 of numbers stored in arr and return the index at which the numbers stop
 increasing and begin decreasing or stop decreasing and begin increasing.
  For example: if arr is [1, 2, 4, 6, 4, 3, 1] then your program should
  return 3 because 6 is the last point in the array where the numbers were
  increasing and the next number begins a decreasing sequence. The array will
   contain at least 3 numbers and it may contains only a single sequence,
    increasing or decreasing. If there is only a single sequence in the array,
     then your program should return -1. Indexing should begin with 0.
'''

def ChangingSequence(arr):

    for index, number in enumerate(arr)
        if arr[index+1] < number:
            decreasing = True
        else:
            increasing = True
        

    return arr

# keep this function call here
# to see how to enter arguments in Python scroll down
print ChangingSequence(raw_input())
