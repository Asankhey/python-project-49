from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    run_game(gcd.RULE, gcd.get_question_and_answer)


if __name__ == '__main__':
    main()
