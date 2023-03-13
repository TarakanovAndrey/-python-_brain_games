import prompt


def show_greet_and_get_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_question(value_for_question):
    print(f'Question: {value_for_question}')


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def end_game(name):
    print('Correct!')
    print(f'Congratulations, {name}!')


def get_correct_answer():
    print('Correct!')


def get_wrong_answer(answer, right_answer, name):
    print(f'"{answer}" is wrong answer ;(. '
          f'Correct answer was "{right_answer}".')
    print(f"Let's try again, {name}!")


def launch_game(task, game):
    name = show_greet_and_get_name()
    number_of_rounds = 3
    count_of_rounds = 1
    task()
    while count_of_rounds <= number_of_rounds:
        value_for_question, right_answer = game()
        get_question(value_for_question)
        answer = get_answer()
        if answer == right_answer and count_of_rounds == number_of_rounds:
            end_game(name)
            break
        elif answer == right_answer:
            get_correct_answer()
            count_of_rounds += 1
        else:
            get_wrong_answer(answer, right_answer, name)
            break
