#!/usr/bin/env python3


import prompt
from brain_games.library.create_progression import create_progression
from brain_games.library.greet import show_greet_and_get_name
from brain_games.library.task_brain_progression import show_task


def find_number_in_progression():
    name = show_greet_and_get_name()
    show_task()
    for i in range(3):
        result = create_progression()
        right_answer = result[1]
        print(f'Question: {result[0]}')
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
    find_number_in_progression()


if __name__ == '__main__':
    main()
