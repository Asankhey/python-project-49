import random

START_MIN = 1
START_MAX = 10
STEP_MIN = 2
STEP_MAX = 5
LENGTH_MIN = 5
LENGTH_MAX = 10
HIDDEN_ELEMENT = '..'
RULE = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    length = random.randint(LENGTH_MIN, LENGTH_MAX)

    progression = [str(start + step * i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = HIDDEN_ELEMENT
    question = ' '.join(progression)
    return question, correct_answer
