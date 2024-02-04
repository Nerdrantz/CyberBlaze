# game_data_manager.py

from dataclasses import asdict
import json

from models import Ship


class GameDataEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Ship):
            return asdict(o)
        return super().default(o)

class GameDataDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if "fleet" in obj and isinstance(obj["fleet"], list):
            obj["fleet"] = [Ship(**ship) for ship in obj["fleet"]]
        return obj


class GameDataManager:
    @staticmethod
    def save_game_data(data, filename='game_data.json'):
        with open(filename, 'w') as file:
            json.dump(data, file, cls=GameDataEncoder)

    @staticmethod
    def load_game_data(filename='game_data.json'):
        try:
            with open(filename, 'r') as file:
                return json.load(file, cls=GameDataDecoder)
        except:
            return None
