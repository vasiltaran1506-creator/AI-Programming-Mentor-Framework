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

'''
Открыть файл 
    спросить у пользователя, какой именно файл он хочет открыть
    открыть указанный пользователем файл
прочитать файл
отдать прочитанное содержание в метод обработки
    разделить файл на отдельные слова по строчкам, с разделителем ","
    сохранить результат обработки
    отдать результат обработки в метод чтения
получить результат обработки
записать результат обработки
'''

def process_file(file):
    unique_tags = set(file)
    sorted_tags = sorted(unique_tags)
    splitted_tags = 
    


    for tag in sorted_tags:
        stripped_tag = tag.
    return


# Read tags from file
def read_tags(unique_tags):
    # получаю имя файла, который нужно открыть
    filename = input("Input file name.txt:\n")
    # пробую открыть файл, указанный пользователем
    try:
        with open(filename, "r", encoding="utf-8") as file:
            process_file(file)
    except:
        print(f"No file {filename} founded")
    return 

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
    unique_tags = []
    menu(unique_tags)

main()