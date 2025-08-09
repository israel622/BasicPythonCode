from cryptography import fernet
from cryptography.fernet import Fernet

master_pwd = input('Enter your master password: ')

# def write_key():
#     key = Fernet.generate_key()
#     with open('key.txt', 'wb') as key_file:
#         key_file.write(key)

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()+ master_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as file:
        for line in file.readlines():
           data = line.rstrip()
           name_user, passw = data.split('|')
           print('username:', name_user + '\n' +  'password:', str(fer.decrypt(passw.encode()).decode()))


def add():
    name = input('Enter your account name: ')
    pwd = input('Enter your password: ')

    with open('password.txt', 'a') as file:
        file.write(name + '|' + str(fer.encrypt(pwd.encode())) + '\n')



while True:
    mode = input('Do you want to enter your password? or view your password : (add or view), q to quit ').lower()
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode == 'q':
        break

    else:
        print('Invalid mode')
        continue