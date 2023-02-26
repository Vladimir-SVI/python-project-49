import random

rules_game = 'What number is missing in the progression?'


def run_game():
    length_progression = 10
    list_progression = []
    first_element_progression = random.randint(1, 100)
    denominator_progression = random.randint(1, 10)
    list_progression.append(str(first_element_progression))
    for i in range(1, length_progression):
        progression_elements = first_element_progression \
            + denominator_progression
        list_progression.append(str(progression_elements))
        first_element_progression = progression_elements
    number_choice = random.choice(list_progression)
    number_index = list_progression.index(number_choice)
    list_progression[number_index] = '..'
    question = ' '.join(list_progression)
    print(f"Question: {question}")
    return number_choice
