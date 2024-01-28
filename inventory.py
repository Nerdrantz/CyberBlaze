# inventory.py

from typing import Dict, List

from loot_types import loot_types_dict
from term_utils import center_text, center_input

class Inventory:
    def __init__(self, player_credits, player_fleet, player_inventory) -> None:
        self.credits: int = max(player_credits, 0)
        self.fleet: List[str] = player_fleet or list()
        self.inventory: Dict[str, int] = player_inventory or dict()

    def display_inventory(self):
        print(center_text(
            f"Inventory: {', '.join(f'{name}: {amount}' for name, amount in self.inventory.items())}\n"
            f"Credits: {self.credits}\n"
            f"Fleet: {', '.join(self.fleet)}\n"
        ))

    def add_credits(self, amount):
        self.credits += amount

    def subtract_credits(self, amount):
        self.credits = max(0, self.credits - amount)

    def add_ship_to_fleet(self, ship_name):
        self.fleet.append(ship_name)
        print(center_text(f"\nUpdated fleet: {', '.join(self.fleet)}"))

    def update_inventory(self, loot_type, loot_amount):
        self.inventory[loot_type] = self.inventory.get(loot_type, 0) + loot_amount

    def show_sellable_items(self):
        print(center_text("\nSellable Items: "))
        for i, (name, quantity) in enumerate(self.inventory.items(), start=1):
            print(center_text(f"{i}, {name} - Quantity: {quantity}"))

    def sell_item(self, item_index):
        if item_index < 1 or item_index > len(self.inventory):
            print("Invalid item choice. Please enter a valid number.")
            return
        name, quantity = list(self.inventory.items())[item_index - 1]
        loot_type = loot_types_dict.get(name)
        if not loot_type:
            print("Invalid item type. Unable to sell.")
            return
        sell_value = loot_type.value * quantity
        self.add_credits(sell_value)  # Update player_credits
        del self.inventory[name]
        print(center_text(f"You sold {quantity} {name}(s) for {sell_value} credits."))
