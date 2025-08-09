import random

user_wins = 0
computer_wins = 0

option = ['rock', 'paper', 'scissors']


while True:
    user_input = input('ROCK / PAPER / SCISSORS or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in option:
        continue
    random_number = random.randint(0, 2)
    # rock =1 # paper = 2 # scissors = 3
    computer_choice = option[random_number]
    print(f'computer choice is {computer_choice}')

    if computer_choice == user_input:
        print('it\'s a draw')
    elif computer_choice == 'rock':
        if user_input == 'paper':
            user_wins += 1
            print('user wins')
        elif user_input == 'scissors':
            computer_wins += 1
            print('computer wins')
    elif computer_choice == 'paper':
        if user_input == 'rock':
            computer_wins += 1
            print('computer wins')
        elif user_input == 'scissors':
            user_wins += 1
            print('user wins')
    elif computer_choice == 'scissors':
        if user_input == 'paper':
            computer_wins += 1
            print('computer wins')
        elif user_input == 'rock':
            user_wins += 1
            print('user wins')
    else:
        print('you lost')
print('your score is ' + str(user_wins) )
print('computer score is ' + str(computer_wins))

print('goodbye')