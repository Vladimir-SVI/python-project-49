#!/usr/bin/env python3

import brain_games.scripts.brain_games
import random
import prompt


def brain_event(player_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_attempts = 3
    while number_of_attempts > 0:
        questions = random.randint(1, 10)
        print(f"Question: {questions}")
        answer = prompt.string('Your answer: ').strip()
        correct_answer = 'no'
        if questions % 2 == 0:
            correct_answer = 'yes'
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            break
        number_of_attempts = number_of_attempts - 1
        if number_of_attempts == 0:
            print(f"Congratulations, {player_name}!")


def main():
    player_name = brain_games.scripts.brain_games.main()
    brain_event(player_name)


if __name__ == '__main__':
    main()
