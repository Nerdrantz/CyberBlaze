# cyberblaze.py

import time
import sys

from game_data_manager import GameDataManager
from game_logic import start_game_logic
from term_utils import clear_screen, center_text, center_input

# Wait for seconds to start the game
time.sleep(2)


# How to play description
def show_how_to_play():
    clear_screen()
    # Display instructions on how to play
    print(
        center_text(
            """
    Welcome to CyberBlaze!
    - This game was made entirely in raw python with no additional libraries
    - Use the options on the menu to get started
    - This is a space mining game built in python to run fully in your terminal! 
    - While I would like to currently have an end game, right now there really is no defined end game.
    - You buy ships, send them out to collect resources, then sell the resources to gain more currency.
    - At some point I will add more functionality, maybe factions or something?
    - Feel free to leave some feedback!
    - Have fun!
    
    -FAQ
    -Each Player starts with 100 credits
    -Buy your first ship, then send it on an expedition. The longer the expedition, the more loot you get.
    -Sell your loot to buy better ships. 
    """
        )
    )
    input(center_text("Press any key to return to the menu..."))

def load_game():
    return GameDataManager.load_game_data()

# Main menu
def show_menu():
    clear_screen()
    title = r"""
    _________        ___.               __________.__                        
    \_   ___ \___.__.\_ |__   __________\______   \  | _____  ________ ____  
    /    \  \<   |  | | __ \_/ __ \_  __ \    |  _/  | \__  \ \___   // __ \ 
    \     \___\___  | | \_\ \  ___/|  | \/    |   \  |__/ __ \_/    /\  ___/ 
     \______  / ____| |___  /\___  >__|  |______  /____(____  /_____ \\___  >
            \/\/          \/     \/             \/          \/      \/    \/   
    """
    print(center_text(title))

    menu_options = [
        "Developed by Nerdrantz",
        "Select an option:",
        "1. How to play",
        "2. New Game",
        "3. Load Game",
        "4. Quit",
    ]

    while 1:
        for option in menu_options:
            print(center_text(option))

        match center_input("\nEnter a number: "):
            case "1":
                show_how_to_play()
            case "2":
                start_game_logic()  # Call the game logic function
            case "3":
                start_game_logic(load_game())
            case "4":
                print("Exiting the program. Goodbye!")
                sys.exit(0)
            case _:
                print("Invalid choice. Please enter 1 or 2 or 3.")


# Initial display of the menu
if __name__ == "__main__":
    show_menu()
