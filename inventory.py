# inventory.py

initial_credits = 100
player_credits = initial_credits
player_fleet = []
player_inventory = []
   
def display_inventory():
    inventory_str = ", ".join([f"{item['name']}: {item['amount']}" for item in player_inventory])
    print(f"Inventory: {inventory_str}")
    print(f"Credits: {player_credits}")
    print(f"Fleet: {', '.join(player_fleet)}")
    
def add_credits(amount):
    global player_credits
    player_credits += amount

def subtract_credits(amount):
    global player_credits
    print("Player_Credits: " + str(player_credits))
    if player_credits >= amount:
        player_credits -= amount
    else:
        print("Insufficient credits.")
        
def add_ship_to_fleet(ship_name):
    player_fleet.append(ship_name)
    print("Updated fleet:", player_fleet)
    
def update_inventory(loot_type, loot_amount):
    global player_credits
    found = False
    for item in player_inventory:
        if item['name'] == loot_type:
            item['amount'] += loot_amount
            found = True
            break
            
    if not found:
        player_inventory.append({"name": loot_type, "amount": loot_amount})