# Module 07 — Application Architecture & Software Design

**Framework:** AI Programming Mentor Framework (APMF)  
**Stage:** 2 — Python Application Foundations / Architecture Transition  
**Prerequisites:** Module 00, Module 01, Module 02, Module 03, Module 04, Module 05, Module 06  
**Primary language:** Python 3  
**Teaching language:** English  
**Estimated difficulty:** Intermediate+ → Advanced Foundations  
**Estimated workload:** ~18 hours (expected range: 15–22 hours)  
**Primary project:** QR Warehouse architectural refactoring  
**Module type:** Guided architecture and design practice

---

# Module Overview

The previous modules gradually moved the student through several levels of software design:

```text
Module 02
Data + Functions
        ↓
Module 03
Modules + Program Structure
        ↓
Module 04
Components + Contracts + Testing
        ↓
Module 05
Objects + State + Behavior
        ↓
Module 06
Relationships + Polymorphism + Abstraction
        ↓
Module 07
Application Architecture + System Boundaries
```

Module 06 marked an important transition.

The student learned that good design is not about collecting classes, inheritance hierarchies, or design patterns. The real skill is identifying relationships, defining contracts, keeping responsibilities coherent, and choosing the least unnecessarily complex abstraction.

Module 07 continues that same philosophy at a larger scale.

The central question changes from:

> **How should I design this class or component?**

to:

> **How should the components of an entire application depend on and communicate with one another?**

This module introduces application architecture as a practical engineering skill.

It does **not** attempt to teach every architectural style, every enterprise pattern, or every backend framework. The goal is smaller and more important:

> **Learn to recognize architectural boundaries, control dependencies, isolate business rules from infrastructure, and make large programs easier to change.**

---

# Core Principle

> **Architecture is the arrangement of responsibilities, boundaries, and dependencies that determines how safely a system can change.**

A good architecture is not necessarily the one with the most layers.

It is the one that makes important changes understandable and local.

The student should repeatedly ask:

```text
What responsibility does this component own?

What does it need from other components?

What does it know about them?

Which direction does the dependency point?

Can I change the infrastructure without rewriting business rules?

Can I test the core behavior without starting the whole application?

Is this abstraction solving a real problem?
```

---

# What This Module Is NOT

This module intentionally does not turn into a survey course on every architecture term.

Do not treat the following as core material in this module:

- microservices;
- Kubernetes;
- distributed systems;
- event sourcing;
- CQRS in depth;
- Domain-Driven Design in full depth;
- Clean Architecture in full formalism;
- Hexagonal Architecture as a memorization exercise;
- dependency injection frameworks;
- advanced web frameworks;
- cloud infrastructure;
- database administration;
- asynchronous architecture in depth.

These subjects become much easier to understand later because the student will first have a solid grasp of boundaries, responsibilities, and dependencies.

The module may mention larger architectural ideas when useful, but the student is not expected to master them yet.

---

# Learning Goals

By the end of Module 07, the student should be able to:

1. explain what software architecture means in practical terms;
2. distinguish architecture from folder structure or file organization;
3. identify responsibilities and boundaries between components;
4. recognize when a component has too many responsibilities;
5. explain Separation of Concerns at application scale;
6. distinguish domain logic, application logic, and infrastructure concerns;
7. understand the purpose of architectural layers;
8. recognize the difference between inward and outward dependencies;
9. explain Dependency Inversion in practical terms;
10. use Dependency Injection without relying on a framework;
11. understand the purpose of Repository-style abstractions;
12. separate persistence concerns from domain behavior;
13. understand the purpose of application services / use cases;
14. distinguish a domain object from an application workflow;
15. test business behavior without requiring real infrastructure;
16. distinguish a fake, stub, and mock at a practical level;
17. use test doubles only when they provide a clear engineering benefit;
18. refactor a growing application without changing its behavior;
19. identify architectural coupling;
20. recognize common forms of dependency leakage;
21. make trade-offs between simple and elaborate designs;
22. resist overengineering while still recognizing real architectural problems;
23. explain why a chosen architecture is appropriate for the problem;
24. apply these ideas to the QR Warehouse project;
25. independently review a small application and identify its architectural weaknesses.

The strongest completion criterion is not the ability to repeat the names of patterns.

It is the ability to say:

> **"This component owns this responsibility, it depends on this contract, and I chose this boundary because it makes this kind of change safer."**

---

# Methodological Context

The student has already learned several principles that this module will reuse rather than re-teach from scratch:

### From Module 03

- modules and imports;
- separation of responsibilities;
- configuration and data boundaries;
- validation;
- exceptions;
- filesystem and JSON I/O.

### From Module 04

- pure functions and side effects;
- explicit inputs and outputs;
- dependency awareness;
- contracts;
- dependency injection;
- business logic vs I/O;
- reusable components;
- type hints;
- dataclasses;
- pytest;
- refactoring.

### From Module 05

- objects as meaningful domain entities;
- ownership of state;
- encapsulation;
- object responsibilities;
- composition;
- object collaboration.

### From Module 06

- interfaces;
- `ABC` and `@abstractmethod`;
- polymorphism;
- duck typing;
- Strategy;
- Factory;
- Template Method;
- Dependency Injection + polymorphism;
- Liskov Substitution Principle;
- architectural trade-offs;
- avoiding unnecessary abstraction.

Module 07 should therefore feel like a **synthesis**, not a reset.

---

# Central Mental Model

A useful first model for this module is:

```text
                 APPLICATION

   ┌─────────────────────────────────────┐
   │                                     │
   │       What the system does           │
   │                                     │
   │   use cases / workflows / rules      │
   │                                     │
   └──────────────────┬──────────────────┘
                      │
                      │ depends on
                      ↓
             stable contracts
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
     DATABASE                   FILES
     HTTP API                   QR scanner
     GUI / CLI                  external services
```

The outer world changes frequently.

The important business rules should change less frequently.

Architecture is partly the art of preventing unstable details from infecting stable logic.

---

# Learning Sequence

The module follows this progression:

```text
Problem
  ↓
Responsibilities
  ↓
Boundaries
  ↓
Dependencies
  ↓
Layers
  ↓
Contracts
  ↓
Repositories
  ↓
Use Cases
  ↓
Test Doubles
  ↓
Refactoring
  ↓
Architecture Review
```

Do not skip directly to the final architecture.

The student should experience the problems that motivate each boundary.

---

# Section I — What Is Software Architecture?

## 1.1. Architecture Is About Relationships

A beginner often thinks architecture means:

```text
src/
├── models/
├── services/
├── utils/
└── main.py
```

That is file organization.

It may reflect architecture, but it is not architecture by itself.

Two projects can have identical folder structures while having completely different dependency relationships.

A more useful definition is:

> **Software architecture describes the major responsibilities, boundaries, and dependencies that shape the behavior and evolution of a system.**

For example:

```text
CLI → Service → Database
```

is an architectural relationship.

