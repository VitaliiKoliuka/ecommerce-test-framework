import os
import configparser

config = configparser.RawConfigParser()

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config_dev.ini"))

if not os.path.exists(path):
    raise FileNotFoundError(f"Config file not found at {path}")

config.read(path)

class ReadConfig():
    @staticmethod
    def get_property(key):
        return config.get("commonInfo",key)

BASE_URL = config.get("commonInfo", "base_url")