import operator
import random
from brain_games.library.random_1_100 import choice_random_number


def calculation_result():
    number_1 = choice_random_number()
    number_2 = choice_random_number()
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    operator_list = ["+", "-", "*"]
    operator_value = random.choice(operator_list)
    right_answer = action[operator_value](number_1, number_2)
    print(f'Question: {number_1} {operator_value} {number_2}')
    return right_answer

