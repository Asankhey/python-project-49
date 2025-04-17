import prompt
from brain_games import cli

ATTEMPTS_COUNT = 3  # Вместо "магической тройки"


def run_game(game):
    user_name = cli.welcome_user()
    print(game.RULE)

    for _ in range(ATTEMPTS_COUNT):
        question, correct_answer = game.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"\nLet's try again, {user_name}!"
            )
            return

    print(f'Congratulations, {user_name}!')
