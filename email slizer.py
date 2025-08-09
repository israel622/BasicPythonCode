enter_email = input('enter email : ')

enter_email1 = enter_email.split('@',)

enter_email2 = enter_email1[1].split('.')
print(f'{enter_email2[1]} is the extension')
print(f'your useranme is {enter_email1[0]} and the domain name is {enter_email2[0]}')