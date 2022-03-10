from random import randint

GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def qest_result():
    number = randint(2, 100)
    print("Question:", number)
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if number == 1:
        return 'no'
    elif count == 2:
        return 'yes'
    else:
        return 'no'
