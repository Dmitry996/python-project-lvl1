from random import randint, choice

GAME_CONDITION = 'What is the result of the expression?'


def qwest_result():
    mat_signs = ['+', '*', '-']
    a, b = randint(1, 20), randint(1, 20)
    s = f'{a} {choice(mat_signs)} {b}'
    print("Question: " + s)
    user_answer = int(input('You answer: '))
    answer = eval(s)
    return user_answer, answer
