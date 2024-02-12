import random

rules_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_round():
    random_number = random.randint(1, 10)
    result = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, result
