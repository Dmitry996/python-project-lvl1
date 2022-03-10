from random import randint

GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def quest_result():
    number = randint(1, 100)
    if number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return answer, number
