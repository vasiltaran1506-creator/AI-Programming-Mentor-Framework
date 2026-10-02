# Questions

**Version:** 2.0
**Status:** Active
**Maintained by:** AI Programming Mentor

---

## Purpose

Questions are one of the most valuable learning resources in the framework.

Every unanswered question identifies a boundary between the student's current understanding and a topic that requires further exploration.

Questions should not disappear after a lesson answers them. They remain part of the learning history and may be revisited when later topics reveal a deeper layer of the same concept.

This document is therefore both:

* a list of current knowledge gaps;
* a record of concepts that have already been explored through practice.

---

# 1. Question States

Every question belongs to one state.

```text
Open
  ↓
Discussing
  ↓
Answered
  ↓
Mastered
```

### Open

The student has identified the question but does not yet have sufficient understanding or practical experience.

### Discussing

The topic is currently being explored. The student's understanding may still be incomplete.

### Answered

The student can explain the concept and understands the basic idea, but further practical application is desirable.

### Mastered

The student has demonstrated the concept through practical work and can use it in a known context.

**Important:** "Mastered" in this document means **demonstrated and stable within the contexts already practiced**. It does not mean that the student has exhaustive knowledge of the subject.

---

# 2. Rules

Questions are not deleted.

A question may move between states.

A previously mastered question may return to Open if a later topic reveals an important limitation or deeper misunderstanding.

This is normal and should be treated as part of learning rather than as regression.

Questions should be updated when practical experience changes the student's understanding.

---

# 3. Current Open Questions

## Q-0001 — Why does Python start indexing at zero?

**Status:** Open
**Priority:** Medium

The student understands zero-based indexing in practice but has not yet studied its historical and technical rationale in depth.

**Related topics:**

* Arrays;
* Memory layout;
* Index arithmetic;
* Python sequence semantics.

---

## Q-0002 — What actually happens inside memory when variables change?

**Status:** Open
**Priority:** High

The student has a practical mental model of variables, assignment, objects, and references, but has not studied Python's memory model and object implementation in depth.

**Related topics:**

* Objects;
* References;
* Assignment;
* `id()`;
* CPython implementation;
* Memory management;
* Garbage collection.

---

## Q-0004 — How does hashing work inside sets and dictionaries?

**Status:** Open
**Priority:** Medium

The student understands that sets and dictionaries provide efficient lookup but has not yet studied hash tables and their implementation in detail.

**Related topics:**

* Hash functions;
* Hash tables;
* Collisions;
* Dictionary implementation;
* Set implementation;
* Complexity.

---

## Q-0006 — What are lambda functions and when should I use them?

**Status:** Open
**Priority:** High

The student has used `lambda` as a `key` function but still wants a systematic understanding of:

* anonymous functions;
* `lambda` vs `def`;
* higher-order functions;
* `map`;
* `filter`;
* `sorted`;
* appropriate and inappropriate uses of lambdas.

---

## Q-0010 — What are the SOLID principles and how do they connect to what I have already learned?

**Status:** Open
**Priority:** Medium

The student has encountered several SOLID principles through practical architecture work:

* SRP through separation of responsibilities;
* OCP through extensible policies;
* LSP through inheritance analysis;
* ISP through focused repository and Pydantic contracts;
* DIP through repository abstractions and dependency injection.

The remaining gap is a systematic study of the complete SOLID framework and its limitations.

The goal should not be to memorize five definitions, but to understand when these principles are useful, when they conflict with simplicity, and when applying them would constitute overengineering.

---

## Q-0025 — How do relational databases work internally?

**Status:** Open
**Priority:** Medium

The practical SQL and schema-design portion of database work has already been demonstrated.

The remaining question concerns the internal mechanisms:

* B-trees;
* pages;
* indexes;
* query planning;
* `EXPLAIN QUERY PLAN`;
* query optimization;
* SQLite internals;
* differences between SQLite and PostgreSQL;
* when different database models are appropriate.

---

## Q-0026 — How do I test thick Use Cases that coordinate multiple repositories?

**Status:** Open
**Priority:** High

The student has written API-level tests with `pytest` and FastAPI `TestClient`.

The remaining practical gap is testing application logic independently of HTTP.

Topics to practice:

* in-memory fakes;
* Use Case unit tests;
* multi-repository coordination;
* transaction success;
* rollback after failure;
* Historical Snapshot behavior;
* insufficient stock;
* missing equipment;
* missing estimates;
* test isolation.

---

## Q-0027 — How would the commercial version of QR Warehouse work?

