from random import randint
import math

GAME_CONDITION = 'Find the greatest common divisor of given numbers.'
MAX_RANDOM_VALUE = 50


def get_round():
    a, b = randint(1, MAX_RANDOM_VALUE), randint(1, MAX_RANDOM_VALUE)
    quest = f'{a} {b}'
    answer = str(math.gcd(a, b))
    return answer, quest
