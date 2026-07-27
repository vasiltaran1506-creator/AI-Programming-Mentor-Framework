
def collect_info(data_basket):
    while True:
        username = input("Enter your name (or press Enter to continue): ")
        if username == "":
            break
        else:
            userage = input("Enter your age: ")
            usercity = input("Enter your city: ")
            data_basket[username] = {
                "age": userage,
                "city": usercity,
            }

def print_info(data_basket):
    for name, info in data_basket.items():
        print(f"Name: {name}, Age: {info['age']}, City: {info['city']}")

def ask_action(data_basket):
    while True:
        action = input("\n1 - Add Profile, 2 - Show Profiles list, 3 - Exit: ")
        if action == "1":
            collect_info(data_basket)
        elif action == "2":
            print_info(data_basket)
        elif action == "3":
            print("Exiting program")
            break
        else:
            print("Invalid choise, try again")



def main():
    profile = {}
    ask_action(profile)
    print("Final result", profile)
    return

main()