import random
import operator


def print_task():
    print('What is the result of the expression?')


def choice_random_number():
    number = random.randint(1, 100)
    return number


def get_question_right_answer():
    number_1 = choice_random_number()
    number_2 = choice_random_number()
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    operator_list = ["+", "-", "*"]
    oper_value = random.choice(operator_list)
    right_answer = action[oper_value](number_1, number_2)
    question = str(number_1) + ' ' + str(oper_value) + ' ' + str(number_2)
    return [question, str(right_answer)]
