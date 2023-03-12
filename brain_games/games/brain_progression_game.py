import random


def print_task():
    print('What number is missing in the progression?')


def get_random_number():
    number = random.randint(1, 100)
    return number


def create_progression():
    start_num = get_random_number()
    diff = random.randint(1, 10)
    progression = [start_num]
    for i in range(9):
        value = start_num + diff
        progression.append(value)
        start_num = value
    choice_num = random.choice(progression)
    progression_for_question = ''
    for num, el in enumerate(progression):
        if el == choice_num:
            el = '..'
        progression_for_question = progression_for_question + str(el) + ' '

    return [progression_for_question, choice_num]


def get_question_right_answer():
    value_for_question, right_answer = create_progression()
    return [value_for_question, str(right_answer)]
