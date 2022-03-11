from random import randint
import math

GAME_CONDITION = 'Find the greatest common divisor of given numbers.'
NUM_A, NUM_B = randint(1, 50), randint(1, 50)


def get_round():
    quest = f'{NUM_A} {NUM_B}'
    answer = str(math.gcd(NUM_A, NUM_B))
    return answer, quest
