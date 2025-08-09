import random

def roll_dice():
    
    roll = input('do you want to roll dice? y/n: ')

    while roll.lower() == 'y':
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print('dice rolled:', dice_1, dice_2)
        roll = input('do you want to roll dice again? y/n: ')

roll_dice()
