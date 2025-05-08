import random
import operator

MIN_NUMBER = 1
MAX_NUMBER = 20
RULE = 'What is the result of the expression?'

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question_and_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator_sign = random.choice(list(OPERATORS.keys()))
    question = f'{number1} {operator_sign} {number2}'
    result = OPERATORS[operator_sign](number1, number2)
    correct_answer = str(result)
    return question, correct_answer
