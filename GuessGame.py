import random
from scores import update_scores

def play_GuessGame(difficulty, name):
    def generate_number():
        return random.randint(0, difficulty)

    def get_guess_from_user():
        guess = input('Guess the number!\n')
        return int(guess)  # Convert input to an integer

    def compare_results(value1, value2):
        return value1 == value2

    try:
        random_number = generate_number()
        guess = get_guess_from_user()
        x = compare_results(guess, random_number)
        if x:
            print("You Won")
            update_scores(name, difficulty)
        else:
            print("Try Again :)")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


