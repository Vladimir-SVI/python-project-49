import random

rules_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_data():
    random_number = random.randint(2, 100)
    prime = is_prime(random_number)
    result = prime is False and 'no' or 'yes'
    return random_number, str(result)