The exact filenames are secondary.

---

## 1.2. Architecture Becomes Visible Through Change

One of the best ways to inspect architecture is to ask what happens when requirements change.

Imagine an application that stores warehouse equipment in JSON files.

Requirement:

> Replace JSON with PostgreSQL.

In a tightly coupled application, the change may touch:

```text
models
business logic
CLI
validation
tests
configuration
```

In a better-separated design, the change may be mostly isolated to:

```text
infrastructure/
    json_repository.py
        ↓
    postgres_repository.py
```

while the business logic continues to operate against the same contract.

This is one of the most useful architectural tests:

> **What parts of the system must change when a particular external detail changes?**

---

## 1.3. Architecture Is Also About Cost of Change

A system does not need to be perfect.

It needs to be economically maintainable.

Consider two designs.

### Design A

```text
main.py
└── everything
```

Very little structure.

Easy to start.

Difficult to grow.

### Design B

```text
presentation
application
 domain
infrastructure
ports
adapters
factories
configuration
```

Very structured.

But potentially excessive for a 200-line script.

The correct answer depends on the problem.

This leads to a fundamental principle:

> **Architecture should be proportional to complexity.**

---

# Exercise 1 — Architecture From Change

Imagine three changes:

1. JSON storage becomes SQLite.
2. CLI becomes a web API.
3. The warehouse adds a second inventory source.

For each change, answer:

```text
Which component should ideally change?
Which components should remain unchanged?
Why?
```

Do not write code yet.

The objective is to develop architectural thinking before implementation.

---

# Section II — Responsibilities and Boundaries

## 2.1. Responsibility Is Not the Same as Action

A function may perform an action without owning the responsibility behind it.

For example:

```python
save_equipment(equipment)
```

The function performs saving.

But who owns the responsibility for deciding **whether the equipment should be saved**?

That may belong elsewhere.

This distinction becomes increasingly important as systems grow.

---

## 2.2. A Component Should Have a Coherent Reason to Change

Consider:

```python
class WarehouseManager:
    def scan_qr(self):
        ...

    def validate_equipment(self):
        ...

    def connect_to_database(self):
        ...

    def create_html_response(self):
        ...

    def calculate_rental_price(self):
        ...
```

Technically, this can work.

Architecturally, the class has several unrelated reasons to change:

```text
QR scanner changes
validation rules change
database changes
UI changes
pricing rules change
```

This creates coupling.

A better architecture asks:

> **What should this component be responsible for, and what should it deliberately not know?**

---

## 2.3. Boundary Thinking

A useful boundary says:

> "You can ask me for this result, but you do not need to know how I produce it."

For example:

```text
RentalService
    │
    │ asks for equipment
    ↓
EquipmentRepository
```

The service does not need to know whether the repository uses:

- JSON;
- SQLite;
- PostgreSQL;
- an in-memory dictionary.

The boundary hides the implementation detail.

---

# Exercise 2 — Responsibility Mapping

Given these responsibilities:

```text
Read QR scanner input
Find equipment by ID
Check whether enough equipment is available
Reserve stock
Save reservation
Format result for user
Print result
```

Group them into sensible responsibilities.

A good answer should produce several components, not one giant manager class.

Then explain why each responsibility belongs where you placed it.

---

# Section III — Separation of Concerns at Application Scale

## 3.1. The Principle

Separation of Concerns means keeping different kinds of decisions separate so that changes in one concern do not unnecessarily affect others.

At the function level, you have already used this idea:

```text
read file
    ↓
parse data
    ↓
validate data
    ↓
perform business logic
    ↓
format output
```

At application scale, the same idea becomes:

```text
Presentation
    ↓
Application
    ↓
Domain
    ↓
Infrastructure
```

These names are not magical.

What matters is the separation of concerns they represent.

---

## 3.2. Presentation

Presentation is how the outside world communicates with the application.

Examples:

- CLI;
- GUI;
- HTTP API;
- command handler;
- web frontend integration.

Presentation should translate external input into something the application understands.

It should not contain the entire business process.

Bad example:

```python
if request.method == "POST":
    data = request.json
    # 200 lines of rental business logic
    # database calls
    # validation
    # formatting
```

Better:

```python
command = CreateRentalCommand(...)
result = create_rental.execute(command)
return to_http_response(result)
```

The handler coordinates translation.

It does not become the business engine.

---

## 3.3. Application Layer

The application layer coordinates meaningful system actions.

Examples:

```text
RegisterEquipment
RentEquipment
ReturnEquipment
FindEquipment
CreateEstimate
```

These are not necessarily domain entities.

They describe **things the system does**.

This distinction becomes important later.

---

## 3.4. Domain Layer

The domain layer contains concepts and rules that describe the problem being solved.

Examples for QR Warehouse:

```text
Equipment
Inventory
Rental
Estimate
```

Examples of domain rules:

```text
stock cannot become negative
an item cannot be rented when unavailable
an estimate total equals the sum of its items
```

These rules should ideally not depend directly on a specific UI or database implementation.

---

## 3.5. Infrastructure Layer

Infrastructure deals with technical details outside the core business rules.

Examples:

```text
JSON files
SQLite
PostgreSQL
filesystem
QR scanner driver
HTTP client
email provider
clock
```

Infrastructure is often replaceable.

That does not mean it is unimportant.

It means its technical details should not leak unnecessarily into the core domain.

---

# Mental Model — The Outer World

Think about the application like this:

```text
         HUMAN / WEB / DEVICE
                 │
                 ↓
          PRESENTATION
                 │
                 ↓
          APPLICATION
                 │
                 ↓
             DOMAIN
                 │
                 ↓
          INFRASTRUCTURE
                 │
                 ↓
         FILES / DB / APIs
```

The lower layers handle details.

The upper layers express intent.

The domain should not need to know whether a command came from a web request or a CLI call.

---

# Exercise 3 — Layer Sorting

Place each item into the most appropriate architectural area:

```text
PostgreSQL connection
Equipment class
HTTP request parser
RentEquipment use case
Inventory invariant
JSON repository
CLI command parsing
Rental entity
SQL query
HTTP response formatting
```

Then identify any item whose placement is debatable.

Architecture often involves judgment rather than a single mechanically correct answer.

---

# Section IV — Dependency Direction

## 4.1. Dependencies Are Arrows

Whenever one component uses another component, there is a dependency.

For example:

```python
class RentalService:
    def __init__(self, database):
        self.database = database
```

`RentalService` depends on `database`.

Represent this as:

```text
RentalService → Database
```

Architecture becomes easier to reason about when you explicitly draw these arrows.

---

## 4.2. Why Dependency Direction Matters

Imagine:

```text
Business Logic → PostgreSQL
```

The business logic now knows about a specific database implementation.

Changing databases becomes harder.

Instead, we can introduce a stable abstraction:

```text
Business Logic → Repository Contract ← PostgreSQL Implementation
```

