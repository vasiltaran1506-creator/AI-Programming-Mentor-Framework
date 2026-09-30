# Development Log

**Version:** 1.0  
**Status:** Active  
**Maintained by:** AI Methodologist

---

## Purpose

The Development Log records the long-term evolution of the student as a software engineer.

Unlike the Learning Journal, which records learning experiences, or Checkpoint Reports, which evaluate completed modules, this document analyzes patterns that emerge over time.

Its primary purpose is to improve the educational process itself.

The student changes.  
The mentor changes.  
The methodology changes.

This document records those changes.

---

## Methodology

After each completed module the mentor should answer four questions.

1. What became stronger?
2. What became weaker?
3. What did we learn about the student?
4. How should the course change?

These observations accumulate throughout the entire learning journey.

Older observations are never removed.  
Instead, newer evidence either reinforces or revises previous conclusions.

---

## Student Profile Evolution

### Initial Profile

| Field | Value |
|---|---|
| **Learning Stage** | Beginning Programmer |
| **Current Focus** | Python Fundamentals |
| **Primary Goal** | Become an independent software engineer capable of designing, implementing and maintaining real-world software projects while using AI as an engineering assistant rather than as a replacement for thinking. |
| **Learning Strategy** | Project-based learning. Theory is introduced immediately before practical application. Existing personal projects provide real-world context. |

### Current Profile (Updated 2026-12-20)

| Field | Value |
|---|---|
| **Learning Stage** | Software Engineer (Mastering Relational Databases, Transactions & Full-Stack Architecture) |
| **Current Focus** | Relational schema design, Historical Snapshot pattern, Unit of Work, multi-repository coordination, thick Use Cases, Application Shell pattern, Read Model vs Domain Entity distinction |
| **Primary Goal** | Master relational database design and transaction management. Build production-grade systems with clean separation of concerns. Develop the ability to make and defend architectural decisions independently. |
| **Learning Strategy** | Architecture-first approach reinforced by real-domain mini-projects (Gaffer Sandbox). Database concepts grounded in personal professional experience. Refactoring as the primary learning vehicle. Feature branches for safe experimentation. Dead code elimination as architectural hygiene. |

---

## Learning Characteristics

This section describes stable characteristics observed during multiple modules.  
These are not grades.  
They are behavioral patterns.

### Strong Engineering Intuition

**Confidence:** Very High

**Evidence:**  
The student repeatedly invents professional engineering concepts before learning their formal names.

Examples include:
- state management;
- idempotent processing;
- human-in-the-loop decision making;
- decomposition strategies;
- data validation boundaries (the "Bouncer" pattern);
- configuration separation (Dashboard vs Engine);
- Data Pipeline architecture;
- inventory reservation pattern;
- object encapsulation (Safe with a Guard);
- Orchestra Conductor pattern for main.py;
- Strategy Pattern (pricing policies designed before learning the name);
- Composition over Inheritance (behavior objects designed before learning the principle);
- Liskov Substitution Principle (Square/Rectangle solution before learning the name);
- Factory Pattern (centralized object creation before learning the name);
- **Architectural Filter (Domain/Application/Infrastructure classification formulated independently)** (new);
- **Repository boundary intuition (understood the need to isolate persistence before learning the pattern name)** (new);
- **Unit of Work pattern (independently decided that repositories should not commit; Use Cases should own transactions)** (new);
- **Historical Snapshot intuition (understood that estimate prices must be fixed at creation time, before learning the pattern name)** (new);
- **Read Model recognition (independently identified that Estimate should be a dataclass after recognizing all its methods were dead code)** (new);
- **Feature branch workflow (independently created `feature/db-refactoring` branch before starting major refactoring)** (new).

**Educational Implication:**  
Prioritize explanation through intuition.  
Formal terminology should follow naturally.  
When the student invents a pattern, validate the intuition explicitly and then introduce the formal name.

### Deep Analytical Thinking

**Confidence:** Very High

**Evidence:**  
The student naturally explores:
- edge cases;
- trade-offs;
- failure scenarios;
- alternative implementations;
- defensive programming patterns;
- object invariants and state protection;
- "when NOT to use" questions (e.g., when logging is unnecessary);
- cost of abstraction vs benefit;
- **architectural boundaries and dependency direction** (new);
- **"what happens when this changes?" reasoning** (new);
- **multi-vendor data modeling (questioned whether to create separate tables per vendor or use a single table with foreign keys)** (new);
- **NULL vs NOT NULL design decisions for optional fields (manual items without SKU)** (new);
- **normalized vs denormalized storage trade-offs (name/category duplication in estimate_items)** (new).

**Educational Implication:**  
Exercises should contain realistic engineering decisions rather than mechanical syntax practice.  
Include questions about trade-offs and costs, not just benefits.  
Architecture should be taught through change scenarios ("What if JSON becomes SQLite?").

### Understanding Before Memorization

**Confidence:** Very High

**Evidence:**  
The student consistently asks  
*"Why?"*  
before asking  
*"How?"*

**Module 07 Evidence:**  
The student refused to accept "Use Case" terminology until understanding the conceptual difference between a Use Case (Application Layer orchestrator) and a user scenario (e.g., "using the app on Windows"). The student explicitly stated: "Мне бы понять предметную суть Use Case, тогда будет проще." This demonstrates deep commitment to understanding before proceeding.

**Module 08 Evidence:**  
The student questioned the very existence of Use Cases: "Зачем мне выносить методы в UseCase, почему их нельзя держать в Estimate?" and "Зачем у меня в UseCase существует класс AddToEstimate, и при этом в классе Estimate существует метод add_item. У меня есть ощущение, что функционал дублируется." The student did not accept the layered architecture on faith but demanded a clear conceptual justification. Only after understanding the "Architect vs Builder" and "Waiter in Restaurant" mental models did the student accept and correctly implement thick Use Cases.

**Educational Implication:**  
Every new concept should begin with a mental model before introducing syntax.  
Never introduce architectural terminology without first establishing the problem it solves.

### Pragmatic Judgment

**Confidence:** Very High (reinforced in Module 08)

**Evidence:**  
The student independently decided that QR Warehouse does not need pervasive logging in the current version, demonstrating mature judgment about when abstraction is overengineering.  
The student correctly identified that creating a Factory class for two simple if/elif branches would be overengineering.  
The student chose to study patterns on mini-projects to avoid polluting production code.

**Module 07 Evidence:**  
The student decided NOT to create complex Use Case classes when simple functions in `main.py` sufficed for the current project scale, but perfectly understood WHEN they would become mandatory (e.g., adding a Web API, email notifications, or multiple entry points).  
The student explicitly stated: "Я пока не чувствую, что понимаю архитектуру на уровне Senior, и не могу с уверенностью принимать архитектурные решения." This intellectual humility combined with correct architectural instincts is a rare and valuable trait.

