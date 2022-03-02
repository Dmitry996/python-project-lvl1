#!/usr/bin/env python3
from random import randint
from prompt import string


def main():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print('Hello, ' + user_name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 100)
        print("Question:", number)
        answer = string("Your answer: ")
        if number % 2 == 0:
            if answer == "yes":
                print("Correct!")
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again,", user_name)
                return
        else:
            if answer == "no":
                print("Correct!")
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again,", user_name)
                return
    print("Congratulations,", user_name)


if __name__ == '__main__':
    main()
