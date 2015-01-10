__author__ = 'syedaali'


'''
The human player enters the number of points required for a win.
During the play of the game the human player selects whether to play a rock,
 paper, or scissors by using the keyboard. The human player may also end the
 game by pressing the Control-D sequence at any time. (Ending the game early
 does not allow a winner to be determined if the human player is ahead.)

'''

import  random

# 0 = rock
# 1 = paper
# 2 = scissors

def main():
    turns = 0
    while True:
        s = raw_input('r/p/s-> ')
        if s == 'r':
            ans = 0
        elif s == 'p':
            ans = 1
        n = random.randrange(0,3)
        for ans  in 'rps':
            if ans == s:
                draw = True
                turns += 1
            elif ans <

if __name__ == '__main__':
    main()