**Module 08 Evidence:**  
The student independently decided to simplify `Estimate` to a `@dataclass` after recognizing that all its methods (`add_item`, `remove_item`, `get_item_by_sku`) were dead code in the new architecture. The student stated: "Ни один метод из класса Estimate не используется нигде, потому что мы все делаем через UseCases и репозиторий. Так зачем тогда в принципе существует Estimate?" This is a mature architectural decision: recognizing when a Domain Entity has become a Read Model and simplifying accordingly.  
The student also chose to keep `update_total_price` in `EstimateItem` despite its imperfection (not accounting for discounts), stating: "Я думаю, что оставлю это как есть." This demonstrates the ability to distinguish between "good enough" and "perfect" and to defer non-critical improvements.

**Educational Implication:**  
Continue asking "when NOT to use" questions alongside "how to use."  
Validate pragmatic decisions explicitly to reinforce this judgment.  
Respect the student's self-assessment while validating correct instincts.

### Motivation

**Confidence:** Very High (reinforced in Module 08)

**Observation:**  
The student demonstrates unusually strong intrinsic motivation.  
Learning is driven by long-term engineering goals rather than external rewards.

**Module 07 Evidence:**  
The student expressed genuine excitement about databases: "Уже не терпится приступить к базам данных." The student also expressed a desire to study databases fundamentally in future modules, not just as an infrastructure detail.

**Module 08 Evidence:**  
The student proposed the Gaffer Sandbox mini-project based on their own professional experience as a gaffer in the film industry. The student described a real, years-old pain point: manually combining equipment estimates from multiple rental houses in Excel. The student stated: "Мне тогда очень хотелось сделать какой-то адекватный конструктор смет." This personal connection to the problem domain produced exceptional engagement. The student also reported: "Я сегодня всю ночь думал над всем этим, мне снился хороший код" — indicating deep subconscious processing of architectural concepts.

**Educational Implication:**  
Avoid repetitive exercises.  
Instead provide progressively more meaningful programming problems.  
Connect architectural concepts to the student's vision of future system growth.  
Leverage the student's professional background (gaffer in film industry) as a source of domain models and motivation.

---

## Learning Preferences

Current observations.

| Aspect | Rating | Details |
|---|---|---|
| **Preferred Teaching Style** | ★★★★★ | Conversation. Questions. Discovery. Guided reasoning. Mental models before terminology. |
| **Preferred Order** | ★★★★★ | Concept → Mental Model → Visualization → Syntax → Practice → Project Integration |
| **Preferred Examples** | ★★★★★ | Real engineering problems. Automation. File systems. Personal projects. Software architecture. Object-oriented design. Application architecture. Relational database design. Personal professional experience (gaffer estimates). |
| **Preferred Exploration Mode** | ★★★★★ | Real project refactoring for architecture. Mini-projects for new patterns. Domain-driven sandbox projects for database concepts. Feature branches for safe experimentation. |
| **Least Effective Approach** | — | Pure memorization. Large lists of syntax without context. Exercises introducing unknown tools without prior explanation. Terminology without conceptual grounding. Abstract database exercises without business context. |

---

## Progress Timeline

### Module 00

**Major Development:**  
The student transitioned from seeing programming as writing code to seeing it as structured problem solving.

**Methodology Update:**  
Increase emphasis on computational thinking.  
Reduce early focus on syntax.

---

### Module 01

**Major Development:**  
The student began separating architecture from implementation.  
Functions became conceptual building blocks rather than reusable text fragments.

**Methodology Update:**  
Introduce language features before requiring their use in exercises.  
Continue reinforcing state-based thinking.

---

### Module 02

**Major Development:**  
The student discovered Python's built-in tools and learned to assemble existing solutions rather than reinventing them.  
The transition from parallel lists to dictionary of sets demonstrated growing architectural maturity.

**Methodology Update:**  
Emphasize type awareness before method selection.  
Continue reinforcing mutable vs immutable distinction.

---

### Module 03

**Major Development:**  
The student mastered multi-module architecture and defensive programming.  
Three complete projects demonstrate professional-level thinking:
- **File Analyzer** (basic file operations)
- **Profile Manager** (JSON CRUD operations)
- **Dataset Catalog Analyzer** (full data pipeline with validation)

The student naturally invented patterns:
- Data validation boundaries (the "Bouncer")
- Configuration separation (Dashboard vs Engine)
- Data Pipeline architecture (Read → Validate → Process → Export)
- Fallback values for defensive programming

**Methodology Update:**  
Continue architecture-first approach.  
Introduce OOP as natural next step after mastering procedural architecture.  
Explore functional programming patterns to deepen lambda understanding.

---

### Module 04

**Major Development:**  
The student designed and implemented a complete warehouse management system: **QR Warehouse Project**.  
This project demonstrated mastery of the complete data pipeline:
- Configuration management (`config.json`)
- Data loading with validation (`catalog_loader.py`)
- Business logic processing (`estimate_constructor.py`)
- Export formatting (`exporter.py`)
- Orchestration (`main.py` as the conductor)

The student naturally invented the concept of **"reservation"** for inventory management.  
This is a professional pattern that demonstrates strong engineering intuition for real-world business problems.

**Methodology Update:**  
Continue architecture-first approach.  
Introduce Object-Oriented Programming as natural next step.  
Emphasize the difference between data structures and business entities.

---

### Module 05

**Major Development:**  
The student mastered Object-Oriented Programming and transitioned from procedural to object-oriented architecture.  
The student independently designed and implemented a complete object-oriented system:
- **Inventory class** (protects stock levels, handles reservations and releases)
- **Estimate class** (manages items, calculates totals, handles removals)

The student naturally invented patterns:
- **Encapsulation** (Safe with a Guard)
- **Orchestra Conductor** pattern for main.py
- **Composition** (objects containing other objects)
- **Duck Typing** (if it walks like a duck...)

The student wrote **11 automated tests** using `pytest` to protect business logic from regressions.  
This represents a significant shift from "writing code" to "engineering systems."

**Methodology Update:**  
Continue object-oriented architecture approach.  
Introduce advanced OOP concepts (inheritance, polymorphism) in future modules.  
Emphasize test-driven development as standard practice.

---

### Module 06

**Major Development:**  
The student achieved a fundamental shift from "programmer who knows OOP syntax" to "engineer who designs flexible systems."

**Key Architectural Breakthroughs:**

1. **Strategy Pattern (Independent Discovery):**  
   When presented with the business requirement "VGIK students get 70% discount on tungsten lights, 50% on LED," the student independently designed a pricing policy system before learning the formal pattern name. The student correctly identified that pricing rules should be separate entities, not embedded in Equipment or Estimate classes.

