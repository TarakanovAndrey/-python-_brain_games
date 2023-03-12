import random


def get_number():
    number = random.randint(1, 1000)
    return number


def get_right_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def print_task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_question_right_answer():
    value_for_question = get_number()
    right_answer = get_right_answer(value_for_question)
    return [value_for_question, right_answer]
