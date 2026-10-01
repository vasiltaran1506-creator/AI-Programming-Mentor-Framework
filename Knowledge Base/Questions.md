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

**Module 08 Progress Note:**  
The student further deepened practical understanding of SRP (splitting a single repository into `SQLEquipmentRepository` and `SQLEstimateRepository`, separating schema creation into `init_database()`, simplifying `Estimate` to a dataclass when behavior was no longer needed) and DIP (Use Cases depend on repository contracts, not concrete implementations; `Application` class wires concrete implementations at the composition root). The student also practically demonstrated Interface Segregation by keeping repository contracts minimal and focused. Formal SOLID study would now be extremely productive as the student has lived experience with at least four of the five principles.

**Module 09 Progress Note:**  
The student practically demonstrated Single Responsibility at the HTTP boundary: endpoints are pure "Translators" that only extract data, call Use Cases, and map responses — they contain no business logic or SQL. The student also demonstrated Interface Segregation by designing Pydantic models that accept only the fields needed for each specific operation (e.g., `AddItemToEstimateRequest` only contains `sku` and `quantity`, not `estimate_id` which comes from the Path). Formal SOLID study would now unify five principles with lived experience.

---

### Q-0025

**Title**  
How do relational databases store data internally, and how do query optimizers work?

**Reason**  
During Module 08, the student mastered practical SQL and schema design but explicitly expressed interest in understanding what happens "under the hood." This question was split from Q-0023 after the practical SQL portion was mastered. The student wants to understand:

- How B-trees and pages store data on disk
- How the query optimizer chooses execution plans
- Why indexes speed up reads but slow down writes
- How `EXPLAIN QUERY PLAN` works in SQLite
- The difference between SQLite, PostgreSQL, and MySQL architectures
- When to choose a relational database vs document store vs key-value store

**Related Topics**  
B-Trees  
Pages  
Query Optimizer  
EXPLAIN QUERY PLAN  
Index Internals  
SQLite Architecture  
PostgreSQL Architecture  
Database Selection Criteria

**Priority**  
Medium

**Status**  
Open

---

### Q-0026

**Title**  
How do I test thick Use Cases that coordinate multiple repositories?

**Reason**  
During Module 08, the student built six thick Use Cases that coordinate `SQLEquipmentRepository` and `SQLEstimateRepository` within transactions. However, no tests were written for the new architecture. The student needs to understand:

- How to create in-memory fakes for both repositories
- How to test transaction behavior (commit on success, rollback on failure)
- How to test Historical Snapshot (prices fixed at creation time)
- How to test multi-repository coordination (stock reservation + estimate update)
- How to test error paths (equipment not found, not enough stock, estimate not found)

**Related Topics**  
Unit Testing  
Integration Testing  
Test Doubles (Fakes, Stubs, Mocks)  
Transaction Testing  
In-Memory Repositories  
pytest fixtures

**Priority**  
High

**Status**  
Open

**Module 09 Progress Note:**  
In Module 09, the student wrote automated API tests using `pytest` and FastAPI's `TestClient`, covering both success and error paths for the HTTP endpoints. However, these are API-level tests, not Use Case unit tests. The student still needs to write unit tests for the thick Use Cases using in-memory fakes to isolate business logic from the HTTP layer. The API tests demonstrate the student's growing testing maturity, but the specific techniques for testing multi-repository coordination remain open.

---

### Q-0027

**Title**  
How would the commercial version of QR Warehouse work?

**Reason**  
During Module 08, the student described their long-term vision: "В конечном счете, когда я дойду до коммерческой реализации проекта, мне нужно будет приехать на склад, вручную записать каждую позицию в базу, присвоив ей sku, и выпустить qr-код для этого sku." The student also described the workflow for handling items without SKU: "кладовщик должен нажать кнопку 'Добавить вручную', и ввести все нужные данные." This question captures the future commercial requirements:

- QR code generation and printing for physical inventory
- Multi-user support (multiple warehouse workers scanning simultaneously)
- Mobile interface for warehouse workers (scanning QR codes)
- Manager interface for confirming estimates
- Client interface for browsing catalog and requesting estimates
- Bulk import of existing inventory (thousands of items)
- The "manual item" workflow for unregistered equipment

