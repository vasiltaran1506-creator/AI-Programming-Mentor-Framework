
def show_tag_summary(master_tags):
    total_tags = len(master_tags)
    unique_count = len(set(master_tags))
    print(f"Total tags: {total_tags},\n Unique tags: {unique_count}")

def show_unique_tags(master_tags):
    unique_tags = set(master_tags)
    sorted_tags = sorted(unique_tags)
    print("\nTags list:\n")
    for N, tag in enumerate(sorted_tags):
        print(f"{N + 1}. {tag}")
    return

def add_tags(master_tags):
    new_tags = input("\nInput your tags: ")
    splitted_tags = new_tags.split(",")
    for tag in splitted_tags:
        normalized_tag = tag.strip().lower()
        if normalized_tag != "":
            master_tags.append(normalized_tag)
    return master_tags

def show_menu(master_tags):
    while True:
        user_action = input("\nEnter '1' to add tags,\nEnter '2' to show tag summary,\nEnter '3' to show unique tags,\nEnter '4' to exit\n\nEnter number 1-4: ")
        if user_action == "1":
            add_tags(master_tags)
        elif user_action == "2":
            show_tag_summary(master_tags)
        elif user_action == "3":
            show_unique_tags(master_tags)
        elif user_action == "4":
            break
        else:
            print("Incorrect number, enter again")

def main():
    master_tags = []
    show_menu(master_tags)

main()