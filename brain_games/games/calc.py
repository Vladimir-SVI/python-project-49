import random

RULES_GAME = 'What is the result of the expression?'


def generate_data():
    operators = '+-*'
    operand_left = random.randint(1, 10)
    operand_right = random.randint(1, 10)
    operator = random.choice(operators)
    question = f'{operand_left} {operator} {operand_right}'
    if operator == '+':
        result = operand_left + operand_right
    elif operator == '-':
        result = operand_left - operand_right
    elif operator == '*':
        result = operand_left * operand_right
    else:
        raise Warning("operator is not among the operators used")
    return question, str(result)
