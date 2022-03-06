#!/usr/bin/env python3
from random import randint
from brain_games.cli import greeting


def main():
    user_name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 100)
        print("Question:", number)
        answer = input("Your answer: ")
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
