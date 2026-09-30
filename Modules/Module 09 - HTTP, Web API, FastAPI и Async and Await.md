# Module 09 --- HTTP, Web API, FastAPI и Async/Await

## Статус

Следующий учебный модуль APMF после Module 08.

## Предварительная оценка времени

Ориентир: **22--28 часов**.

При темпе около 5 часов полезной работы в день: примерно **4--6 дней**.

Скорость не является основной целью. В этом модуле важно впервые
построить настоящий HTTP-интерфейс поверх уже существующей Application
Layer QR Warehouse и понять, где заканчивается веб-слой и начинается
собственно приложение.

------------------------------------------------------------------------

# 1. Зачем нужен Module 09

До этого момента QR Warehouse является приложением, которое можно
запустить и использовать через CLI.

После Module 07 у приложения есть архитектурные границы.

После Module 08 у приложения появилась полноценная реляционная модель и
транзакционная работа с SQLite.

Следующий вопрос естественный:

> **Как сделать так, чтобы внешняя программа --- браузер, мобильное
> приложение, другой сервис или JavaScript-клиент --- могла пользоваться
> теми же бизнес-возможностями?**

Ответом становится Web API.

Общая схема теперь будет такой:

``` text
                    Внешний мир
                         │
                         │ HTTP
                         ▼
                ┌─────────────────┐
                │ Presentation    │
                │ HTTP / FastAPI  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Application     │
                │ Use Cases       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Infrastructure  │
                │ Repository      │
                └────────┬────────┘
                         │
                         ▼
                    SQLite / DB
```

Самая важная идея модуля:

> **Web API --- это новый способ входа в уже существующее приложение, а
> не новое место для бизнес-логики.**

Это прямое продолжение архитектурной работы Module 07--08.

------------------------------------------------------------------------

# 2. Главный переход в мышлении

Раньше у тебя был примерно такой поток:

``` text
Пользователь
    ↓
CLI
    ↓
Use Case
    ↓
Repository
    ↓
Database
```

Теперь станет:

``` text
Browser / Frontend / Client
            ↓
          HTTP
            ↓
        FastAPI
            ↓
        Use Case
            ↓
        Repository
            ↓
         Database
```

CLI при этом не обязан исчезать.

Возможны два входа:

``` text
                 ┌── CLI ────────┐
                 │               │
                 ▼               │
            Application          │
                 ▲               │
                 │               │
                 └── HTTP API ───┘
```

Оба интерфейса могут вызывать одну и ту же Application Layer.

Это и есть практическая демонстрация идеи, которая была открытым
вопросом Q-0024: что произойдет, если к CLI добавить Web API.

------------------------------------------------------------------------

# 3. Что такое HTTP

## Mental Model --- «Почта между клиентом и сервером»

Представь, что клиент отправляет серверу письмо.

В письме есть:

``` text
Кому?          → URL
Что сделать?   → HTTP method
Доп. сведения  → Headers
Данные         → Body
```

Сервер отвечает другим письмом:

``` text
Результат      → Status Code
Доп. сведения  → Headers
Данные         → Body
```

Это и есть базовая модель HTTP request/response.

Не нужно пока думать о браузере как о чем-то магическом. Браузер ---
всего лишь один из клиентов HTTP.

Другими клиентами могут быть:

-   Python-программа;
-   JavaScript frontend;
-   мобильное приложение;
-   Postman/Insomnia;
-   другой backend;
-   автоматический тест.

------------------------------------------------------------------------

# 4. HTTP Request и Response

Запрос концептуально выглядит примерно так:

``` text
POST /estimates
Content-Type: application/json

{
    "project_name": "Scene 12",
    "days": 3
}
```

Ответ:

``` text
201 Created
Content-Type: application/json

{
    "estimate_id": 42,
    "project_name": "Scene 12",
    "days": 3
}
```

Задача этого раздела --- понять, что каждая часть запроса и ответа
означает.

------------------------------------------------------------------------

# 5. HTTP Methods

Основные методы, которые нужно знать к концу модуля:

  Method   Основной смысл
  -------- -----------------------------------------------------------
  GET      Получить ресурс/представление данных
  POST     Создать ресурс или выполнить действие с побочным эффектом
  PUT      Полностью заменить представление ресурса
  PATCH    Частично изменить ресурс
  DELETE   Удалить ресурс

Для Module 09 особенно важно перестать воспринимать эти методы как
произвольные названия кнопок.

Они выражают намерение операции.

Например:

``` text
GET /equipment/LIGHT-00001
```

означает получение информации.

А:

``` text
DELETE /estimates/17
```

означает удаление ресурса.

POST обычно связан с созданием ресурса или операцией, которая меняет
состояние.

PUT и PATCH требуют отдельного понимания различия между полной и
частичной заменой.

HTTP определяет семантику методов; клиент и сервер должны придерживаться
этой семантики, а не использовать методы как случайные ярлыки. [MDN HTTP
Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)

------------------------------------------------------------------------

# 6. HTTP Status Codes

Код состояния сообщает клиенту, чем закончилась обработка запроса.

Нужно уверенно понимать хотя бы:

``` text
200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Content
500 Internal Server Error
```

Не нужно пока заучивать сотни кодов.

Главная идея:

``` text
2xx → успешно
3xx → перенаправление
4xx → проблема запроса/клиента
5xx → проблема на стороне сервера
```