**Related Topics**  
QR Code Generation  
Multi-user Architecture  
Mobile Development  
Role-based Access Control  
Bulk Data Import  
Production Deployment

**Priority**  
Low

**Status**  
Open

**Module 09 Progress Note:**  
The Module 09 Web API implementation significantly advanced readiness for the commercial vision. The student now has a fully functional HTTP API with 11 endpoints covering CRUD operations for both Estimates and Equipment. This API can serve as the backend for a mobile interface (warehouse workers scanning QR codes), a manager interface (confirming estimates), and a client interface (browsing catalog). The student also independently discovered API security principles (Information Leakage prevention) and Actionable Error Responses, which are critical for a production system. The next steps for the commercial vision are: authentication/authorization, QR code generation, and production deployment.

---

### Q-0037

**Title**  
How do I deploy a FastAPI application to a production server?

**Reason**  
During Module 09, the student successfully built and tested a Web API locally using Uvicorn and Swagger UI. The student now needs to understand how to make this API accessible from the internet and handle real-world production concerns:

- How to configure Uvicorn/Gunicorn for production
- How to use environment variables for configuration (instead of hardcoded paths)
- How to set up a reverse proxy (Nginx) for HTTPS and load balancing
- How to use Docker for containerization
- How to deploy to a cloud platform (e.g., Railway, Render, AWS)
- How to manage database migrations in production
- How to set up logging and monitoring for a production API

**Related Topics**  
Production Deployment  
Uvicorn  
Gunicorn  
Nginx  
Docker  
Cloud Platforms  
Environment Variables  
Database Migrations  
Logging and Monitoring

**Priority**  
Medium

**Status**  
Open

---

### Q-0038

**Title**  
How do I implement authentication and authorization for a multi-user Web API?

**Reason**  
During Module 09, the student built a Web API that is currently open to anyone who knows the URL. For the commercial version of QR Warehouse, different users need different permissions:

- Warehouse workers can scan QR codes and update stock
- Managers can confirm estimates and apply discounts
- Clients can browse the catalog and request estimates
- Administrators can manage the equipment catalog and user accounts

The student needs to understand:

- Authentication vs Authorization (who you are vs what you can do)
- JWT tokens and session management
- Password hashing (bcrypt)
- Role-based access control (RBAC)
- How to protect specific endpoints with FastAPI dependencies
- How to store user credentials securely

**Related Topics**  
Authentication  
Authorization  
JWT Tokens  
Password Hashing  
Role-based Access Control  
FastAPI Dependencies  
Security Best Practices

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

**Module 08 Progress Note:**  
В ходе рефакторинга Module 08 студент самостоятельно принял решение перевести `Estimate` из обычного класса в `@dataclass`, распознав, что все методы класса (`add_item`, `remove_item`, `get_item_by_sku`) стали мёртвым кодом в новой архитектуре, где Use Cases координируют репозитории напрямую. Студент сформулировал это так: "Ни один метод из класса Estimate не используется нигде, потому что мы все делаем через UseCases и репозиторий. Так зачем тогда в принципе существует Estimate?" Это демонстрирует глубокое понимание того, что выбор между `@dataclass` и обычным классом зависит от архитектурного контекста, а не от фиксированного правила.

---

### Q-0009

**Title**  
How to write automated tests for business logic using pytest?

**Reason**  
The student wanted to learn how to protect business logic from regressions and ensure code correctness during refactoring.  
The student asked how to test object state transitions and edge cases automatically.

**Resolution**  
Студент освоил инструменты `pytest` для модульного тестирования. Он настроил конфигурацию тестов (`pytest.ini`), написал 11 автотестов для проверки бизнес-логики (бронирование, удаление, пересчет итогов) и научился использовать фикстуры для подготовки тестовых данных. Студент понял концепцию "красный-зеленый-рефакторинг" и успешно применил тестирование для защиты критических методов `check_and_reserve`, `add_item` и `remove_one`. Концепция закреплена на практике и все тесты успешно проходят.

