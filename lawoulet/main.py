from utils import *

username = input_username()
while True:
    user_input_str = input("Guess the number (between 0 and 100): ")
    if not user_input_str:
        print("Please enter a number.")
        continue
    try:
        user_input = int(user_input_str)
        if user_input < 0 or user_input > 100:
            print("Please enter a number between 0 and 100.")
        else:
            game_rules(user_input, username)
        input("Press any key to continue... ")
        if input:
            pass
        clear()
        play_again = input(
            "Do you want to play again? Pres any key \n[K] quit the game:[>... ").strip().lower()
        clear()
        if play_again == 'k':
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        clear()
