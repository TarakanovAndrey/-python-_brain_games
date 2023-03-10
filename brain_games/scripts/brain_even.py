#!/usr/bin/env python3


from brain_games.library.greets import greets
from brain_games.library.task_brain_even import task
from brain_games.library.is_even import is_even
from brain_games.library.random_1_1000 import random_num


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
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break


def main():
    even()


if __name__ == '__main__':
    main()
