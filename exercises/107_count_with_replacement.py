__author__ = 'syedaali'

'''
Return the number of times that the string "code"
appears anywhere in the given string, except we'll
accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb')  1
count_code('codexxcode')  2
count_code('cozexxcope')  2
'''

import re


def count_code(s):
    l = re.findall(r'co[\w]e', s)
    return len(l)

print count_code('aaacodebbb')
print count_code('codexxcode')
print count_code('cozexxcope')

alphas = 'abcdefghijklmnopqrstuvwxyz'

# another way doing the same without using re module


def count_code_again(s):
    count = 0
    for index, letter in enumerate(s):
        if letter == 'c':
            if s[index + 1] == 'o':
                if s[index + 2] in alphas:
                    if s[index + 3] == 'e':
                        count += 1
    return count


print count_code_again('aaacodebbb')
print count_code_again('codexxcode')
print count_code_again('cozexxcope')
