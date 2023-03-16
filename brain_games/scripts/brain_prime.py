#!/usr/bin/env python3


from brain_games.games.brain_prime_game import get_question_right_answer as game
from brain_games.engine_brain_games import launch_game


def brain_prime():
    launch_game(game)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
