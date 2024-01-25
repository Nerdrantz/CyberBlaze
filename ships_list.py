import time
import os
import random  # Import the random module
import sys

from inventory import subtract_credits, player_credits, add_ship_to_fleet, player_fleet, update_inventory
from loot_types import get_random_loot


buyable_ships_list = [
    {"name": "Starship Alpha", "cost": 100, "Stats": "Fast and lightweight"},
    {"name": "Galactic Voyager", "cost": 150, "Stats": "Fast and slow turning speed"},
    {"name": "Cosmic Explorer", "cost": 200, "Stats": "Heavy and tanky armor"},
    # Add more ships as needed
]

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac

def show_buyable_ships():
    print("Available Ships:")
    for i, ship in enumerate(buyable_ships_list, start=1):
        print(f"{i}. {ship['name']} - Cost: {ship['cost']} credits - Stats: {ship['Stats']}")

def buy_ship(choice):
    try:
        choice = int(choice)
        if 1 <= choice <= len(buyable_ships_list):
            selected_ship = buyable_ships_list[choice - 1]
            if player_credits >= selected_ship["cost"]:
                subtract_credits(selected_ship["cost"])
                add_ship_to_fleet(selected_ship['name'])
                print(f"You've bought {selected_ship['name']} for {selected_ship['cost']} credits.")
                time.sleep(2)
            else:
                print("You don't have enough credits for this ship.")
                # Do not add ship to fleet if credits are insufficient
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def ship_event(selected_ship):
    # Introduce ship events based on ship stats
    if "Fast and lightweight" in selected_ship["Stats"]:
        event_chance = random.randint(1, 10)  # Random event chance
        if event_chance <= 3:  # 30% chance of encountering an event
            print(f"{selected_ship['name']} encountered a space anomaly. It safely maneuvered through.")
        else:
            print(f"{selected_ship['name']} had a smooth expedition.")
    elif "Fast and slow turning speed" in selected_ship["Stats"]:
        event_chance = random.randint(1, 10)
        if event_chance <= 5:  # 50% chance of encountering an event
            print(f"{selected_ship['name']} encountered pirates. It managed to escape, but the ship sustained some damage.")
    elif "Heavy and tanky armor" in selected_ship["Stats"]:
        event_chance = random.randint(1, 10)
        if event_chance <= 2:  # 20% chance of encountering an event
            print(f"{selected_ship['name']} encountered a hostile alien race. Its heavy armor absorbed the damage, but it's returning with battle scars.")

def send_ship_on_expedition():
    try:
        print("Select a ship for the expeditions:")
        for i, ship_name in enumerate(player_fleet, start=1):
            print(f"{i}. {ship_name}")

        ship_choice = int(input("Enter the number of the ship you want to send: "))

        if 1 <= ship_choice <= len(player_fleet):
            selected_ship = buyable_ships_list[ship_choice - 1]

            expedition_duration = int(input("Enter the duration of the expedition in minutes: "))

            loot_multiplier = 2 + (expedition_duration / 60)
            loot_amount = int(10 * loot_multiplier)

            random_loot = get_random_loot()

            print(f"{selected_ship['name']} is on an expedition for {expedition_duration} minutes.")
            for remaining_time in range(expedition_duration, 0, -1):
                print(f"Time remaining: {remaining_time} minutes")
                time.sleep(60)

            ship_event(selected_ship)  # Introduce ship events
            update_inventory(random_loot['name'], loot_amount)

            print(f"{selected_ship['name']} has returned from the expedition!")
            print(f"Collected loot: {random_loot['name']}")

        else:
            print("Invalid ship choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