**Status:** Open
**Priority:** Low

The student has already developed the architectural foundation of QR Warehouse, including persistence, Use Cases, and an HTTP API.

The commercial system still requires separate investigation of:

* QR generation and printing;
* multi-user access;
* warehouse scanning workflow;
* manager interface;
* authentication and authorization;
* bulk inventory import;
* manual item creation;
* deployment;
* integration with existing company systems such as 1C;
* operational requirements and user roles.

This question represents a product-development problem rather than a single programming concept.

---

## Q-0037 — How do I deploy a FastAPI application to a production server?

**Status:** Open
**Priority:** Medium

The student can currently run and test a FastAPI application locally.

The production deployment question remains open.

Relevant topics:

* Uvicorn;
* production process management;
* environment variables;
* reverse proxy;
* HTTPS;
* Docker;
* database configuration;
* migrations;
* logging;
* monitoring;
* backups;
* deployment workflow.

---

## Q-0038 — How do I implement authentication and authorization for a multi-user Web API?

**Status:** Open
**Priority:** Medium

The current API does not yet implement a complete user authentication and authorization system.

Relevant topics:

* authentication vs authorization;
* sessions and tokens;
* JWT;
* password hashing;
* roles and permissions;
* RBAC;
* FastAPI dependencies;
* secure credential storage;
* access control at the application boundary.

This is particularly relevant to the future QR Warehouse system.

---

# 4. Discussing

There are currently no questions in the Discussing state.

When a new module directly addresses an Open question, the mentor should move that question to Discussing rather than immediately marking it as mastered.

---

# 5. Answered

There are currently no questions that require the intermediate Answered state.

A question may use this state when the student understands the concept theoretically but has not yet demonstrated it sufficiently through practical work.

---

# 6. Mastered Through Practical Work

The following questions have been sufficiently demonstrated in the student's existing projects.

These entries should be interpreted as **practical mastery in demonstrated contexts**, not as claims of exhaustive expertise.

---

## Q-0003 — Why do some functions return values while others modify existing objects?

**Status:** Mastered

The student understands the practical difference between mutating mutable objects and producing new values from immutable objects.

The concept has been reinforced through practical Python work involving lists, dictionaries, strings, functions, and object state.

---

## Q-0005 — What is the difference between `pathlib.Path` and string paths?

**Status:** Mastered

The student understands why `Path` objects are preferable for structured filesystem operations and has used `pathlib` in practical projects.

---

## Q-0007 — What is Object-Oriented Programming and when is it useful?

**Status:** Mastered

The student has practical experience with:

* classes;
* objects;
* methods;
* encapsulation;
* composition;
* inheritance;
* polymorphism;
* domain objects;
* dataclasses.

The student also learned that OOP is a tool rather than a requirement for every program.

---

## Q-0008 — What is the difference between `@dataclass` and regular classes?

**Status:** Mastered

The student has demonstrated the ability to distinguish passive data structures from objects that need behavior.

During QR Warehouse refactoring, the student also recognized that an existing class could become a dataclass when its behavior was no longer required by the architecture.

---

## Q-0009 — How do I write automated tests using pytest?

**Status:** Mastered

The student has practical experience with:

* pytest;
* test functions;
* fixtures;
* assertions;
* `pytest.raises`;
* unit tests;
* API tests;
* test data isolation.

The current gap is not learning pytest from zero, but expanding testing toward integration tests and more complex application coordination.

---

## Q-0011 — What is the difference between inheritance and composition?

**Status:** Mastered

The student understands the practical distinction between:

```text
is-a → inheritance

has-a / uses-a → composition
```

The student has also encountered Liskov Substitution through practical inheritance examples.

---

## Q-0012 — What is polymorphism and how does it reduce conditional logic?

**Status:** Mastered

The student implemented different pricing policies behind a common interface and used polymorphism to avoid large conditional branches.

The concept was applied in QR Warehouse and related exercises.

---

## Q-0013 — What are Abstract Base Classes and when should I use them?

**Status:** Mastered

The student understands:

* `ABC`;
* `@abstractmethod`;
* explicit contracts;
* why abstract methods can prevent incomplete implementations.

The concept was applied to pricing policies and repository contracts.

---

## Q-0014 — What is the Factory pattern and when should I use it?

**Status:** Mastered

The student has implemented and analyzed a factory for notification processors and understands that factories are useful when object creation contains meaningful complexity or repetition.

The student also understands that a factory can be unnecessary when object creation is already trivial.

