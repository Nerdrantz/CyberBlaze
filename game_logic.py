# game_logic.py

import time

from game_menu import game_menu
from term_utils import clear_screen, center_text


game_starting = ("Game is starting...\nCalculating thrust vectors...")


def get_player_name():
    return input("Enter your name: ")
    
def start_game_logic():
    clear_screen()
    # Wait for seconds to start the game
    time.sleep(2)
    
    # Add your game logic here
    print(center_text(game_starting))
    time.sleep(2)
    
    # Clear the screen and then load the player data
    clear_screen()
    game_data = {
    "player_name": get_player_name()
    }
    
    # Clear the screen again and then add the players name to the screen
    # and load the menu
    clear_screen()
    player_name = game_data["player_name"]
    print(center_text(f"Welcome Commander {player_name}"))
    game_menu()
    
    # Sleep for 2 seconds after buying the ship so the player can actually
    # read what the heck they bought and for how much 
    time.sleep(2)
    
    # After buying the ship clear the screen and go back to the game menu
    clear_screen()
    game_menu()
    
    input("Press any key to return to the menu...")
    
