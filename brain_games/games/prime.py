from random import randint

GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_RANDOM_VALUE = 100


def is_prime(num):
    count = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            count += 1
        if count > 2:
            return False
    return True


def get_round():
    number = randint(1, MAX_RANDOM_VALUE)
    if is_prime(number):
        return 'yes', number
    else:
        return 'no', number
