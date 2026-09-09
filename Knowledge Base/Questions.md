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