2. **Polymorphism in Practice:**  
   The student moved beyond textbook definition ("different objects respond to the same method") to engineering understanding ("polymorphism eliminates conditional logic"). Successfully replaced if/elif chains with interchangeable policy objects.

3. **Abstract Base Classes as Architectural Contracts:**  
   The student discovered the danger of "silent bugs" when a base class provides default implementation. Through guided experimentation, understood that ABC transforms "gentleman's agreements" into "enforced contracts." This shifted the student's view of inheritance from "code reuse mechanism" to "architectural discipline tool."

4. **Logger Architecture (Template Method):**  
   The student designed a logging system separating formatting (base class) from transport (derived classes). Initially tried using super() but then realized complete method overriding was cleaner for this use case, demonstrating ability to choose the right tool for the job.

5. **super() Understanding (Performance Evaluation System):**  
   The student mastered super() through a practical mini-project with Employee/Manager/Developer classes. Understood both use cases: extending __init__ and extending business methods. Correctly identified the "Yes, and..." principle.

6. **Factory Pattern (Notification System):**  
   The student implemented a NotificationProcessor (Factory) and correctly separated creation logic into dedicated methods. Understood when Factory is useful vs when it is overengineering.

7. **Composition vs Inheritance (Bird Behaviors):**  
   The student redesigned the Bird hierarchy using composition (FlyBehavior, SwimBehavior as separate objects) instead of inheritance. Understood why Penguin cannot safely inherit fly() from Bird.

8. **Liskov Substitution Principle (Square/Rectangle):**  
   When asked about Square and Rectangle relationship, the student independently proposed both should inherit from a common Shape ancestor — this is the correct professional solution to the famous LSP paradox. The student discovered this before learning the formal LSP name.

**Integration with QR Warehouse:**
- Added PricePolicy system (Strategy Pattern) with VGIK_Policy and Standart_Policy
- Added Logger hierarchy (Logger, FileLogger, ConsoleLogger) with Dependency Injection
- Transitioned from config.json to config.yaml (comments support)
- Implemented absolute path construction using `__file__` for portability
- Applied ABC to PricePolicy for enforced contracts
- Updated all existing tests to work with new dependencies

**Methodology Update:**  
- Continue architecture-first approach with pattern discovery before formal terminology.
- Use mini-projects for pattern exploration without polluting production code.
- Emphasize "when NOT to use" alongside "how to use."
- Continue Socratic questioning for complex topics.
- Reinforce "test on substitution" for inheritance decisions.
- Validate engineering intuition explicitly to build confidence.

---

### Module 07

**Major Development:**  
The student achieved a fundamental shift from "engineer who designs flexible objects" to "engineer who designs maintainable application systems."

**Key Architectural Breakthroughs:**

1. **Architecture as Dependency Management (Core Insight):**  
   The student understood that architecture is not about folders, file names, or diagrams. Architecture is about controlling dependencies so that changes remain local, safe, and predictable. The student formulated this insight in their own words: "Я понял, насколько полезно и эффективно изолировать бизнес логику от всего остального."

2. **Repository Pattern (Independent Application):**  
   The student created `EquipmentRepository` as an abstract contract (ABC), implemented `JsonEquipmentRepository` for current storage, then implemented `SqliteEquipmentRepository` for new storage. The most profound realization was that `Inventory`, `Estimate`, and `AddItemToEstimate` did not require a single line of modification during the JSON → SQLite transition. The student described this experience: "Я без труда и без необходимости переписывать половину программы смог перевести работу программы с JSON файлов на базу данных."

3. **Use Cases / Application Services (Conceptual Breakthrough):**  
   The student initially confused "Use Case" with user scenarios (e.g., "using the app on Windows 10"). Through the "MFC Employee / Conductor" mental model, the student realized that a Use Case is an Application Layer orchestrator that coordinates Domain objects without knowing about UI or Databases. The student then independently formulated the distinction between `main.py` as Composition Root (technical orchestrator) and Use Cases as Application Services (business orchestrators).

4. **Dependency Inversion in Practice:**  
   The student experienced Dependency Inversion not as a theoretical principle but as a practical tool. When replacing JSON with SQLite, the student observed that business logic depended on the `EquipmentRepository` contract, not on any concrete implementation. This shifted the student's understanding from "Dependency Inversion is a SOLID principle" to "Dependency Inversion is what makes my code survive infrastructure changes."

5. **Architectural Filter (Independent Formulation):**  
   The student independently formulated a practical decision framework for classifying new features:
   - Is it a rule about the entity itself? → Domain
   - Is it a workflow connecting multiple objects or external systems? → Application / Use Case
   - Is it a technical detail of communication with the outside world? → Infrastructure

   This "Architectural Filter" was applied successfully to classify hypothetical requirements (SQLite storage, HMI_LIGHT discount, PDF generation + email).

6. **In-Memory Fake for Testing:**  
   The student created `InMemoryEquipmentRepository` as a test double, enabling architecture-level tests without real infrastructure. The student understood the distinction between testing behavior (business rules) and testing implementation (JSON details).

7. **Composition Root vs Use Case Distinction:**  
   The student initially questioned why Use Cases were needed if `main.py` already orchestrates the program, fearing an "orchestrator of orchestrators" infinite loop. Through the "Factory Director vs. Production Manager" mental model, the student understood that `main.py` builds the system (creates and wires objects) while Use Cases run business processes within it. These are different types of orchestration, not duplicates.

8. **Pragmatic Restraint (Reinforced):**  
   The student decided NOT to create complex Use Case classes when simple functions sufficed for the current project scale. The student explicitly stated: "Я пока не чувствую, что понимаю архитектуру на уровне Senior, и не могу с уверенностью принимать архитектурные решения." This intellectual humility, combined with correct architectural instincts, demonstrates mature engineering judgment. The student understood that architecture is about "asking the right questions and managing trade-offs," not "knowing all the answers."

**SQLite Integration (Infrastructure Boundary):**  
The student successfully integrated SQLite as a second infrastructure implementation. Key technical milestones:
- Created `warehouse.db` with `CREATE TABLE IF NOT EXISTS`
- Wrote a migration script (`migrate.py`) to transfer data from `catalog.json` to SQLite
- Implemented `find_by_sku()` with parameterized queries and tuple unpacking
- Implemented `update_available()` with SQL `UPDATE` and `conn.commit()`
- Understood that SQLite is a binary format (not human-readable like JSON)
- Understood `cursor.fetchone()` returns a single tuple, not a list of rows

