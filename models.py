from dataclasses import dataclass


@dataclass
class Loot:
    name: str
    value: int


@dataclass
class Ship:
    name: str
    cost: int
    stats: str
