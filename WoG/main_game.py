from Live import *
from GuessGame import play_guess
from MemoryGame import play_memory
from CurrencyRoulette import play_currency
import Score
greeting_name()
game_chosen, difficulty_chosen = load_game()

if game_chosen == 1:
    my_score = play_memory(difficulty_chosen)
elif game_chosen == 2:
    my_score = play_guess(difficulty_chosen)
elif game_chosen == 3:
    my_score = play_currency(difficulty_chosen)

Score.add_score(difficulty_chosen)
