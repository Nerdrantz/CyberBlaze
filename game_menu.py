# game_menu.py

from inventory import display_inventory
from sell_items import sell_item, show_sellable_items
from term_utils import center_text, center_input


# Main menu in game after leaving the original main menu.
def game_menu():
    
    # Get the list of ships in the ship list.
    from ships_list import show_buyable_ships, buy_ship, send_ship_on_expedition
    
    #Menu options
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
