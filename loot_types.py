# loot_types.py

import random

loot_types = [
    {"name": "Gold", "value": 20},
    {"name": "Platinum", "value": 30},
    {"name": "Diamonds", "value": 50},
    {"name": "Silver", "value": 15},
    {"name": "Sapphires", "value": 40},
    {"name": "Emeralds", "value": 35},
    {"name": "Ruby", "value": 45},
    {"name": "Copper", "value": 10},
    {"name": "Titanium", "value": 60},
    {"name": "Opals", "value": 25},
    {"name": "Amethyst", "value": 30},
    {"name": "Topaz", "value": 25},
    {"name": "Obsidian", "value": 18},
    {"name": "Jade", "value": 40},
    {"name": "Pearls", "value": 35},
    {"name": "Quartz", "value": 15},
    {"name": "Ruby", "value": 50},
    {"name": "Aquamarine", "value": 28},
    {"name": "Malachite", "value": 22},
    {"name": "Moonstone", "value": 32}
]

def get_random_loot():
    return random.choice(loot_types)