import json
from pathlib import Path

def load_config():
    default_settings = {
        "default_path": r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\Homework\Module 03\JSON Reader\profiles_library.json",
        "max_profiles": 100,
    }
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return default_settings
    if _validate_settings(settings):
        return settings
    else:
        return default_settings

def edit_save_path():
    settings = load_config()
    new_path = Path(input("Enter new save path:\n"))
    settings["default_path"] = str(new_path)
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, ensure_ascii=False)
    print(f"Save path updated successfully!")

def edit_max_profiles():
    settings = load_config()
    max_profiles = input("Enter max profiles:\n")
    settings["max_profiles"] = int(max_profiles)
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, ensure_ascii=False)
    print(f"Max profiles updated successfully!")

def _validate_settings(settings):
    if "default_path" not in settings:
        return False
    if not isinstance(settings["default_path"], str):
        return False
    if "max_profiles" not in settings:
        return False
    if not isinstance(settings["max_profiles"], int):
        return False
    return True

    
if __name__ == "__main__":
    print("Test")
    load_config()
    edit_save_path()

