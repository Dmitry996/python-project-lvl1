import prompt


def welcome():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name)
    return user_name
