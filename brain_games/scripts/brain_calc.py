#!/usr/bin/env python3
import prompt
from random import randint
import random


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello {user_name}! \nWhat is the result of the expression?")
    index = 0
    score = 3
    while index < score:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        operations = ['+', '-', '*']
        oper = random.choice(operations)
        solution = f"{number1} {oper} {number2}"
        result = eval(solution)
        print(f"Question: {solution}")
        answer = prompt.string("Your answer: ")
        if int(answer) == result:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {result}")
            return
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
