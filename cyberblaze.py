# cyberblaze.py

import os
import time
import sys
from game_logic import start_game_logic

# Wait for seconds to start the game
time.sleep(2)

# function for clearing the screen
def clear_screen():
    # Check if the operating system is Windows or not
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac
        
# function for centering text
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

# Center the user input in the terminal.
def center_input(prompt):
    # Get the user input
    user_input = input(center_text(prompt))
    return user_input

# How to play description
def show_how_to_play():
    clear_screen()
    # Display instructions on how to play
    instructions = """
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
    print(center_text(instructions))
    input("Press any key to return to the menu...")
    show_menu()
 
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
        "\nSelect an option:",
        "1. How to play",
        "2. New Game"
        "\n3. Load Game"
        "\n4. Quit"
    ]

    for option in menu_options:
        print(center_text(option))

    choice = center_input("\nEnter a number: ")

    if choice == "1":
        show_how_to_play()
    elif choice == "2":
        start_game_logic()  # Call the game logic function
        show_menu()
    elif choice == "3":
        print("Not usable yet")
        show_menu()
    elif choice == "4":
        sys.exit("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter 1 or 2 or 3.")
        show_menu()

# Initial display of the menu
show_menu()
