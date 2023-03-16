import random


def print_task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_right_answer(num):
    if num == 2:
        return 'yes'
    for i in range(2, num):
        if num % i == 0:
            return 'no'
    return 'yes'


def get_question_right_answer():
    number = random.randint(1, 100)
    value_for_question = number
    right_answer = get_right_answer(number)
    return value_for_question, right_answer
