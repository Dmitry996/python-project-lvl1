from brain_games.welcomes_user import welcome


def engine(game):
    user_name = welcome()
    print(game.GAME_CONDITION)
    for _ in range(3):
        right_answer = game.qest_result()
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
