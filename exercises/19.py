__author__ = 'syedaali'

# From http://www.ling.gu.se/~lager/python_exercises.html
# Ex 19

#"99 Bottles of coke" is a traditional song in the United States and Canada.
# It is popular to sing on long trips, as it has a very repetitive format
# which is easy to memorize, and can take a long time to sing. The song's
# simple lyrics are as follows:
# 99 bottles of coke on the wall, 99 bottles of coke.
# Take one down, pass it around, 98 bottles of coke on the wall.
# The same verse is repeated, each time with one fewer bottle. The song is
# completed when the singer or singers reach zero.
# Your task here is write a Python program capable of generating all the
# verses of the song.

for index in xrange(99, 0, -1):
    print "{0} bottles of coke on the wall, {1} bottles of coke.".format(index, index)
    left = index - 1
    print "Take one down, pass it around, {0} bottles of coke on the wall.".format(left)
