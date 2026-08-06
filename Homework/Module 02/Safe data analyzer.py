"""
Отлично! Давай сделаем небольшое, но очень полезное задание, которое закрепит понимание **изменяемости объектов** — одну из самых важных концепций, которую мы изучили в Главе 5.

## Задание: "Безопасный анализатор данных"

**Сценарий:**
Представь, что ты пишешь функцию для своего Dataset Composer, которая анализирует список тегов. Функция должна:
1. Принять список тегов
2. Убрать дубликаты
3. Отсортировать по алфавиту
4. Вернуть чистый список

**НО** (и это самое важное!) — оригинальный список, который передали в функцию, **НЕ должен измениться**.

### Твое задание:

Напиши функцию `clean_tags(tags_list)`, которая:
- Принимает список тегов (с дубликатами и в любом порядке)
- Возвращает **новый** список (без дубликатов, отсортированный)
- **НЕ изменяет** оригинальный список

### Пример работы:

```python
original = ["beach", "sunset", "beach", "rain", "sunset"]
cleaned = clean_tags(original)

print("Original:", original)
# Должно вывести: ['beach', 'sunset', 'beach', 'rain', 'sunset']
# (НЕ изменился!)

print("Cleaned:", cleaned)
# Должно вывести: ['beach', 'rain', 'sunset']
# (новый список, без дубликатов, отсортирован)
```

### Подсказки:
- Используй `set()` для удаления дубликатов
- Используй `sorted()` для сортировки (а НЕ `.sort()`)
- Помни разницу между методами, которые изменяют объект на месте, и функциями, которые создают новый объект

### Тестовые случаи:

```python
# Тест 1: Базовый случай
tags1 = ["cat", "dog", "cat", "bird"]
result1 = clean_tags(tags1)
assert tags1 == ["cat", "dog", "cat", "bird"], "Оригинал изменился!"
assert result1 == ["bird", "cat", "dog"], "Неправильный результат"

# Тест 2: Пустой список
tags2 = []
result2 = clean_tags(tags2)
assert tags2 == [], "Оригинал изменился!"
assert result2 == [], "Неправильный результат"

# Тест 3: Уже уникальный
tags3 = ["apple", "banana", "cherry"]
result3 = clean_tags(tags3)
assert tags3 == ["apple", "banana", "cherry"], "Оригинал изменился!"
assert result3 == ["apple", "banana", "cherry"], "Неправильный результат"

print("✅ Все тесты пройдены!")
```

---

### Почему это задание важно?

Это задание закрепляет три ключевые концепции:
1. **Изменяемость vs Неизменяемость** — ты понимаешь, какие операции создают новый объект, а какие изменяют существующий
2. **Побочные эффекты** — функция НЕ должна изменять свои входные данные, если это не явно требуется
3. **Чистые функции** — функция, которая всегда возвращает одинаковый результат для одинаковых входных данных и не имеет побочных эффектов

Это принцип профессиональной разработки, который используется в реальном Dataset Composer повсеместно.

Напиши функцию `clean_tags` и протестируй её! 🙂

"""

def menu(library):
    while True:
        print("1. Add category\n2. Add tags to category\n3. Show all categories and tags\n4. Exit\n")
        user_action = input("Enter action:")
        if user_action == "1":
            add_cat(library)
        elif user_action == "2":
            add_tags(library)
        elif user_action == "3":
            show_cats()
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
            print(f"Category '{new_cat}' added successfuly")
            library.append(new_cat)

        print(library)
    
def add_tags(library):
    if len(library) == 0:
        print("\nNo categories, add tag category first")
        return
    else:
        print("List of categories:")
        for N, cat_name in enumerate(library):
            print(f"{N + 1}. {cat_name}")
        choosed_cat = int(input("Enter category number from list (or press Enter to exit): "))
        if choosed_cat == "":
            return
        cat_in_list = (choosed_cat) - 1
        while True:    
            input_tag = input("Enter tag to category (or press enter to exit):")
            if input_tag == "":
                break
            library[cat_in_list].append(input_tag)
            print(library)


def show_cats():

    pass



def main():
    library = []
    menu(library)
    pass

main()