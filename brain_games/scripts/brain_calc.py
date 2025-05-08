from brain_games.engine import run_game
from brain_games.games import calc


def main():
    run_game(calc.RULE, calc.get_question_and_answer)


if __name__ == '__main__':
    main()