**Module 09 Progress Note:**  
В ходе Module 09 студент расширил навыки тестирования на уровень HTTP API. Он написал автоматические тесты через `pytest` и `TestClient` FastAPI, покрывающие успешные и ошибочные сценарии (создание сметы, получение существующей и несуществующей сметы, невалидные данные). Студент также освоил прагматичный подход к изоляции тестовых данных: вместо сложной фабрики приложений была использована простая очистка через API в конце теста. Это демонстрирует зрелое понимание того, что тестирование может быть одновременно надёжным и простым.

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

**Module 08 Progress Note:**  
В ходе Module 08 студент самостоятельно принял решение разделить единый репозиторий на два: `SQLEquipmentRepository` (для каталога оборудования) и `SQLEstimateRepository` (для смет и позиций). Студент сформулировал это так: "Мне кажется, что в QR Warehouse нам следует сделать два репозитория для общения с нашей базой. Первый будет отвечать за equipment, а второй за estimates и estimate_items." Это демонстрирует понимание границ агрегатов: каждый репозиторий обслуживает одну концептуальную область данных. Студент также реализовал полный набор методов для обоих репозиториев, включая `find_by_sku`, `update_available`, `create_estimate`, `get_estimate`, `add_equipment_to_estimate`, `change_equipment_quantity`, `delete_equipment_from_estimate`, `delete_estimate`, и `show_all_estimates`.

---

### Q-0019

**Title**  
What are Use Cases (Application Services) and how do they differ from domain objects?

**Reason**  
The student initially confused "Use Case" with user scenarios (e.g., "using the app on Windows 10" or "working offline"). This was a terminology collision between software architecture and product management/QA contexts. The student explicitly stated: "Мне бы понять предметную суть Use Case, тогда будет проще." Additionally, the student questioned why Use Cases were needed if `main.py` already orchestrates the program, fearing an "orchestrator of orchestrators" infinite loop.

**Resolution**  
Через ментальную модель "Сотрудник МФЦ / Дирижёр" студент понял, что Use Case — это оркестратор Слоя Приложения, который координирует доменные объекты для выполнения бизнес-процесса, не зная про UI или базу данных. Через модель "Директор завода против Начальника производства" студент понял разницу между Composition Root (`main.py` — создаёт и соединяет объекты) и Use Case (выполняет бизнес-процесс внутри уже собранной системы). Студент извлёк `AddItemToEstimate` как Use Case в отдельный файл `use_cases.py`, координирующий `Inventory` и `Estimate`. Студент также проявил прагматичность: решил НЕ создавать сложные классы Use Cases, когда простые функции в `main.py` достаточны для текущего масштаба проекта, но чётко понял, КОГДА они станут обязательными (добавление Web API, email-уведомлений, нескольких точек входа). Концепция закреплена на практике в проекте QR Warehouse.

**Module 08 Progress Note:**  
В ходе Module 08 студент пережил второй концептуальный прорыв в понимании Use Cases. Первоначально студент создал "тонкие" Use Cases, которые просто проксировали вызовы к репозиториям. Затем студент задал фундаментальный вопрос: "Зачем у меня в UseCase существует класс AddToEstimate, и при этом в классе Estimate существует метод add_item. У меня есть ощущение, что функционал дублируется." Через ментальные модели "Архитектор против Строителя" и "Официант в ресторане" студент понял, что Use Cases должны быть "толстыми" координаторами: принимать сырые данные (estimate_id, sku, quantity), создавать доменные объекты (EstimateItem), проверять бизнес-правила (смета существует, оборудование существует, достаточно на складе), координировать несколько репозиториев и управлять транзакциями. Студент реализовал шесть толстых Use Cases: `CreateEstimate`, `GetEstimate`, `DeleteEstimate`, `AddItemToEstimate`, `ChangeItemQuantity`, `DeleteItemFromEstimate`. Каждый Use Case принимает примитивные параметры, возвращает строковые статусы и управляет `commit()`/`rollback()`.

---

### Q-0020

