import random

rules_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    random_number = random.randint(1, 100)
    count = 0
    for i in range(2, random_number // 2 + 1):
        if (random_number % i == 0):
            count = count + 1
    result = 'no'
    if (count <= 0):
        result = 'yes'
    print(f"Question: {random_number}")
    return str(result)
