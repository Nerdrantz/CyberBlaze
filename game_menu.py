# game_menu.py

from typing import Any, Dict

from inventory import Inventory
from ships_list import show_buyable_ships, buy_ship, send_ship_on_expedition
from term_utils import center_text, center_input, input_number

# Menu options
menu_options = [
    "\nSelect an option:",
    "1. Buy a ship",
    "2. Send ship on expedition",
    "3. Inventory",
    "4. Sell items",
    "5. Main menu",
]


# Main menu in game after leaving the original main menu.
def start_game(game_data: Dict[str, Any]):
    inventory_data = {
        "credits": game_data.get("credits", 0),
        "fleet": game_data.get("fleet", list()),
        "inventory": game_data.get("inventory", dict()),
    }
    inventory = Inventory(**inventory_data)

    while 1:
        for option in menu_options:
            print(center_text(option))

        match center_input("\nEnter a number: "):
            case "1":
                show_buyable_ships()
                buy_choice = input_number("\nEnter the number of the ship you want to buy: ")
                if buy_choice is not None:
                    buy_ship(buy_choice, inventory)
            case "2":
                send_ship_on_expedition(inventory)
            case "3":
                inventory.display_inventory()
            case "4":
                inventory.show_sellable_items()
                sell_choice = input_number("\nEnter the number of the item you want to sell: ")
                if sell_choice is not None:
                    inventory.sell_item(sell_choice)
            case "5":
                game_data.update(inventory.as_dict())
                break
            case _:
                print("Invalid choice. Please enter 1 or 2 or 3.")
