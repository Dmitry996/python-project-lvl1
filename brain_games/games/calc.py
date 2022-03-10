from random import randint, choice

GAME_CONDITION = 'What is the result of the expression?'


def get_round():
    mat_signs = ['+', '*', '-']
    a, b = randint(1, 20), randint(1, 20)
    mat_sign = choice(mat_signs)
    quest = f'{a} {mat_sign} {b}'
    if mat_sign == '+':
        answer = str(a + b)
    elif mat_sign == '-':
        answer = str(a - b)
    elif mat_sign == '*':
        answer = str(a * b)
    return answer, quest