Now the business logic depends on what it needs rather than on the concrete technical mechanism.

---

## 4.3. Dependency Inversion

Dependency Inversion can be explained without memorizing SOLID terminology.

The practical idea is:

> **Stable business rules should not be forced to depend directly on unstable technical details. Both can depend on an abstraction whose contract expresses the needed behavior.**

For example:

```text
                 EquipmentRepository
                        ▲
                        │
              ┌─────────┴─────────┐
              │                   │
        JSONRepository      SQLRepository

                ▲
                │
          RentalService
```

`RentalService` does not care which repository implementation is used.

---

# Section V — Dependency Injection Revisited

## 5.1. Module 04 Connection

In Module 04, dependency injection was introduced as a way to make dependencies explicit.

Module 07 expands that idea from individual functions/classes to architecture.

Instead of:

```python
class RentalService:
    def __init__(self):
        self.repository = PostgreSQLRepository()
```

prefer:

```python
class RentalService:
    def __init__(self, repository):
        self.repository = repository
```

Construction happens outside the service.

The service receives what it needs.

---

## 5.2. Why This Helps

Dependency Injection provides:

```text
explicit dependency
        ↓
replaceable implementation
        ↓
testable component
        ↓
less coupling
```

For tests:

```python
service = RentalService(InMemoryEquipmentRepository())
```

For production:

```python
service = RentalService(PostgresEquipmentRepository(...))
```

The use case can stay unchanged.

---

## 5.3. Do Not Turn DI Into Ceremony

Dependency Injection does not require:

- a framework;
- a service container;
- decorators everywhere;
- abstract classes for every object.

Passing an object into a constructor is already dependency injection.

Example:

```python
class ReportService:
    def __init__(self, repository):
        self.repository = repository
```

Simple explicit dependency injection is often enough.

---

# Exercise 4 — Find the Dependency Leak

Consider:

```python
class RentalService:
    def rent(self, equipment_id):
        db = sqlite3.connect("warehouse.db")
        row = db.execute(
            "SELECT quantity FROM equipment WHERE id = ?",
            (equipment_id,)
        ).fetchone()

        if row is None:
            raise ValueError("Equipment not found")

        if row[0] <= 0:
            raise ValueError("Equipment unavailable")

        db.execute(
            "UPDATE equipment SET quantity = quantity - 1 WHERE id = ?",
            (equipment_id,)
        )
```

Identify at least four responsibilities that have become coupled together.

Then describe a better dependency direction before writing code.

---

# Section VI — Domain, Application, and Infrastructure

## 6.1. The Three-Layer Mental Model

For this module, use the following conceptual split:

```text
Domain
    What is true about the problem?

Application
    What does the system do?

Infrastructure
    How does the system communicate with the outside world?
```

Presentation can be treated as the external delivery mechanism around the application layer.

---

## 6.2. Domain Example

A domain rule might be:

```python
class Inventory:
    def reserve(self, quantity):
        if quantity > self.available:
            raise ValueError("Not enough stock")
        self.available -= quantity
```

This rule should not need to know whether the inventory came from:

```text
PostgreSQL
JSON
HTTP
memory
```

That information belongs elsewhere.

---

## 6.3. Application Example

An application service could coordinate several domain operations:

```text
RentEquipment
    ↓
find equipment
    ↓
check availability
    ↓
reserve stock
    ↓
create rental record
    ↓
save changes
```

The application layer is concerned with the workflow.

The domain objects remain responsible for their own rules.

---

## 6.4. Infrastructure Example

A repository implementation may contain:

```python
class SqlEquipmentRepository:
    def get_by_id(self, equipment_id):
        ...

    def save(self, equipment):
        ...
```

It knows about SQL.

That is exactly why it belongs at the infrastructure boundary.

---

# Section VII — Repository Pattern

## 7.1. The Problem

Suppose your application uses:

```python
json.load(...)
```

throughout the business logic.

Then every business operation knows how the storage works.

For example:

```text
RentEquipment
   ↓
json.load()
json.dump()
```

This creates persistence coupling.

---

## 7.2. Repository as a Boundary

A Repository provides a domain-oriented interface to persistence.

Conceptually:

```text
Business Logic
      ↓
EquipmentRepository
      ↓
Persistence implementation
```

The application asks:

```python
get_by_id(id)
save(equipment)
remove(id)
```

rather than:

```python
SELECT ...
json.load(...)
open(...)
```

---

## 7.3. Repository Contract

An interface may look like:

```python
from abc import ABC, abstractmethod


class EquipmentRepository(ABC):
    @abstractmethod
    def get_by_id(self, equipment_id):
        pass

    @abstractmethod
    def save(self, equipment):
        pass
```

The exact methods depend on the real use cases.

Do not design a giant generic repository automatically.

---

## 7.4. Repository Is Not a Universal Solution

For a tiny script, a repository abstraction may be needless complexity.

For a growing application whose business logic should survive a storage change, it can be very useful.

The decision should be based on:

```text
How likely is storage to change?
How many use cases depend on it?
How difficult is it to test without the real storage?
Does persistence logic leak into business rules?
```

---

# Exercise 5 — Design a Repository

Design a minimal repository interface for equipment management.

Requirements:

```text
Find equipment by ID
List equipment
Save equipment
Delete equipment
```

Do not create a repository for every domain object yet.

First explain:

1. why the repository exists;
2. what knowledge it hides;
3. what the application actually needs from it;
4. which methods are genuinely necessary.

Only then write the interface.

---

# Section VIII — Application Services and Use Cases

## 8.1. Domain Object vs Use Case

A domain object represents a concept.

A use case represents an action the application performs.

Example:

```text
Equipment
    = thing in the domain

RentEquipment
    = action performed by the system
```

This distinction helps avoid giant manager classes.

---

## 8.2. Use Case as a Workflow Boundary

A use case may coordinate several collaborators:

```text
RentEquipment
      │
      ├── EquipmentRepository
      ├── RentalRepository
      └── Clock
```

The use case expresses the workflow.

The collaborators provide capabilities.

---

## 8.3. A Use Case Should Have a Clear Contract

For example:

```python
class RentEquipment:
    def __init__(self, equipment_repository, rental_repository):
        self.equipment_repository = equipment_repository
        self.rental_repository = rental_repository
```

It might expose:

```python
execute(equipment_id, customer_id)
```

The exact naming is not important.

The important part is that the use case has a coherent responsibility.

---

## 8.4. Use Cases Should Not Become Mini-Frameworks

A use case does not need:

- six layers of wrappers;
- generic command buses;
- event systems;
- dependency containers;
- dozens of abstractions.

Start with the smallest object that expresses the workflow clearly.

---

# Exercise 6 — Extract a Use Case

Take this process:

```text
User scans a QR code.
System finds equipment.
System checks availability.
System reserves one unit.
System records the rental.
System returns a result.
```

Design the use case boundary.

Answer:

