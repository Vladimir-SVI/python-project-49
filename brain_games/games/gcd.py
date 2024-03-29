import random
import math

RULES_GAME = 'Find the greatest common divisor of given numbers.'


def generate_data():
    number_left = random.randint(1, 100)
    number_right = random.randint(1, 100)
    question = f'{number_left} {number_right}'
    result = math.gcd(number_left, number_right)
    return question, str(result)
