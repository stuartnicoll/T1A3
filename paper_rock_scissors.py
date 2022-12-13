#this is the bonus game section of the program
#import random and math functions
#make input choice for human 
#and make computer choice random
#use ceil (n/2) method to create best of n wins
#use if/than statements to set the conditions
#and output messages 
#import random
#import math

import random
import math 



def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the human beats the robot
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') | (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the robot until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        #if tied
        if result == 0:
            print('The robot and the human have tied for {}. \n'.format(user))
        # Human wins
        elif result == 1:
            player_wins += 1
            print('The human chose {} and the robot chose {}. The human wins!\n'.format(user, computer))
        #Robot wins
        else:
            computer_wins += 1
            print('The human choose {} and the robot chose {}. The human loses as was expected! \n'.format(user, computer))

    if player_wins > computer_wins:
        print('The human has won best out of {} games! It remains free from hard labour :|'.format(n))
    else:
        print('Unfortunately for you the robot has won the best of {} games. Time to go to the pit! :)'.format(n))


if __name__ == '__main__':
    play_best_of(3) # 2r



