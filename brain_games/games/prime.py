import random

RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_data():
    random_number = random.randint(2, 100)
    result = 'yes' if is_prime(random_number) else 'no'
    return random_number, str(result)
