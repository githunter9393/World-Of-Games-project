from currency_converter import CurrencyConverter
import random
from scores import update_scores



def play_CurrencyRouletteGame(difficulty,name):
    # Define the variable 'y' (adjust as needed)
    y = 5 - difficulty

    def get_money_interval():
        random_number = random.randint(1, 100)
        c = CurrencyConverter()
        usd_amount = random_number
        ils_amount = c.convert(usd_amount, 'USD', 'ILS')
        print(f"Random USD amount: {usd_amount:.2f}")
        return ils_amount

    def get_guess_from_user():
        user_input = input("Enter your guess (ILS): ")
        return float(user_input)

    try:
        y = 5 - difficulty  # Define the difficulty (or pass it as an argument)
        generated_ils = get_money_interval()
        user_ils_guess = get_guess_from_user()

        if generated_ils - y <= user_ils_guess <= generated_ils + y:
            print("Congratulations! Your guess is within the valid range.")
            update_scores(name, difficulty)
        else:
            print(f"Oops! Your guess is outside the valid range. The random ILS amount was {generated_ils:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play_CurrencyRouletteGame()


