import random


def print_task():
    print('What number is missing in the progression?')


def get_random_number():
    number = random.randint(1, 100)
    return number


def get_question_right_answer():
    start_num = get_random_number()
    diff = random.randint(1, 10)
    progression = [start_num]
    for i in range(9):
        value = start_num + diff
        progression.append(value)
        start_num = value
    right_answer = random.choice(progression)
    value_for_question = ''
    for num, el in enumerate(progression):
        if el == right_answer:
            el = '..'
        value_for_question = value_for_question + str(el) + ' '

    return [value_for_question, right_answer]