import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def launch_game_logic(player_name, rules_game, run_game):
    print(rules_game)
    number_of_attempts = 3
    while number_of_attempts > 0:
        correct_answer = run_game()
        answer = prompt.string('Your answer: ').strip()
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            break
        number_of_attempts = number_of_attempts - 1
        if number_of_attempts == 0:
            print(f"Congratulations, {player_name}!")
