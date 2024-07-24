#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}! \nAnswer 'yes' if the number is even, otherwise answer 'no'.")
    index = 0
    score = 3
    while index < score:
        randon_number = randint(1, 100)
        print(f"Question: {randon_number}")
        answer = prompt. string("Your answer: ")
        if answer == 'yes' and randon_number % 2 == 0 or answer == 'no' and randon_number % 2 > 0:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