```text
What enters the use case?
What collaborators does it require?
What should it return?
What should it not know about?
```

Do this before coding.

---

# Section IX — Domain Rules vs Application Workflow

This distinction is central to the module.

Consider:

> "Equipment quantity cannot become negative."

That is a domain rule.

Consider:

> "When the customer rents equipment, first load the equipment, then reserve it, then create the rental record."

That is an application workflow.

A useful mental model is:

```text
Domain
    protects truths

Application
    coordinates actions
```

The layers interact, but they are not the same thing.

---

## 9.1. Why This Matters

If business rules are scattered through controllers, repository implementations, and UI code, changes become dangerous.

For example:

```text
CLI contains stock rule
API contains stock rule
Database procedure contains stock rule
GUI contains stock rule
```

Now one rule exists in four places.

That is a duplication problem at the architecture level, not merely at the code level.

---

# Exercise 7 — Classify the Rule

Classify each statement as primarily:

```text
Domain Rule
Application Workflow
Infrastructure Detail
Presentation Concern
```

Statements:

1. An equipment item cannot have negative stock.
2. Read the scanner's keyboard input.
3. Use PostgreSQL to save an equipment record.
4. After a successful rental, create a rental record.
5. Return HTTP 404 when equipment does not exist.
6. An estimate total equals the sum of its items.
7. Parse a JSON file.

Explain any ambiguous cases.

---

# Section X — The Repository and Domain Boundary

A common mistake is to create domain objects that know too much about persistence.

For example:

```python
class Equipment:
    def save_to_postgres(self):
        ...
```

This mixes domain and infrastructure responsibilities.

A stronger separation is:

```text
Equipment
    = domain concept

EquipmentRepository
    = persistence contract

PostgresEquipmentRepository
    = infrastructure implementation
```

This is one of the clearest examples of abstraction serving a real purpose.

---

# Section XI — Testable Architecture

## 11.1. The Goal

The goal of architectural testing is not to test every layer independently just because the layers exist.

The goal is to make important behavior testable without unnecessary environmental setup.

For example:

```text
RentEquipment
    ↓
Fake Repository
```

You can test the rule without:

- starting PostgreSQL;
- creating real files;
- using a real scanner;
- launching a GUI.

---

## 11.2. In-Memory Fake

A simple fake repository might use a dictionary:

```python
class InMemoryEquipmentRepository:
    def __init__(self, equipment):
        self.items = {item.id: item for item in equipment}

    def get_by_id(self, equipment_id):
        return self.items.get(equipment_id)

    def save(self, equipment):
        self.items[equipment.id] = equipment
```

This is often extremely useful in tests.

Notice that it behaves like a repository without being a real database.

---

## 11.3. Stub vs Fake vs Mock

The distinctions are practical.

### Stub

A stub provides predetermined answers.

```text
"When asked for equipment 42, return this object."
```

### Fake

A fake is a lightweight working implementation.

```text
InMemoryEquipmentRepository
```

### Mock

A mock is usually used to verify interactions:

```text
Was save() called?
Was it called once?
Was this exact argument passed?
```

The student only needs a practical understanding at this stage.

Do not turn test doubles into a separate career specialty.

---

## 11.4. Behavior Before Interaction

Prefer tests that prove meaningful outcomes.

For example:

```text
Given available stock,
when the customer rents one item,
then available stock decreases by one.
```

This is usually stronger than a test whose primary purpose is:

```text
repository.save was called exactly once
```

Interaction tests have their place, but they should not replace behavior-oriented tests.

---

# Section XII — Architectural Test Strategy

The student should distinguish several levels of testing.

```text
Domain tests
    ↓
Use-case tests
    ↓
Integration tests
    ↓
End-to-end tests
```

For Module 07, focus mostly on the first three.

### Domain Tests

Fast tests of business rules.

### Use-Case Tests

Test workflows with fakes or simple doubles.

### Integration Tests

Verify that infrastructure implementations actually connect correctly to the real persistence mechanism.

Do not attempt to replace integration tests with mocks everywhere.

---

# Exercise 8 — Test the Architecture

Design tests for a `RentEquipment` use case.

At minimum cover:

```text
successful rental
unknown equipment
insufficient stock
persistence behavior
```

Decide which tests use:

```text
real domain objects
in-memory fakes
real infrastructure
```

Explain why.

---

# Section XIII — Architectural Coupling

## 13.1. What Is Coupling?

Coupling describes how strongly one component depends on another component's details.

Some coupling is necessary.

A system with zero dependencies would not do anything useful.

The engineering goal is not:

> eliminate all coupling.

It is:

> **control coupling and place it deliberately.**

---

## 13.2. Stable vs Unstable Details

Examples of relatively unstable details:

```text
UI framework
web framework
SQL schema
filesystem format
third-party API
scanner driver
```

Examples of comparatively stable concepts:

```text
rent equipment
return equipment
stock cannot be negative
estimate total
```

Good boundaries help prevent unstable details from spreading into stable logic.

---

## 13.3. Dependency Leakage

Dependency leakage happens when an outer technical concern becomes visible in an inner business abstraction without a real reason.

Examples:

```python
class Inventory:
    def load_from_postgres(...):
        ...
```

or:

```python
class RentEquipment:
    def execute(self):
        return jsonify(...)
```

or:

```python
class EquipmentRepository:
    def create_http_response(...):
        ...
```

Each component has knowledge from another concern.

This makes changes travel farther through the system.

---

# Section XIV — Refactoring Toward Architecture

Architecture is often discovered by refactoring rather than designed perfectly at the beginning.

Suppose the project begins as:

```text
main.py
    ↓
JSON
```

Then grows:

```text
main.py
    ↓
WarehouseManager
    ↓
JSON
```

Then more features are added and `WarehouseManager` becomes enormous.

The response should not be:

> "Create fifteen classes."

Instead:

```text
identify responsibilities
        ↓
identify changing concerns
        ↓
identify stable rules
        ↓
extract coherent boundaries
        ↓
introduce contracts only where useful
        ↓
move dependencies outward
        ↓
run tests
        ↓
repeat
```

---

## 14.1. Refactoring Rule

> **Make one architectural improvement at a time and keep behavior stable.**

This is where the testing knowledge from Module 04–06 becomes extremely important.

Without tests, architectural refactoring becomes guesswork.

With tests, you can separate:

```text
"Did behavior change?"

from

"Did structure change?"
```

---

# Exercise 9 — Refactor a Monolith on Paper

Imagine this class:

```python
class WarehouseManager:
    def scan_qr(self):
        ...

    def load_json(self):
        ...

    def save_json(self):
        ...

    def find_equipment(self):
        ...

    def reserve(self):
        ...

    def create_rental(self):
        ...

    def format_cli_output(self):
        ...
```

Design a migration plan.

Do not rewrite everything at once.

Your plan should identify:

```text
first extraction
second extraction
contract introduction
final dependency direction
```

Explain why your sequence is safe.

