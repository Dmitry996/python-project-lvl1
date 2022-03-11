from random import randint

GAME_CONDITION = 'What number is missing in the progression?'
MAX_RANDOM_VALUE_STARTS = 50
MAX_RANDOM_VALUE_STEPS = 10


def get_round():
    step = randint(3, MAX_RANDOM_VALUE_STEPS)
    start = randint(1, MAX_RANDOM_VALUE_STARTS)
    numbers = [str(i) for i in range(start, start + (step * 10), step)]
    index = randint(0, len(numbers) - 1)
    answer = numbers[index]
    numbers[index] = '..'
    quest = ' '.join(numbers)
    return answer, quest
