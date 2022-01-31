from Live import *
from GuessGame import play_guess
greeting_name()
game_chosen, difficulty_chosen = load_game()

if game_chosen == 2:
    play_guess(difficulty_chosen)
