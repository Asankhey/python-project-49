#!/usr/bin/env python3
import prompt
from random import randint, choice


def calculate(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello {user_name}!\nWhat is the result of the expression?")
    index = 0
    score = 3
    while index < score:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        oper = choice(['+', '-', '*'])
        result = calculate(number1, number2, oper)
        print(f"Question: {number1} {oper} {number2}")
        answer = prompt.string("Your answer: ")
        if answer.isdigit() and int(answer) == result:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was {result}")
            return
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
