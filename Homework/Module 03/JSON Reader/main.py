import json
from pathlib import Path
import config

def main():
    settings = config.load_config()
    path = Path(settings["default_path"])
    
    while True:
        print("Choose action:\n1. Add user profile.\n2. Show available user profiles.\n3. Edit save path.\n4. Exit.")
        action = input()
        if action == "1":
            user_profile = {
                "username": None,
                "userage": None,
                "skills": None,
                "is_active": None,
                }
            ask_name(user_profile)
            ask_age(user_profile)
            ask_skills(user_profile)
            ask_is_active(user_profile)

            save_to_lib(user_profile, path)

        elif action == "2":
            show_profiles(path)
            
        elif action == "3":
            print(f"Current safe path: {settings['default_path']}")
            config.edit_save_path()
            settings = config.load_config()
        elif action == "4":
            break
        
        else: 
            print("Incorrect action, try again.")


def ask_name(user_profile):
    username = input("Enter your username:\n")
    user_profile["username"] = username

    return user_profile

def ask_age(user_profile):
    userage = input("Enter your age:\n")
    user_profile["userage"] = userage

    return user_profile

def ask_skills(user_profile):
    skills = input("Enter yous skills (use ,):\n").strip()
    splitted_skills = skills.split(",")
    user_profile["skills"] = splitted_skills
    
    return user_profile

def ask_is_active(user_profile):
    active = input("Enter 1 if active, enter 0 if not active:\n")
    if active == "1":
        user_profile["is_active"] = True
    elif active == "0":
        user_profile["is_active"] = False
    else:
        print("Unavailable action")


def save_to_lib(user_profile, path):
    profiles = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            profiles = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    profiles.append(user_profile)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(profiles, file, ensure_ascii=False, indent=4)

def show_profiles(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            loaded_profiles = json.load(file)
    except FileNotFoundError:
        print(f"File {path} not found")
    else:
        print(f"Profiles loaded successfully!")
        print(loaded_profiles)

    


main()