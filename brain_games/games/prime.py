from random import randint

GAMECONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def qwest_res():
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
             61, 67, 71, 73, 79, 83, 89, 97]
    number = randint(2, 100)
    print("Question:", number)
    user_answer = input("Your answer: ")
    if number in prime:
        answer = "yes"
    else:
        answer = "no"
    return user_answer, answer
