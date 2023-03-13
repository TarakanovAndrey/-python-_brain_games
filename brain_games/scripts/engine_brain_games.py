import prompt


def show_greet_and_get_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def launch_game(task, game):
    name = show_greet_and_get_name()
    number_of_rounds = 3
    count_of_rounds = 1
    task()
    while count_of_rounds <= number_of_rounds:
        value_for_question, right_answer = game()
        print(f'Question: {value_for_question}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer and count_of_rounds == number_of_rounds:
            print('Correct!')
            print(f'Congratulations, {name}!')
            break
        elif answer == right_answer:
            print('Correct!')
            count_of_rounds += 1
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break
