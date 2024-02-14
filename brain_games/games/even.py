import random

RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data():
    random_number = random.randint(1, 10)
    result = 'yes' if random_number % 2 == 0 else 'no'
    return random_number, result