**Title**  
What is Dependency Inversion and how does it work in practice?

**Reason**  
The student needed to understand how to make stable business rules independent from unstable technical details. The initial code had `Inventory` directly storing catalog data in internal dictionaries (`self._catalog`, `self._stock`), creating tight coupling between business logic and the specific way data was loaded.

**Resolution**  
Студент пережил Dependency Inversion не как теоретический принцип SOLID, а как практический инструмент. Когда бизнес-логика (`Inventory`) стала зависеть от абстрактного контракта `EquipmentRepository`, а не от конкретной реализации, замена JSON на SQLite стала тривиальной. Студент понял: "Бизнес-логика зависит от контракта, а не от конкретного механизма хранения." Студент также освоил Dependency Injection на уровне приложения: `Inventory(repository)` получает зависимость извне через конструктор, а `main.py` (Composition Root) решает, какую конкретную реализацию передать. Студент создал три реализации одного контракта (JSON, SQLite, InMemory), доказав, что бизнес-логика не знает и не должна знать, какая именно реализация используется. Концепция закреплена на практике в проекте QR Warehouse и подтверждена архитектурными тестами.

**Module 08 Progress Note:**  
В ходе Module 08 студент применил Dependency Inversion на новом уровне: класс `Application` получает конфигурацию через конструктор и создаёт все зависимости (логгер, репозитории, Use Cases) в `__init__`. Use Cases получают репозитории и логгер через конструктор, не зная об их конкретных реализациях. `PricePolicy` передаётся в `AddItemToEstimate` после выбора пользователем, демонстрируя отложенное внедрение зависимостей. Студент также самостоятельно предложил вынести создание `AddItemToEstimate` из `_create_usecases()` в `run()`, чтобы обеспечить правильное внедрение `PricePolicy` после выбора пользователем.

---

### Q-0021

**Title**  
How do I separate Domain, Application, Presentation, and Infrastructure?

**Reason**  
The student needed a practical framework for deciding where each piece of code belongs. Without this framework, responsibilities drift and components accumulate unrelated reasons to change.

**Resolution**  
Студент самостоятельно сформулировал "Архитектурный фильтр" для классификации: (1) Это правило о самой сущности? → Домен. (2) Это рабочий процесс, связывающий несколько объектов или внешних систем? → Приложение / Use Case. (3) Это техническая деталь взаимодействия с внешним миром? → Инфраструктура. Студент успешно применил этот фильтр к гипотетическим требованиям: хранение в SQLite → Инфраструктура; скидка 20% на HMI_LIGHT при аренде больше 5 дней → Домен; генерация PDF и отправка по email после сохранения сметы → Use Case. Студент понял ключевое различие: Домен защищает истины (инварианты), Приложение координирует действия (рабочие процессы), Инфраструктура обеспечивает техническую поддержку (БД, файлы, сеть), Презентация переводит внешний мир на язык приложения. Концепция закреплена на практике в проекте QR Warehouse.

**Module 08 Progress Note:**  
В ходе Module 08 студент успешно применил Архитектурный фильтр к новой структуре проекта: `models.py` и `_estimate.py` → Домен; `_use_cases.py` → Приложение; `_repository.py` и `_database.py` → Инфраструктура; `app.py` → Composition Root / Presentation. Студент самостоятельно удалил мёртвый код из Домена (методы `add_item`, `remove_item`, `get_item_by_sku` из `Estimate`), распознав, что в новой архитектуре эти обязанности перешли к Use Cases и репозиториям. Студент также удалил класс `Inventory`, чьи обязанности были поглощены толстыми Use Cases. Это демонстрирует зрелое понимание того, что слои архитектуры не являются фиксированными — они эволюционируют по мере изменения системы.

---

### Q-0022

**Title**  
How do I test business logic without real infrastructure (Fakes, Stubs, Mocks)?

**Reason**  
The student needed to verify that business logic works correctly without depending on real JSON files or SQLite databases. Testing against real infrastructure is slow, fragile, and makes tests depend on the environment.

