from brain_games.cli import greeting


def engine(game):
    user_name = greeting()
    print(game.GAMECONDITION)
    for _ in range(3):
        answers = game.qwest_res()
        if answers[0] == answers[1]:
            print('Correct!')
        else:
            print(f"'{answers[0]}' is wrong answer ;(."
                  f"\nCorrect answer was '{answers[1]}'.)"
                  f" Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
