#!/usr/bin/env python3

import prompt
from brain_games.library.greet import show_greet_and_get_name
from brain_games.library.task_brain_prime import show_task
from brain_games.library.random_1_1000 import choice_random_number
from brain_games.library.is_prime import is_prime_number


def brain_prime():
    name = show_greet_and_get_name()
    show_task
    for i in range(3):
        number = choice_random_number()
        right_answer = is_prime_number(number)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == str(right_answer):
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break
            
            
def main():
    brain_prime()


if __name__ == '__main__':
    main()
