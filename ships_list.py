import time
import random  # Import the random module

from inventory import Inventory
from loot_types import get_random_loot
from models import Ship
from term_utils import input_number, center_text
from loading_bar import loading_bar_expeditions

_ships_list = [
    ("Starship Alpha", 100, "Fast and lightweight"),
    ("Galactic Voyager", 1500, "Fast and slow turning speed"),
    ("Cosmic Explorer", 2000, "Heavy and tanky armor"),
    ("Nebula Striker", 1200, "Agile and stealthy"),
    ("Quantum Cruiser", 1800, "Versatile with advanced weaponry"),
    ("Celestial Guardian", 2500, "Massive and heavily armed"),
    ("Solar Specter", 1300, "High-speed with advanced cloaking"),
    ("Interstellar Beacon", 1600, "Well-balanced and adaptable"),
    ("Lunar Sentinel", 1900, "Medium-class with superior shielding"),
    ("Astro Blazer", 1100, "Speedy and nimble"),
    ("Orion Battler", 1700, "Sturdy with energy-based weaponry"),
    ("Stellar Warden", 2200, "Guardian-class with support capabilities"),
    ("Cosmic Phantom", 1400, "Stealth capabilities and rapid firing"),
    ("Galaxy Guardian", 2000, "Durable with advanced targeting systems"),
    ("Nebula Raider", 1500, "Quick strikes with hit-and-run tactics"),
    ("Astral Enforcer", 2400, "Versatile and well-armored"),
    ("Supernova Hunter", 11600, "Aggressive with long-range missiles"),
    ("Solar Serpent", 22100, "Sleek design for rapid interplanetary travel")
    # Add more ships as needed
]


buyable_ships_list = list(map(lambda args: Ship(*args), _ships_list))


def show_buyable_ships():
    print(center_text("\nAvailable Ships:"))
    for i, ship in enumerate(buyable_ships_list, start=1):
        print(center_text(f"{i}. {ship.name} - Cost: {ship.cost} credits - Stats: {ship.stats}"))


def buy_ship(choice: int, inventory: Inventory):
    if choice < 1 or choice > len(buyable_ships_list):
        print(center_text("Invalid choice. Please enter a valid number."))
        return

    selected_ship = buyable_ships_list[choice - 1]
    if inventory.credits >= selected_ship.cost:
        inventory.subtract_credits(selected_ship.cost)
        inventory.add_ship_to_fleet(selected_ship)
        print(center_text(f"You've bought {selected_ship.name} for {selected_ship.cost} credits."))
        time.sleep(2)
    else:
        # Do not add ship to fleet if credits are insufficient
        print(center_text("You don't have enough credits for this ship."))


def ship_event(selected_ship: Ship):
    # Introduce ship events based on ship stats
    if "Fast and lightweight" in selected_ship.stats:
        event_chance = random.randint(1, 10)  # Random event chance
        if event_chance <= 3:  # 30% chance of encountering an event
            print(center_text(f"\n{selected_ship.name} encountered a space anomaly. It safely maneuvered through."))
        else:
            print(center_text(f"{selected_ship.name} had a smooth expedition."))
    elif "Fast and slow turning speed" in selected_ship.stats:
        event_chance = random.randint(1, 10)
        if event_chance <= 5:  # 50% chance of encountering an event
            print(center_text(f"{selected_ship.name} encountered pirates. It managed to escape, but the ship sustained some damage."))
    elif "Heavy and tanky armor" in selected_ship.stats:
        event_chance = random.randint(1, 10)
        if event_chance <= 2:  # 20% chance of encountering an event
            print(center_text(f"\n{selected_ship.name} encountered a hostile alien race. Its heavy armor absorbed the damage, but it's returning with battle scars."))


def send_ship_on_expedition(inventory: Inventory):
    print(center_text("\nSelect a ship for the expeditions:"))
    for i, ship in enumerate(inventory.fleet, start=1):
        print(center_text(f"{i}. {ship.name}"))

    ship_choice = input_number("Enter the number of the ship you want to send: ")
    if not ship_choice or ship_choice < 0 or ship_choice > len(inventory.fleet):
        print(center_text("\nInvalid ship choice. Please enter a valid number."))
        return

    selected_ship = inventory.fleet[ship_choice - 1]
    expedition_duration = input_number("Enter the duration of the expedition in minutes: ")

    if not expedition_duration:
        print("\nInvalid duration. Please enter a valid number of minutes.")
        return

    loot_multiplier = 2 + (expedition_duration / 60)
    loot_amount = int(10 * loot_multiplier)

    random_loot = get_random_loot()
    
    print(center_text(f"{selected_ship.name} is on an expedition for {expedition_duration} minutes."))
    for remaining_time in range(expedition_duration * 60, 0, -1):
        loading_bar_expeditions(expedition_duration * 60, remaining_time)
        time.sleep(1)
        
    ship_event(selected_ship)  # Introduce ship events
    inventory.update_inventory(random_loot.name, loot_amount)

    print(center_text(
        f"{selected_ship.name} has returned from the expedition!\n"
        f"Collected loot: {random_loot.name}\n"
    ))
    
