from random import randint
from math import gcd

GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def qest_result():
    a, b = randint(1, 50), randint(1, 50)
    print(f'Question: {a} {b}')
    answer = str(gcd(a, b))
    return answer