---

# Section XV — Presentation as an Adapter

A CLI and an HTTP API may perform the same business action.

For example:

```text
CLI                HTTP API
 │                     │
 └────────┬────────────┘
          ↓
    RentEquipment
          ↓
       Domain
```

The external interface changes.

The use case does not necessarily have to change.

This teaches an important architectural idea:

> **Different interfaces can be different entry points into the same application behavior.**

---

## 15.1. Translation Boundary

Presentation should usually translate:

```text
external representation
        ↓
application input
        ↓
use case
        ↓
application result
        ↓
external representation
```

For example:

```text
HTTP JSON
    ↓
Python command object
    ↓
RentEquipment
    ↓
result
    ↓
HTTP JSON response
```

The business logic does not need to know that JSON or HTTP existed.

---

# Section XVI — Architecture Without Frameworks

It is important to understand the architecture before using a framework.

A framework may give you:

```text
routing
dependency injection
request objects
database tooling
serialization
```

But it does not automatically give you good architecture.

A badly designed application can exist inside any framework.

The student should therefore be able to express the architecture using plain Python first.

Only later should a framework provide infrastructure around those ideas.

---

# Section XVII — Trade-offs and Simplicity

## 17.1. Every Boundary Has a Cost

Adding a layer creates:

- another abstraction;
- another file;
- another name;
- another place to navigate;
- another concept the programmer must understand.

Therefore:

> **Abstractions are not free.**

A repository may reduce persistence coupling, but it also introduces an interface and an implementation boundary.

A use-case object may improve workflow clarity, but it may be unnecessary for a tiny function.

The correct question is:

> **Does the benefit of this boundary exceed its cognitive and maintenance cost?**

---

## 17.2. Signals That an Abstraction May Be Justified

A new boundary is more likely to be useful when:

```text
multiple components share the same contract
an implementation may change
business logic should be isolated from infrastructure
repeated coupling is causing pain
testing is difficult because of an external dependency
one component has multiple unrelated reasons to change
```

These are signals, not laws.

---

## 17.3. Signals That You May Be Overengineering

Be cautious when:

```text
there is only one simple implementation
there is no realistic variation
the abstraction adds indirection without hiding complexity
you are naming patterns before identifying a problem
the code is harder to understand after the refactor
```

A good architecture review should be able to remove abstractions as well as add them.

---

# Mental Model — Pattern Tax Is Real

Every pattern introduces a cost:

```text
pattern
  ↓
new names
  ↓
new files
  ↓
new indirection
  ↓
new mental overhead
```

The benefit must be greater than the tax.

This continues the lesson from Module 06:

> **Do not abstract because you can. Abstract because the system benefits from it.**

---

# Section XVIII — QR Warehouse Architecture

This module's main practical objective is to revisit the QR Warehouse system through the architectural lens.

The project has already accumulated:

- domain objects;
- validation;
- scanning-related input;
- inventory behavior;
- estimate logic;
- tests;
- modular code;
- object-oriented design;
- polymorphic components where useful.

The objective is not to rebuild the project from zero.

The objective is to ask:

> **What architectural boundaries now become useful because the project is becoming a real product?**

---

## 18.1. First Architectural Snapshot

Start by drawing the existing system as it actually exists.

Do not redesign it first.

Create a diagram such as:

```text
Input
  ↓
Current entry point
  ↓
Current business logic
  ↓
Current storage
```

Then annotate each dependency.

For example:

```text
main.py
  ├── imports domain classes
  ├── reads JSON
  ├── validates data
  ├── runs rental logic
  └── formats output
```

The goal is to observe before changing.

---

## 18.2. Identify Stable Business Rules

List rules that should remain true regardless of infrastructure.

Examples:

```text
inventory cannot become negative
an item cannot be reserved beyond available stock
an estimate total must remain correct
an equipment ID must be valid
```

Mark these as domain-level behavior.

---

## 18.3. Identify Infrastructure

List details likely to change independently:

```text
JSON storage
future database
QR scanner integration
future HTTP API
CLI
filesystem
configuration source
```

Do not automatically abstract all of them.

First identify them.

---

## 18.4. Identify Application Actions

List meaningful workflows such as:

```text
RegisterEquipment
RentEquipment
ReturnEquipment
FindEquipment
CreateEstimate
```

Decide which ones deserve explicit use-case boundaries.

Again, avoid creating a class for every verb simply because the architecture diagram looks cleaner.

---

# Section XIX — Proposed Target Architecture

A reasonable target architecture for the learning project is:

```text
                 PRESENTATION
            ┌──────────┴──────────┐
            │                     │
           CLI                  API
            │                     │
            └──────────┬──────────┘
                       ↓
                  APPLICATION
            ┌──────────┼──────────┐
            │          │          │
        Use Cases   Services   Commands
            │          │          │
            └──────────┼──────────┘
                       ↓
                    DOMAIN
            ┌──────────┼──────────┐
            │          │          │
        Equipment   Inventory   Rental
            │          │          │
            └──────────┼──────────┘
                       ↓
                 CONTRACTS / PORTS
                       ↑
              ┌────────┴────────┐
              │                 │
        Infrastructure       Fakes
              │
        ┌─────┴─────┐
        ↓           ↓
       JSON        SQL
```

This is a **learning target**, not a requirement that every project must look exactly like this.

The actual implementation should contain only the boundaries justified by the project.

---

# Practical Project — Architectural Refactoring

## Goal

Refactor the existing QR Warehouse project into a clearer application architecture **without changing its intended behavior**.

The student should be able to demonstrate:

```text
clear boundaries
controlled dependencies
isolated domain rules
testable use cases
replaceable persistence
reasonable simplicity
```

---

## Phase 1 — Architecture Map

Produce:

1. a dependency diagram;
2. a list of major responsibilities;
3. a list of current infrastructure dependencies;
4. a list of important domain rules;
5. a list of meaningful application workflows.

Do not refactor yet.

---

## Phase 2 — Extract Persistence Boundary

Introduce a repository boundary only if the existing storage coupling justifies it.

At minimum consider:

```text
EquipmentRepository
```

Implement:

```text
current storage implementation
in-memory implementation for tests
```

Keep the interface minimal.

---

## Phase 3 — Extract One Use Case

Choose a meaningful workflow such as:

```text
RentEquipment
```

or:

```text
RegisterEquipment
```

Extract the workflow from presentation code.

The use case should depend on explicit collaborators.

---

## Phase 4 — Protect Domain Rules

Move or refine business rules so that they live in the appropriate domain objects or domain services.

Examples:

```text
stock invariants
availability rules
estimate invariants
```

Do not duplicate the same rule across layers.

---

## Phase 5 — Add Architecture-Level Tests

Create tests that prove:

```text
use case works with a fake repository
invalid states are rejected
business behavior does not depend on JSON details
refactoring preserved previous behavior
```

Use pytest as the safety net.

Remember the Module 06 principle:

