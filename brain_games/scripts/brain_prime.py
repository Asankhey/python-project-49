from brain_games.engine import run_game
from brain_games.games import prime


def main():
    run_game(prime.RULE, prime.get_question_and_answer)


if __name__ == '__main__':
    main()
