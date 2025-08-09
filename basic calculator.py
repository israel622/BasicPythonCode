def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2


while True:
    enter_operator = input('enter operator : ')


    if enter_operator == 'multiply':
        num1 = int(input('enter first number : '))
        num2 = int(input('enter second number : '))
        result = multiply(num1, num2)
        print(result)
    elif enter_operator == 'divide':
        num1 = int(input('enter first number : '))
        num2 = int(input('enter second number : '))
        result= divide(num1, num2)
        print(result)
    elif enter_operator == 'add':
        num1 = int(input('enter first number : '))
        num2 = int(input('enter second number : '))
        result = add(num1, num2)
        print(result)
    elif enter_operator == 'sub':
        num1 = int(input('enter first number : '))
        num2 = int(input('enter second number : '))
        result = sub(num1, num2)
        print(result)
    elif enter_operator == 'quit':
        break
