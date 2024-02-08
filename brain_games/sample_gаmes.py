import prompt


def launch_game_logic(rules_game, run_game):
    print("Welcome to the Brain Games!")
    player_name = prompt.string('May I have your name? ')
    print(f"Hello, {player_name}!")
    print(rules_game)
    for i in range(1, 4):
        correct_answer = run_game()
        print(f"Question: {correct_answer['question']}")
        answer = prompt.string('Your answer: ').strip()
        if answer == correct_answer['result']:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer['result']}'.")
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f"Congratulations, {player_name}!")
