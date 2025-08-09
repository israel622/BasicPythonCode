import random
import string
chars = list(string.ascii_letters + string.digits + string.punctuation)
def generate_password():
    length = input('enter length of password: ')

    random.shuffle(chars)
    password = []

    for i in range(int(length)):
        password.append(random.choice(chars))
    random.shuffle(password)

    password = ''.join(password)
    print('Your password is: ', password)

option = input('Do you want to generate another password? y/n: ')
if option == 'y':
    generate_password()

elif option == 'n':
    print('Thank you!')
    quit()

else:
    print('invalid input!')


