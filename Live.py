def greeting_name():
    name = input("Please state your name for the record: ")
    print(f"Hello {name} and welcome to the World Of Games (WoG). Here you can find many cool games to play")


def load_game():
    print(f"Please choose a game to play: "
          f"\n 1 Memory Game - a sequence fo numbers will appear for 1 second and you have to guess back "
          f"\n 2 Guess Game - Guess a number and see if you chose like the computer "
          f"\n 3 Currency Roulette - try and guess the value of a random amount of USD in ILS ")

    while True:
        try:
            game_chosen = input("Please enter the corresponding number of the game you wish to load: ")
            game_chosen = int(game_chosen)
            if game_chosen == 1:
                print("You've chosen to play The Memory Game")
                break
            elif game_chosen == 2:
                print("You've chosen to play The Guess Game")
                break
            elif game_chosen == 3:
                print("You've chosen to play The Currency Roulette")
                break
        except:
            print(f"Your input is invalid: {game_chosen} Use a number please.")

    while True:
        try:
            difficulty_chosen = input("Please enter difficulty level from 1 to 5: ")
            difficulty_chosen = int(difficulty_chosen)
            if difficulty_chosen < 1:
                print("Incorrect input. please use number from 1 to 5")
            elif difficulty_chosen > 5:
                print("Incorrect input. please use number from 1 to 5")
            elif 1 <= difficulty_chosen <= 5:
                print(f"You'll be playing on level {difficulty_chosen} difficulty")
            break
        except:
            print(f"Invalid input --> {difficulty_chosen} difficulty level.")

    return game_chosen, difficulty_chosen
