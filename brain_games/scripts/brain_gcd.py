#!/usr/bin/env python3


import prompt
from brain_games.library.finding_gcd import finding_gcd
from brain_games.library.task_brain_gcd import show_task
from brain_games.library.greet import show_greet_and_get_name
from brain_games.library.random_1_100 import choice_random_number


name = show_greet_and_get_name()
show_task()
    

def brain_gcd():
    
    for i in range(3):
        number_1 = choice_random_number()
        number_2 = choice_random_number()
        right_answer = finding_gcd(number_1, number_2)
        print(f'Question: {number_1}  {number_2}')
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
    brain_gcd()


if __name__ == '__main__':
    main()