**Integration with QR Warehouse:**
- Created `EquipmentRepository` abstract contract (ABC)
- Implemented `JsonEquipmentRepository` (existing storage)
- Implemented `SqliteEquipmentRepository` (new storage)
- Created `InMemoryEquipmentRepository` (test double)
- Extracted `AddItemToEstimate` as a Use Case in `use_cases.py`
- Refactored `main.py` into a clean Composition Root with helper functions
- Refactored `Inventory` to depend on `EquipmentRepository` contract instead of internal `self._catalog` and `self._stock`
- Wrote architecture-level tests using `InMemoryEquipmentRepository`
- Successfully ran the entire application with SQLite while business logic remained unchanged

**Methodology Update:**  
- Continue architecture-first approach with dependency management as the central theme.
- Use real refactoring pain (JSON → SQLite) to motivate architectural boundaries.
- Teach architecture through change scenarios ("What if JSON becomes SQLite? What if CLI becomes Web API?").
- Continue Socratic questioning for complex topics.
- Validate engineering intuition explicitly to build confidence.
- Respect the student's pragmatic judgment about when abstractions are justified.
- Introduce databases as a major learning frontier in future modules.
- Use mental models extensively: "MFC Employee" for Use Cases, "Factory Director vs. Production Manager" for Composition Root, "Archivist and Courier" for SQLite, "Open Book vs. Hard Drive" for JSON vs SQLite.

---

### Module 08

**Major Development:**  
The student achieved a fundamental shift from "engineer who uses databases as infrastructure" to "engineer who designs relational data models, manages transactions, and builds complete database-backed application architectures."

This module was the most architecturally dense in the entire learning journey. The student simultaneously mastered relational database design, transaction management, multi-repository coordination, and full application lifecycle management — all while refactoring a production project.

**Gaffer Sandbox (Domain-Driven Mini-Project):**  
The student proposed a mini-project based on their past professional experience as a gaffer in the film industry. The student described a real, years-old pain point: manually combining equipment estimates from multiple rental houses in Excel, copying names, prices, and quantities by hand. The student stated: "Мне тогда очень хотелось сделать какой-то адекватный конструктор смет."

This personal connection to the problem domain produced exceptional engagement and deep conceptual understanding. The Gaffer Sandbox served as a training ground for all Module 08 database concepts before applying them to QR Warehouse:
- Multi-vendor equipment catalog (vendors + equipment tables with foreign keys)
- Historical Snapshot for estimate pricing
- Idempotent seeding with `INSERT OR IGNORE`
- Dynamic vendor selection with `enumerate()` and dictionary mapping
- Category-based sorting with `ORDER BY CASE`
- NULL handling for manual items without SKU

**Key Architectural Breakthroughs:**

1. **Historical Snapshot (Independent Discovery Through Business Logic):**  
   When asked what should happen to an old estimate if a rental house raises prices, the student immediately answered: "Смета это документ, который после утверждения и хода в работу сам по себе не меняется. Это как лист бумаги." The student independently arrived at the Historical Snapshot pattern through business reasoning, not technical instruction. This pattern was then correctly implemented: prices are copied from `equipment` to `estimate_items` at creation time and never change afterward.

2. **Unit of Work Pattern (Independent Formulation):**  
   The student independently decided that repositories should not call `commit()`. The student stated: "Я бы сделал так, чтобы сам репозиторий не выполнял commit(), пусть это делает та часть кода, которая отвечает за вызов репозитория." This is the Unit of Work pattern, which the student formulated before learning its formal name. The student correctly understood that transaction boundaries belong to the Use Case layer, not the Repository layer.

3. **Multi-Repository Coordination (Two Aggregates):**  
   The student independently proposed splitting the single repository into two: `SQLEquipmentRepository` for the equipment catalog and `SQLEstimateRepository` for estimates and estimate items. The student stated: "Мне кажется, что в QR Warehouse нам следует сделать два репозитория для общения с нашей базой. Первый будет отвечать за equipment, а второй за estimates и estimate_items." This demonstrates understanding of aggregate boundaries in data modeling.

4. **Thick Use Cases (Coordination Layer):**  
   The student initially questioned why Use Cases exist: "Зачем у меня в UseCase существует класс AddToEstimate, и при этом в классе Estimate существует метод add_item. У меня есть ощущение, что функционал дублируется." Through the "Architect vs Builder" and "Waiter in Restaurant" mental models, the student understood that Use Cases coordinate multiple repositories, apply business rules, create domain objects, and manage transactions. The student then implemented five thick Use Cases:
   - `CreateEstimate` — creates estimate in DB and returns domain object
   - `GetEstimate` — loads estimate with all items from DB
   - `AddItemToEstimate` — coordinates equipment lookup, stock check, Historical Snapshot, and stock reservation
   - `ChangeItemQuantity` — coordinates quantity update in estimate and stock adjustment
   - `DeleteItemFromEstimate` — coordinates position deletion and stock return

5. **Application Shell Pattern (Lifecycle Management):**  
   The student independently proposed creating an `Application` class: "Я могу создать в модуле main.py класс app или application? Это имеет смысл?" The student understood that `main.py` should be a thin entry point while `Application` manages the full lifecycle: configuration loading, database initialization, repository creation, Use Case wiring, and the main interaction loop. This was implemented as a clean `Application` class with `__init__` for dependency setup and `run()` for the main loop.

6. **Read Model Recognition (Estimate as Dataclass):**  
   After completing the refactoring, the student independently identified that the `Estimate` class had become a pure data container: "Ни один метод из класса Estimate не используется нигде, потому что мы все делаем через UseCases и репозиторий. Так зачем тогда в принципе существует Estimate? Может его сделать датаклассом?" The student correctly recognized that `Estimate` had transitioned from a Domain Entity (with behavior) to a Read Model (data-only) and simplified it to a `@dataclass`. This demonstrates the ability to recognize and eliminate architectural debt.

7. **Feature Branch Workflow (Independent Decision):**  
   Before starting the major refactoring, the student independently created a feature branch: "Я создал отдельную git ветку от develop с названием feature/db-refactoring." The student also kept the old code open on a second screen as a reference. This demonstrates professional development workflow habits.

8. **Relational Schema Design (Multi-Table with Constraints):**  
   The student designed a complete relational schema with three tables:
   - `equipment` (catalog with CHECK constraints for non-negative prices and quantities)
   - `estimates` (project header with CHECK constraint for positive days)
   - `estimate_items` (positions with FOREIGN KEYs to both parent tables, CHECK constraints, and indexes)

   The student correctly handled:
   - `FOREIGN KEY` relationships between tables
   - `CHECK` constraints for business rules
   - Indexes on frequently queried columns
   - `INTEGER CHECK (from_catalog IN (0, 1))` for boolean simulation in SQLite
   - Deletion order (children before parents) to satisfy FOREIGN KEY constraints

