from random import randint, choice

DESCRIPTION = "What is the result of the expression?"


def calculate(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2


def generate_round():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    oper = choice(['+', '-', '*'])
    question = f"{number1} {oper} {number2}"
    correct_answer = str(calculate(number1, number2, oper))
    return question, correct_answer
