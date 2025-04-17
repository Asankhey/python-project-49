from random import randint
import math

RULE = "Find the greatest common divisor of given numbers."


def generate_round():
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