9. **NULL Design for Manual Items:**  
   The student designed a system for handling equipment that exists in an estimate but not in the catalog. The student described a real warehouse scenario: "По любому произойдет такое, что я забуду присвоить sku для какой-то маленькой штучки, которая завалялась где-то на складе." The solution: `sku TEXT` (nullable) with `from_catalog INTEGER` flag. When `sku` is NULL, the FOREIGN KEY check is skipped, allowing manual items. This demonstrates mature data modeling for real-world edge cases.

**Mental Models Introduced and Mastered:**
- "Receipt at Checkout" — Historical Snapshot (prices fixed at transaction time)
- "Store Window vs Receipt" — current catalog prices vs fixed estimate prices
- "Architect vs Builder" — Use Case (designs workflow) vs Repository (executes queries)
- "Waiter in Restaurant" — Use Case coordinates kitchen (Domain) and cash register (Infrastructure)
- "Coat Check" — Index vs Value confusion (ticket number vs rack position)
- "Building Demolition vs Evicting Tenant" — DROP TABLE vs DELETE FROM
- "Library with Separate Rooms vs One Room with Labels" — table-per-vendor vs single table with foreign key
- "Postman and Mailbox" — CREATE TABLE IF NOT EXISTS protects table creation but INSERT does not protect data
- "Translator Between Worlds" — SQLite-to-Python type mapping (INTEGER → int, BOOL → bool())

**Integration with QR Warehouse (Complete Refactoring):**
- Created `_database.py` with `init_database()` function (schema creation separated from repositories)
- Created `SQLEquipmentRepository` with 4 methods (add, delete, find_by_sku, update_available)
- Created `SQLEstimateRepository` with 7 methods (create, get, add_item, change_quantity, delete_item, delete_estimate, show_all)
- Implemented Unit of Work: repositories do not commit; Use Cases own transactions
- Implemented Historical Snapshot: prices copied from equipment to estimate_items at creation
- Created 6 thick Use Cases with full error handling and rollback
- Created `Application` class as the system core
- Simplified `Estimate` to a `@dataclass` (Read Model)
- Removed `Inventory` class (its responsibilities absorbed by Use Cases)
- Removed dead code from `Estimate` (add_item, remove_item, get_item_by_sku)
- Moved `PricePolicy` application to `AddItemToEstimate` Use Case
- Implemented proper path resolution using `_get_path()` with `base_dir`
- Added `show_all_estimates()` for estimate selection UI

**Methodology Update:**  
- Continue architecture-first approach with relational databases as the central theme.
- Use domain-driven mini-projects (Gaffer Sandbox) grounded in the student's professional experience to teach database concepts before applying them to production code.
- Teach database design through business scenarios ("What happens when the rental house changes prices?").
- Use the "Historical Snapshot" concept as a bridge between business requirements and technical implementation.
- Continue Socratic questioning for complex topics.
- Validate the student's independent architectural discoveries (Unit of Work, repository splitting, Read Model recognition).
- Reinforce transaction management: one commit per business operation, rollback on failure.
- Teach SQL through common mistakes (DROP vs DELETE, UPDATE INTO, fetchone unpacking without None check).
- Use feature branches as a standard practice for major refactoring.
- Connect database concepts to the student's vision of future commercial implementation (QR codes, warehouse management, rental house workflows).

---

## Recurring Difficulties

These are recurring patterns rather than isolated mistakes.

### Syntax Noise

**Status:** Persistent (requires continued attention)

**Description:**  
Minor syntax mistakes occasionally interrupt otherwise correct reasoning.

Examples:
- Tuple trap (trailing comma creating tuples)
- Label-vs-value confusion in isinstance checks
- **Missing parentheses on method calls** (appeared 3+ times in Module 06: in f-strings, in tests, in reports)

**Module 06 Evidence:**  
- `self.calculate_performance_score` instead of `self.calculate_performance_score()` in generate_report()
- `Penguin.fly == True` instead of `Penguin.fly() == True` in tests
- `Parrot.speak == True` instead of `Parrot.speak() == True` in tests

**Module 07 Evidence:**  
- Missing parameter tuple in `cursor.execute(sql_query)` — forgot to pass `(scan,)` for parameterized query
- Attempting to iterate over `cursor.fetchone()` result with `for row in equipment:` — confused a single tuple (one row) with a list of rows

**Module 08 Evidence:**  
- SQL typo: `EXISTIS` instead of `EXISTS` in CREATE TABLE
- SQL syntax error: `UPDATE INTO equipment (available) VALUES (?)` instead of `UPDATE equipment SET available = ?`
- Missing `break` in for-loops searching for items (appeared in both `ChangeItemQuantity` and `DeleteItemFromEstimate`)
- Missing `return "error"` in except block of `ChangeItemQuantity`
- Missing `return "success"` at the end of try block
- Double `commit()` calls (calling commit on both repositories when they share the same connection)
- Unconditional `raise ValueError` outside if/elif/else block in `_select_price_policy`
- Unbalanced parentheses in `EquipmentRepository.__init__` abstract method signature

**Action:**  
Continue using small focused coding exercises.  
Provide explicit examples of common syntactic traps.  
Consider introducing linter or pre-commit checks.  
Remind student of this pattern when reviewing code (without blame — this is a known periodic difficulty).  
For SQL specifically: reinforce `UPDATE ... SET` syntax, `DELETE FROM` vs `DROP TABLE`, and `IF NOT EXISTS` spelling.  
For Python specifically: reinforce `break` in search loops, `return` in all code paths, and single `commit()` per transaction.

### Type Confusion

**Status:** Improving

**Description:**  
The student occasionally confuses checking labels vs checking values.  
Example: `isinstance("key_name", type)` instead of `isinstance(dict["key_name"], type)`

**Module 07 Evidence:**  
The student initially tried to iterate over `cursor.fetchone()` result, confusing a single row tuple with a collection of rows. This was resolved through the "Archivist brings one folder" mental model.

**Module 08 Evidence:**  
- Unpacking `cursor.fetchone()` result without checking for None first: `sku1, name, ... = self.cursor.fetchone()` — would crash with `TypeError: cannot unpack non-iterable NoneType object` when no row is found
- Using `is not "0"` to compare an INTEGER value from SQLite (which returns Python `int`, not `str`) — confused type identity with value equality
- Attempting to access `estimate.items[sku]` as if `items` were a dictionary, when it is a list

