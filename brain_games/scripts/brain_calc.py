#!/usr/bin/env python3
from random import randint, choice
from prompt import string


def main():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print('Hello, ' + user_name)
    mat_signs = ['+', '*', '-']
    print('What is the result of the expression?')
    for _ in range(3):
        a = randint(1, 20)
        b = randint(1, 20)
        s = f'{a} {choice(mat_signs)} {b}'
        print()
        print(eval(s))


if __name__ == '__main__':
    main()
