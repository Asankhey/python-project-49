#!/usr/bin/env python3
from random import randint
from brain_games.engine import run_game

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def main():
    run_game(generate_round)


if __name__ == '__main__':
    main()
