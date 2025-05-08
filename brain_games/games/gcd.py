import random
import math

MIN_NUMBER = 1
MAX_NUMBER = 100
RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