> Tests should verify behavior, not merely class names or implementation details.

---

## Phase 6 — Add a Second Infrastructure Implementation

Only if the design warrants it, implement a second repository backend or a more realistic substitute.

Possible options:

```text
JSON + in-memory
JSON + SQLite
in-memory + SQLite
```

The point is to demonstrate that the application depends on the contract, not the storage technology.

Do not add PostgreSQL merely because the architecture diagram contains SQL.

---

## Phase 7 — Architecture Review

After the refactoring, answer:

```text
What responsibilities became clearer?

Which dependency was most problematic before?

What does the application layer know now?

What does it no longer know?

Which domain rules are isolated?

Can the use case run without the real database?

Which abstraction was most useful?

Which abstraction almost became unnecessary?

What would become easier if a web API were added later?

What would become harder if the system doubled in size?
```

---

# Section XX — Advanced Exercise: Architecture Comparison

Compare three designs for the same feature.

## Design A — Monolith

```text
HTTP handler
    ↓
all business logic
    ↓
SQL
```

## Design B — Layered

```text
HTTP
 ↓
Application
 ↓
Domain
 ↓
Repository
 ↓
SQL
```

## Design C — Overengineered

```text
HTTP
 ↓
Controller
 ↓
Command Bus
 ↓
Handler
 ↓
Service
 ↓
Domain Service
 ↓
Port
 ↓
Adapter Factory
 ↓
Repository
 ↓
Unit of Work
 ↓
ORM
 ↓
SQL
```

Answer:

```text
What problem does Design B solve?

Why might Design C be too much for a small project?

When could Design C become reasonable?

What would make Design A acceptable?
```

The expected skill is not choosing B automatically.

The expected skill is **defending the choice using the problem's constraints.**

---

# Section XXI — Architecture Review Checklist

Use this checklist when reviewing an application.

## Responsibilities

```text
Does each component have a coherent responsibility?
Does any component have many unrelated reasons to change?
```

## Dependencies

```text
Who depends on whom?
Are concrete technical details leaking into business logic?
Can unstable infrastructure be replaced without rewriting core rules?
```

## Domain

```text
Are important business invariants protected?
Are domain concepts represented clearly?
```

## Application

```text
Are workflows easy to find?
Does the application layer coordinate rather than duplicate domain rules?
```

## Infrastructure

```text
Is persistence logic kept near persistence?
Are external system details isolated?
```

## Testing

```text
Can important behavior be tested without real infrastructure?
Are tests focused on behavior?
Are mocks being overused?
```

## Simplicity

```text
Does each abstraction solve a real problem?
Could the design be simplified without losing important properties?
```

---

# Section XXII — Common Architectural Mistakes

## ARCH-001 — God Object

One class coordinates everything.

Symptoms:

```text
many methods
many dependencies
many unrelated responsibilities
hard-to-test behavior
```

---

## ARCH-002 — Persistence Leakage

Business logic directly manipulates SQL, JSON, files, or ORM details.

---

## ARCH-003 — Presentation Leakage

Domain code returns HTTP responses, CLI strings, GUI widgets, or framework objects.

---

## ARCH-004 — Dependency Direction Reversal

Stable core logic imports concrete infrastructure because it is convenient.

---

## ARCH-005 — Giant Service

A supposedly clean architecture creates a massive `WarehouseService` containing all domain behavior.

Moving everything into a service layer is not the same as designing a good architecture.

---

## ARCH-006 — Generic Repository Explosion

Creating:

```text
GenericRepository[T]
BaseRepository
CrudRepository
AsyncRepository
CachedRepository
```

before a real need exists.

---

## ARCH-007 — Pattern-Driven Design

The student starts from:

> "Which patterns should I use?"

instead of:

> **"What problem do I actually have?"**

---

## ARCH-008 — Framework-Driven Architecture

The application's structure is dictated entirely by framework conventions, while business concepts become difficult to identify.

---

## ARCH-009 — Premature Infrastructure

The student introduces PostgreSQL, containers, APIs, and configuration systems before the domain problem itself is stable.

---

## ARCH-010 — Architecture Theater

The repository, interfaces, services, factories, adapters, and layers all exist, but changing anything still requires touching everything.

A diagram can look professional while the dependency graph remains poor.

---

# Section XXIII — Debugging Architectural Problems

When an architectural issue appears, do not begin by editing code randomly.

Use this sequence:

```text
1. Describe the change that became difficult.
2. Identify which component should own that responsibility.
3. Trace the dependency arrows.
4. Find where an unrelated concern leaked across a boundary.
5. Choose the smallest structural improvement.
6. Make the change.
7. Run tests.
8. Re-evaluate the dependency graph.
```

Ask:

```text
What changed?
Why did the change spread?
Which boundary failed to contain it?
What knowledge did this component have that it should not need?
```

This is architecture debugging.

---

# Section XXIV — Independent Design Challenge

The student receives a new problem unrelated to the warehouse.

Example:

> A small delivery company needs a system for creating deliveries, assigning couriers, tracking status, and calculating delivery fees. The first version uses an in-memory store. A web API may be added later.

The student must design the architecture before coding.

Deliverables:

```text
1. domain concepts
2. domain rules
3. application use cases
4. infrastructure dependencies
5. dependency diagram
6. repository decision
7. testing strategy
8. explanation of why the architecture is not overengineered
```

The mentor should not immediately provide the architecture.

The student should defend the design.

---

# Final Project — QR Warehouse Architecture Review

The final project is not simply "make the code work."

It is an architectural exercise.

## Requirements

The resulting project should demonstrate, where justified:

```text
Domain objects with clear responsibilities
Application-level workflows
Explicit infrastructure boundaries
Dependency injection
A minimal repository boundary
In-memory test doubles
Automated tests
Clear dependency direction
No unnecessary framework dependence
No pattern-for-pattern's-sake abstraction
```

The student should be able to run the important business workflows without requiring the final production infrastructure.

---

# Final Assessment Tasks

The mentor should evaluate the student through several tasks rather than a single code dump.

## Task A — Explain the Architecture

The student must explain the system in their own words.

They should be able to answer:

```text
What is the domain?
What are the use cases?
Where is infrastructure?
Where is presentation?
Which direction do dependencies point?
Why?
```

---

## Task B — Trace a Request

Given a user action such as:

> Scan QR code and rent one camera.

The student should trace:

```text
input
 ↓
presentation
 ↓
use case
 ↓
domain
 ↓
repository contract
 ↓
infrastructure
```

Then trace the result back outward.

---

## Task C — Change the Infrastructure

The mentor changes one requirement:

> Replace JSON storage with SQLite.

The student must identify which parts of the system should change and which should remain stable.

---

## Task D — Change the Interface

The mentor changes:

> Replace CLI entry points with HTTP API entry points.

The student should explain how the business behavior can remain reusable.

---

## Task E — Identify Overengineering

Give the student an architecture with unnecessary layers.

