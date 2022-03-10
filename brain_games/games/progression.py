from random import randint

GAME_CONDITION = 'What number is missing in the progression?'


def get_round():
    STEP = randint(3, 10)
    START = randint(1, 50)
    numbers = [str(i) for i in range(START, START + (STEP * 10), STEP)]
    INDEX = randint(0, 9)
    answer = numbers[INDEX]
    numbers[INDEX] = '..'
    quest = ' '.join(numbers)
    return answer, quest
