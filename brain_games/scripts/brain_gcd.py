#!/usr/bin/env python3
import prompt
from random import randint
import math


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!\nFind the greatest common divisor of given numbers.")
    index = 0
    score = 3
    while index < score:
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        gcd = math.gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        if int(answer) == gcd:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {gcd}")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
