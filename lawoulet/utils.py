import os
import pickle
import random
import time


def clear(): return os.system('cls')


def input_username():
    while True:
        username = input('Please enter a username: ').lower()
        clear()

        existing_user = get_user(username)
        if existing_user:
            time.sleep(1)
            clear()
            print(f"Welcome back, {existing_user['username']}!")
            time.sleep(1)
            print(f"Your score is {existing_user['score']}")
            time.sleep(1)
            print("\t\t\tStarting the game...")
            progress_bar(20, 5)
            clear()
            return username

        else:
            if " " in username:
                print("Username cannot contain spaces.")
                time.sleep(2)
                clear()
            elif username == "":
                print("Username cannot be empty.")
                time.sleep(2)
                clear()
            elif username.isdigit():
                print("Username cannot be a number.")
                time.sleep(2)
                clear()
            else:
                register_name(username)
                print('Username registered successfully!')
                time.sleep(2)
                clear()
                print(f"Welcome, {username}!")
                time.sleep(2)
                clear()
                time.sleep(1)
                print("\t\t\tStarting the game...")
                progress_bar(20, 5)
                time.sleep(2)
                return username


def register_name(username, score=0):
    database = load_database()
    user_exists = False
    for user in database:
        if user['username'] == username:
            user_exists = True
            break

    if not user_exists:
        database.append({
            'username': username,
            'score': score
        })
    save_database(database)


def load_database():
    try:
        with open('database.pickle', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def save_database(database):
    with open('database.pickle', 'wb') as file:
        pickle.dump(database, file)


def get_user(username):
    database = load_database()
    for user in database:
        if user['username'] == username:
            return user
    return None


def get_user_score(username):
    database = load_database()
    for user in database:
        if user['username'] == username:
            return user['score']
    return None


def update_user_score(username, score):
    database = load_database()
    for user in database:
        if user['username'] == username:
            user['score'] += score
            break
    save_database(database)


def game_rules(user_input, username):
    computer_choice = random.randint(0, 1)
    life = 10
    while life > 0:
        old_score = get_user_score(username)

        try:
            user_input = int(input("Guess again: "))
            clear()
            if user_input < 0 or user_input > 100:
                print("Please enter a number between 0 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_input < computer_choice:
            print("Your guess is too low")
        elif user_input > computer_choice:
            print("Your guess is too high")
        elif user_input == computer_choice:
            score = life * 30
            update_user_score(username, score)
            newscore = get_user_score(username)
            print(f"You win! Your score is {score} points")
            print(
                f"Congratulations! You set a new high score of {newscore} points.")
            if score > old_score:
                update_user_score(username, newscore)
                print(f"Your previous score was {old_score} points.")
                print(f"Your new high score is {newscore} points.")
            else:
                print(f"Your high score was at {old_score} points.")
            break
        life -= 1
    else:
        print(f"You lose. The number was {computer_choice}")


def progress_bar(total_iterations, total_duration):
    delay = total_duration / total_iterations
    for i in range(total_iterations + 1):
        progress = i / total_iterations
        bar_length = 40
        block = int(round(bar_length * progress))
        progress_text = f"[{'#' * block}{'-' * (bar_length - block)}] {progress * 100:.1f}%"
        print(progress_text, end='\r', flush=True)
        time.sleep(delay)

    print()
