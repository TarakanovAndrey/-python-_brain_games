import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_right_answer(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_question_right_answer():
    value_for_question = random.randint(1, 1000)
    if get_right_answer(value_for_question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return value_for_question, right_answer