**Resolution**  
Студент создал `InMemoryEquipmentRepository` как тестовый дублёр (Fake), реализующий тот же контракт `EquipmentRepository`, но хранящий данные в обычном словаре Python в оперативной памяти. Студент написал архитектурные тесты, доказывающие: успешное бронирование уменьшает доступное количество; отказ при отсутствии товара; возврат оборудования увеличивает количество. Все тесты проходят без реальных файлов и баз данных. Студент понял практическую разницу: Stub — предопределённые ответы; Fake — лёгкая рабочая реализация (InMemoryRepository); Mock — проверка взаимодействий (был ли вызван метод, с какими аргументами). Студент также понял принцип "поведение прежде взаимодействий": тесты должны доказывать значимые бизнес-результаты, а не просто проверять, что метод был вызван. Концепция закреплена на практике в проекте QR Warehouse.

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
Mastered (practical portion)

**Resolution**  
Студент полностью освоил практическую часть работы с реляционными базами данных в ходе Module 08. Через мини-проект "Песочница гафера" (основанный на личном профессиональном опыте студента как гафера в киноиндустрии) и полный рефакторинг QR Warehouse студент освоил:

**Систематический SQL:** студент уверенно использует `SELECT` с `JOIN`, `WHERE`, `ORDER BY` (включая `ORDER BY CASE` для бизнес-сортировки по категориям), `INSERT INTO`, `UPDATE ... SET`, `DELETE FROM`, параметризованные запросы через `?`, `cursor.fetchone()` и `cursor.fetchall()`.

**Проектирование схем:** студент спроектировал реляционную схему из трёх таблиц (`equipment`, `estimates`, `estimate_items`) с `FOREIGN KEY` связями, `CHECK` ограничениями для бизнес-правил (неотрицательные цены, положительное количество), индексами на часто запрашиваемых колонках, и симуляцией булевых значений через `INTEGER CHECK (from_catalog IN (0, 1))`.

**Транзакции и атомарность:** студент самостоятельно сформулировал паттерн Unit of Work: "Я бы сделал так, чтобы сам репозиторий не выполнял commit(), пусть это делает та часть кода, которая отвечает за вызов репозитория." Студент реализовал атомарные транзакции с `commit()` при успехе и `rollback()` при ошибке, координируя два репозитория через одно соединение.

**Исторический снимок (Historical Snapshot):** студент самостоятельно пришёл к этому паттерну через бизнес-рассуждение: "Смета это документ, который после утверждения и хода в работу сам по себе не меняется." Цены, названия и категории копируются из каталога в `estimate_items` в момент создания позиции и никогда не изменяются.

**Обработка NULL:** студент спроектировал систему для ручных позиций без SKU (`sku TEXT` без `NOT NULL`, `from_catalog INTEGER`), основанную на реальном сценарии: "По любому произойдёт такое, что я забуду присвоить sku для какой-то маленькой штучки."

**Идемпотентное наполнение:** студент освоил `INSERT OR IGNORE` с `UNIQUE` ограничениями для безопасного повторного запуска наполнения базы.

Внутреннее устройство баз данных (B-деревья, страницы, планировщик запросов) и сравнение SQLite с PostgreSQL остаются для будущего изучения (см. Q-0025).

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
Mastered

**Module 08 Progress Note:**  
The Module 08 refactoring significantly improved readiness for this transition. The student now has thick Use Cases that accept raw data and return status strings (easily mapped to HTTP responses), an `Application` class that demonstrates lifecycle management (a web framework would replace this with its own lifecycle), and a clean separation where the CLI loop in `Application._main_loop()` is the only presentation-specific code. The six Use Cases (`CreateEstimate`, `GetEstimate`, `DeleteEstimate`, `AddItemToEstimate`, `ChangeItemQuantity`, `DeleteItemFromEstimate`) could be exposed as REST endpoints with minimal changes. The student also independently proposed the `Application` class pattern, demonstrating understanding of the composition root concept that would transfer directly to a web framework's dependency injection system.