---

## Q-0015 — What is `super()` and when should I use it?

**Status:** Mastered

The student understands the difference between replacing inherited behavior and extending it with `super()`.

The concept was practiced with inherited initialization and business methods.

---

## Q-0016 — How do I test expected exceptions using `pytest.raises`?

**Status:** Mastered

The student can use:

```python
with pytest.raises(ValueError):
    ...
```

and can inspect the resulting exception when necessary.

The concept has been applied in automated tests.

---

## Q-0017 — What is software architecture and how is it different from file organization?

**Status:** Mastered

The student now understands architecture primarily as:

* responsibilities;
* boundaries;
* dependencies;
* change propagation;
* system structure.

The student has applied this understanding during QR Warehouse refactoring.

---

## Q-0018 — What is the Repository pattern and when should I use it?

**Status:** Mastered

The student has implemented repository abstractions and concrete persistence implementations.

The student also experienced the practical benefit of changing storage from JSON to SQLite without rewriting the core business logic.

During Module 08, the student separated equipment and estimate persistence into different repositories.

---

## Q-0019 — What are Use Cases and how do they differ from domain objects?

**Status:** Mastered

The student understands Use Cases as application-level coordinators of business workflows.

The student has implemented multiple Use Cases that:

* accept application input;
* validate business conditions;
* coordinate repositories;
* create required data objects;
* manage transactions;
* return structured business results.

---

## Q-0020 — What is Dependency Inversion and how does it work in practice?

**Status:** Mastered

The student has practical experience with:

* abstractions;
* dependency injection;
* repository contracts;
* concrete implementations;
* composition roots.

The key demonstrated model is:

```text
Business logic
      ↓
  abstraction
      ↑
concrete implementation
```

---

## Q-0021 — How do I separate Domain, Application, Presentation, and Infrastructure?

**Status:** Mastered

The student can classify responsibilities using an architectural filter:

```text
Rule about the domain
        ↓
      Domain

Business workflow
        ↓
    Application

External interface
        ↓
   Presentation

Technical mechanism
        ↓
  Infrastructure
```

This model has been applied directly to QR Warehouse.

---

## Q-0022 — How do I test business logic without real infrastructure?

**Status:** Mastered

The student understands the purpose of test doubles and has practical experience with an in-memory repository.

The student can distinguish the general roles of:

* Fake;
* Stub;
* Mock.

Further experience with more advanced mocking strategies is still useful but is not required to consider the basic question resolved.

---

## Q-0023 — How do relational databases work and how do I use SQL systematically?

**Status:** Mastered — practical portion

The student has demonstrated practical knowledge of:

* `SELECT`;
* `INSERT`;
* `UPDATE`;
* `DELETE`;
* `JOIN`;
* `WHERE`;
* `ORDER BY`;
* parameterized queries;
* foreign keys;
* constraints;
* indexes;
* relational schema design;
* SQLite transactions.

The internal implementation of relational databases remains open under Q-0025.

---

## Q-0024 — How would QR Warehouse change if a Web API were added alongside the CLI?

**Status:** Mastered

Module 09 provided direct practical confirmation.

The student added an HTTP API as a second entry point while preserving the same application logic and repositories.

The resulting model is:

```text
             CLI
              ↓
       Presentation Layer
              ↓
          Use Cases
              ↓
        Repositories
              ↓
           Database


             HTTP
              ↓
       Presentation Layer
              ↓
          Use Cases
              ↓
        Repositories
              ↓
           Database
```

The student also introduced a structured `Result` object so that business outcomes could be translated into HTTP responses without coupling Use Cases to HTTP.

---

## Q-0028 — How do I model multi-vendor data in a relational database?

**Status:** Mastered

The student understands why multiple vendors should normally be represented as rows in a shared relational model rather than by creating a new table for every vendor.

The concept was applied in the Gaffer Sandbox database design.

---

## Q-0029 — What is the Historical Snapshot pattern?

**Status:** Mastered

The student understands why documents such as estimates may need to preserve historical information even when the source catalog changes.

The student implemented the practical concept by copying relevant equipment information into estimate items when the item is added.

---

## Q-0030 — What is the Unit of Work pattern and who owns transactions?

**Status:** Mastered

The student independently identified the problem of repositories committing separately and implemented transaction coordination at the application/use-case level.

The practical model is:

```text
Use Case
   ↓
Repository A
   ↓
Repository B
   ↓
commit()

or, on failure:

rollback()
```

The student understands the relationship between atomicity and multi-repository operations.

