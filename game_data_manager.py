# game_data_manager.py

import json

class GameDataManager:
    @staticmethod
    def save_game_data(data, filename='game_data.json'):
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_game_data(filename='game_data.json'):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None
