def menu(library):
    while True:
        print("1. Add category\n2. Add tags to category\n3. Show all categories and tags\n4. Exit\n")
        user_action = input("Enter action:")
        if user_action == "1":
            add_cat(library)
        elif user_action == "2":
            add_tags(library)
        elif user_action == "3":
            show_cats_with_tags(library)
        elif user_action == "4":
            break
        else:
            print(f"Invalid action")
    pass

def add_cat(library):
    while True:
        new_cat = input("Enter category name (or press Enter to exit): ")
        if new_cat == "":
            break
        if new_cat in library:
            print(f"Category '{new_cat}' already exists")
        else:
            library[new_cat] = set()
            print(f"Category '{new_cat}' added successfully")
        # TEST PRINT
        print(library)
    
def add_tags(library):
    if len(library) == 0:
        print("\nNo categories, add tag category first")
        return
    else:
        print("List of categories:")
        for N, cat_name in enumerate(library):
            print(f"{N + 1}. {cat_name}")
        while True:
            choosed_cat = input("Enter category name from list (or press Enter to exit): ")
            if choosed_cat == "":
                return
            elif choosed_cat not in library:
                print(f"No category '{choosed_cat}' in library, try again")
            else:
                while True:    
                    input_tag = input("Enter tag to category (or press enter to exit):")
                    if input_tag == "":
                        break
                    library[choosed_cat].add(input_tag)
                    # TEST PRINT
                    print(library)


def show_cats_with_tags(library):
    if len(library) == 0:
        print("Library is empty, enter categories first")
        return
    for cat_name, tags in library.items():
        tag_count = len(tags)
        print(f"{tag_count} tags in category '{cat_name}'")
        if tag_count == 0:
            print("    (empty)")
        else:
            for tag in sorted(tags):
                print(f"    {tag}")

def main():
    library = {}
    menu(library)
    pass

main()