__author__ = 'syedaali'

'''
Using the Python language, have the function ThirdGreatest(strArr)
take the array of strings stored in strArr and return the third
largest word within in. So for example: if strArr is ["hello",
"world", "before", "all"] your output should be world because "before"
is 6 letters long, and "hello" and "world" are both 5, but the output
should be world because it appeared as the last 5 letter word in the array.
If strArr was ["hello", "world", "after", "all"] the output should be a
fter because the first three words are all 5 letters long, so return the
last one. The array will have at least three strings and each string
will only contain letters.
'''

def ThirdGreatest(strArr):
    s = sorted(strArr, key=lambda x: len(x))
    return s[-3]

print ThirdGreatest(["hello","world", "before", "all"])

'''
another user's example:
def k(v):
    return v[1]
  return sorted([(word, -len(word)) for word in strArr], key=k)[2][0]

'''
