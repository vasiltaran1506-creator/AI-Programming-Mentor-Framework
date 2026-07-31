"""
**Сценарий:**
Твой движок сформировал очередь из сцен, которые нейросеть должна отрисовать. В процессе работы эту очередь нужно активно модифицировать: добавлять срочные кадры, удалять битые промпты, забирать задачи в работу и сортировать их для логирования.

**Твоя задача:** Написать скрипт, который пошагово выполняет следующие действия. 

1. **Инициализация:** Создай список `queue` с тремя начальными сценами: 
   `["beach_sunset", "library_reading", "cafe_drinking"]`.
2. **Добавление в конец:** Добавь в конец очереди сцену `"park_walking"` (используй метод, который добавляет один элемент).
3. **Срочная задача:** Пришел VIP-заказ! Добавь сцену `"studio_portrait"` в **самое начало** списка (под индексом `0`), чтобы она ушла на рендер первой (используй `insert`).
4. **Удаление брака:** Оказалось, что `"library_reading"` содержит логическую ошибку. Удали эту сцену из очереди по её значению (используй `remove`).
5. **Взятие в работу:** Забери самую **последнюю** сцену из списка, чтобы отправить её на рендер прямо сейчас. Сохрани её в переменную `current_scene` и выведи на экран: `print(f"Rendering now: {current_scene}")`. (Используй `pop`).
6. **Массовое добавление:** У тебя есть список дополнительных задач: 
   `extra_scenes = ["rainy_street", "snowy_forest"]`. 
   Высыпь их содержимое в основную очередь `queue` так, чтобы они стали отдельными элементами, а не вложенным списком (используй `extend`).
7. **Ловушка Инженера (`sort` vs `sorted`):**
   * **Шаг А (Отчет):** Тебе нужно вывести в консоль алфавитный список всех запланированных сцен для отчета, но **не менять** порядок в самой рабочей очереди `queue`. Создай переменную `report`, положи туда отсортированную копию очереди и выведи `report`.
   * **Шаг Б (Наведение порядка):** А теперь отсортируй саму рабочую очередь `queue` по алфавиту **на месте** и выведи её.

---

### ⚠️ Важное напоминание (Ментальная модель "Корзины")
Помни, что список — это корзина. 
* Методы вроде `.append()`, `.insert()`, `.remove()`, `.extend()`, `.sort()` просто залезают в корзину и перекладывают вещи. Они **ничего не возвращают** (возвращают `None`). 
* Если ты напишешь `queue = queue.append("...")`, ты случайно затрешь свой список пустотой (`None`)!
* Функция `sorted()` работает как Ксерокс: она делает копию и возвращает её.

Напиши этот скрипт, запусти его и покажи мне результат (код + то, что вывелось в консоль). Как только мы убедимся, что ты идеально чувствуешь разницу между изменением на месте и созданием копии, мы перейдем к **Главе 6 (Чтение документации)**! Жду твой код. 🙂
"""




"""
### На что стоит обратить внимание (Подводные камни)

**Ловушка 1: Поиск внутри Списка Словарей**
Если `queue` — это список словарей, то проверка `if "scene_001.txt" in queue:` **не сработает**. Оператор `in` будет искать *целый словарь*, а не просто строку с именем. 
*Решение:* Тебе придется написать небольшую вспомогательную функцию (или цикл), которая проходит по `queue` и проверяет: `if task["filename"] == target_name:`.

**Ловушка 2: Изменение статуса "на лету"**
Когда ты берешь задачу в работу (`pop(0)`), ты забираешь словарь из списка. Теперь этот словарь лежит в переменной (например, `current_task`). Ты можешь спокойно поменять его статус: `current_task["status"] = "processed"`, а затем, если нужно, положить его обратно в список "архива" или просто вывести на экран.

**Ловушка 3: Пустая очередь**
Что произойдет, если пользователь нажмет "Start processing", а в очереди нет ни одного файла? Метод `.pop(0)` упадет с ошибкой `IndexError: pop from empty list`.
*Решение:* Перед тем как "брать файл в работу", программа всегда должна проверять: `if len(queue) > 0:` (или `if queue:`).


### Твое задание
1. Скопируй этот скелет в VS Code.
2. Заполни пропуски `???` (их всего 6 штук). В одном месте тебе понадобится ключевое слово `del` (оно удаляет элемент из списка по индексу: `del my_list[0]`).
3. Запусти программу и протестируй сценарий:
   * Добавь два обычных файла.
   * Добавь один срочный.
   * Посмотри очередь (срочный должен быть первым!).
   * Обработай одну задачу.
   * Удали оставшуюся задачу как "брак".

Как только этот "Менеджер задач" заработает, ты можешь с полной уверенностью сказать, что **Глава 5 (Методы списков)** и **Глава 8 (Мини-проект)** пройдены! Жду твой код и результаты тестов. 🙂
"""





# Init. Create files queue
# Add files to queue (input()) 
   # Assign status (new, processing, processed, error, top_priority)
# Show qurrent file queue with statuses
# Start processing scene from queue
   # Get first scene from queue
   # Assign status processing
   # Assign status processed
   # Return scene with status

# LOGICAL ERROR. Delete scene with error from file queue
   # Assign error status to file
   # Delete file from main queue

# URGENT TASK. Add prioritized scene to queue
   # Assign status top_priority to file
   # Place it to start of a queue



def main():
   queue = []
   menu(queue)
   return

def menu(queue):
   while True:
      print("List of actions:")
      print("1. Add file to queue.")
      print("2. Add URGENT file")
      print("3. Show queue")
      print("4. Process next file")
      print("5. Mark errored file")
      print("6. Exit")
      user_action = input("\nEnter action: \n")
      if user_action == "1":
         add_file(queue)
      elif user_action == "2":
         add_urgent_file(queue)
      elif user_action == "3":
         show_current_queue(queue)
      elif user_action == "4":
         process_file_from_queue(queue)
      elif user_action == "5":
         process_error(queue)
      elif user_action == "6":
         break
      else:
         print("Invalid choise")

def add_file(queue):
   filename = input("Enter file name: ")
   task = {
      "filename":filename,
      "status":"new"
   }
   queue.append(task)
   print(f"File '{filename}' added to queue")

def add_urgent_file(queue):
   filename = input("Enter urgent file name: ")
   task = {
      "filename":filename,
      "status":"urgent"
   }
   queue.insert(0, task)
   print(f"Urgent file '{filename}' added to queue")

def show_current_queue(queue):
   print("Current queue:")
   if len(queue) == 0:
      print("Queue is empty")
      return
   else: 
      for N, task in enumerate(queue):
         print(f"{N + 1}. [{task['filename']:<4}] Status: [{task['status']:<10}]")

def process_file_from_queue(queue):
   if len(queue) == 0:
      print("Queue is empty, nothing to process")
   else:
      current_task = queue.pop(0)
      print(f"Processing {current_task['filename']}")
      input("Press Enter to finish processing")
      current_task["status"] = "processed" 
      print(f"Task {current_task['filename']} processed successfuly")
      queue.append(current_task)

def process_error(queue):
   print(f"Choose file from queue:\n")
   for N, task in enumerate(queue):
      print(f"{N + 1}. [{task['filename']:<4}] Status: [{task['status']:<10}]")
   error_file = input("Enter filename to mark as ERRORED")

   found_index = -1
   for i in range(len(queue)):
         if queue[i]["filename"] == error_file:
            found_index = i 
            break
   if found_index != -1:
      del queue[found_index]
      print(f"Task '{error_file}' removed due to error")
   else:
      print(f"File '{error_file}' not found")


main ()
