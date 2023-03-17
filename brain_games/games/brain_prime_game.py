import random
from math import sqrt


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, round(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def get_question_right_answer():
    value_for_question = random.randint(2, 100)
    if is_prime(value_for_question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return value_for_question, right_answer