The student should simplify it while preserving useful boundaries.

---

## Task F — Design a New System

Give a small unfamiliar domain.

The student should independently produce:

```text
components
responsibilities
boundaries
dependencies
tests
trade-offs
```

This is the strongest measure of transfer.

---

# Completion Criteria

Module 07 is complete when the student can independently:

- explain software architecture in practical terms;
- identify component responsibilities;
- identify architectural boundaries;
- separate domain, application, presentation, and infrastructure concerns;
- trace dependency direction;
- identify dependency leakage;
- explain Dependency Inversion without relying on memorized wording;
- use straightforward Dependency Injection;
- decide when a repository boundary is useful;
- create a minimal repository contract;
- implement or reason about an in-memory fake;
- distinguish domain rules from application workflows;
- identify appropriate use cases;
- test use cases without real infrastructure;
- use fakes, stubs, and mocks appropriately;
- refactor incrementally while preserving behavior;
- compare simple, layered, and overengineered designs;
- identify architectural coupling;
- defend architectural trade-offs;
- review the QR Warehouse architecture;
- transfer the architecture principles to an unfamiliar problem.

Most importantly, the student should be able to say:

> **"I know where this responsibility belongs, what this component should depend on, and why this boundary makes the system easier to change."**

---

# Competency Targets

The mentor should evaluate the following competencies.

## Architecture Thinking

### Level 1 — Recognition

Can identify the term "architecture" but mainly associates it with folders and project structure.

### Level 2 — Guided Analysis

Can identify responsibilities and boundaries with mentor questions.

### Level 3 — Independent Application

Can design a sensible component structure for a familiar application.

### Level 4 — Independent Design Judgment

Can compare architectures, explain trade-offs, and choose a proportional design.

---

## Dependency Reasoning

### Level 1

Recognizes direct dependencies.

### Level 2

Can draw dependency arrows with guidance.

### Level 3

Can deliberately control dependencies using interfaces and injection.

### Level 4

Can diagnose dependency direction as a source of maintenance cost and design a better boundary independently.

---

## Architectural Restraint

### Level 1

Tends to add abstractions because they look professional.

### Level 2

Can recognize obvious overengineering after discussion.

### Level 3

Usually adds abstractions only when a concrete problem exists.

### Level 4

Can deliberately choose between adding, keeping, and removing abstractions based on cost, change pressure, and system boundaries.

---

# Self-Check Questions

Before declaring the module complete, the student should answer these in their own words.

1. What is software architecture?
2. How is architecture different from file organization?
3. Why does architecture become visible through change?
4. What is a responsibility?
5. What is an architectural boundary?
6. What is Separation of Concerns?
7. What belongs in the domain layer?
8. What belongs in the application layer?
9. What belongs in infrastructure?
10. Why should presentation usually remain outside core business logic?
11. What is a dependency?
12. Why does dependency direction matter?
13. What is Dependency Inversion in practical terms?
14. What is Dependency Injection?
15. Why can a repository be useful?
16. When would a repository be unnecessary?
17. What is a use case?
18. How is a use case different from a domain object?
19. What is dependency leakage?
20. What is coupling?
21. How can coupling make changes expensive?
22. What is a fake?
23. What is a stub?
24. What is a mock?
25. Why should behavior remain the focus of tests?
26. How can tests support architectural refactoring?
27. Why is a giant service class not automatically good architecture?
28. Why can too many abstractions be harmful?
29. When should a second infrastructure implementation be added?
30. How would you decide whether a boundary is worth its cost?
31. How would you separate a CLI from business logic?
32. How would you replace JSON with SQL without rewriting use cases?
33. What should remain stable when a web API is added?
34. What architectural mistake is easiest for you to make?
35. How do you know when an architecture is simpler than it needs to be?

---

# Practical Design Drills

The mentor should use short design drills between larger tasks.

## Drill 1 — Classify Responsibility

Give the student a function or class and ask:

```text
What does it know?
What does it do?
What does it own?
What could change independently?
```

## Drill 2 — Draw Dependency Arrows

Given 5–7 components, ask the student to draw arrows before writing code.

## Drill 3 — Find Leakage

Show a domain class containing SQL, HTTP, or filesystem code.

Ask what boundary was violated.

## Drill 4 — Remove an Abstraction

Give an overengineered design and ask the student to simplify it.

## Drill 5 — Add a Boundary

Give a tangled design and ask where a boundary would create the most value.

## Drill 6 — Change the Requirement

Change one external dependency and ask which components should remain unchanged.

---

# AI Mentor Teaching Policy

Qwen should continue the methodology established in Modules 04–06.

The student has demonstrated strong architectural intuition and increasing independence. Therefore, Module 07 should emphasize reasoning before implementation.

When the student asks:

> "How should I structure this application?"

the mentor should first ask the student to identify:

```text
1. major responsibilities
2. stable business rules
3. external dependencies
4. likely points of change
5. current dependency direction
```

If these are unclear:

> return to analysis before coding.

If the student has a sensible design but does not know the syntax:

> provide the smallest useful implementation hint.

If the student has working code:

> review behavior first, then architecture.

Do not rewrite the student's architecture merely to match a textbook diagram.

---

# Calibrated Hint Policy

Maintain a graduated hint system.

## Hint Level 0 — Question

Ask a question that directs attention.

Examples:

> Which part of this code actually depends on the database?

> Which part of the system should care about HTTP?

> What would need to change if JSON disappeared tomorrow?

---

## Hint Level 1 — Direction

Identify the relevant architectural idea without revealing the design.

Example:

> Separate the workflow from the persistence mechanism.

---

## Hint Level 2 — Structural Hint

Suggest a boundary.

Example:

> Consider introducing a component that expresses what the application needs from storage, without exposing how storage works.

---

## Hint Level 3 — Minimal Code Fragment

Provide a minimal structural example:

```python
class EquipmentRepository:
    ...
```

The student completes the contract.

---

## Hint Level 4 — Focused Implementation

Provide a larger fragment if the student is genuinely blocked.

Then require the student to explain:

```text
Why is this boundary here?
What dependency does it hide?
What would happen without it?
```

---

## Hint Level 5 — Full Solution

Provide a complete implementation only when:

- the student explicitly asks for it;
- the remaining obstacle is implementation rather than reasoning;
- repeated attempts are no longer producing useful learning;
- comparing the correct architecture with the student's version has educational value.

After providing the solution, return to architectural reasoning.

---

# Testing Policy

Testing remains a supporting engineering skill rather than the primary specialization.

Qwen may provide partial test scaffolding when it helps the student focus on architecture.

For example:

```python
def test_rent_equipment_reduces_stock():
    repository = InMemoryEquipmentRepository(...)
    use_case = RentEquipment(repository, ...)

    # student writes assertions
```

The student should learn to:

- read tests as specifications;
- understand what behavior they protect;
- use fakes and simple stubs;
- interpret failures;
- preserve tests during refactoring;
- distinguish unit-level tests from integration concerns.

