# Show all collected tags in all files
def show_tags_collection(unique_tags):
    all_tags = set()
    for filename in unique_tags:
        tags_inside = unique_tags[filename]
        all_tags.update(tags_inside)
    print(f"Total files in collection: {len(unique_tags)}")
    print(f"Total tags in collection: {len(all_tags)}\n")
    for tag in sorted(all_tags):
        print(f"- {tag}")

# Choose file from program memory
def choose_file_from_collection(unique_tags):
    print(f"\nAvailable files:\n")
    for filename in unique_tags:
        print(f"- {filename}")
    choosed_file = input("\nEnter from what file.txt show tags:\n")
    if choosed_file in unique_tags:
        return choosed_file
    else:
        print(f"No file {choosed_file} existed\n")
    return None

# Show tags from file
def show_tags_from_file(unique_tags):
    if len(unique_tags) == 0:
        print("\nTags library is empty, read a file first\n")
        return
    current_file = choose_file_from_collection(unique_tags)
    if current_file == None:
        return
    else:
        tags_from_file = unique_tags[current_file]
        print(f"Tags in {current_file}:\n")
        for tag in sorted(tags_from_file):
            print(f"- {tag}")
    return

# Process tags from .txt file
def process_file(file):
    unique_tags = set()
    for line in file:
        stripped_line = line.strip()
        if stripped_line != "" and not stripped_line.startswith("#"):
            tags = stripped_line.split(",")
            for tag in tags:
                clean_tag = tag.strip()
                if clean_tag:
                    unique_tags.add(clean_tag)
    return unique_tags

# Read tags from file
def read_tags():
    # получаю имя файла, который нужно открыть
    filename = input("\nInput file name.txt:\n")
    # пробую открыть файл, указанный пользователем
    try:
        with open(filename, "r", encoding="utf-8") as file:
            processed_file = process_file(file)
        print("File readed successfuly!\n")
        return processed_file, filename
    except FileNotFoundError:
        print(f"No file {filename} found\n")
        return set(), None

# Choose action menu
def menu(unique_tags):
    while True:
        user_action = input("Enter '1' - read tags from file\nEnter '2' - show tags from file\nEnter '3' - show all available tags\nEnter '4' - exit\n")
        if user_action == "1":
            file_tags, filename = read_tags()
            if filename:
                unique_tags[filename] = file_tags
        elif user_action == "2":
            show_tags_from_file(unique_tags)
        elif user_action == "3":
            show_tags_collection(unique_tags)
        elif user_action == "4":
            break
        else:
            print("Invalid action, try again")

def main():
    unique_tags = {}
    menu(unique_tags)

main()