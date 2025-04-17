from brain_games import cli
import prompt

ATTEMPTS_COUNT = 3


def run_game(game):
    name = cli.welcome_user()
    print(game.RULE)
    for _ in range(ATTEMPTS_COUNT):
        question, correct_answer = game.get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
