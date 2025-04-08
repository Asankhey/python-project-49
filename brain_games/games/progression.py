#!/usr/bin/env python3
import prompt
from random import randint


def generate_progression(start, step, length):
    """Генерация арифметической прогрессии"""
    return [str(start + step * i) for i in range(length)]


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}! \nWhat number is missing in the progression?")
    index = 0
    score = 3
    while index < score:
        start = randint(1, 10)
        step = randint(1, 5)
        length = 10
        progression = generate_progression(start, step, length)

        element_index = randint(0, length - 1)
        correct_answer = progression[element_index]
        progression[element_index] = '..'
        question = ' '.join(progression)

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
