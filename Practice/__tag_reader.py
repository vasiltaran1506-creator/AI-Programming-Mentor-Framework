# Твоя задача:
# Напиши скрипт, который:
# Создает пустое множество unique_tags = set().
# Открывает test_tags.txt с помощью with open(...).
# Проходит по файлу циклом for line in file:.
# Чистит строчку (.strip()).
# Проверяет, что строчка не пустая (!= "") и не является комментарием (не начинается с # — подсказка: для этого есть строковый метод .startswith("#")).
# Если строчка прошла фильтры, добавляет её в множество (unique_tags.add(...)).
# В конце выводит отсортированный список уникальных тегов на экран.



# Show all collected tags
def show_tags_collection():

    return

# Show tags from file
def show_tags_from_file(unique_tags):

    return

# Read tags from file
def read_tags(unique_tags):
    filename = input("Input file name.txt:\n")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_tag = line.strip()
                readed_tags = set(cleaned_tag)
                N = 0
                print(f"List of tags in file {filename}:\n")
    except:
        print(f"No file {filename} founded")
    return readed_tags

# Choose action menu
def menu(unique_tags):
    while True:
        user_action = input("Enter '1' - read tags from file\nEnter '2' - show tags from file\nEnter '3' - show all available tags\nEnter '4' - exit\n")
        if user_action == "1":
            read_tags(unique_tags)
        elif user_action == "2":
            show_tags_from_file(unique_tags)
        elif user_action == "3":
            show_tags_collection(unique_tags)
        elif user_action == "4":
            break
        else:
            print("Invalid action, try again")

def main():
    unique_tags = set()
    menu(unique_tags)

main()