import random

rules_game = 'What is the result of the expression?'


def run_game():
    operators = '+-*'
    operand_left = random.randint(1, 10)
    operand_right = random.randint(1, 10)
    operator = random.choice(operators)
    question = f'{operand_left} {operator} {operand_right}'
    print(f"Question: {question}")
    if operator == '+':
        result = operand_left + operand_right
    elif operator == '-':
        result = operand_left - operand_right
    else:
        result = operand_left * operand_right
    return str(result)
