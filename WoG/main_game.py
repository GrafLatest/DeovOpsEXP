from Live import *
from GuessGame import play_guess
from MemoryGame import play_memory
from CurrencyRoulette import play_currency
greeting_name()
game_chosen, difficulty_chosen = load_game()

if game_chosen == 1:
    play_memory(difficulty_chosen)
elif game_chosen == 2:
    play_guess(difficulty_chosen)
elif game_chosen == 3:
    play_currency(difficulty_chosen)
