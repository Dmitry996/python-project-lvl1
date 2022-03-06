from random import randint

GAMECONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def qwest_res():
    number = randint(1, 100)
    print("Question:", number)
    user_answer = input("Your answer: ")
    if number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return user_answer, answer
