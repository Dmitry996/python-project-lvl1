from random import randint

GAME_CONDITION = 'What number is missing in the progression?'
STEP = randint(3, 10)
START = randint(1, 50)
INDEX = randint(0, 9)


def get_round():
    numbers = [str(i) for i in range(START, START + (STEP * 10), STEP)]
    answer = numbers[INDEX]
    numbers[INDEX] = '..'
    quest = ' '.join(numbers)
    return answer, quest
