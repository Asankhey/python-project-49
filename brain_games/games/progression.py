from random import randint

RULE = "What number is missing in the progression?"


def generate_progression(start, step, length):
    return [str(start + step * i) for i in range(length)]


def get_question_answer():
    start = randint(1, 10)
    step = randint(1, 5)
    length = 10
    progression = generate_progression(start, step, length)

    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer
