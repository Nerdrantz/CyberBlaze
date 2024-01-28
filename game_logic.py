# game_logic.py

import time
import sys

from game_menu import start_game
from term_utils import clear_screen, center_text


game_starting = "Game is starting...\nCalculating thrust vectors..."


def load_save():
    ...


def default_data():
    try:
        player_name = input("Enter your name: ")
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
    time.sleep(2)

    # Clear the screen and then load the player data
    clear_screen()
    game_data = load_save() or default_data()

    # Clear the screen again and then add the players name to the screen
    # and load the menu
    clear_screen()
    print(center_text(f"Welcome Commander {game_data.pop('player_name')}"))
    try:
        start_game(game_data)
    except KeyboardInterrupt:
        # or `pass` will return to the main menu
        sys.exit(0)
