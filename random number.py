import random

take_number = input('Take a number:  ')
if take_number.isdigit():
    take_number = int(take_number)

    if take_number <= 0:
        print('your guess must be greater than 0')
        quit()
else:
    print('enter a valid number')
    quit()

random_number= random.randint(1, take_number)
guess =0
while True:
    guess += 1
    user_input = input('enter a number: ')
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print('enter a valid number')
        continue
    if user_input < random_number:
        print(f'your guess is too low')

    elif user_input >random_number:
            print(f'your guess is too high')

    elif user_input == random_number:
            print(f'your guess is correct')
            break



print(f'you got it in {guess} guesses')






