from random import randint

GAME_CONDITION = 'What number is missing in the progression?'


def qwest_result():
    step = randint(3, 10)
    start = randint(1, 50)
    numbers = [str(i) for i in range(start, start + (step * 10), step)]
    index = randint(0, 9)
    answer = numbers[index]
    numbers[index] = '..'
    print("Question:", ' '.join(numbers))
    user_answer = input("Your answer: ")
    return user_answer, answer
