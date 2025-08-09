print('Welcome to my computer quiz')

playing = input(' do yu want to play? (y/n): ')

score = 0
if playing.lower() == 'n':
     quit()

answer = input(' what does cpu stand for ')

if answer.lower() == 'central processing unit':
    print('correct answer!! ')
    score += 1

else:
    print('wrong answer!! ')

answer = input('what does RAM stand for ')

if answer.lower() == 'random access memory':
    print('correct answer!! ')
    score += 1
else:
    print('wrong answer!! ')

answer = input(' what does psu stand for ')

if answer.lower() == 'power supply unit':
    print('correct answer!! ')
    score += 1
else:
    print('wrong answer!! ')

print(f'your score is {score}')
print(f'your score is {(score / 3)*100}')