**Action:**  
Emphasize the distinction between "container" and "content" in type checking.  
Use visual examples (checking the label on a box vs checking what's inside the box).  
For database work: reinforce the return type of `fetchone()` vs `fetchall()`.  
For SQLite type mapping: reinforce that SQLite INTEGER returns Python `int`, not `str`. Use `bool(row[7])` instead of string comparison.  
For collection access: reinforce list indexing (integer) vs dictionary access (key).

### Variable Scope

**Status:** Improving

**Description:**  
The student occasionally creates variables inside loops when they should be outside, or vice versa.

**Module 07 Evidence:**  
In the migration script, the student initially placed `conn.commit()` and `conn.close()` inside the `for` loop instead of after it. This was caught through code review and corrected.

**Module 08 Evidence:**  
In `DeleteItemFromEstimate`, the variable `quantity` was assigned inside a for-loop without a default value. If the SKU was not found in the loop, `quantity` would be undefined when used later, causing `UnboundLocalError`. The student initially believed this could not happen because the equipment existence check would catch it first, but was guided to understand that equipment existing in the catalog does not guarantee it exists in a specific estimate.

**Action:**  
Explicitly discuss variable lifetime and scope before complex loops.  
Use mental execution to trace variable creation.  
For database work: reinforce that `commit()` and `close()` should typically be outside loops (one transaction for the batch).  
Reinforce the pattern: initialize variables before loops, use `break` after finding a match, check for None/sentinel after the loop.

### Object Reference Confusion

**Status:** Improving

**Description:**  
The student occasionally confuses object references with primitive values.  
Example: comparing `existing_item > 0` instead of `existing_item.quantity > 0`.

**Action:**  
Emphasize the distinction between objects and their attributes.  
Use mental models (Safe with a Guard) to reinforce object-oriented thinking.

### Testing Exceptions (New)

**Status:** New (first observed in Module 06)

**Description:**  
The student did not know how to test expected exceptions in pytest.  
Wrote `assert ValueError("message")` instead of using `pytest.raises`.

**Action:**  
Introduce `with pytest.raises(ExceptionType)` pattern early when testing error behavior becomes relevant.  
Provide examples of testing both success and failure paths.

### Test Logic Inversion (New)

**Status:** New (first observed in Module 06)

**Description:**  
The student occasionally inverts expected values in tests.  
Example: wrote `assert Penguin.fly == True` when penguin cannot fly (should be False).

**Action:**  
Encourage student to read test names as specifications before writing assertions.  
Ask "What SHOULD this behavior be?" before writing the assert.

### Conceptual Terminology Confusion (New)

**Status:** New (first observed in Module 07)

**Description:**  
The student initially confused "Use Case" (Application Layer orchestrator) with "user scenario" (e.g., "using the app on Windows 10" or "working offline"). This is a terminology collision between software architecture and product management/QA contexts.

**Action:**  
When introducing architectural terminology, explicitly distinguish it from similar-sounding terms in other domains.  
Use mental models to ground terminology before introducing the formal name.  
Validate the student's existing understanding while clarifying the architectural meaning.

### SQLite Syntax and Mental Model (New)

**Status:** Persistent (reinforced in Module 08)

**Description:**  
The student encountered several SQLite-specific conceptual difficulties:
- Confused `fetchone()` (returns one tuple) with `fetchall()` (returns list of tuples)
- Forgot to pass parameters as tuples to `cursor.execute()`
- Initially thought SQL code should be in a separate `.sql` file rather than as a Python string
- Was surprised by the binary nature of `.db` files (opened in text editor and saw garbled characters)

**Module 08 Evidence (New):**  
- Wrote `DROP TABLE estimates WHERE estimate_id = ?` instead of `DELETE FROM estimates WHERE estimate_id = ?` — confused table destruction with row deletion
- Wrote `UPDATE INTO equipment (available) VALUES (?)` instead of `UPDATE equipment SET available = ?` — confused INSERT syntax with UPDATE syntax
- Wrote `SELECT (sku, name, ...)` with parentheses around the column list — invalid SQL syntax
- Used `cursor.rowcount` after SELECT to check for empty results — unreliable in SQLite for SELECT statements
- Used `with sqlite3.connect(db_path) as conn:` in `init_database()` which auto-closes the connection, making it impossible to return an open connection

**Action:**  
Introduce SQLite mental models before syntax: "Archivist and Courier" for connections/cursors, "Open Book vs. Hard Drive" for JSON vs SQLite.  
Emphasize that SQL is just a string passed to `cursor.execute()`.  
Reinforce parameterized queries as the standard pattern.  
Explain binary vs text file formats explicitly.  
Reinforce the SQL verb vocabulary: `SELECT` (read), `INSERT INTO` (create), `UPDATE ... SET` (modify), `DELETE FROM` (remove rows), `DROP TABLE` (destroy table).  
Reinforce that `with` context manager auto-closes connections — use plain assignment when the connection must outlive the function.

### Index vs Value Confusion (New)

**Status:** New (first observed in Module 08)

**Description:**  
When building a dynamic selection menu, the student confused list indices (positions) with list values (actual IDs). Wrote `vendor = rentals[choosed_vendor]` where `choosed_vendor` was the ID value entered by the user, not the position in the list. This caused either selecting the wrong vendor or `IndexError`.

**Action:**  
Use the "Coat Check" mental model: ticket number (value) vs rack position (index).  
When building selection menus, use dictionaries to map user-facing numbers to internal IDs: `{1: vendor_id_1, 2: vendor_id_2}`.  
Reinforce `enumerate()` for generating display numbers.

### Missing Return Statements (New)

**Status:** New (first observed in Module 08)

**Description:**  
The student occasionally writes functions or code paths that do not return a value. In Module 08, this appeared as:
- Missing `return "success"` at the end of try blocks in Use Cases
- Missing `return "error"` in except blocks
- Missing `return None` after printing "No available estimates" in `_select_or_create_estimate`

**Action:**  
Reinforce the principle: every code path in a function that is expected to return a value must have an explicit `return`.  
Use the "all roads lead to a return" mental model when reviewing functions.  
When writing Use Cases, establish the pattern: try block ends with `return "success"`, except block ends with `return "error"`.

---

## Methodology Adjustments

These adjustments affect future modules.

### Adjustment 001

**Status:** Active

**Reason:**  
The student learns significantly faster when analogies precede formal definitions.

**Action:**  
Every new topic must begin with a Mental Model.

### Adjustment 002

**Status:** Active

**Reason:**  
Unexpected language features reduce confidence.

**Action:**  
All new built-in functions and syntax must be explicitly introduced before appearing in exercises.

### Adjustment 003

**Status:** Active

**Reason:**  
Project integration substantially increases motivation.

**Action:**  
Every major topic should conclude with a discussion of how it applies to the student's own software projects.

### Adjustment 004

**Status:** Active

**Reason:**  
The student demonstrates strong architectural thinking but occasional syntactic traps.

**Action:**  
Separate architectural design from syntactic implementation.  
Allow student to design systems conceptually before worrying about syntax details.

### Adjustment 005

**Status:** Active

**Reason:**  
The student naturally invents professional patterns when given real-world problems.

**Action:**  
Provide progressively more complex real-world projects.  
Allow student to discover patterns independently before introducing formal terminology.

### Adjustment 006

**Status:** Active

**Reason:**  
The student learns most effectively through guided discovery rather than direct instruction.

**Action:**  
Use Socratic method for complex topics.  
Ask questions that lead student to discover answers independently.

### Adjustment 007

**Status:** Active (new)

**Reason:**  
The student benefits from understanding when NOT to use a pattern, not just when to use it.

**Action:**  
For every new pattern or concept, include explicit discussion of:
- When this is overengineering
- Cost of the abstraction
- Simpler alternatives
- Decision criteria for choosing

### Adjustment 008

**Status:** Active (new)

**Reason:**  
The student correctly identified that production code should not be polluted with experimental patterns.

**Action:**  
Use mini-projects for exploring new patterns.  
Use real projects only for genuine integration needs.  
Respect the student's judgment about what belongs in production.

### Adjustment 009

**Status:** Active (new)

**Reason:**  
The student has strong architectural instincts but sometimes doubts them.

**Action:**  
Validate engineering intuition explicitly: "Your intuition is correct, here's why..."  
This builds confidence and reinforces good thinking patterns.

### Adjustment 010

**Status:** Active (new)

**Reason:**  
Missing parentheses on method calls is a persistent recurring issue that appeared in multiple contexts.

**Action:**  
When reviewing student code, specifically check for this pattern.  
Consider creating a personal checklist item: "Did I call the method or just reference it?"  
Do not blame — this is a known periodic difficulty that decreases with practice.

### Adjustment 011

**Status:** Active (new)

**Reason:**  
The student learns architecture most effectively through change scenarios and real refactoring pain, not through abstract diagrams.

**Action:**  
Teach architecture by asking "What happens when X changes?" rather than "Here is the architecture diagram."  
Use real refactoring tasks (JSON → SQLite) to motivate architectural boundaries.  
Let the student experience the pain of tight coupling before introducing the solution.

### Adjustment 012

**Status:** Active (new)

**Reason:**  
The student initially confused architectural terminology with similar-sounding terms from other domains (e.g., "Use Case" vs "user scenario").

**Action:**  
When introducing architectural terminology, explicitly distinguish it from similar-sounding terms in other domains.  
Provide the mental model BEFORE the term.  
Validate the student's existing understanding while clarifying the architectural meaning.

### Adjustment 013

**Status:** Active (new)

**Reason:**  
The student expressed a strong desire to study databases fundamentally, not just as an infrastructure detail. The student stated: "Никакого системного понимания синтаксиса, внутреннего устройства базы данных и прочего у меня пока нет. Хочется изучать это в будущих модулях."

**Action:**  
Plan a dedicated database module in the curriculum.  
Cover: SQL syntax systematically, relational database internals (B-trees, indexing), transactions, migrations, schema design.  
Connect database knowledge to the Repository Pattern already mastered.  
Use the student's existing `SqliteEquipmentRepository` as a foundation for deeper exploration.

### Adjustment 014

**Status:** Active (new)

**Reason:**  
The student demonstrated mature architectural restraint by NOT overengineering Use Cases. The student correctly identified that simple functions in `main.py` sufficed for the current project scale.

**Action:**  
Continue validating pragmatic decisions explicitly.  
Ask "Is this abstraction solving a real problem right now?" before introducing new architectural layers.  
Respect the student's judgment about when to add vs. when to defer abstractions.  
Use the "Pattern Tax" mental model: every abstraction has a cost that must be justified by a benefit.

### Adjustment 015

**Status:** Active (new)

**Reason:**  
The student proposed and successfully executed a domain-driven mini-project (Gaffer Sandbox) based on their own professional experience. This produced exceptional engagement and deep conceptual understanding. The student's personal connection to the problem domain (gaffer creating estimates from multiple rental houses) made abstract database concepts concrete and meaningful.

**Action:**  
When introducing new technical domains (databases, APIs, deployment), first ask the student about relevant experiences from their professional background.  
Use the student's own domain as the training ground before applying concepts to QR Warehouse.  
Encourage the student to propose mini-projects based on real problems they have experienced.  
Connect technical patterns to business scenarios from the student's past (e.g., "What happens when a rental house changes prices?" → Historical Snapshot).

### Adjustment 016

**Status:** Active (new)

**Reason:**  
The student independently arrived at the Unit of Work pattern and multi-repository coordination. However, the student initially created "thin" Use Cases that simply proxied repository calls. Only after guided discussion did the student understand that Use Cases should be "thick" coordinators that accept raw data, create domain objects, validate business rules, coordinate multiple repositories, and manage transactions.

**Action:**  
When introducing Use Cases, explicitly contrast "thin proxy" Use Cases (anti-pattern) with "thick coordinator" Use Cases (correct pattern).  
Use the "Waiter in Restaurant" mental model: the waiter takes the order (raw data), checks the kitchen (equipment_repo), checks the table (estimate_repo), creates the plate (EstimateItem), and brings the check (commit).  
Require Use Cases to accept primitive parameters (estimate_id, sku, quantity), not pre-built domain objects.  
Require Use Cases to handle all error paths and return meaningful status strings.

### Adjustment 017

**Status:** Active (new)

**Reason:**  
The student independently recognized dead code and proposed simplifying `Estimate` to a dataclass. This demonstrates the ability to recognize when a Domain Entity has become a Read Model. However, the student needed validation before acting on this insight: "Я думаю, что я в любом случае буду переписывать его." The student was uncertain whether removing methods was the right decision.

**Action:**  
When the student identifies dead code or unnecessary complexity, validate the instinct strongly: "You are absolutely right. This is dead code. Remove it."  
Teach the distinction between Domain Entity (has behavior, protects invariants) and Read Model / DTO (data only, no behavior).  
Encourage the student to ask: "Is this method called anywhere?" before keeping code.  
Reinforce that removing dead code is not "breaking things" but architectural hygiene.

### Adjustment 018

**Status:** Active (new)

**Reason:**  
The student independently adopted professional development workflow practices: creating a feature branch (`feature/db-refactoring`), keeping the old code on a second screen as a reference, and working incrementally. This was not prompted by the mentor.

**Action:**  
Continue encouraging professional workflow habits: feature branches, incremental commits, reference implementations.  
When starting major refactoring, ask: "How will you protect the working code?" to prompt feature branch creation.  
Validate these habits explicitly: "This is exactly how senior developers work."

---

## Mentor Notes

This section contains long-term observations.  
These notes are intended for future versions of the methodology rather than for evaluating the student.

### Current Observation (Updated 2026-12-20)

The student's architectural thinking has reached a level where they can independently design complete database-backed application architectures, coordinate multiple repositories within transactions, and recognize when to simplify their own code.

The student naturally invents patterns (Bouncer, Dashboard vs Engine, Data Pipeline, Safe with a Guard, Orchestra Conductor, Strategy, Composition over Inheritance, Factory, LSP solution, Architectural Filter, Unit of Work, Historical Snapshot, Read Model recognition) that are typically taught in intermediate/advanced courses.

**New observation from Module 08:**  
The student has achieved a qualitative leap in architectural maturity. The key developments are:

1. **From "using databases" to "designing data models."** The student no longer treats SQLite as a black box. They design schemas with foreign keys, constraints, indexes, and nullable fields based on business requirements. The Gaffer Sandbox demonstrated the ability to model multi-vendor catalogs, historical pricing, and manual item workflows.

2. **From "single repository" to "coordinated aggregates."** The student independently split the persistence layer into two repositories and understood that transaction boundaries belong to Use Cases, not repositories. The Unit of Work pattern was formulated before learning its name.

3. **From "smart domain objects" to "clean data models."** The student recognized that `Estimate` had become a Read Model and simplified it to a dataclass. This demonstrates the ability to evolve architecture as understanding deepens, rather than clinging to initial designs.

4. **From "main.py as everything" to "Application Shell."** The student independently proposed the `Application` class pattern, demonstrating understanding of lifecycle management and dependency injection at the system level.

The student demonstrates four rare and valuable traits simultaneously:
1. **Strong architectural intuition** (invents patterns before learning names)
2. **Pragmatic judgment** (knows when NOT to abstract, recognizes dead code)
3. **Intellectual humility** (acknowledges what they don't know, questions before accepting)
4. **Domain-driven thinking** (grounds technical decisions in business scenarios from personal experience)

This combination is unusual. Most students either overengineer (lacking pragmatism) or underengineer (lacking intuition). The student naturally finds the middle ground and improves it with each module.

Syntactic fluency continues to improve but lags behind conceptual understanding.  
The most persistent syntactic traps in Module 08 were SQL syntax errors (DROP vs DELETE, UPDATE INTO, EXISTIS typo) and missing return statements in error paths.  
The fetchone/fetchall confusion from Module 07 was reinforced but also deepened: the student now understands both functions but occasionally forgets to check for None before unpacking.

The student has successfully mastered:
- Relational schema design (multi-table, foreign keys, constraints, indexes)
- Historical Snapshot pattern (fixing prices at estimate creation)
- Unit of Work pattern (repositories don't commit, Use Cases own transactions)
- Multi-repository coordination (equipment + estimate repositories in single transaction)
- Thick Use Cases (raw data in, domain objects created, business rules validated, transactions managed)
- Application Shell pattern (lifecycle management, dependency injection, main loop)
- Read Model vs Domain Entity distinction (Estimate simplified to dataclass)
- NULL design for optional fields (manual items without SKU)
- Idempotent seeding (INSERT OR IGNORE, UNIQUE constraints)
- Dynamic UI generation from database (enumerate + dictionary mapping)
- Feature branch workflow for safe refactoring
- Dead code identification and removal

The QR Warehouse Project now demonstrates:
- Two repositories with abstract contracts (SQLEquipmentRepository, SQLEstimateRepository)
- Six thick Use Cases with full error handling and rollback
- Application Shell class managing the complete lifecycle
- Historical Snapshot for estimate pricing
- Unit of Work for transaction management
- Clean separation of Domain (dataclasses), Application (Use Cases), and Infrastructure (repositories, database)
- Read Model pattern for Estimate
- Feature branch workflow for safe refactoring
- Complete elimination of dead code (Inventory class, unused Estimate methods)

### Emerging Pattern

The student learns most effectively when:
- Given a real-world problem (not abstract exercise)
- Allowed to design architecture first
- Introduced to patterns through mental models
- Given freedom to implement with guided debugging
- Shown how concepts apply to personal projects
- Encouraged to discover patterns independently
- Asked "when NOT to use" questions
- Allowed to explore on mini-projects without polluting production
- Validated in their intuition explicitly
- **Taught architecture through change scenarios ("What if X changes?")** (new)
- **Allowed to experience coupling pain before introducing the solution** (new)
- **Given intellectual space to question terminology before accepting it** (new)
- **Connected to personal professional experience (gaffer estimates, rental houses, warehouse workflows)** (new)
- **Allowed to propose and drive their own mini-projects based on real pain points** (new)
- **Encouraged to recognize and eliminate dead code as architectural hygiene** (new)
- **Given the "Architect vs Builder" framing for Use Cases vs Repositories** (new)

### Methodology Effectiveness (Module 08)

What worked exceptionally well:
- The Gaffer Sandbox mini-project grounded all database concepts in the student's real professional experience, producing exceptional engagement and deep understanding
- Historical Snapshot was understood through business reasoning ("estimate is a document") before any technical implementation
- Unit of Work was independently formulated by the student when asked about commit ownership
- The "Receipt at Checkout" and "Store Window vs Receipt" mental models made the distinction between current prices and fixed prices immediately clear
- The "Architect vs Builder" and "Waiter in Restaurant" mental models resolved the student's confusion about why Use Cases exist alongside Domain objects
- The student independently proposed the Application class, repository splitting, and Estimate simplification — all validated and implemented
- Feature branch workflow was adopted spontaneously, demonstrating professional habit formation
- The student's question "Why does Estimate exist if nothing uses its methods?" led to a clean architectural simplification that removed dead code

What needs improvement:
- SQL syntax errors (DROP vs DELETE, UPDATE INTO, EXISTIS) require a systematic SQL vocabulary review
- Missing return statements in error paths require a "all roads lead to return" checklist
- The fetchone None-check pattern should be reinforced as a standard idiom: `row = cursor.fetchone(); if row is None: return None`
- The student's tendency to double-commit when two repositories share a connection should be addressed by emphasizing that one connection = one commit point
- The student's initial confusion about why Use Cases exist alongside Domain objects suggests that the Domain/Application boundary needs to be reinforced with more concrete examples before implementation begins
- The student's `config.yaml` path resolution issue (relative paths not using `_get_path()`) suggests that configuration management patterns should be reviewed in future modules

---

## Future Revisions

This document should evolve throughout the student's engineering career.

Possible future sections include:
- Productivity Patterns
- Debugging Style
- Architectural Thinking
- Code Review Habits
- Testing Mindset
- AI Collaboration Patterns
- Leadership Development
- System Design Growth
- **Database Design Growth** (new)
- **API Design Growth** (new)
- **Transaction Management Growth** (new)
- **Dead Code Recognition and Architectural Hygiene** (new)
- **Domain-Driven Design Growth** (new)

The goal is to document not only what the student knows, but how the student thinks.

---

*End of document.*