import prompt


NUMBER_OF_ROUNDS = 3


def show_greet_and_get_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def launch_game(game):
    name = show_greet_and_get_name()
    count_of_rounds = 0
    print(game.TASK)
    while count_of_rounds < NUMBER_OF_ROUNDS:
        value_for_question, right_answer = game.get_question_right_answer()
        print(f'Question: {value_for_question}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            count_of_rounds += 1
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            return
    if count_of_rounds == NUMBER_OF_ROUNDS:
        print(f'Congratulations, {name}!')
