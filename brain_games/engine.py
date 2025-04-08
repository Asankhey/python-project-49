import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    print(game.DESCRIPTION)
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    score = 3
    for _ in range(score):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
