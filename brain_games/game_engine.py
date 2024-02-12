import prompt

NUMBER_OF_QUESTIONS = 3


def launch(game):
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f"Hello, {player_name}!")
    print(game.rules_game)
    for i in range(NUMBER_OF_QUESTIONS):
        question, correct_answer = game.generate_data()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ').strip()
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f"Congratulations, {player_name}!")
