from Live import *
from GuessGame import play_guess
from MemoryGame import play_memory
from CurrencyRoulette import play_currency
import Score
name = greeting_name()
game_chosen, difficulty_chosen = load_game()

if game_chosen == 1:
    win = play_memory(difficulty_chosen)
    if win == True:
        Score.add_score(difficulty_chosen)
    else:
        print("wrong")
elif game_chosen == 2:
    win = play_guess(difficulty_chosen)
    if win == True:
        Score.add_score(difficulty_chosen)
    else:
        print("wrong")
elif game_chosen == 3:
    win = play_currency(difficulty_chosen)
    if win == True:
        Score.add_score(difficulty_chosen)
    else:
        print("wrong")

# Score.add_score(difficulty_chosen)
