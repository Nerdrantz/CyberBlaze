# game_logic.py

import os
import time
from ships_list import show_buyable_ships, buy_ship, send_ship_on_expedition
from inventory import display_inventory
from game_menu import game_menu

game_starting = ("Game is starting...\nCalculating thrust vectors...")

def center_input(prompt):
    # Get the user input
    user_input = input(center_text(prompt))
    return user_input
    
def center_text(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Calculate the width of the terminal
    terminal_width = os.get_terminal_size().columns
    
    # Create a list to store centered lines
    centered_lines = []
    
    for line in lines:
        # Calculate the number of spaces needed to center each line
        padding = (terminal_width - len(line)) // 2
        centered_lines.append(" " * padding + line)
    
    # Return the joined centered lines
    return '\n'.join(centered_lines)
    
def clear_screen():
    # Check if the operating system is Windows or not
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac




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
    
