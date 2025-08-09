quiz ={
   'question1' : {
       'question' : 'what is the capital of france ?',
       'answer' : 'Paris'
   },
    'question2' : {
        'question' : 'what is the capital of germany ?',
        'answer' : 'Berlin'
    },
    'question3' : {
        'question' : 'what is the capital of Austria ?',
        'answer' : 'Vienna'
    },
    'question4' : {
        'question' : 'what is the capital of nigeria ?',
        'answer' : 'Abuja'
    },
    'question5' : {
        'question' : 'what is the capital of italy ?',
        'answer' : 'Rome'
    },
    'question6' : {
        'question' : 'what is the capital of Spain ?',
        'answer' : 'Madrid'
    },
    'question7' : {
        'question' : 'what is the capital of Portugal ?',
        'answer' : 'Lisbon'
    },
}

score = 0
for key,value in quiz.items():
    print(value['question'])
    answer = input(f'Answer: ')

    if answer.lower() == value['answer'].lower():
        print(f'Correct!')
        score += 1
        print(f'Your score is {score}')
    else:
        print(f'Incorrect!')
        print(f'the correct answer is: {value["answer"]}')
        print(f'Your score is {score}')

print(f'You answered{score} questions correct')

