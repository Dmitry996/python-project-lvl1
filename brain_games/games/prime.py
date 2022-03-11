from random import randint

GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_NUMBER = randint(2, 100)


def is_prime(num):
    count = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            count += 1
        if count > 2:
            return False
    return True


def get_round():
    if is_prime(RANDOM_NUMBER):
        return 'yes', RANDOM_NUMBER
    else:
        return 'no', RANDOM_NUMBER