**Resolution**  
В ходе Module 09 студент полностью ответил на этот вопрос через практику. Студент добавил `presentation/api/routes.py` как вторую точку входа, не изменив ни одной строчки в бизнес-логике (Use Cases) или инфраструктуре (репозитории). Ключевой инсайт был сформулирован через ментальную модель "Два входа в одно здание": CLI — это главный вход, HTTP API — служебный вход, оба ведут в одну и ту же кухню (Application Layer). Студент успешно запустил оба входа одновременно, разделяя одну базу данных и одни и те же Use Cases. Студент также самостоятельно перешёл от строковых статусов к структурированному паттерну `Result` (`success`, `status`, `details`), что позволило чисто отделить бизнес-результаты от HTTP-перевода. Концепция закреплена на практике в проекте QR Warehouse.

---

### Q-0028

**Title**  
How do I model multi-vendor data in a relational database?

**Reason**  
During the Gaffer Sandbox mini-project, the student needed to model equipment from multiple rental houses (vendors). The student initially proposed creating a separate table per vendor (`ACT_Equipment`, `KinoPolis_Equipment`), which would lead to schema explosion. The student asked: "Рентал номер 1 будет иметь свою собственную таблицу, например, ACT_Equipment, рентал номер 2 будет иметь свою таблицу KinoPolis_Equipment."

**Resolution**  
Через ментальную модель "Библиотека с отдельными комнатами против одной комнаты с наклейками" студент понял, что правильная модель — одна таблица `equipment` с колонкой `vendor_id` (FOREIGN KEY на таблицу `vendors`), а не отдельные таблицы для каждого поставщика. Студент понял разницу: отдельные таблицы приводят к "взрыву схемы" (нужно создавать новую таблицу для каждого нового поставщика, переписывать все запросы, делать UNION для аналитики), в то время как одна таблица с внешним ключом позволяет фильтровать по поставщику через `WHERE vendor_id = ?`, делать аналитику через `GROUP BY vendor_id`, и добавлять новых поставщиков простым `INSERT` в таблицу `vendors`. Студент также понял, что одинаковые приборы (например, Arri M90) в разных ренталах — это разные записи с разными `id`, разными `vendor_id`, разными SKU и разными ценами, но одинаковым `name`. Концепция закреплена на практике в мини-проекте "Песочница гафера".

---

### Q-0029

**Title**  
What is the Historical Snapshot pattern and when should I use it?

**Reason**  
During the Gaffer Sandbox and QR Warehouse refactoring, the student needed to ensure that confirmed estimates never change their prices, even if the equipment catalog changes. The student asked: "Что, если на, допустим, Arri M90 в рентале номер 1 цена 5000, а в рентале номер 2 цена будет 6000?" and later: "Что произойдёт со старой сметой, если рентал поднимет цены?"

**Resolution**  
Студент самостоятельно пришёл к паттерну Исторического Снимка через бизнес-рассуждение: "Смета это документ, который после утверждения и хода в работу сам по себе не меняется. Это как лист бумаги. Ты написал на нем название и цену, и больше ничего с этим сделать не можешь." Через ментальную модель "Витрина магазина против Чека на кассе" студент понял разницу между текущими ценами в каталоге (могут меняться) и зафиксированными ценами в смете (никогда не меняются). Технически это реализовано копированием `name`, `category`, `price_per_unit` из таблицы `equipment` в таблицу `estimate_items` в момент создания позиции. Поле `total_position_price` вычисляется и сохраняется при создании, фиксируя итоговую стоимость. Студент также сохранил `days_in_rent` для каждой позиции, позволяя разному оборудованию иметь разный срок аренды. Концепция закреплена на практике в проектах "Песочница гафера" и QR Warehouse.

---

### Q-0030

**Title**  
What is the Unit of Work pattern and who owns transactions?

**Reason**  
During the QR Warehouse refactoring, the student needed to coordinate two repositories (`SQLEquipmentRepository` and `SQLEstimateRepository`) within a single business operation. The student independently asked: "Я бы сделал так, чтобы сам репозиторий не выполнял commit(), пусть это делает та часть кода, которая отвечает за вызов репозитория."

