from random import randint, choice

GAME_CONDITION = 'What is the result of the expression?'
MAX_RANDOM_VALUE = 20


def get_round():
    answer = 0
    mat_signs = ['+', '*', '-']
    a, b = randint(1, MAX_RANDOM_VALUE), randint(1, MAX_RANDOM_VALUE)
    mat_sign = choice(mat_signs)
    quest = f'{a} {mat_sign} {b}'
    if mat_sign == '+':
        answer = str(a + b)
    elif mat_sign == '-':
        answer = str(a - b)
    elif mat_sign == '*':
        answer = str(a * b)
    return answer, quest
