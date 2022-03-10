from random import randint
from math import gcd

GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def quest_result():
    a, b = randint(1, 50), randint(1, 50)
    quest = f'{a} {b}'
    answer = str(gcd(a, b))
    return answer, quest
