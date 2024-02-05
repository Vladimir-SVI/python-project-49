import random

rules_game = 'What number is missing in the progression?'


def run_game():
    length_progression = 10
    first_element_progression = random.randint(1, 100)
    denominator_progression = random.randint(1, 10)
    progression = list(range(first_element_progression,
                       first_element_progression+length_progression*denominator_progression,
                       denominator_progression))
    list_progression = list(map(str, progression))
    number_choice = random.choice(list_progression)
    number_index = list_progression.index(number_choice)
    list_progression[number_index] = '..'
    question = ' '.join(list_progression)
    return {'result': number_choice, 'question': question}
