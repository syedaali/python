__author__ = 'syedaali'

'''
Bob is a lackadaisical teenager. In conversation, his responses are very
limited.

Bob answers 'Sure.' if you ask him a question.

He answers 'Whoa, chill out!' if you yell at him.

He says 'Fine. Be that way!' if you address him without actually saying
anything.

He answers 'Whatever.' to anything else.
'''


def hey(what):
    what = what.rstrip()
    if what.endswith('?'):
        if what.isupper():
            return 'Whoa, chill out!'
        else:
            return 'Sure.'
    elif what == '':
        return 'Fine. Be that way!'
    elif what.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
