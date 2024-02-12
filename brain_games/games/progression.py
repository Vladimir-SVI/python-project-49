import random

rules_game = 'What number is missing in the progression?'


def generate_data():
    length_progression = 10
    first_element_progression = random.randint(1, 100)
    denominator_progression = random.randint(1, 10)
    start = first_element_progression
    stop = start + length_progression * denominator_progression
    step = denominator_progression
    progression = list(range(start, stop, step))
    list_progression = list(map(str, progression))
    number_choice = random.choice(list_progression)
    number_index = list_progression.index(number_choice)
    list_progression[number_index] = '..'
    question = ' '.join(list_progression)
    return question, number_choice
