#!/usr/bin/env python3
from random import randint

RULE = "What number is missing in the progression?"


def generate_progression(start, step, length):
    """Генерация арифметической прогрессии"""
    return [str(start + step * i) for i in range(length)]


def generate_round():
    start = randint(1, 10)
    step = randint(1, 5)
    length = 10
    progression = generate_progression(start, step, length)

    element_index = randint(0, length - 1)
    correct_answer = progression[element_index]
    progression[element_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer
