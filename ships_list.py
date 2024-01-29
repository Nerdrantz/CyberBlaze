import time
import random  # Import the random module

from inventory import Inventory
from loot_types import get_random_loot
from models import Ship
from term_utils import input_number, center_text


_ships_list = [
    ("Starship Alpha", 100, "Fast and lightweight"),
    ("Galactic Voyager", 150, "Fast and slow turning speed"),
    ("Cosmic Explorer", 200, "Heavy and tanky armor"),
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
    for remaining_time in range(expedition_duration, 0, -1):
        print(center_text(f"Time remaining: {remaining_time} minutes"))
        time.sleep(60)

    ship_event(selected_ship)  # Introduce ship events
    inventory.update_inventory(random_loot.name, loot_amount)

    print(center_text(
        f"{selected_ship.name} has returned from the expedition!\n"
        f"Collected loot: {random_loot.name}\n"
    ))
