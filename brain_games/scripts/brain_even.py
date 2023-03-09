#!/usr/bin/env python3


import prompt
import random


def greets():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def task():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def random_num():
    num = random.randint(1, 1000)
    return num


def even():
    name = greets()
    task()
    for i in range(3):
        num = random_num()
        right_answer = is_even(num)
        print(f'Question: {num}')
        answer = input()
        if answer == right_answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}"')
            print(f"Let's try again, {name}!")
            break


def main():
    even()

if __name__ == '__main__':
    main()



