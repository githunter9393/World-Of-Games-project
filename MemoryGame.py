import random
import time
from scores import update_scores

def play_MemoryGame(difficulty, name):

 def generate_sequence(n):
    """
    Generates a list of 'n' random numbers and displays them briefly.
    """
    random_numbers = [random.randint(1, 100) for _ in range(n)]
    print(f"Generated numbers: {random_numbers}")
    time.sleep(1)
    print("\n" * 100)
    return random_numbers

 def get_list_from_user(n):
    """
    Gets 'n' numbers from the user.
    """
    user_numbers = []
    for i in range(n):
        user_input = input(f"Enter number {i + 1}: ")
        user_numbers.append(int(user_input))  # Convert input to an integer
    return user_numbers

 def is_list_equal(list1, list2):
    """
    Compares two lists and determines if they are equal.
    """
    return list1 == list2

# Example usage:
 try:
    n = difficulty
    generated_list = generate_sequence(n)
    user_list = get_list_from_user(n)

    result = is_list_equal(generated_list, user_list)
    if result:
        print("Congratulations! The lists are equal.")
        update_scores(name, n)
    else:
        print("Oops! The lists are not equal.")
 except ValueError:
    print("Invalid input. Please enter a valid integer for the number of elements.")