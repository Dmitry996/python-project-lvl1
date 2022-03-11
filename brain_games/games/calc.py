from random import randint, choice

GAME_CONDITION = 'What is the result of the expression?'
mat_signs = ['+', '*', '-']
NUM_A, NUM_B = randint(1, 20), randint(1, 20)
MAT_SIGN = choice(mat_signs)


def get_round():
    quest = f'{NUM_A} {MAT_SIGN} {NUM_B}'
    if MAT_SIGN == '+':
        answer = str(NUM_A + NUM_B)
    elif MAT_SIGN == '-':
        answer = str(NUM_A - NUM_B)
    elif MAT_SIGN == '*':
        answer = str(NUM_A * NUM_B)
    return answer, quest
