#!/usr/bin/env python3


import prompt


def show_greet_and_get_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def main():
    show_greet_and_get_name()


if __name__ == '__main__':
    main()
