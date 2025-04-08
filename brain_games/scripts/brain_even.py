#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}! \nAnswer "yes" if the number is even, otherwise answer "no".')
    index = 0
    score = 3
    while index < score:
        random_number = randint(1, 100)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        if answer == correct_answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
