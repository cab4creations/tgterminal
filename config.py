import yaml

CONFIG_PATH = "config.yaml"

with open(CONFIG_PATH) as file:
    config = yaml.safe_load(file)

API_ID = config["API_ID"]
API_HASH = config["API_HASH"]

# don't change if you don't know what you are doing
CHAT_DB = "chats.json"
