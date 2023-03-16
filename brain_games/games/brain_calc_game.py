import random
import operator


def print_task():
    print('What is the result of the expression?')


def get_question_right_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    operator_list = ["+", "-", "*"]
    operator_value = random.choice(operator_list)
    right_answer = action[operator_value](number_1, number_2)
    value_for_question = f'{number_1} {operator_value} {number_2}'
    return value_for_question, str(right_answer)
