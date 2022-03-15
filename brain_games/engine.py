import prompt

NUMBER_OF_ROUND = 3


def engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name)
    print(game.GAME_CONDITION)
    for _ in range(NUMBER_OF_ROUND):
        right_answer, quest = game.get_round()
        print(f'Question: {quest}')
        user_answer = input("Your answer: ")
        if user_answer.lower() == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"\nCorrect answer was '{right_answer}'.)"
                  f" Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
