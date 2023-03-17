import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_right_answer(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question_right_answer():
    number = random.randint(1, 100)
    value_for_question = number
    if get_right_answer(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return value_for_question, right_answer
