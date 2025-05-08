from brain_games.engine import run_game
from brain_games.games import progression


def main():
    run_game(progression.RULE, progression.get_question_and_answer)


if __name__ == '__main__':
    main()
