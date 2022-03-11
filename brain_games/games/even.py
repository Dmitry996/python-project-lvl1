from random import randint

GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_RANDOM_VALUE = 100


def get_round():
    number = randint(1, MAX_RANDOM_VALUE)
    if number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return answer, number
