from random import randint

GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    count = 0
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            count += 1
        if count > 2:
            return False
    return True


def get_round():
    number = randint(2, 100)
    if is_prime(number):
        return 'yes', number
    else:
        return 'no', number
