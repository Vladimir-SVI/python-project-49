import random
import math

rules_game = 'Find the greatest common divisor of given numbers.'


def run_game():
    number_left = random.randint(1, 100)
    number_right = random.randint(1, 100)
    question = f'{number_left} {number_right}'
    result = math.gcd(number_left, number_right)
    return {'result': str(result), 'question': question}
