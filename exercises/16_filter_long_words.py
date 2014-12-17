__author__ = 'syedaali'

# Write a function filter_long_words() that takes a list of words
# and an integer n and returns the list of words that are longer than n.


long_list = [['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'c', 'd']]


def check_size(a_list):
    size = 2
    if len(a_list) > size:
        return True
    else:
        return False

result_list = filter(check_size, long_list)

print result_list
