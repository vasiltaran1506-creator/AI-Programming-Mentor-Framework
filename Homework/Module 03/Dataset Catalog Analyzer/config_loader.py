import json
from pathlib import Path


def load_config():
    default_settings = {
    "input_file_path": r"D:/VASILY/Projects/AI-Programming-Mentor-Framework/Homework/Module 03/Dataset Catalog Analyzer/Datasets/datasets.json",
    "output_file_path": r"D:/VASILY/Projects/AI-Programming-Mentor-Framework/Homework/Module 03/Dataset Catalog Analyzer/Datasets/report.json",
    "min_images_required": 100
    }

    try:
        with open("config.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return default_settings
    if _validate_settings_config(settings):
        return settings
    else:
        return default_settings

def _validate_settings_config(settings):

    # Input file path validation
    if "input_file_path" not in settings:
        return False
    if not isinstance(settings["input_file_path"], str):
        return False

    # Output file path validation
    if "output_file_path" not in settings:
        return False
    if not isinstance(settings["output_file_path"], str):
        return False

    # Min images validation
    if "min_images_required" not in settings:
        return False
    if not isinstance(settings["min_images_required"], int):
        return False

    return True

def edit_input_path():
    settings = load_config()
    new_path = Path(input("Enter new input file path:\n"))
    settings["input_file_path"] = str(new_path)
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, ensure_ascii=False)
    print(f"Input file path updated successfully!")

def edit_output_path():
    settings = load_config()
    new_path = Path(input("Enter new output file path:\n"))
    settings["output_file_path"] = str(new_path)
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, ensure_ascii=False)
    print(f"Output file path updated successfully!")
    

def edit_min_required_images():
    settings = load_config()
    min_images = input("Enter minimum images required:\n")
    try:
        settings["min_images_required"] = int(min_images)
    except ValueError:
        print("Incorrect input, enter numbers only")
        return 
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, ensure_ascii=False)
    print("Minimum required images updated successfully!")


# Test
if __name__ == "__main__":
    print("Config loader test started")
    load_config()
    edit_input_path()
    edit_output_path()
    edit_min_required_images()