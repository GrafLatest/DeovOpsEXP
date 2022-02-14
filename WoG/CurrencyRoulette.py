from currency_converter import CurrencyConverter
from Live import *
import random
difficulty = 0
c = CurrencyConverter()
t = int(random.uniform(1, 100))
x = c.convert(t, 'USD', 'ILS')
y = round(x, 2)


def get_money_interval():
    inter = (y - (5 - difficulty), y + (5 - difficulty))
    inter = list(inter)
    return inter


def get_guess_from_user():
    get_guess = input(f"How much you think {t} Dollars is in New Israeli Shekels? ")
    get_guess = float(get_guess)
    return get_guess


def play_currency(difficulty_chosen):
    global difficulty
    difficulty = difficulty_chosen
    inter = get_money_interval()
    get_guess = get_guess_from_user()
    print(f"You believe {get_guess} is close to be right, let's see...")
    if float(inter[0]) <= float(get_guess) <= float(inter[1]):
        win = True
        print(f"The correct answer is between {float(inter[0])} and {float(inter[1])}")
        print("Well done, you're a conversion genius!")
    else:
        win = False
        print(f"The correct answer is between {float(inter[0])} and {float(inter[1])}")
        print("Sorry you're way off, try again soon!")
    return win







