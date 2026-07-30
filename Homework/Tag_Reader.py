# Твоя задача:
# Напиши скрипт, который:
# Создает пустое множество unique_tags = set().
# Открывает test_tags.txt с помощью with open(...).
# Проходит по файлу циклом for line in file:.
# Чистит строчку (.strip()).
# Проверяет, что строчка не пустая (!= "") и не является комментарием (не начинается с # — подсказка: для этого есть строковый метод .startswith("#")).
# Если строчка прошла фильтры, добавляет её в множество (unique_tags.add(...)).
# В конце выводит отсортированный список уникальных тегов на экран.

"""


"""
# ./Tag_Reader.py




# Show all collected tags
def show_tags_collection(unique_tags):
    
    return


def choose_file_from_collection(filebase):
    for file in filebase:
        print(f"List of files:\n{file}\n")
    choosed_file = input("Enter from what file.txt show tags:\n")
    if choosed_file in filebase:
        return choosed_file
    else:
        print(f"No file {choosed_file} existed\n")
    return None

# Show tags from file
def show_tags_from_file(unique_tags, filebase, choodsed_file):
    current_file = choose_file_from_collection(filebase)
    if current_file == None:
        return
    else:
        '''
        я получил текущий файл
        теперь мне нужно достать из текущего файла список тегов, которые в нем лежат
        '''
    return

# Process tags from .txt file
def process_file(file):
    unique_tags = set()
    for line in file:
        stripped_line = line.strip()
        if stripped_line != "" and not stripped_line.startwith("#"):
            tags = stripped_line.split(",")
            for tag in tags:
                clean_tag = tag.strip()
                if clean_tag:
                    unique_tags.add(clean_tag)
    return unique_tags

# Read tags from file
def read_tags():
    # получаю имя файла, который нужно открыть
    filename = input("Input file name.txt:\n")
    # пробую открыть файл, указанный пользователем
    try:
        with open(filename, "r", encoding="utf-8") as file:
            processed_file = process_file(file)
        print("File readed successfuly!")
        return processed_file, filename
    except:
        print(f"No file {filename} founded")
        return set()


# Choose action menu
def menu(unique_tags):
    filebase = set()
    while True:
        user_action = input("Enter '1' - read tags from file\nEnter '2' - show tags from file\nEnter '3' - show all available tags\nEnter '4' - exit\n")
        if user_action == "1":
            file_tags, filename = read_tags()
            if filename:
                unique_tags.append(file_tags)
                filebase.add(filename)
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