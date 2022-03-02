#!/usr/bin/env python3
from random import randint
from prompt import string


def main():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print('Hello, ' + user_name)
    for _ in range(3):
        number = randint(1, 100)
        print("Question:", number)
        answer = string("Your answer: ")
        if number % 2 == 0:
            if answer == "yes":
                print("Correct!")
            else:
                return print("'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again,", user_name)
        else:
            if answer == "no":
                print("Correct!")
            else:
                return print("'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again,", user_name)
    print("Congratulations,", user_name)


if __name__ == '__main__':
    main()

