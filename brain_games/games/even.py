import random

rules_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_round():
    question = random.randint(1, 10)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result
