import random

rules_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count = count + 1
    result = 'no'
    if count <= 0:
        result = 'yes'
    return result


def play_round():
    random_number = random.randint(2, 100)
    result = is_prime(random_number)
    return random_number, str(result)
