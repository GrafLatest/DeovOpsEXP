import os


def utils():
    SCORES_FILE_NAME = "Scores.txt"
    BAD_RETURN_CODE = -1
    return SCORES_FILE_NAME


def screen_clr():
    x = input("Please input 'clr' to clear the screen")
    if x == "clr":
        os.system('clear'), os.system('clr')
    else:
        print("Incorrect input. please use 'clr' ")
    return screen_clr()

