def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play.")

def load_game(name):
    from GuessGame import play_GuessGame
    from MemoryGame import play_MemoryGame
    from CurrencyRouletteGame import play_CurrencyRouletteGame

    chosen_game = int(input('''Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second, and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS: '''))

    print(' ')
    difficulty = int(input('Please choose game difficulty from 1 to 5: '))

    if 1 <= difficulty <= 5:
        if chosen_game == 2:
            play_GuessGame(difficulty,name)
        elif chosen_game == 1:
            play_MemoryGame(difficulty,name)
        elif chosen_game == 3:
            play_CurrencyRouletteGame(difficulty,name)
        else:
            print("Please enter a number from 1 to 3")

    else:
        print("Invalid difficulty. Please choose a number between 1 and 5.")
    return