---

## Q-0031 — What is the difference between a Domain Entity and a Read Model?

**Status:** Mastered

The student recognized that an object does not have to remain a behavior-rich domain entity merely because it originally started as one.

During QR Warehouse refactoring, `Estimate` became a simpler data representation when its business behavior moved into Use Cases.

---

## Q-0032 — What is the Application Shell pattern?

**Status:** Mastered

The student independently identified the need to move application lifecycle and dependency wiring out of an increasingly large `main.py`.

The resulting model separates:

```text
Entry point
    ↓
Application Shell
    ↓
Dependencies + Use Cases
    ↓
Application behavior
```

---

## Q-0033 — How do I handle optional fields and manual data entry in a relational database?

**Status:** Mastered

The student designed a practical model for catalog and manually entered estimate items using nullable foreign-key data and an explicit source indicator.

The solution was derived from a real warehouse requirement rather than from an abstract database exercise.

---

## Q-0034 — What is the Result pattern and how does it decouple business logic from HTTP?

**Status:** Mastered

The student implemented a structured `Result` containing information such as:

```text
success
status
details
```

Use Cases return business-level outcomes.

The Presentation Layer translates those outcomes into HTTP status codes and responses.

This keeps HTTP-specific knowledge outside the business logic.

---

## Q-0035 — How do I design API errors without leaking sensitive information?

**Status:** Mastered — practical principle

The student demonstrated the ability to distinguish between:

* information useful for solving a problem;
* information that should not be exposed to an external client.

The concept was applied to API error responses in the Crew Scheduler project.

Further security study is still required under Q-0038.

---

## Q-0036 — How do I build a multi-entry-point architecture where CLI and HTTP API share business logic?

**Status:** Mastered

The student implemented the architecture directly in QR Warehouse.

The CLI and HTTP API share:

* the same Use Cases;
* the same repositories;
* the same database;
* the same business rules.

Only the presentation/translation layer differs.

---

# 7. Current Knowledge-Gap Map

After Module 09, the most important unresolved areas are:

### Python internals

* memory and object model;
* hashing;
* implementation details.

### Python language features

* lambda and higher-order functions.

### Architecture

* formal SOLID study;
* recognizing when architectural abstractions are justified;
* working with unfamiliar codebases.

### Databases

* internal database architecture;
* indexes;
* query planning;
* PostgreSQL;
* migrations;
* deeper transaction and concurrency behavior.

### Testing

* thick Use Case unit tests;
* multi-repository coordination;
* transaction testing;
* broader integration testing;
* advanced test isolation.

### Web development

* authentication;
* authorization;
* security boundaries;
* production deployment;
* configuration;
* observability.

### Production engineering

* Linux server administration;
* Docker;
* reverse proxy;
* HTTPS;
* deployment;
* logging;
* monitoring;
* backups.

These gaps should guide future modules without implying that all of them must be completed before the student can build useful software.

---

# 8. Mentor Responsibilities

The mentor should review this document when beginning a new module.

If the lesson naturally addresses an existing Open question, the mentor should explicitly connect the lesson to that question.

For example:

> This lesson directly addresses Q-0026.

When a question is only partially resolved, the mentor should update its status or add a progress note instead of prematurely marking it as Mastered.

The mentor should avoid converting practical exposure into claims of universal mastery.

---

# 9. Student Responsibilities

The student should record new questions whenever they appear.

Questions do not need to be polished.

Examples:

```text
Why?

How?

What if...?

Why is it designed this way?

What happens if this component fails?

Why do we need this abstraction?
```

The mentor may refine rough questions into useful engineering questions without changing the underlying curiosity.

---

# 10. Quality Rules

A good question is:

* specific;
* motivated by curiosity;
* connected to programming or software engineering;
* answerable through study and/or practice;
* useful for identifying a knowledge boundary.

Poor:

> How does Python work?

Better:

> What happens to Python objects in memory when two variables refer to the same object?

Poor:

> What is architecture?

Better:

> Which dependency direction allows the business logic to remain independent of SQLite?

Questions should become increasingly precise as the student's understanding develops.

---

# 11. Long-Term Vision

This document should remain a map of the student's intellectual development.

Some questions will become simple.

Others will split into several deeper questions.

Some will return after the student encounters a more complex system.

This is expected.

The purpose of the document is not to demonstrate that the student has "no unanswered questions."

The purpose is to make the boundaries of current understanding visible so that the next learning step can be chosen deliberately.

---

*End of Questions v2.0*
