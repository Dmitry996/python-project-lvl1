#!/usr/bin/env python3
from random import randint, choice
from brain_games.cli import greeting


def main():
    user_name = greeting()
    mat_signs = ['+', '*', '-']
    print('What is the result of the expression?')
    for _ in range(3):
        a = randint(1, 20)
        b = randint(1, 20)
        s = f'{a} {choice(mat_signs)} {b}'
        print("Question: " + s)
        answer = int(input('You answer: '))
        if answer == eval(s):
            print('Correct!')
        else:
            print(f"\'{answer}\' is wrong answer ;(. "
                  f"Correct answer was \'{eval(s)}\'.\n"
                  f'Let\'s try again, {user_name}')
            return
    print(f'Congratulations, {user_name}!')
