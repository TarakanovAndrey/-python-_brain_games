import random


TASK = 'What number is missing in the progression?'


def get_question_right_answer():
    start_number = random.randint(1, 100)
    diff = random.randint(1, 10)
    end_num = start_number + diff * 10
    choice_number = random.randint(0, 9)
    value_for_question = ''
    right_answer = 0
    for num, i in enumerate(range(start_number, end_num, diff)):
        if num == choice_number:
            value_for_question += '..' + ' '
            right_answer = i
        else:
            value_for_question += str(i) + ' '
    return value_for_question[:-1], str(right_answer)
