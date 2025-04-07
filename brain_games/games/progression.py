#!/usr/bin/env python3
from random import randint
from brain_games.engine import run_game

DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    return [str(start + step * i) for i in range(length)]


def get_round():
    start = randint(1, 10)
    step = randint(1, 5)
    length = 10
    progression = generate_progression(start, step, length)

    element_index = randint(0, length - 1)
    correct_answer = progression[element_index]
    progression[element_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer


def main():
    from brain_games.games import progression
    run_game(progression)


if __name__ == '__main__':
    main()
