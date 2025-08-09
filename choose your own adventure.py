user_name = input('What is your name? ')
print('welcome,' + user_name + ' to the adventure')
answer= input('you are at the end of a dirt road, do you want to go left or right ??').lower()
if answer == 'left':
    q2 = input('you have come to a river, do you want to swim or walk around it, type walk or swim??').lower()
    if q2 == 'swim':
        print('you were eaten by a crocodile')
    elif q2 == 'walk':
        print('you walked for many miles and died')
    else:
        print('not a valid option')
elif answer == 'right':
    q3 = input('You come to a bridge do you want to cross or go back.cross or back').lower()
else:
    print('not a valid option')

print('thanks for playing' + user_name + '!')