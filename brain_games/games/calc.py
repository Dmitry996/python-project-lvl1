from random import randint, choice

GAME_CONDITION = 'What is the result of the expression?'


def quest_result():
    mat_signs = ['+', '*', '-']
    a, b = randint(1, 20), randint(1, 20)
    quest = f'{a} {choice(mat_signs)} {b}'
    answer = str(eval(quest))
    return answer, quest
