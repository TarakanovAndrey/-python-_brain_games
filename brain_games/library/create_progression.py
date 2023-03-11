import random
from brain_games.library.random_1_100 import choice_random_number
from brain_games.library.random_1_10 import choice_random_number_1_10


def create_progression():
    start_num = choice_random_number()
    diff = choice_random_number_1_10()
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