Коды 2xx--5xx образуют классы HTTP status codes по первой цифре. [MDN
HTTP Status
Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

Особое внимание QR Warehouse:

``` text
Оборудование не найдено
        ↓
       404

Недостаточно оборудования
        ↓
       409

Невалидные входные данные
        ↓
       422 / 400

Неожиданная ошибка сервера
        ↓
       500
```

Это не означает, что именно такая карта кодов всегда обязательна.
Научная цель упражнения --- научиться отделять **внутреннюю ошибку
приложения** от **HTTP-представления этой ошибки**.

------------------------------------------------------------------------

# 7. URL и ресурсы

HTTP API удобно мыслить через ресурсы.

В QR Warehouse естественными ресурсами могут быть:

``` text
/equipment
/equipment/{sku}
/estimates
/estimates/{estimate_id}
/estimates/{estimate_id}/items
```

Например:

``` text
GET /equipment
```

получить список оборудования.

``` text
GET /equipment/LIGHT-00001
```

получить конкретную позицию.

``` text
POST /estimates
```

создать смету.

``` text
POST /estimates/42/items
```

добавить позицию в смету.

``` text
PATCH /estimates/42/items/7
```

изменить количество.

``` text
DELETE /estimates/42/items/7
```

удалить позицию.

Это не единственный возможный дизайн API. Важнее научиться объяснять,
почему выбранная структура URL и метод соответствуют смыслу операции.

------------------------------------------------------------------------

# 8. JSON как язык обмена между Presentation и Application

В Module 03 JSON был изучен как формат данных.

Теперь ты увидишь его в новой роли.

Например:

``` json
{
    "project_name": "Commercial",
    "days": 5
}
```

может прийти в HTTP request body.

FastAPI преобразует и проверяет входные данные, после чего Presentation
Layer передаст нужные значения Use Case.

Это важно:

> JSON не становится бизнес-объектом только потому, что он пришёл по
> HTTP.

HTTP/JSON --- транспортный формат.

Application Layer по-прежнему должна работать с понятными ей данными и
правилами.

------------------------------------------------------------------------

# 9. FastAPI

FastAPI --- Python framework для построения API.

Он позволяет определить HTTP-операцию декоратором:

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
```

Современная документация FastAPI показывает такой минимальный подход и
запуск через `fastapi dev`. В актуальном руководстве для установки также
описан вариант `pip install "fastapi[standard]"`; проектная команда
`uv add "fastapi[standard]"` используется в документации при работе с
`uv`. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)

При этом сейчас тебя интересует не запоминание FastAPI-декораторов.

Тебе нужно понять модель:

``` text
@app.get("/equipment")
        │
        └── HTTP контракт
              │
              ▼
        Python функция
              │
              ▼
          Use Case
```

------------------------------------------------------------------------

# 10. Path, Query и Body Parameters

Это три разные формы входных данных.

## Path parameter

``` text
GET /equipment/LIGHT-00001
```

`LIGHT-00001` является частью URL.

В FastAPI:

``` python
@app.get("/equipment/{sku}")
def get_equipment(sku: str):
    ...
```

## Query parameter

``` text
GET /equipment?category=LIGHT&available=true
```

Параметры после `?` являются query parameters.

Например:

``` python
@app.get("/equipment")
def list_equipment(category: str | None = None):
    ...
```

## Body

Для POST/PATCH клиент может прислать JSON:

``` json
{
    "project_name": "Scene 12",
    "days": 3
}
```

В FastAPI для структурированного body используются модели Pydantic.

------------------------------------------------------------------------

# 11. Pydantic и валидация

Здесь появляется новый важный уровень границы.

Входящие данные из HTTP нельзя считать доверенными.

``` text
Internet
   ↓
HTTP request
   ↓
Pydantic validation
   ↓
Presentation
   ↓
Application
```

Пример концептуально:

``` python
from pydantic import BaseModel


class CreateEstimateRequest(BaseModel):
    project_name: str
    days: int
```

Теперь API может ожидать структуру данных, а FastAPI/Pydantic выполняют
валидацию входа.

Здесь важно связать Module 03 и Module 09:

> **The Bouncer вернулся.**

Раньше он охранял границу файлового приложения.

Теперь он охраняет границу HTTP API.

Но не следует автоматически переносить всю бизнес-валидацию в Pydantic.

Например:

``` text
"days должно быть целым числом"
        ↓
Presentation / input validation

"Аренда должна длиться больше нуля дней"
        ↓
может быть HTTP validation + business rule

"Эту позицию нельзя добавить, если на складе недостаточно единиц"
        ↓
Application / Domain business rule
```

Точные границы будут зависеть от модели проекта. Цель --- уметь
объяснить, **почему** правило находится в конкретном слое.

------------------------------------------------------------------------

# 12. Response Models

API должен не только принимать правильные данные, но и формировать
предсказуемый ответ.

Например:

``` python
class EstimateResponse(BaseModel):
    estimate_id: int
    project_name: str
    days: int
```

и операция может описывать ожидаемый результат.

Это помогает сделать API контрактом между клиентом и сервером.

В этом модуле нужно понять принцип:

``` text
Request Model ≠ Domain Entity ≠ Database Row ≠ Response Model
```

Они могут иметь одинаковые поля, но выполняют разные роли.

Это важное продолжение идеи из Module 08 о различии доменной модели и
Read Model.

------------------------------------------------------------------------

# 13. HTTP ошибки и граница слоев

Одна из важных практических задач --- понять, где превращать внутреннюю
ошибку в HTTP response.

Плохой вариант:

``` python
class AddItemToEstimate:
    ...
    raise HTTPException(status_code=404)
```

Почему это подозрительно?

Потому что Use Case теперь знает о HTTP.

Мы снова получили утечку инфраструктуры / presentation concerns в
Application Layer.

Гораздо чище мыслить так:

``` text
Use Case
   ↓
EquipmentNotFound / DomainError / BusinessError
   ↓
FastAPI boundary
   ↓
HTTP 404 / 409 / 422
```

Точные классы исключений ты выберешь в ходе упражнения.

Главная идея:

> **Application Layer говорит на языке приложения. Presentation Layer
> переводит этот язык в HTTP.**

------------------------------------------------------------------------

# 14. Dependency Injection в FastAPI

Ты уже изучил Dependency Injection на уровне приложения.

Теперь FastAPI позволит увидеть его ещё раз в другом месте.

FastAPI имеет собственную систему зависимостей, через которую можно
передавать общие компоненты, соединения, безопасность и другие
зависимости в path operation functions. [FastAPI
Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)

Но здесь есть важная методическая оговорка:

> **Не нужно считать FastAPI `Depends()` новой заменой всего Dependency
> Injection, который ты изучал раньше.**

Сначала ты должен понять обычную идею DI:

``` text
создать зависимость
        ↓
передать зависимость
        ↓
использовать зависимость
```

и только потом изучать API конкретного framework.

В QR Warehouse конечная цель:

``` text
FastAPI endpoint
      ↓
Use Case
      ↓
Repository contract
      ↓
Concrete Repository
```

а не:

``` text
FastAPI endpoint
      ↓
SQL query
```

------------------------------------------------------------------------

# 15. Главный практический переход: CLI → API

Это центральная задача Module 09.

До:

``` text
Application
   └── CLI loop
         ├── input()
         ├── print()
         └── Use Cases
```

После:

``` text
FastAPI
   ├── request parsing
   ├── validation
   ├── status mapping
   └── Use Cases
```

CLI можно сохранить.

Поэтому результат должен выглядеть примерно так:

``` text
                ┌─────────────┐
                │ CLI         │
                └──────┬──────┘
                       │
                       ▼
                 Application
                       ▲
                       │
                ┌──────┴──────┐
                │ FastAPI     │
                └─────────────┘
```

Нужно добиться того, чтобы добавление HTTP не потребовало переписывать
бизнес-правила работы со сметами.

------------------------------------------------------------------------

# 16. Vertical Slice для QR Warehouse

Не следует пытаться сразу делать весь сайт.

В этом модуле нужен один полноценный вертикальный срез.

Рекомендуемый первый срез:

``` text
GET /equipment
       ↓
FastAPI
       ↓
Equipment repository
       ↓
SQLite
       ↓
JSON response
```

Второй:

``` text
POST /estimates
       ↓
FastAPI
       ↓
CreateEstimate
       ↓
Repository
       ↓
SQLite
       ↓
201 Created
```

Третий:

``` text
POST /estimates/{id}/items
       ↓
FastAPI
       ↓
AddItemToEstimate
       ↓
EquipmentRepository
EstimateRepository
       ↓
Transaction
       ↓
201 / 404 / 409
```

После этого у тебя уже будет настоящий backend vertical slice.

------------------------------------------------------------------------

# 17. Тестирование API

Module 08 выявил важный пробел: новая архитектура пока недостаточно
покрыта тестами.

Module 09 должен начать закрывать этот пробел.

FastAPI предоставляет удобный способ использовать `TestClient` вместе с
pytest для тестирования API. В документации FastAPI для этого
используется HTTPX под капотом. [FastAPI
Testing](https://fastapi.tiangolo.com/tutorial/testing/)

Пример концептуального теста:

``` python
response = client.post(
    "/estimates",
    json={"project_name": "Scene 12", "days": 3},
)

assert response.status_code == 201
assert response.json()["project_name"] == "Scene 12"
```

Важно различать два уровня тестов:

``` text
Use Case tests
     ↓
проверяют application behavior

API tests
     ↓
проверяют HTTP contract + mapping
```

Не нужно дублировать все тесты на всех слоях без причины.

------------------------------------------------------------------------

# 18. Async/Await --- зачем мы вообще его изучаем

До этого момента можно построить полноценный FastAPI API без
полноценного освоения async.

И это специально.

Сначала нужно понять проблему.

Представь обработчик, который делает сетевой запрос:

``` text
Request A
   ↓
ждём сеть
   ↓
ответ
```

Вместо того чтобы бездумно считать ожидание «просто медленной функцией»,
нам нужно понять I/O-bound работу.

Когда задача большую часть времени **ждёт внешний ресурс**, асинхронная
модель позволяет одной event loop эффективно переключаться между
готовыми к продолжению задачами.

Python `asyncio` предоставляет infrastructure для concurrent code с
`async`/`await`; event loop может переключаться на другую Task, пока
текущая coroutine ждёт awaitable. [Python
asyncio](https://docs.python.org/3/library/asyncio.html)

------------------------------------------------------------------------

# 19. Mental Model --- «Официант, который не стоит у кухни»

Обычная последовательность:

``` text
Клиент
  ↓
Официант
  ↓
Кухня
  ↓
ждать у кухни
  ↓
получить блюдо
  ↓
клиент
```

Если официант буквально стоит и ничего больше не делает, это похоже на
блокирующее ожидание.

Асинхронная модель:

``` text
Официант
  ↓
передал заказ кухне
  ↓
свободен
  ↓
обслуживает другой стол
  ↓
кухня завершила работу
  ↓
возвращается к первому столу
```

Это не означает, что готовка стала быстрее.

Это означает, что время ожидания одного дела можно использовать для
другой работы.

------------------------------------------------------------------------

# 20. `async def` и `await`

Минимальная форма:

``` python
async def get_data():
    result = await some_async_operation()
    return result
```

Ключевое правило:

``` text
await
  ↓
можно использовать внутри async def
```

Но само объявление:

``` python
async def
```

ещё не означает, что функция автоматически выполняется параллельно.

Вызов coroutine без ожидания не выполняет её тело немедленно как обычную
функцию. Coroutine нужно либо `await`-нуть, либо запланировать как Task.
[Python asyncio Coroutines and
Tasks](https://docs.python.org/3/library/asyncio-task.html)

Это различие должно стать понятным на практике.

------------------------------------------------------------------------

# 21. Concurrency ≠ Parallelism

Это одно из мест, где требуется аккуратный mental model.

**Concurrency** --- несколько задач находятся в процессе выполнения и
получают возможность продвигаться вперёд.

**Parallelism** --- несколько задач реально исполняются одновременно на
разных вычислительных ресурсах.

Для event loop полезно мыслить так:

``` text
Task A → работа → await → пауза
                         ↓
Task B → работа → await → пауза
                         ↓
Task C → работа
```

Event loop использует кооперативную модель планирования: когда Task
ожидает Future/awaitable, loop может выполнять другую Task. [Python
asyncio Tasks](https://docs.python.org/3/library/asyncio-task.html)

Не нужно пока уходить в multiprocessing, CPU scheduling или GIL как
отдельную тему. Они относятся к другому набору проблем.

------------------------------------------------------------------------

# 22. Самая важная ловушка async в FastAPI

Нельзя делать вывод:

> «Раз я использую FastAPI, все функции должны быть `async def`».

Официальная документация FastAPI прямо описывает ситуацию, когда
используемая библиотека не поддерживает `await`: тогда path operation
можно определить как обычную `def`; FastAPI выполняет такие обычные path
functions в внешнем threadpool. [FastAPI
async/await](https://fastapi.tiangolo.com/async/)

Для текущего QR Warehouse это особенно важно, потому что стандартный
`sqlite3` в Python --- синхронный интерфейс.

Поэтому первый API на SQLite можно и нужно построить **с синхронными
repository methods**, вместо того чтобы искусственно оборачивать всё в
`async def`.

Правильный порядок:

``` text
Сначала понять HTTP
        ↓
Сначала сделать рабочий sync API
        ↓
Понять I/O и блокирующее ожидание
        ↓
Изучить async/await на маленьком отдельном примере
        ↓
Позже применять async там, где используемые библиотеки и архитектура действительно это оправдывают
```

Это одно из важнейших правил Module 09.

------------------------------------------------------------------------

# 23. Первый async mini-project

Перед интеграцией async в QR Warehouse нужно отдельно выполнить
небольшой эксперимент.

Например:

``` python
import asyncio


async def worker(name: str, delay: float):
    print(f"start {name}")
    await asyncio.sleep(delay)
    print(f"finish {name}")
```

Затем сравнить последовательный и concurrent варианты.

Цель не в том, чтобы выучить `asyncio.sleep()`.

Цель:

> **увидеть собственными глазами, что ожидание одной coroutine не
> обязано останавливать прогресс остальных Tasks.**

После эксперимента студент должен суметь объяснить временную диаграмму
выполнения.

------------------------------------------------------------------------

# 24. Что async НЕ решает

Async не делает автоматически быстрее:

``` text
CPU-heavy computation
```

Например:

``` python
for _ in range(10_000_000):
    calculate_something_expensive()
```

не становится магически быстрым от `async def`.

Также async не исправляет:

-   плохую архитектуру;
-   неэффективный SQL;
-   отсутствие индексов;
-   неправильные транзакции;
-   неоптимальную модель данных.

Он решает специфическую проблему **конкурентной обработки I/O-bound
операций**.

------------------------------------------------------------------------

# 25. Async в архитектуре QR Warehouse

В перспективе:

``` text
                     FastAPI
                       │
             ┌─────────┴─────────┐
             │                   │
        sync endpoint       async endpoint
             │                   │
             ▼                   ▼
       sync repository      async repository
             │                   │
             ▼                   ▼
          SQLite             PostgreSQL
```

Не надо пытаться заставить SQLite architecture стать асинхронной только
потому, что FastAPI умеет `async`.

Когда проект перейдёт на PostgreSQL и асинхронные драйверы/библиотеки
станут частью выбранного стека, async станет практически более значимым.

------------------------------------------------------------------------

# 26. Главный архитектурный эксперимент Module 09

После завершения первоначального API тебе нужно ответить на вопрос:

> **Сколько существующей бизнес-логики пришлось изменить, чтобы добавить
> Web API?**

Идеальный для обучения результат:

``` text
CLI code           изменился сильно / частично
HTTP Presentation  добавилась
Use Cases          почти не менялись
Domain             не менялся
Repositories       почти не менялись
Database           не менялась
```

Если для добавления HTTP тебе пришлось переносить SQL в endpoint
functions, это сигнал архитектурной проблемы.

Если Use Case начал возвращать `HTTPException`, это тоже сигнал утечки
Presentation Layer.

Если браузер знает структуру `sqlite3.Row`, это сигнал утечки
Infrastructure.

Module 09 должен учить видеть такие нарушения архитектуры.

------------------------------------------------------------------------

# 27. Практическая последовательность

## Part A --- HTTP Fundamentals

Изучить:

-   request/response;
-   URL;
-   headers;
-   body;
-   methods;
-   status codes;
-   query/path parameters;
-   JSON.

Задание:

Сделать маленький HTTP mental model exercise и вручную разобрать
несколько запросов/ответов.

------------------------------------------------------------------------

## Part B --- FastAPI Basics

Изучить:

-   FastAPI application;
-   path operation;
-   routing;
-   parameters;
-   request body;
-   Pydantic models;
-   response models;
-   status codes;
-   automatic validation;
-   development server;
-   interactive API documentation.

Задание:

Создать маленький API для абстрактного каталога оборудования.

------------------------------------------------------------------------

## Part C --- API Testing

Изучить:

-   `TestClient`;
-   pytest + HTTP;
-   успешные ответы;
-   невалидные запросы;
-   404;
-   409;
-   response JSON.

Задание:

Сделать минимальный набор API tests.

------------------------------------------------------------------------

## Part D --- QR Warehouse Web Entry Point

Добавить HTTP entry point к существующим Use Cases.

Минимум:

``` text
GET  /equipment
GET  /equipment/{sku}
POST /estimates
GET  /estimates/{id}
POST /estimates/{id}/items
PATCH /estimates/{id}/items/{item_id}
DELETE /estimates/{id}/items/{item_id}
DELETE /estimates/{id}
```

Точная структура endpoint'ов может быть скорректирована во время
проектирования.

------------------------------------------------------------------------

## Part E --- Error Mapping

Для каждого Use Case определить:

``` text
внутренняя ошибка
        ↓
HTTP representation
```

Например:

``` text
EquipmentNotFound
        ↓
404

InsufficientStock
        ↓
409

InvalidInput
        ↓
422 / 400
```

При этом Application Layer не должна импортировать FastAPI.

------------------------------------------------------------------------

## Part F --- Dependency Injection

Перенести сборку API-зависимостей в Composition Root / app factory style
setup.

Цель:

``` text
FastAPI endpoint
        ↓
получает Use Case
        ↓
использует Use Case
```

а не создаёт новый repository и database connection внутри каждого
endpoint.

------------------------------------------------------------------------

## Part G --- Async/Await

Отдельно изучить:

-   coroutine;
-   `async def`;
-   `await`;
-   event loop;
-   Task;
-   concurrency;
-   blocking vs non-blocking I/O;
-   `asyncio.run()`;
-   `asyncio.create_task()`;
-   почему coroutine без `await` не выполняется сама по себе.

Задание:

Сделать mini-project с 3--5 coroutine и временной диаграммой.

После этого провести анализ:

> Какие части QR Warehouse потенциально могут стать async? Какие пока не
> должны становиться async и почему?

------------------------------------------------------------------------

# 28. Изменение структуры QR Warehouse

К концу модуля архитектура может прийти к чему-то вроде:

``` text
src/
│
├── domain/
│   ├── models.py
│   └── errors.py
│
├── application/
│   └── use_cases.py
│
├── infrastructure/
│   ├── database.py
│   ├── equipment_repository.py
│   └── estimate_repository.py
│
├── presentation/
│   ├── cli/
│   └── api/
│       ├── routes.py
│       ├── schemas.py
│       └── dependencies.py
│
└── main.py
```

Не нужно воспринимать эту структуру как обязательную.

Она всего лишь иллюстрирует границу:

``` text
API / CLI
   ↓
Application
   ↓
Domain + Infrastructure contracts
```

Количество файлов должно определяться ответственностями и изменениями, а
не желанием получить «красивую архитектуру».

------------------------------------------------------------------------

# 29. Что пока НЕ входит в Module 09

Чтобы не превратить модуль в мини-университет, следующие темы пока не
являются центральными:

-   полноценная frontend-разработка;
-   React/Vue;
-   CSS;
-   OAuth/OpenID Connect;
-   сложная аутентификация;
-   RBAC;
-   WebSockets;
-   background tasks как основной механизм;
-   Docker deployment;
-   Kubernetes;
-   микросервисы;
-   Celery;
-   продакшен-мониторинг;
-   полноценное PostgreSQL administration;
-   глубокий SQL optimization.

Они будут становиться актуальны позже.

------------------------------------------------------------------------

# 30. Практическая цель модуля

Module 09 считается практически успешным, если ты можешь запустить:

``` text
FastAPI server
        ↓
HTTP request
        ↓
Pydantic validation
        ↓
API endpoint
        ↓
Use Case
        ↓
Repository
        ↓
SQLite
        ↓
HTTP response
```

и объяснить каждую границу.

Не просто «оно работает».

Ты должен понимать:

> кто преобразовал JSON;

> кто решил, что запрос является ошибочным;

> кто знает про HTTP status code;

> кто знает про бизнес-правило;

> кто выполняет SQL;

> кто владеет транзакцией;

> где находится dependency injection;

> почему endpoint не должен содержать SQL;

> почему Use Case не должен знать о HTTP.

------------------------------------------------------------------------

# 31. Независимое архитектурное задание

После изучения основной части не начинать сразу писать код QR Warehouse.

Сначала спроектировать API для незнакомой предметной области.

Предлагаемый домен:

**Система аренды кино-оборудования с доставкой.**

Требования:

``` text
Клиент создаёт заказ.
К заказу можно добавлять оборудование.
Оборудование имеет остаток на складе.
Доставка имеет адрес.
Заказ можно подтвердить.
Подтверждённый заказ нельзя изменить без специальной операции.
```

Нужно сначала на русском языке определить:

-   ресурсы;
-   endpoint'ы;
-   HTTP methods;
-   request/response models;
-   status codes;
-   Use Cases;
-   ошибки;
-   границы слоёв.

Только после этого переходить к коду.

Задача проверяет перенос архитектурного мышления в новый контекст, а не
способность повторить QR Warehouse.

------------------------------------------------------------------------

# 32. Final Challenge --- QR Warehouse API

Финальная работа модуля состоит из следующих частей.

### 1. Existing application remains usable

CLI или текущая внутренняя точка входа должна продолжать работать
настолько, насколько это предусмотрено проектом.

### 2. Add HTTP presentation layer

Создать FastAPI application.

### 3. Expose core operations

Реализовать CRUD/command endpoints, необходимые для текущего ядра QR
Warehouse.

### 4. Keep layers separated

API не выполняет SQL напрямую.

Use Cases не импортируют FastAPI.

Repository не формирует HTTP responses.

### 5. Validate requests

Некорректные JSON/body/path/query данные должны отклоняться на границе
API.

### 6. Map domain/application failures

Ошибки приложения должны преобразовываться в понятные HTTP responses.

### 7. Add API tests

Минимум:

``` text
успешное создание сметы
получение существующей сметы
получение несуществующей сметы
добавление оборудования
недостаток оборудования
изменение количества
удаление позиции
невалидный request body
```

### 8. Async experiment

Отдельный mini-project с asyncio.

### 9. Architecture report

Ответить на вопросы:

``` text
Какие файлы изменились при добавлении API?
Какие бизнес-правила остались нетронутыми?
Где находится HTTP-specific code?
Где находится validation?
Кто формирует status codes?
Кто владеет transaction boundary?
Можно ли было бы заменить FastAPI другим HTTP framework?
Что изменилось бы при добавлении второго Presentation Layer?
```

------------------------------------------------------------------------

# 33. Common Mistakes

## HTTP-001 --- Использование HTTP methods как случайных имён

Проблема:

``` text
POST для любого изменения
GET для удаления
```

Исправление:

Сначала описать смысл операции, затем выбрать метод.

------------------------------------------------------------------------

## HTTP-002 --- SQL внутри endpoint

Проблема:

``` python
@app.get("/equipment")
def get_equipment():
    cursor.execute("SELECT ...")
```

Почему плохо:

Presentation Layer получает ответственность Infrastructure.

------------------------------------------------------------------------

## HTTP-003 --- Use Case знает FastAPI

Проблема:

``` python
raise HTTPException(status_code=404)
```

в Application Layer.

Почему плохо:

Application больше нельзя использовать независимо от HTTP.

------------------------------------------------------------------------

## HTTP-004 --- Endpoint создаёт инфраструктуру сам

Проблема:

``` python
@app.post("/estimates")
def create_estimate(...):
    conn = sqlite3.connect(...)
    repo = SQLEstimateRepository(conn)
```

Почему плохо:

Composition Root / dependency management начинают размазываться по
endpoint'ам.

------------------------------------------------------------------------

## HTTP-005 --- Возвращать database rows напрямую

Проблема:

``` python
return cursor.fetchone()
```

Это слишком сильно связывает Presentation с Infrastructure
representation.

Нужно формировать понятный API response model.

------------------------------------------------------------------------

## HTTP-006 --- Считать JSON бизнес-моделью

JSON --- transport representation.

Он не должен автоматически становиться Domain Entity.

------------------------------------------------------------------------

## HTTP-007 --- Считать `async def` обязательным для FastAPI

Нельзя делать:

``` python
@app.get(...)
async def ...:
    result = sync_database_call()
```

только потому, что «FastAPI требует async».

Сначала выясняется, является ли используемый I/O API асинхронным.

FastAPI поддерживает как `async def`, так и обычные `def` path
operations; синхронные обработчики выполняются через внешний threadpool.
[FastAPI async/await](https://fastapi.tiangolo.com/async/)

------------------------------------------------------------------------

## HTTP-008 --- Путать async и parallelism

``` text
async ≠ magic parallel CPU execution
```

Async прежде всего полезен для конкурентной работы с ожиданием I/O.

------------------------------------------------------------------------

## HTTP-009 --- Создать coroutine и не await-нуть её

``` python
result = get_data()
```

если `get_data()` --- coroutine.

Это не то же самое, что выполнить обычную функцию.

------------------------------------------------------------------------

## HTTP-010 --- Переносить всю бизнес-валидацию в Pydantic

Pydantic может проверять форму входных данных.

Но бизнес-правила не исчезают из Application/Domain просто потому, что
существует схема request body.

------------------------------------------------------------------------

## HTTP-011 --- Дублировать все Use Cases в endpoints

Плохо:

``` text
Use Case: AddItemToEstimate
API endpoint: повторяет всю его логику
```

API должен адаптировать транспорт, а не копировать Application Layer.

------------------------------------------------------------------------

## HTTP-012 --- Сначала делать весь frontend

Module 09 не требует законченного сайта.

Сначала должен существовать рабочий API contract и vertical slice.

------------------------------------------------------------------------

# 34. Mental Models

## 1. Почта

HTTP --- обмен письмами между клиентом и сервером.

## 2. Бюро переводчика

API переводит внешний язык HTTP в язык Application Layer.

## 3. Bouncer 2.0

Pydantic / request validation охраняет входную границу.

## 4. Ресепшен и кухня

API принимает заказ. Use Case организует выполнение. Repository получает
данные. Database хранит данные.

## 5. Официант без простоя

Async позволяет Task отдать I/O-операцию и пока она ожидается дать event
loop возможность продвинуть другие задачи.

## 6. Контракт билета

Request/Response models --- публичный контракт API.

## 7. Переводчик ошибок

Application errors → HTTP status codes.

## 8. Два входа в одно здание

CLI и HTTP могут быть двумя Presentation Layers одного Application
Layer.

------------------------------------------------------------------------

# 35. Self-Check Questions

К концу модуля студент должен суметь ответить своими словами.

### HTTP

1.  Что такое HTTP request?
2.  Что такое HTTP response?
3.  Что такое URL?
4.  Для чего нужен HTTP method?
5.  Чем GET отличается от POST?
6.  Чем PUT отличается от PATCH?
7.  Что означает 200?
8.  Что означает 201?
9.  Что означает 404?
10. Что означает 409?
11. Чем 4xx отличается от 5xx?
12. Что такое header?
13. Что такое request body?
14. Чем path parameter отличается от query parameter?

### API design

15. Что такое ресурс в контексте API?
16. Почему endpoint не должен содержать SQL?
17. Почему Use Case не должен знать о HTTP?
18. Где должен находиться перевод application error в HTTP status code?
19. Зачем нужны request/response models?
20. Чем request model отличается от Domain Entity?
21. Почему JSON нельзя автоматически считать Domain Model?
22. Что значит «API является контрактом»?

### FastAPI

23. Что такое `FastAPI()` application?
24. Что делает `@app.get()`?
25. Что делает path operation function?
26. Для чего нужен Pydantic model?
27. Что делает response model?
28. Что такое dependency в FastAPI?
29. Как FastAPI связан с Dependency Injection?
30. Как протестировать FastAPI endpoint через pytest?

### Architecture

31. Как добавить HTTP API к существующим Use Cases без переписывания
    бизнес-логики?
32. Что должно остаться неизменным при добавлении новой Presentation
    Layer?
33. Где должен находиться Composition Root?
34. Кто создаёт Repository?
35. Кто владеет transaction boundary?
36. Что является признаком leakage между слоями?

### Async

37. Что такое coroutine?
38. Что делает `async def`?
39. Что делает `await`?
40. Почему `await` можно использовать только внутри `async def`?
41. Что происходит, если вызвать coroutine и не await-нуть её?
42. Что такое event loop?
43. Что такое Task?
44. Что такое concurrency?
45. Чем concurrency отличается от parallelism?
46. Почему async особенно полезен для I/O-bound работы?
47. Почему `async def` не делает CPU-bound функцию магически быстрее?
48. Почему не все FastAPI endpoints обязаны быть `async def`?
49. Почему sync `sqlite3` --- важный нюанс для текущего QR Warehouse?
50. Когда применение async было бы искусственным?

### Transfer

51. Как выглядел бы API для нового незнакомого проекта?
52. Какие решения в API нужно принимать до написания FastAPI-кода?
53. Как понять, что endpoint стал слишком «умным»?
54. Как понять, что Application Layer начал зависеть от HTTP?
55. Как проверить, что архитектура пережила появление второй
    Presentation Layer?

------------------------------------------------------------------------

# 36. Completion Criteria

Module 09 считается завершённым, когда студент:

``` text
[ ] Понимает request/response модель HTTP.

[ ] Понимает методы GET/POST/PUT/PATCH/DELETE.

[ ] Понимает базовые HTTP status codes.

[ ] Умеет различать path/query/body.

[ ] Понимает JSON как transport format.

[ ] Может создать простой FastAPI application.

[ ] Может определить несколько path operations.

[ ] Может использовать Pydantic для входных данных.

[ ] Может задать response model.

[ ] Может связать endpoint с существующим Use Case.

[ ] Не помещает SQL в endpoint.

[ ] Не импортирует FastAPI в Application Layer.

[ ] Понимает перевод внутренних ошибок в HTTP responses.

[ ] Может тестировать API через pytest/TestClient.

[ ] Построил минимум один полноценный QR Warehouse vertical slice.

[ ] Понимает базовую модель async/await.

[ ] Самостоятельно объясняет event loop и Task.

[ ] Может объяснить, почему async не равен parallelism.

[ ] Понимает, почему текущий sync SQLite repository не следует искусственно превращать в async.

[ ] Провёл отдельный async mini-project.

[ ] Выполнил независимое API design exercise на незнакомом домене.
```

------------------------------------------------------------------------

# 37. Recommended Time Budget

Ориентир для текущего уровня:

``` text
HTTP fundamentals                  2.5–3 h
HTTP methods/status/URLs           2–2.5 h
FastAPI basics                     2–3 h
Pydantic + request/response        2–3 h
API errors + DI                    2–2.5 h
API testing                        2–3 h
QR Warehouse vertical slice       4–5 h
Async/await fundamentals           2–3 h
Async mini-project                 1.5–2 h
Independent design challenge       1.5–2 h
Final integration/review           2–3 h

Total                              ~22–28 h
```

Это ориентир, а не норматив.

Если какая-то концепция требует значительно больше времени, задержка на
ней предпочтительнее поверхностного прохождения.

------------------------------------------------------------------------

# 38. Как Module 09 меняет твоё положение относительно MVP

До Module 09:

``` text
Python
OOP
Design Patterns
Application Architecture
SQL
SQLite
Transactions
Repositories
Use Cases
        ↓
хорошее внутреннее приложение
```

После Module 09:

``` text
Python
OOP
Architecture
SQL / Database
        ↓
FastAPI / HTTP
        ↓
Web API
        ↓
QR Warehouse
```

Это очень важный переход.

Ты впервые получаешь возможность сделать настоящий vertical slice:

``` text
Browser / API client
        ↓
HTTP
        ↓
FastAPI
        ↓
Use Case
        ↓
Repository
        ↓
SQLite
```

С этого момента дальнейшее обучение всё больше можно совмещать с
развитием реального продукта.

------------------------------------------------------------------------

# 39. Куда ведёт Module 09

После Module 09 следующим естественным направлением становятся темы,
которых сейчас не хватает для полноценного многопользовательского
backend:

``` text
Module 09
HTTP + API + FastAPI + async fundamentals
        ↓
Authentication / Authorization
        ↓
PostgreSQL
        ↓
Production configuration
        ↓
Deployment
        ↓
Client / Frontend integration
        ↓
QR scanner integration
        ↓
Real MVP
```

Точный порядок следующих модулей может измениться после практики Module
09.

Например, если API выявит, что SQLite или текущая архитектура создают
ограничения, PostgreSQL может подняться в приоритете.

------------------------------------------------------------------------

# 40. Как использовать AI в этом модуле

AI здесь не должен быть генератором готового backend.

Правильная последовательность:

``` text
1. Спроектировать endpoint.
2. Объяснить его смысл.
3. Решить, какой Use Case он вызывает.
4. Определить request/response models.
5. Определить ошибки.
6. Только после этого попросить AI помочь с синтаксисом.
7. Проверить реализацию самостоятельно.
8. Написать тест.
9. Проанализировать, не протекли ли слои.
```

Хороший запрос:

> «Я хочу сделать POST /estimates. Вот требования и мой Use Case.
> Проверь границу между API и Application Layer, но не переписывай код
> целиком.»

Плохой запрос:

> «Сделай мне весь FastAPI backend QR Warehouse.»

Цель модуля --- научиться использовать AI как reviewer и implementation
assistant, сохраняя авторство инженерных решений.

------------------------------------------------------------------------

# 41. Mentor Calibration --- правило качества обратной связи

С Module 09 вводится отдельное правило.

**Обычная корректность не является выдающимся достижением.**

Если студент:

-   исправил опечатку в SQL после подсказки;
-   добавил забытый `break` после замечания;
-   написал корректный `@app.get()` по образцу;
-   исправил `return` после ревью;
-   использовал синтаксис FastAPI точно так, как было показано;
-   написал правильный HTTP status code после объяснения;

это следует отмечать спокойно и предметно:

> «Да, теперь код корректен.»

или:

> «Исправление верное. Причина ошибки была в X.»

Не нужно описывать такие действия как исключительный прорыв,
профессиональный подвиг или доказательство уровня Senior.

### Когда похвала уместна

Более сильная положительная обратная связь оправдана, когда студент:

1.  сам обнаружил проблему до подсказки;
2.  самостоятельно сформулировал принцип, который переносится на другие
    задачи;
3.  выбрал архитектурное решение и может объяснить trade-off;
4.  применил ранее изученный принцип в новом незнакомом контексте;
5.  сознательно отказался от ненужной сложности и обосновал отказ;
6.  заметил противоречие между текущей архитектурой и новым требованием;
7.  самостоятельно улучшил решение после анализа последствий.

### Запрещённый стиль обратной связи

Не использовать автоматически:

``` text
«Это гениально»
«Ты мыслишь как Senior»
«Это уровень профессионального архитектора»
«Ты открыл профессиональный паттерн»
«Невероятное инженерное достижение»
```

для каждой правильно написанной строки кода или исправления после
подсказки.

Сильные характеристики должны использоваться редко и только тогда, когда
накоплено достаточно доказательств.

### Предпочтительный стиль

Обратная связь должна отвечать на четыре вопроса:

``` text
Что было сделано?
Почему это правильно/неправильно?
Насколько решение было самостоятельным?
Какой принцип переносится на следующую задачу?
```

Например:

> «Ты самостоятельно заметил, что endpoint начал содержать SQL. Это
> важно не из-за самого SQL, а потому что ты увидел нарушение границы
> Presentation → Infrastructure. Такой вывод переносится на другие API.»

Это полезнее, чем просто написать «Отлично!».

------------------------------------------------------------------------

# 42. Mentor Behavior Adjustment

Для Module 09 применяются следующие правила методики.

### Adjustment 019 --- Calibrated Praise

Причина:

Постоянная высокая похвала снижает информативность обратной связи.

Действие:

Разделять:

``` text
correct
→ просто корректно

good reasoning
→ умеренно положительная оценка

independent transferable insight
→ сильная положительная оценка
```

### Adjustment 020 --- Reward Independence, Not Compliance

Исправление после подсказки не считать самостоятельным открытием.

Отмечать отдельно:

``` text
student discovered
vs.
student understood after explanation
vs.
student successfully applied pattern
```

### Adjustment 021 --- Evidence Before Labels

Не использовать labels вроде «Senior», «professional», «architect» как
эмоциональные оценки.

Сначала приводить конкретное наблюдение.

Например:

``` text
«Ты сохранил Use Case независимым от HTTP»
```

вместо:

``` text
«Ты уже мыслишь как Senior backend architect»
```

### Adjustment 022 --- Maintain Difficulty Calibration

Не поднимать сложность только ради ощущения прогресса.

Каждая следующая тема должна возникать из реальной проблемы предыдущей
архитектуры.

------------------------------------------------------------------------

# 43. Final Mentor Note

Module 09 не должен превратить студента в человека, который умеет писать
FastAPI-декораторы.

Его задача значительно глубже:

> **Научиться превращать существующее приложение в сервис, доступный
> через сеть, не разрушая границы архитектуры.**

После Module 07 студент научился контролировать зависимости.

После Module 08 студент научился строить реляционную модель и управлять
транзакциями.

После Module 09 он должен увидеть следующий уровень:

``` text
Внешний мир
    ↓
HTTP
    ↓
Presentation
    ↓
Application
    ↓
Infrastructure
    ↓
Database
```

и понять, что это не пять независимых технологий.

Это единый поток данных, проходящий через границы.

Именно здесь архитектурные идеи Module 07 получают второе важное
подтверждение:

> **Если Application Layer можно подключить к CLI и к HTTP без
> переписывания бизнес-правил, значит граница действительно работает.**

Async/Await в этом модуле является не новой религией и не обязательным
украшением каждого endpoint.

Это следующий mental model о том, как сервер работает с ожиданием I/O.

На текущем этапе достаточно понять механизм, увидеть его на маленьком
эксперименте и научиться определять, где async полезен, а где он был бы
искусственным.

------------------------------------------------------------------------

# 44. Концептуальный переход

После Module 08 основной вопрос звучал:

> «Как правильно хранить и изменять данные?»

После Module 09 он должен стать:

> **«Как безопасно предоставить возможности приложения внешнему миру
> через HTTP, сохранив архитектурные границы?»**

Это подготавливает следующий этап:

``` text
Database-backed application
          ↓
Web backend
          ↓
Authentication / multi-user access
          ↓
PostgreSQL
          ↓
Deployment
          ↓
Real QR Warehouse MVP
```

------------------------------------------------------------------------

# 45. Integration with Programming Handbook

После прохождения Module 09 в Programming Handbook должны появиться
разделы:

``` text
HTTP
Request / Response
HTTP Methods
HTTP Status Codes
REST concepts
API resources
FastAPI
Pydantic
Request / Response Models
API validation
Dependency Injection in FastAPI
API error mapping
API testing
async / await
Coroutines
Tasks
Event Loop
Concurrency vs Parallelism
Blocking vs Non-blocking I/O
FastAPI sync vs async path operations
API architecture in QR Warehouse
```

Learning Journal должен сохранить:

``` text
первое понимание HTTP
первую работающую API
первый vertical slice
первый async experiment
первую архитектурную проблему при добавлении HTTP
```

Questions должны сохранить новые открытые вопросы.

Development Log должен зафиксировать:

``` text
как изменилось архитектурное мышление после появления второй Presentation Layer
как изменилось понимание I/O и concurrency
какие новые ошибки стали повторяться
как изменилась степень самостоятельности
```

------------------------------------------------------------------------

# 46. Final Principle

Не стремись после Module 09 сказать:

> «Я умею FastAPI.»

Гораздо полезнее, если ты сможешь сказать:

> **«Я понимаю, как HTTP-клиент входит в моё приложение, где проходит
> граница API и Application Layer, как запрос превращается в данные для
> Use Case, как ошибка превращается в HTTP response и почему async нужен
> только там, где он действительно решает проблему ожидания I/O.»**

Это и есть инженерная цель Module 09.
