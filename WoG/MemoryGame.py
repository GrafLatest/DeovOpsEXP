from Live import *
import random
import subprocess
from subprocess import call
import time
difficulty = 0


def generate_sequence():
    generated = [random.randrange(1, 101) for i in range(difficulty)]
    print(generated)
    time.sleep(2)
    print(chr(27) + "[2J")
    return generated


def get_list_from_user():
    list_from_input = []

    for i in range(0, difficulty):
        num = int(input(f"Please input the number {i}: "))
        list_from_input.append(num)
    return list_from_input


def is_list_equal(generated, list_from_input):
    list1 = generated
    list2 = list_from_input
    if list2 == list1:
        win = True
        print("Great job! you remembered correctly!")
    else:
        win = False
        print("Sorry, you are not correct, please try again soon.")
    return win


def play_memory(difficulty_chosen):
    global difficulty
    difficulty = difficulty_chosen
    is_list_equal(generated=generate_sequence(), list_from_input=get_list_from_user())









