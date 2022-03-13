from Live import *
import random
difficulty = 0


def generate_number():
    secret_num = int(random.uniform(1, difficulty))
    return secret_num


def get_guess_from_user():
    user_input = input(f"Please input a number from 1 to {difficulty}: ")
    user_input = int(user_input)
    return user_input


def compare_results(secret_num, user_input):
    if user_input == secret_num:
        print(f"Congrats, you win! {user_input} is the correct answer")
        win = True
        return win
    else:
        print(f"Sorry... {user_input} is not the correct answer")
        print(f"Number was {secret_num}")
        win = False
        return win


def play_guess(difficulty_chosen):
    global difficulty
    difficulty = difficulty_chosen
    generate_number()
    win = compare_results(secret_num=generate_number(), user_input=get_guess_from_user())
    return win
