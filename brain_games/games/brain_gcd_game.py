import random


def print_task():
    print('Find the greatest common divisor of given numbers.')


def findig_gcd(num1, num2):
    max_num = max([num1, num2])
    min_num = min([num1, num2])
    gcd = min_num
    if max_num % min_num == 0:
        return min_num
    else:
        gcd = min_num // 2
    while gcd >= 1:
        if max_num % gcd == 0 and min_num % gcd == 0:
            return gcd
        else:
            gcd -= 1
    return gcd


def random_num():
    num = random.randint(1, 100)
    return num


def get_question_right_answer():
    num1 = random_num()
    num2 = random_num()
    value_for_question = str(num1) + ' ' + str(num2)
    right_answer = findig_gcd(num1, num2)
    return [value_for_question, str(right_answer)]
