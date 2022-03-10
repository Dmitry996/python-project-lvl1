from random import randint
import math

GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def get_round():
    a, b = randint(1, 50), randint(1, 50)
    quest = f'{a} {b}'
    answer = str(math.gcd(a, b))
    return answer, quest
