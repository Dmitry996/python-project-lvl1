from random import randint

GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_NUMBER = randint(1, 100)


def get_round():
    if RANDOM_NUMBER % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return answer, RANDOM_NUMBER
