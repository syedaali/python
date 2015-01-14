__author__ = 'syedaali'

'''
Using the Python language, have the function MeanMode(arr) take the
array of numbers stored in arr and return 1 if the mode equals the mean,
 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1
 because the mode (3) equals the mean (3)). The array will not be empty,
 will only contain positive integers, and will not contain more than one mode.

'''

def MeanMode(arr):

  mean = sum(arr)/len(arr)

  mode = arr[0]
  mode_cnt = 1
  counts = {}
  for n in arr:
    if not n in counts:
      counts[n] = 0
    counts[n] += 1
    if counts[n] > mode_cnt:
      mode = n
      mode_cnt = counts[n]
  return 1 if mean == mode else 0

print MeanMode([5, 3, 3, 3, 1])
