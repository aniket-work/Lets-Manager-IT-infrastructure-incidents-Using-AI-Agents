import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def load_settings():
    settings_path = os.path.join(os.path.dirname(__file__), 'settings.json')
    with open(settings_path, 'r') as settings_file:
        return json.load(settings_file)