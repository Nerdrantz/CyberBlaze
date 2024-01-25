# game_menu.py

import os
from inventory import display_inventory
from sell_items import sell_item, show_sellable_items

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


def game_menu():
    
    from ships_list import show_buyable_ships, buy_ship, send_ship_on_expedition
    menu_options = [
        "\nSelect an option:",
        "1. Buy a ship",
        "2. Send ship on expedition"
        "\n3. Inventory"
        "\n4. Sell items"
    ]
    
    for option in menu_options:
        print(center_text(option))

    choice = center_input("\nEnter a number: ")

    if choice == "1":
        show_buyable_ships()
        buy_choice = center_input("\nEnter the number of the ship you want to buy: ")
        buy_ship(buy_choice)
        game_menu()
    elif choice == "2":
        send_ship_on_expedition()
        game_menu()
    elif choice == "3":
        display_inventory()
        game_menu()
    elif choice == "4":
        show_sellable_items()
        sell_choice = center_input("\nEnter the number of the item you want to sell: ")
        sell_item(sell_choice)
        game_menu()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3.")
        game_menu()
