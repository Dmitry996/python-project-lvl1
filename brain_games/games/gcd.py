from random import randint
from math import gcd

GAMECONDITION = 'Find the greatest common divisor of given numbers.'


def qwest_res():
    a, b = randint(1, 50), randint(1, 50)
    print(f'Question: {a} {b}')
    user_answer = int(input('You answer: '))
    answer = gcd(a, b)
    return user_answer, answer
