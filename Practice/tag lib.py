
def existing_cats(lib):
    all_cats = "Available categories:"
    for cat in lib:
        all_cats += f"- {cat}\n"
    return all_cats

def choose_cat(lib):
    choosed_cat =  input(f"Choose tag category: \n {existing_cats(lib)}")
    if choosed_cat in lib:
        return choosed_cat   
    else: 
        print("No such category in library")
        return None

def add_tag_in_cat(lib, choosed_cat,):
    while True:
        new_tag = input(f"Enter tag to {choosed_cat} (or press enter to exit): ")
        if new_tag == "":
            break
        elif new_tag in lib[choosed_cat]:
            print(f"Tag {new_tag} already exists in {choosed_cat}")
        else:
            lib[choosed_cat].append(new_tag)
            print(f"'{new_tag}' successfully added to {choosed_cat}!")

def add_cat(lib):
    while True:
        cat_name = input("Enter category name (or press enter to exit): ")
        if cat_name == "":
            break

        elif cat_name in lib:
            print("Category already exists")  

        else:
            lib[cat_name] = []
            print(f"Category '{cat_name}' created successfuly!")


def show_menu(lib,):
    while True:
        action = input("Enter 1 to add new category, enter 2 to add tag in category, enter 3 to show all tags in categories, enter 4 to exit")
        if action == "1":
            add_cat(lib)

        elif action == "2":
            current_cat = choose_cat(lib)
            if current_cat is not None:
                add_tag_in_cat(lib, current_cat)

        elif action == "3":
            for cat_name in lib:
                print(f"{cat_name}: {lib[cat_name]}")

        elif action == "4":
            break

        else: 
            print("Incorrect choise, try again")

def main():
    library = {}
    show_menu(library)

main()