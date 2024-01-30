# game_logic.py

import time
import sys


from game_menu import start_game
from term_utils import clear_screen, center_text
from game_data_manager import GameDataManager
from loading_bar import loading_bar

game_starting = "Game is starting...\nCalculating thrust vectors...\nInitiating spacecraft systems...\nVerifying life support systems...\nEstablishing connection with galactic databases..."


def load_save():
    ...

def save_game(data):
    GameDataManager.save_game_data(data)
    
def default_data():
    try:
        player_name = input(center_text("Enter your name: "))
    except KeyboardInterrupt:
        sys.exit(0)
    return {
        "player_name": player_name,
        "player_credits": 100,
        "player_fleet": list(),
        "player_inventory": list(),
    }

def start_game_logic():    
    clear_screen()
    # Wait for seconds to start the game
    time.sleep(2)

    # Add your game logic here
    print(center_text(game_starting))
     # Display the loading bar for a short duration
    for _ in range(100):  # Adjust the number of iterations as needed
        time.sleep(0.1)
        loading_bar(100, _ + 1)  # Assuming a total of 20 steps
    time.sleep(0)

    # Clear the screen and then load the player data
    clear_screen()
    print(center_text("Welcome Commander! It seems you were hired on to control the next fleet in the Divex System.\n Don't let the spooky bedtime stories of the Aleran get to you, you're going to do just fine.\n First we should get your name so we can astablish who you are...\n"))
    game_data = load_save() or default_data()
    
    player_name = game_data["player_name"] # Store the players name so it can be saved. 
    print(center_text("\nAhh that is a fine name. It suits you very well! Alright, lets get going here as we have much to do!"))
     # Display the loading bar for a short duration
    for _ in range(20):  # Adjust the number of iterations as needed
        time.sleep(0.1)
        loading_bar(20, _ + 1)  # Assuming a total of 20 steps
    time.sleep(0)
    
    # Clear the screen again and then add the players name to the screen
    # and load the menu
    clear_screen()
    print(center_text(f"Welcome Commander {game_data.pop('player_name')}"))
    try:
        start_game(game_data)
    except KeyboardInterrupt:
        # or `pass` will return to the main menu
        sys.exit(0)
    finally:
        game_data["player_name"] = player_name  # Restore player_name in the game_data before saving
        save_game(game_data)