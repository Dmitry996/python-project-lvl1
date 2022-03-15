from random import randint

GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_RANDOM_VALUE = 99


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def get_round():
    number = randint(2, MAX_RANDOM_VALUE)
    right_answer = ['yes', 'no']
    if is_prime(number):
        return right_answer[0], number
    else:
        return right_answer[1], number
