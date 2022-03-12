import os


def utils():
    score_txt = "Scores.txt"
    return score_txt


def screen_clr():
    x = input("Please input 'clr' to clear the screen")
    if x == "clr":
        os.system('clear'), os.system('clr')
    else:
        print("Incorrect input. please use 'clr' ")
    return screen_clr()