**Resolution**  
Студент самостоятельно сформулировал паттерн Unit of Work до изучения его формального названия. Ключевой инсайт: репозитории только выполняют SQL-запросы, а управление транзакциями (commit/rollback) принадлежит Use Case. Студент понял проблему на конкретном примере: если `update_available()` делает `commit()` и затем `save_estimate_items()` падает с ошибкой, склад уже "заморожен" (первый commit сработал), но в смете нет позиций. Целостность нарушена. Решение: оба репозитория работают с одним `connection`, передаваемым через конструктор, и ни один из них не вызывает `commit()`. Use Case вызывает `commit()` после успешного выполнения всех операций и `rollback()` при любой ошибке. Студент реализовал это во всех шести Use Cases: `try` блок заканчивается `conn.commit()`, `except` блок начинается с `conn.rollback()`. Концепция закреплена на практике в проекте QR Warehouse.

---

### Q-0031

**Title**  
What is the difference between a Domain Entity and a Read Model?

**Reason**  
After completing the QR Warehouse refactoring in Module 08, the student noticed that the `Estimate` class had methods (`add_item`, `remove_item`, `get_item_by_sku`) that were never called anywhere in the new architecture. The student asked: "Ни один метод из класса Estimate не используется нигде, потому что мы все делаем через UseCases и репозиторий. Так зачем тогда в принципе существует Estimate? Может его сделать датаклассом?"

**Resolution**  
Студент самостоятельно распознал, что `Estimate` перестал быть Доменной Сущностью (объект с поведением, защищающий инварианты) и стал Моделью Чтения (пассивный контейнер данных для передачи из базы в интерфейс). В новой архитектуре все мутации происходят через репозитории и Use Cases, а объект `Estimate` просто загружается из базы через `get_estimate()` и передаётся в `exporter.format_estimate()` для отображения. Студент принял зрелое архитектурное решение: упростить `Estimate` до `@dataclass` с полями `estimate_id`, `project_name`, `days`, `items` и вычисляемым свойством `grand_total`. Студент также удалил мёртвые методы (`add_item`, `remove_item`, `get_item_by_sku`) и класс `Inventory`, чьи обязанности были поглощены толстыми Use Cases. Это демонстрирует понимание того, что архитектурные роли объектов эволюционируют: объект, который был Доменной Сущностью в одной архитектуре, может стать Моделью Чтения в другой. Концепция закреплена на практике в проекте QR Warehouse.

---

### Q-0032

**Title**  
What is the Application Shell pattern and how does it manage the system lifecycle?

**Reason**  
During the QR Warehouse refactoring, the student's `main.py` was growing into a monolithic function handling configuration, database initialization, repository creation, Use Case wiring, and the main interaction loop. The student independently asked: "Слушай, а я могу создать в модуле main.py класс app или application? Это имеет смысл?"

**Resolution**  
Студент самостоятельно предложил паттерн "Оболочка приложения" (Application Shell) до изучения его формального названия. Через ментальную модель "Точка входа против Ядра приложения" студент понял, что `main.py` должен быть минимальным (чтение конфига, создание `Application`, вызов `run()`), а вся логика координации должна жить в классе `Application`. Студент реализовал `Application` с `__init__` (создание логгера, соединения с БД, репозиториев, Use Cases) и `run()` (выбор ценовой политики, выбор или создание сметы, главный цикл). Студент также правильно решил создавать `AddItemToEstimate` после выбора `PricePolicy`, а не в `__init__`, демонстрируя понимание порядка внедрения зависимостей. Концепция закреплена на практике в проекте QR Warehouse.

---

### Q-0033

**Title**  
How do I handle optional fields and manual data entry in a relational database?

**Reason**  
During the QR Warehouse refactoring, the student described a real warehouse scenario: "По любому произойдёт такое, что я забуду присвоить sku для какой-то маленькой штучки, которая завалялась где-то на складе. И на такой случай у кладовщика должен быть обходной путь." The student needed to allow estimates to contain items that don't exist in the equipment catalog.