Do not force the student to manually produce large volumes of repetitive test code.

The goal remains:

> **Build reliable software while using tests as an architectural safety net.**

---

# Debugging Method

When the student encounters an architectural or integration problem, the mentor should guide them through:

```text
What component failed?

What responsibility does it own?

What dependency was involved?

Which concrete implementation was used?

Which contract was expected?

What happened immediately before the failure?

What does the traceback or error actually say?

Is the problem behavioral, structural, or environmental?
```

The mentor should avoid jumping directly to a framework-specific fix when a dependency or responsibility problem is the deeper issue.

---

# Common Mistakes to Track

Continue all previous patterns:

- type confusion;
- inconsistent contracts;
- scope mistakes;
- architecture vs syntax gap;
- dependency awareness;
- abstraction judgment;
- premature coding;
- inheritance by convenience;
- unnecessary classes;
- weak encapsulation;
- overengineering.

Add:

## ARCH-001 — Responsibility Drift

A component gradually accumulates unrelated responsibilities.

## ARCH-002 — Infrastructure Leakage

Domain or application code directly depends on technical infrastructure details.

## ARCH-003 — Presentation Leakage

Core logic knows about CLI, HTTP, GUI, or framework response objects.

## ARCH-004 — Concrete Dependency Lock-In

Business logic directly constructs or imports a concrete external implementation.

## ARCH-005 — Giant Application Service

A service becomes the new location for all business behavior rather than coordinating meaningful workflows.

## ARCH-006 — Generic Abstraction Too Early

The student creates generic repositories, factories, or base services before real variation appears.

## ARCH-007 — Mock-Heavy Testing

Tests verify implementation interactions while failing to express useful business behavior.

## ARCH-008 — Big-Bang Refactoring

The student changes the entire architecture at once without preserving behavior incrementally.

## ARCH-009 — Framework-First Thinking

The student starts from framework structure instead of application requirements.

## ARCH-010 — Diagram-Driven Architecture

The architecture looks elegant on paper but provides no meaningful benefit in the real code.

---

# Learning Journal Questions

These belong in the Learning Journal, not the Programming Handbook.

After completing the module, reflect on:

```text
What changed in my understanding of architecture?

Did I start seeing dependencies as arrows rather than imports?

Which architectural boundary felt most useful?

Which abstraction initially looked useful but turned out unnecessary?

Did Repository make persistence easier to reason about?

Did Use Cases make workflows easier to identify?

How did tests change my confidence during refactoring?

What kind of coupling do I notice most often in my own code?

Did I become better at deciding where responsibility belongs?

Was I tempted to overengineer the QR Warehouse?

What did I simplify deliberately?

Can I now design architecture for an unfamiliar problem without copying a template?

Where did I still need mentor guidance?
```

---

# Checkpoint Report Requirements

At the end of Module 07, Qwen should produce the usual APMF artifacts:

- Checkpoint Report;
- Learning Journal update;
- Programming Handbook update;
- Questions update;
- Development Log update.

The Checkpoint Report should explicitly evaluate:

1. architecture thinking;
2. responsibility assignment;
3. separation of concerns;
4. dependency direction;
5. Dependency Inversion;
6. Dependency Injection;
7. repository judgment;
8. use-case design;
9. domain/application/infrastructure separation;
10. architectural testing;
11. test-double judgment;
12. refactoring discipline;
13. architectural trade-offs;
14. overengineering restraint;
15. transfer to an unfamiliar domain;
16. independence level.

The report should distinguish:

```text
terminology recall
        vs
conceptual understanding
        vs
independent architecture design
```

---

# Programming Handbook Integration

After Module 07, update the Programming Handbook with technical knowledge from this module.

The Handbook should record concepts such as:

```text
software architecture
responsibilities and boundaries
Separation of Concerns
presentation/application/domain/infrastructure
Dependency Inversion
Dependency Injection at application scale
Repository Pattern
Application Services / Use Cases
architectural coupling
dependency leakage
fakes / stubs / mocks
architecture-aware testing
incremental architectural refactoring
trade-offs and abstraction cost
overengineering avoidance
```

The Handbook should **not** become a copy of this module or of the Checkpoint Report.

The Handbook stores durable technical knowledge.

The Learning Journal stores the student's learning experience.

The Development Log stores methodology evolution.

The Questions document stores curiosity and resolved questions.

---

# Final Conceptual Transition

Module 04 taught:

> **Good structure makes change safer.**

Module 05 taught:

> **Objects can own state and behavior.**

Module 06 taught:

> **Relationships, interfaces, and polymorphism allow related components to vary without unnecessary coupling.**

Module 07 teaches:

> **A maintainable application is a system of components whose responsibilities and dependencies are deliberately controlled.**

The progression becomes:

```text
Data
  ↓
Functions
  ↓
Modules
  ↓
Components
  ↓
Objects
  ↓
Object Collaboration
  ↓
Polymorphism
  ↓
Interchangeable Components
  ↓
Application Boundaries
  ↓
Controlled Dependencies
  ↓
Maintainable Systems
```

The final instinct should not be:

> "Which architecture pattern should I use?"

It should be:

> **"What changes does this system need to survive, which boundaries would contain those changes, and what is the simplest design that achieves that?"**

That question is the core engineering skill of Module 07.

---

# Recommended Time Budget

The module is intentionally estimated rather than fixed.

```text
Architecture fundamentals              ~2 h
Responsibilities and boundaries         ~1.5 h
Layering and dependency direction       ~2 h
DI and Dependency Inversion             ~1.5 h
Repository Pattern                       ~2 h
Use Cases / Application Services         ~2 h
Testing architecture                     ~2 h
Coupling and refactoring                 ~1.5 h
QR Warehouse refactoring                 ~4–5 h
Final design challenge                   ~1.5–2 h
```

Expected total:

```text
~15–22 hours

Target estimate:
~18 hours
```

The student should **not** be pressured to consume all estimated hours. Competence matters more than time spent.

---

# Final Mentor Note

The student is entering a new phase of software development.

Earlier modules focused on constructing correct programs.

Module 07 should increasingly focus on constructing programs that remain understandable when they grow.

The mentor should therefore reward:

```text
good decomposition
+
clear responsibilities
+
controlled dependencies
+
appropriate abstraction
+
strong tests
+
incremental refactoring
+
architectural restraint
+
independent reasoning
```

Do not reward complexity by itself.

Do not treat layered architecture as an achievement unless the layers solve real problems.

Do not push the student toward enterprise architecture prematurely.

The student should leave the module not thinking:

> "I know Repository, Use Case, and Dependency Inversion."

but:

> **"I can look at a growing application, identify where responsibilities and dependencies are causing change to spread, and design a simpler boundary that contains the problem."**

That is the actual purpose of Module 07.

---

*End of Module 07 — Application Architecture & Software Design*
