import random

rules_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    question = random.randint(1, 10)
    result = 'no'
    if question % 2 == 0:
        result = 'yes'
    return question, result
