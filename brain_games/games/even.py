#!/usr/bin/env python3
from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    random_number = randint(1, 100)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    question = str(random_number)
    return question, correct_answer
