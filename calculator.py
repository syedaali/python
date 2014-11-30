__author__ = 'syedaali'

# simple calculator
# input should be in format # <opr> #
# opr should be one of +,-,/,*
# run as: python calculator.py

import re


def add(x, y):
    return (x) + (y)


def subtract(x, y):
    return (x) - (y)


def multiply(x, y):
    return (x) * (y)


def divide(x, y):
    try:
        return (x) / (y)
    except ZeroDivisionError:
        return "Cannot divide by zero"


def decide(num_list):

    a = float(num_list[0])
    b = float(num_list[2])

    if num_list[1] == '+':
        print add(a, b)
    elif num_list[1] == '-':
        print subtract(a, b)
    elif num_list[1] == '*':
        print multiply(a, b)
    elif num_list[1] == '/':
        print divide(a, b)
    else:
        print 'I do not understand, bye'
        exit(1)


def work():
    user_input = raw_input("Expecting # +|-|/|* #: ")
    user_input.strip("\n")
    calculate = re.sub('\s+', '', user_input)

    if calculate == 'q':
        print 'bye'
        exit(0)

    # use http://pythex.org/ for checking regex
    pattern = re.compile(
        r"""^(?P<first>\d+)
            (?P<opr>\+|\-|\*|\/)
            (?P<second>\d+)$""",
        re.VERBOSE)

    match = re.search(pattern, calculate)
    if match:
        num_list = match.group('first'), match.group(
            'opr'), match.group('second')
        decide(num_list)
    else:
        print 'expecting <num><opr><num>'

def main():
    while (1):
        work()

main()
