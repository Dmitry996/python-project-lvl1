from random import randint

GAMECONDITION = 'What number is missing in the progression?'


def qwest_res():
    st = randint(3, 10)
    st_l = randint(1, 50)
    numbers = [str(i) for i in range(st_l, st_l + (st * 10), st)]
    index = randint(0, 9)
    answer = numbers[index]
    numbers[index] = '..'
    print("Question:", ' '.join(numbers))
    user_answer = input("Your answer: ")
    return user_answer, answer
