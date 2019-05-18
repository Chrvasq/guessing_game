#!/usr/bin/env python3

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def get_user_input():
    user_input = ''

    try:
        user_input = int(input('Pick a number between 1 and 10: '))
        if user_input not in range(1, 11):
            raise ValueError
        else:
            return user_input
    except ValueError:
        print('Your guess should be an integer between 1 and 10. ' +
            'Please try again!')

def replay_game():
    user_input = ''

    try:
        user_input = input('Would you like to play again? Y/N: ')
        if user_input.lower() not in ['y', 'n']:
            raise ValueError
        else:
            return user_input
    except ValueError:
        print('That\'s not a correct option. Please enter \'Y\' or \'N\'.')

def start_game(high_score=None, score_tracker=[]):
    # Display an intro/welcome message to the player.
    welcome_message = ' Welcome to the Guessing Game! '
    print('\n')
    print('#' * (len(welcome_message) + 2))
    print(f'#{welcome_message}#')
    print('#' * (len(welcome_message) + 2))
    print('\nObjective: Try to guess the number between 1 and 10!\n')
    
    if high_score:
        print(f'The High Score to beat is {high_score}.\n')

    # Store a random number as the answer/solution.
    solution = random.randint(1,10)
    game_state = True
    guess_count = 0
    replay = True

    # Continuously prompt the player for a guess.
    while game_state:
        guess = get_user_input()

        if guess is None:
            continue
        else:
            if guess > solution:
                print('It\'s lower!')
                guess_count += 1
            elif guess < solution:
                print('It\'s higher!')
                guess_count += 1
            else:
                print('You got it!')
                guess_count += 1
                game_state = False
                score_tracker.append(guess_count)

    print(f'You guessed in {guess_count} attempts!')

    while replay:
        play_again = replay_game()

        if play_again is None:
            continue
        else:
            if play_again.lower() == 'y':
                high_score = min(score_tracker)
                start_game(high_score, score_tracker)
            else:
                print('\n ** The game is now over. Thanks for playing! **\n')
                replay = False


if __name__ == '__main__':
    start_game()
