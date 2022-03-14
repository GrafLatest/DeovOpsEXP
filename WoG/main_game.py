from Live import *
from GuessGame import play_guess
from MemoryGame import play_memory
from CurrencyRoulette import play_currency
import Score
import MainScores
import e2e

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
exec(MainScores.app.run())
exec(e2e.main_function())
# Score.add_score(difficulty_chosen)
