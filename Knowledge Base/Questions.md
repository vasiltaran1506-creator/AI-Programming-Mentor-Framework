```markdown
# Questions

**Version:** 1.0  
**Status:** Active  
**Maintained by:** AI Programming Mentor

---

## Purpose

Questions are one of the most valuable learning resources.

Every unanswered question reveals the boundary between current knowledge and future understanding.

This document exists to preserve curiosity.

A question should never be considered a distraction.  
Instead, it becomes part of the learning roadmap.

Questions should not disappear.  
They move through different stages as understanding develops.

---

## Workflow

Every question belongs to exactly one state.

Open  
↓  
Discussing  
↓  
Answered  
↓  
Mastered

**Open**  
The question has been asked.  
The student does not yet understand the answer.

**Discussing**  
The topic is currently being studied.  
The answer may be incomplete.  
Further clarification may needed.

**Answered**  
The student understands the concept.  
However, additional practical experience is still recommended.

**Mastered**  
The student has successfully applied the concept in real code.  
The knowledge is considered stable.

Mastered questions remain in this document as part of the learning history.

---

## Rules

Questions are never deleted.  
Questions may move between states.

A previously answered question may become Open again if later topics reveal a deeper misunderstanding.  
This is considered normal.

---

## Open Questions

### Q-0001

**Title**  
Why does Python start indexing at zero?

**Reason**  
The student understands that indexing starts at zero but wants to understand the historical and technical reasons behind this design.

**Related Topics**  
Lists  
Memory  
Arrays

**Priority**  
Medium

**Status**  
Open

---

### Q-0002

**Title**  
What actually happens inside memory when variables change?

**Reason**  
The student has a good intuitive understanding of state but wants to understand how Python stores and updates objects internally.

**Related Topics**  
Variables  
Assignment  
Objects  
References

**Priority**  
High

**Status**  
Open

---

### Q-0004

**Title**  
How does hashing work inside sets and dictionaries?

**Reason**  
The student understands that sets provide instant lookup and that dictionaries use keys for fast access.  
However, the underlying mechanism — hashing — has not been explored.  
The student asked why `in` works instantly for sets but requires iteration for lists.

**Related Topics**  
Sets  
Dictionaries  
Hash Tables  
Performance

**Priority**  
Medium

**Status**  
Open

---

### Q-0006

**Title**  
What are lambda functions and when should I use them beyond max()?

**Reason**  
The student successfully applied lambda in `max(valid_datasets, key=lambda x: x["images"])` but acknowledged limited understanding of the concept.  
The student wants to understand:

- What lambda functions are fundamentally
- When to use lambda vs regular def functions
- Other common use cases (map, filter, sorted, etc.)

**Related Topics**  
Functional Programming  
Lambda  
Higher-Order Functions  
map, filter, reduce

**Priority**  
High

**Status**  
Open

---

### Q-0010

**Title**  
What are the SOLID principles and how do they connect to what I have already learned?

**Reason**  
During Module 06, the student independently discovered the Liskov Substitution Principle through the Square/Rectangle paradox.  
The student also demonstrated intuitive understanding of the Open/Closed Principle (code should be open for extension but closed for modification) when analyzing why inheritance by convenience is dangerous.  
The student wants to understand the complete SOLID framework and how all five principles connect to each other.

**Related Topics**  
Single Responsibility Principle  
Open/Closed Principle  
Liskov Substitution Principle  
Interface Segregation Principle  
Dependency Inversion Principle

**Priority**  
Medium

**Status**  
Open

**Module 07 Progress Note:**  
The student has now practically demonstrated understanding of Dependency Inversion (Repository pattern, business logic depending on abstractions rather than concrete implementations) and Single Responsibility (each component owns one coherent responsibility). These were experienced through real refactoring rather than formal study. The formal SOLID framework study remains valuable to unify these practical experiences under a single conceptual umbrella.

---

### Q-0023

**Title**  
How do relational databases work internally, and how do I use SQL systematically?

**Reason**  
During Module 07, the student successfully used SQLite as an infrastructure detail through the Repository pattern. However, the student explicitly stated: "Никакого системного понимания синтаксиса, внутреннего устройства базы данных и прочего у меня пока нет. Хочется изучать это в будущих модулях." The student wants to understand:

- SQL syntax systematically (SELECT, INSERT, UPDATE, DELETE, JOIN)
- How relational databases store data internally (B-trees, pages)
- Indexing and query performance
- Transactions and atomicity
- Schema design and migrations
- The difference between SQLite, PostgreSQL, and other databases
- When to use a database vs files vs in-memory storage

**Related Topics**  
SQL  
Relational Databases  
SQLite  
PostgreSQL  
Indexing  
Transactions  
Schema Design  
Migrations  
Query Optimization

**Priority**  
High

**Status**  
Open

---

### Q-0024

**Title**  
How would the QR Warehouse architecture change if I add a Web API alongside the CLI?

**Reason**  
During Module 07, the student discussed the future vision of the system growing to include a web interface for clients, a manager interface, and a warehouse worker interface. The student understands conceptually that the Use Cases should remain reusable across different Presentation layers, but has not yet experienced this in practice. This question will become relevant when the student is ready to build a second entry point into the application.

**Related Topics**  
Web Frameworks  
HTTP API  
Presentation Layer  
Application Layer reuse  
Multiple entry points  
REST principles

**Priority**  
Medium

**Status**  
Open

---

## Discussing

(No questions currently in this state.)

---

## Answered

(No questions yet.)

---

## Mastered

### Q-0003

**Title**  
Why do some functions return values while others only modify existing objects?

**Reason**  
This question naturally follows the discussion about `print()`, `return()`, and methods such as `append()`.

**Resolution**  
Студент глубоко усвоил разницу между неизменяемыми (immutable) и изменяемыми (mutable) типами данных. Он понял, что строки (камни) требуют `return`, потому что методы создают новые объекты. В то время как списки и словари (корзины) передаются в функции по ссылке, и их можно модифицировать на месте без `return`. Концепция закреплена на практике при написании парсера тегов.

---

### Q-0005

**Title**  
What is the difference between pathlib.Path and string paths?

**Reason**  
The student used pathlib.Path during the Tag Library Manager project and encountered confusion between Path objects and string paths.  
The student understood the basic usage but wants a deeper understanding of when to use Path objects versus plain strings.

**Resolution**  
Студент глубоко усвоил разницу между "умными навигаторами" (Path объекты) и "глупыми строками". Он понял, что Path объекты понимают операционную систему и предоставляют методы для работы с путями (exists(), is_dir(), glob()), в то время как строки требуют ручной обработки. Концепция закреплена на практике при написании File Analyzer и Dataset Catalog Analyzer. Студент теперь последовательно использует Path для всех файловых операций.

---

### Q-0007

**Title**  
What is Object-Oriented Programming and when is it useful?

**Reason**  
The student has mastered procedural programming and multi-module architecture.  
The natural next step is OOP, but the student has not yet explored:

- Classes vs objects
- Methods vs functions
- Inheritance and composition
- When OOP is better than procedural design

**Resolution**  
Студент полностью освоил концепции ООП в ходе работы над проектом "Киносклад". Он самостоятельно спроектировал и реализовал классы `Inventory` и `Estimate`, использующие инкапсуляцию для защиты инвариантов (например, запрет на отрицательные остатки на складе и автоматический пересчет итогов). Студент понял разницу между пассивными структурами данных (`@dataclass`) и активными объектами с поведением, освоил композицию объектов и паттерн "Дирижер оркестра" (когда `main.py` координирует объекты, но не вмешивается в их внутреннюю логику). Концепция закреплена на практике написанием 11 автотестов и успешной интеграцией в основную программу.

---

### Q-0008

**Title**  
What is the difference between @dataclass and regular classes?

**Reason**  
The student encountered confusion about when to use simple data structures versus objects with behavior during the object-oriented design phase.  
The student asked whether Inventory and Estimate should be dataclasses or regular classes.

**Resolution**  
Студент глубоко усвоил разницу между пассивными структурами данных и активными объектами. Он понял, что `@dataclass` идеально подходит для простых контейнеров данных (например, `Equipment`, `EstimateItem`), где данные просто передаются и читаются. В то время как обычные классы с методами нужны для объектов, защищающих свои инварианты и выполняющих бизнес-логику (например, `Inventory`, `Estimate`). Концепция закреплена на практике: студент самостоятельно выбрал `@dataclass` для каталога оборудования и обычные классы для бизнес-логики склада и сметы, что сделало архитектуру чистой и безопасной.

---

### Q-0009

**Title**  
How to write automated tests for business logic using pytest?

**Reason**  
The student wanted to learn how to protect business logic from regressions and ensure code correctness during refactoring.  
The student asked how to test object state transitions and edge cases automatically.

**Resolution**  
Студент освоил инструменты `pytest` для модульного тестирования. Он настроил конфигурацию тестов (`pytest.ini`), написал 11 автотестов для проверки бизнес-логики (бронирование, удаление, пересчет итогов) и научился использовать фикстуры для подготовки тестовых данных. Студент понял концепцию "красный-зеленый-рефакторинг" и успешно применил тестирование для защиты критических методов `check_and_reserve`, `add_item` и `remove_one`. Концепция закреплена на практике и все тесты успешно проходят.

---

### Q-0011

**Title**  
What is the difference between inheritance and composition, and when should I use each?

**Reason**  
The student encountered confusion about when to model relationships through inheritance ("is-a") versus composition ("has-a").  
The student initially suggested that Engine should inherit from Vehicle and CargoCapacity should inherit from Truck, which revealed a need to clarify the fundamental difference between these two relationships.

**Resolution**  
Студент глубоко усвоил разницу между отношениями "является" (is-a) и "имеет" (has-a). Он понял, что наследование должно использоваться только для подлинных концептуальных связей ("Машина является транспортом"), а композиция — для отношений владения или использования ("Машина имеет двигатель"). Студент самостоятельно применил тест "является/имеет" для анализа отношений между классами. Через систему птиц (где Пингвин не может безопасно наследовать `fly()` от Птицы) студент понял опасность "наследования по удобству" и освоил проектирование через композицию поведений (отдельные объекты `FlyBehavior`, `SwimBehavior`, которые вставляются в класс `Bird`). Студент также интуитивно открыл принцип подстановки Лисков через парадокс квадрата и прямоугольника: предложил, чтобы оба класса наследовались от общего предка `Shape`, а не друг от друга. Концепция закреплена на практике в нескольких мини-проектах и применена при анализе архитектуры QR Warehouse.

---

### Q-0012

**Title**  
What is polymorphism and how does it eliminate conditional logic?

**Reason**  
The student needed to implement different discount policies for different client types (VGIK students get 70% discount on tungsten lights, 50% on LED).  
The natural approach was to use if/elif chains, but the student was ready to explore a more flexible solution.

**Resolution**  
Студент самостоятельно спроектировал систему ценовых политик до изучения формального названия паттерна Стратегия. Он понял, что полиморфизм позволяет устранить условную логику: вместо `if/elif` цепочек разные объекты отвечают на один и тот же метод (`calculate_discount`) своим способом. Студент спроектировал абстрактный базовый класс `PricePolicy` с методами `VGIK_Policy` и `Standart_Policy`, каждый из которых реализует свою логику расчета скидок. Вызывающий код (смета) просто вызывает `policy.calculate_discount(category)`, не зная, какая именно политика перед ним. Концепция закреплена на практике в проекте QR Warehouse и нескольких мини-проектах (система уведомлений, система птиц).

---

### Q-0013

**Title**  
What are Abstract Base Classes (ABC) and when should I use them?

**Reason**  
The student encountered a problem where a base class providing a default implementation (returning 0) could mask errors when a subclass forgot to implement the method.  
The student needed a way to enforce that all subclasses must implement certain methods.

**Resolution**  
Студент понял разницу между "джентльменским соглашением" (базовый класс с реализацией по умолчанию) и "юридическим контрактом" (абстрактный класс с `@abstractmethod`). Он освоил модуль `abc`, декоратор `@abstractmethod` и класс `ABC`. Студент понял, что абстрактный класс превращает неявное ожидание в явное требование: если наследник не реализует абстрактный метод, Python выбросит `TypeError` при создании объекта, а не во время выполнения бизнес-логики. Концепция закреплена на практике: студент применил `ABC` в классе `PricePolicy` проекта QR Warehouse, защитив систему от неполных реализаций ценовых политик.

---

### Q-0014

**Title**  
What is the Factory pattern and when should I use it?

**Reason**  
The student wanted to understand how to centralize object creation logic when creation becomes complex or repeated in multiple places.

**Resolution**  
Студент реализовал фабрику `NotificationProcessor` для системы уведомлений (создание `EmailNotification`, `SMSNotification`, `PushNotification`). Он понял, что фабрика полезна, когда: создание объекта требует сложной логики, логика создания повторяется в нескольких местах, или процесс создания требует дополнительных шагов (чтение конфигурации, проверка доступности ресурсов). Студент также понял, когда фабрика является избыточной: если создание объекта тривиально (например, `FileLogger(path)`), и происходит в одном месте, создавать отдельный класс-фабрику не нужно. Концепция закреплена на практике в мини-проекте системы уведомлений и применена при анализе архитектуры QR Warehouse.

---

### Q-0015

**Title**  
What is super() and when should I use it to extend parent behavior?

**Reason**  
The student needed to understand how to extend parent class behavior rather than completely replace it.  
The student encountered the difference between overriding a method (complete replacement) and extending it (adding to existing behavior).

**Resolution**  
Студент освоил принцип "Да, и..." (из театральной импровизации): `super()` говорит "сделай то, что уже написано у родителя", а затем позволяет добавить свою деталь. Через систему оценки сотрудников (`Employee`, `Manager`, `Developer`) студент применил `super()` в двух контекстах: расширение `__init__` для добавления специфичных атрибутов и расширение бизнес-методов (например, `calculate_performance_score`, где менеджер добавляет бонус за размер команды к базовой оценке). Студент понял, что `super()` не следует использовать автоматически при каждом наследовании: он нужен только когда наследник хочет сохранить поведение родителя и дополнить его. Концепция закреплена на практике в мини-проекте системы оценки сотрудников.

---

### Q-0016

**Title**  
How do I test expected exceptions using pytest.raises?

**Reason**  
The student needed to verify that code correctly raises exceptions for invalid input.  
The student initially wrote `assert ValueError("message")` instead of using the proper pytest mechanism for testing exceptions.

**Resolution**  
Студент освоил конструкцию `with pytest.raises(ExceptionType)` для проверки того, что код выбрасывает ожидаемое исключение. Он понял разницу между "поместить код в защитный бункер" (контекстный менеджер ловит исключение и проверяет его тип) и обычным `assert`. Студент также научился проверять текст исключения через `as error_info` и `str(error_info.value)`. Концепция закреплена на практике в тестах фабрики уведомлений (проверка `ValueError` для неизвестного типа уведомления) и применена для защиты бизнес-логики от некорректных входных данных.

---

### Q-0017

**Title**  
What is software architecture and how is it different from file organization?

**Reason**  
The student initially associated architecture with folder structures and file names. Module 07 needed to establish that architecture is about responsibilities, boundaries, and dependencies — not about how files are arranged on disk.

**Resolution**  
Студент глубоко усвоил, что архитектура — это не папки и файлы, а управление зависимостями и контроль над тем, как изменения распространяются по системе. Ключевой инсайт был сформулирован студентом самостоятельно: "Я понял, насколько полезно и эффективно изолировать бизнес логику от всего остального." Студент понял, что архитектура становится видимой через изменения: "Что произойдёт, если JSON станет SQLite? Что произойдёт, если CLI станет Web API?" — эти вопросы позволяют увидеть реальную архитектуру системы. Студент также самостоятельно сформулировал "Архитектурный фильтр" для классификации новых фич: правило о сущности → Домен; рабочий процесс → Приложение; техническая деталь → Инфраструктура. Концепция закреплена на практике через рефакторинг QR Warehouse и успешную замену JSON на SQLite без изменения бизнес-логики.

---

### Q-0018

**Title**  
What is the Repository pattern and when should I use it?

**Reason**  
The student needed to isolate persistence logic from business logic so that changing the storage mechanism (JSON → SQLite → PostgreSQL) would not require rewriting business rules. The student initially stored all catalog data inside `Inventory` as internal dictionaries, creating tight coupling between business logic and data loading.

**Resolution**  
Студент создал абстрактный контракт `EquipmentRepository` (ABC) с методами `find_by_sku()` и `update_available()`, а затем реализовал три конкретные реализации: `JsonEquipmentRepository` (чтение из JSON-файла), `SqliteEquipmentRepository` (работа с базой данных через `sqlite3`), и `InMemoryEquipmentRepository` (для тестов). Студент пережил ключевой архитектурный инсайт: при замене JSON на SQLite ни `Inventory`, ни `Estimate`, ни `AddItemToEstimate` не потребовали ни одной строчки изменений. Студент описал этот опыт словами: "Я без труда и без необходимости переписывать половину программы смог перевести работу программы с JSON файлов на базу данных." Студент также понял, когда Репозиторий избыточен: для крошечного скрипта с одним источником данных абстракция может быть ненужной. Концепция закреплена на практике в проекте QR Warehouse.

---

### Q-0019

**Title**  
What are Use Cases (Application Services) and how do they differ from domain objects?

**Reason**  
The student initially confused "Use Case" with user scenarios (e.g., "using the app on Windows 10" or "working offline"). This was a terminology collision between software architecture and product management/QA contexts. The student explicitly stated: "Мне бы понять предметную суть Use Case, тогда будет проще." Additionally, the student questioned why Use Cases were needed if `main.py` already orchestrates the program, fearing an "orchestrator of orchestrators" infinite loop.

**Resolution**  
Через ментальную модель "Сотрудник МФЦ / Дирижёр" студент понял, что Use Case — это оркестратор Слоя Приложения, который координирует доменные объекты для выполнения бизнес-процесса, не зная про UI или базу данных. Через модель "Директор завода против Начальника производства" студент понял разницу между Composition Root (`main.py` — создаёт и соединяет объекты) и Use Case (выполняет бизнес-процесс внутри уже собранной системы). Студент извлёк `AddItemToEstimate` как Use Case в отдельный файл `use_cases.py`, координирующий `Inventory` и `Estimate`. Студент также проявил прагматичность: решил НЕ создавать сложные классы Use Cases, когда простые функции в `main.py` достаточны для текущего масштаба проекта, но чётко понял, КОГДА они станут обязательными (добавление Web API, email-уведомлений, нескольких точек входа). Концепция закреплена на практике в проекте QR Warehouse.

---

### Q-0020

**Title**  
What is Dependency Inversion and how does it work in practice?

**Reason**  
The student needed to understand how to make stable business rules independent from unstable technical details. The initial code had `Inventory` directly storing catalog data in internal dictionaries (`self._catalog`, `self._stock`), creating tight coupling between business logic and the specific way data was loaded.

**Resolution**  
Студент пережил Dependency Inversion не как теоретический принцип SOLID, а как практический инструмент. Когда бизнес-логика (`Inventory`) стала зависеть от абстрактного контракта `EquipmentRepository`, а не от конкретной реализации, замена JSON на SQLite стала тривиальной. Студент понял: "Бизнес-логика зависит от контракта, а не от конкретного механизма хранения." Студент также освоил Dependency Injection на уровне приложения: `Inventory(repository)` получает зависимость извне через конструктор, а `main.py` (Composition Root) решает, какую конкретную реализацию передать. Студент создал три реализации одного контракта (JSON, SQLite, InMemory), доказав, что бизнес-логика не знает и не должна знать, какая именно реализация используется. Концепция закреплена на практике в проекте QR Warehouse и подтверждена архитектурными тестами.

---

### Q-0021

**Title**  
How do I separate Domain, Application, Presentation, and Infrastructure?

**Reason**  
The student needed a practical framework for deciding where each piece of code belongs. Without this framework, responsibilities drift and components accumulate unrelated reasons to change.

**Resolution**  
Студент самостоятельно сформулировал "Архитектурный фильтр" для классификации: (1) Это правило о самой сущности? → Домен. (2) Это рабочий процесс, связывающий несколько объектов или внешних систем? → Приложение / Use Case. (3) Это техническая деталь взаимодействия с внешним миром? → Инфраструктура. Студент успешно применил этот фильтр к гипотетическим требованиям: хранение в SQLite → Инфраструктура; скидка 20% на HMI_LIGHT при аренде больше 5 дней → Домен; генерация PDF и отправка по email после сохранения сметы → Use Case. Студент понял ключевое различие: Домен защищает истины (инварианты), Приложение координирует действия (рабочие процессы), Инфраструктура обеспечивает техническую поддержку (БД, файлы, сеть), Презентация переводит внешний мир на язык приложения. Концепция закреплена на практике в проекте QR Warehouse.

---

### Q-0022

**Title**  
How do I test business logic without real infrastructure (Fakes, Stubs, Mocks)?

**Reason**  
The student needed to verify that business logic works correctly without depending on real JSON files or SQLite databases. Testing against real infrastructure is slow, fragile, and makes tests depend on the environment.

**Resolution**  
Студент создал `InMemoryEquipmentRepository` как тестовый дублёр (Fake), реализующий тот же контракт `EquipmentRepository`, но хранящий данные в обычном словаре Python в оперативной памяти. Студент написал архитектурные тесты, доказывающие: успешное бронирование уменьшает доступное количество; отказ при отсутствии товара; возврат оборудования увеличивает количество. Все тесты проходят без реальных файлов и баз данных. Студент понял практическую разницу: Stub — предопределённые ответы; Fake — лёгкая рабочая реализация (InMemoryRepository); Mock — проверка взаимодействий (был ли вызван метод, с какими аргументами). Студент также понял принцип "поведение прежде взаимодействий": тесты должны доказывать значимые бизнес-результаты, а не просто проверять, что метод был вызван. Концепция закреплена на практике в проекте QR Warehouse.

---

## Mentor Responsibilities

The mentor should review this document at the beginning of every new module.

If today's lesson naturally answers one of the Open questions, the mentor should explicitly reference it.

Example:  
"This lesson answers Question Q-0002."

This helps the student connect new knowledge with previous curiosity.

---

## Student Responsibilities

The student should add new questions whenever they appear.

Questions do not need to be well written.  
Even incomplete thoughts deserve to be recorded.

Examples:

"Why?"  
"How?"  
"What if...?"

The mentor is responsible for refining them into proper engineering questions.

---

## Quality Rules

A good question is:

- specific;
- motivated by curiosity;
- connected to programming;
- possible to answer.

Poor example:  
"How does Python work?"

Better example:  
"Why are strings immutable in Python?"

---

## Long-Term Vision

Over time this document should become a map of the student's intellectual journey.

Many questions that once seemed impossible will eventually become obvious.  
New questions will replace them.

This continuous cycle of asking, understanding and applying is one of the defining characteristics of professional engineers.

---

*End of document.*
```