import random
import math

rules_game = 'Find the greatest common divisor of given numbers.'


def run_game():
    number_left = random.randint(1, 100)
    number_right = random.randint(1, 100)
    question = f'{number_left} {number_right}'
    print(f"Question: {question}")
    result = math.gcd(number_left, number_right)
    return str(result)
