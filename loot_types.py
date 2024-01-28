# loot_types.py

from dataclasses import dataclass

import random


@dataclass
class Loot:
    name: str
    value: int


# Loot types and value of loot
loot_types = [
    Loot(name, value)
    for name, value in [
        ("Gold", 20),
        ("Platinum", 30),
        ("Diamonds", 50),
        ("Silver", 15),
        ("Sapphires", 40),
        ("Emeralds", 35),
        ("Ruby", 45),
        ("Copper", 10),
        ("Titanium", 60),
        ("Opals", 25),
        ("Amethyst", 30),
        ("Topaz", 25),
        ("Obsidian", 18),
        ("Jade", 40),
        ("Pearls", 35),
        ("Quartz", 15),
        ("Ruby", 50),
        ("Aquamarine", 28),
        ("Malachite", 22),
        ("Moonstone", 32),
    ]
]

loot_types_dict = {loot.name: loot for loot in loot_types}


def get_random_loot():
    return random.choice(loot_types)
