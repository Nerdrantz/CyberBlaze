# sell_items.py

from inventory import player_inventory, player_credits, add_credits
from loot_types import loot_types

def show_sellable_items():
        print("Sellable Items: ")
        for i, item in enumerate(player_inventory, start=1):
            name = item.get('name', 'Unknown Item')
            quantity = item.get('amount', 1)
            print(f"{i}, {name} - Quantity: {quantity}")
            
def sell_item(item_index):
        try:
            global player_credits
            item_index = int(item_index)
            if 1 <= item_index <= len(player_inventory):
                sold_item = player_inventory[item_index -1]
                item_name = sold_item['name']
                item_quantity = sold_item['amount']
                    
                 # Find the loot type and get its value for sale
                loot_type = next((loot for loot in loot_types if loot["name"] == item_name), None)
                if loot_type:
                    sell_value = loot_type['value'] * item_quantity
                    add_credits(sell_value)  # Update player_credits
                    player_inventory.remove(sold_item)
                    print(f"You sold {item_quantity} {item_name}(s) for {sell_value} credits.")
                else:
                    print("Invalid item type. Unable to sell.")
            else:
               print("Invalid item choice. Please enter a valid number.")
        except ValueError:
                print("Invalid input. Please enter a number")