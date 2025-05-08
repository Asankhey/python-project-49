from brain_games.engine import run_game
from brain_games.games import even


def main():
    run_game(even.RULE, even.get_question_and_answer)


if __name__ == '__main__':
    main()
