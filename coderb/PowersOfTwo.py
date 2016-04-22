def PowersofTwo(num):

  # take log base 2 of num
  base2 = math.log(num, 2)

  # this should return true if base2 is a whole number
  # otherwise 2 to some power is not equal to num
  if (base2/int(base2) == 1.0):
    return "true"
  else:
    return "false"


print PowersofTwo(raw_input())

