from pathlib import Path
import json


def load_datasets(settings):
    input_path = Path(settings["input_file_path"])
    loaded_datasets = []
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            loaded_datasets = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        pass
    return loaded_datasets