**Resolution**  
Студент спроектировал систему с `sku TEXT` (без `NOT NULL`) и `from_catalog INTEGER CHECK (from_catalog IN (0, 1))` в таблице `estimate_items`. Когда `sku` заполнен (каталожная позиция), `FOREIGN KEY` проверяет ссылку на таблицу `equipment`. Когда `sku` равен `NULL` (ручная позиция), `FOREIGN KEY` не проверяется, позволяя вставить произвольные данные. Студент понял, что это элегантное решение: `FOREIGN KEY` в SQLite пропускает проверку для `NULL` значений. Студент также описал полный рабочий процесс: кладовщик нажимает "Добавить вручную", вводит название и цену; позже, когда предмет возвращается на склад, администратор выпускает QR-код и SKU, и позиция может быть обновлена. Концепция закреплена на практике в схеме базы данных QR Warehouse.

---

### Q-0034

**Title**  
What is the Result pattern and how does it decouple business logic from HTTP translation?

**Reason**  
During Module 09, the student needed to translate business outcomes (success, equipment not found, not enough stock) into HTTP status codes (200, 404, 409). Initially, Use Cases returned raw strings or tuples, which tightly coupled business logic to specific response formats. The student needed a structured way to communicate business results without knowing about HTTP.

**Resolution**  
Студент самостоятельно спроектировал паттерн `Result` как структурированный ответ Use Case: `Result(success: bool, status: str, details: Any)`. Use Case возвращает бизнес-статус (`"success"`, `"equipment_not_found"`, `"not_enough_stock"`), а эндпоинт переводит этот статус в HTTP-код. Это позволило полностью отделить бизнес-логику от HTTP: Use Cases не знают про статус-коды, а эндпоинты не знают про бизнес-правила. Студент также самостоятельно принял решение использовать `details: Any` вместо `dict | str`, мотивируя это прагматичностью: "Мне не всегда нужно и удобно передавать словарь, иногда проще передать строку." Концепция закреплена на практике в проектах "Планировщик съёмочной группы" и QR Warehouse.

---

### Q-0035

**Title**  
How do I design secure API error responses that don't leak sensitive data?

**Reason**  
During Module 09, when designing the error response for a scheduling conflict in the Crew Scheduler, the mentor suggested returning the `conflicting_project` name. The student needed to think about what data is safe to expose to external clients.

**Resolution**  
Студент самостоятельно открыл принцип предотвращения утечки информации (Information Leakage Prevention) и минимизации данных (Data Minimization) до изучения их формальных названий. Студент отверг предложение вернуть название конфликтующего проекта: "Я решил не добавлять conflicting_project, потому что это точно не та информация, которую должен знать клиент... Если проект снимается секретно, то клиент случайно узнает его название." Студент понял, что ошибки должны быть безопасными (не раскрывать коммерческую тайну) и действенными (помогать клиенту исправить проблему). Студент также самостоятельно предложил возвращать доступные даты при конфликте: "в идеале положить сюда интервалы, в которые человек свободен" — позволяя клиенту автоматически предложить альтернативы. Концепция закреплена на практике в проекте "Планировщик съёмочной группы".

---

### Q-0036

**Title**  
How do I build a multi-entry-point architecture where CLI and HTTP API share the same business logic?

**Reason**  
During Module 09, the student needed to add a Web API to the existing QR Warehouse project without modifying the business logic. The student initially confused FastAPI with an HTTP client ("Does api.py send requests to the Use Cases?") and needed to understand that FastAPI is a server (Presentation Layer), not a client.

**Resolution**  
Через ментальную модель "Два входа в одно здание" студент понял, что веб-приложение — это не отдельная программа, которая общается с вашим приложением, а просто второй вход в то же самое здание. Студент успешно добавил `presentation/api/routes.py` как вторую точку входа, не изменив ни одной строчки в бизнес-логике (Use Cases) или инфраструктуре (репозитории). Студент также успешно разрешил технические проблемы: `sys.path` для импортов, пути к базе данных, потокобезопасность SQLite (`check_same_thread=False`). Студент запустил оба входа одновременно и убедился, что они разделяют одну базу данных. Концепция закреплена на практике в проекте QR Warehouse.

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