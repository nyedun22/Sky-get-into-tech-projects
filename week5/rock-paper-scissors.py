import random

user_win = 0
computer_win = 0
games = 0
print('3...2...1....Play!')


# function to define user 'player 1' move
def user_play():
    player1 = input('Will you play Rock (R), Paper (P) or Scissors (S)? \n').lower()
    if player1 == 'r':
        print(f'You have played Rock')
    elif player1 == 'p':
        print(f'You have played Paper')
    elif player1 == 's':
        print(f'You have played Scissors')
# else statement to catch errors - begin game again.
    else:
        print(f'Error, please enter R, P or S')
        game_play()
    return player1


# automated random game play function for player 2
def computer_play():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = choices[random.randint(0, 2)]
    print(f'The computer played {computer_choice}')
    return computer_choice


# define function to continue playing rounds of the game


# function to determine outcome of the game
def game_play():
    # use global to access variables from outside the func in this function
    global user_win
    global computer_win
    global games
    user = user_play()
    computer = computer_play()

    if user == computer:
        print('Its a tie!')
        games += 1
    elif user == 'r' and computer == 'paper':
        print('You lose, paper has wrapped up your rock!')
        computer_win += 1
        games += 1
    elif user == 'p' and computer == 'scissors':
        print('You lose, scissors have ripped through your paper')
        computer_win += 1
        games += 1
    elif user == 's' and computer == 'rock':
        print('You lose, the rock has smashed up your scissors')
        computer_win += 1
        games += 1
    else:
        print('Congratulations, You win!')
        user_win += 1
        games += 1
    play_round()


# function to continue playing rounds
def play_round():
    rounds = input('Do you want to play again? y/n? \n')
    if rounds == 'y':
        game_play()
    else:
        print(f'Thanks for playing!')
        print(f'You have won {user_win} and the computer has won {computer_win} out of {games} total games')


game_play()


game_play()
