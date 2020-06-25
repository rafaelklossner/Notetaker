import json


class ConfigParser:
    def __init__(self):
        with open('config.json', 'r') as file:
            self.config = json.load(file)

    def get_settings_value(self, key):
        return self.config["settings"][key]

    def get_header_value(self, key):
        return self.config["header"][key]
