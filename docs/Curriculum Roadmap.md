# Curriculum Roadmap

**Framework:** AI Programming Mentor Framework (APMF)

**Version:** 0.2

**Status:** Active

---

# 1. Purpose

This document defines the long-term educational roadmap for the AI Programming Mentor Framework.

The roadmap describes progression from programming fundamentals toward independent software development.

The roadmap is **competency-based**.

Completion of a stage is determined by demonstrated understanding and practical ability rather than by the number of completed lessons or hours spent studying.

The roadmap is also a planning model rather than a rigid sequence. Topics may overlap, return at greater depth, or be introduced earlier when required by a project.

---

# 2. Learning Philosophy

The curriculum follows these principles:

* Fundamentals before unnecessary complexity.
* Understanding before memorization.
* Practice before mastery.
* Real projects alongside structured learning.
* Gradual increase of independence.
* Repeated application of previously learned concepts.
* Architecture should emerge from concrete problems rather than from pattern memorization.
* AI should support learning and engineering work, not replace understanding.
* Progress should be evaluated by what the student can explain, implement, debug, and modify independently.

The goal is not simply to learn Python.

The goal is to develop the ability to reason about software systems and gradually become capable of building and maintaining them independently.

---

# 3. Development Stages Overview

The curriculum consists of the following broad stages:

```text
Stage 0
Computational Thinking

↓

Stage 1
Programming Foundations

↓

Stage 2
Python Fundamentals

↓

Stage 3
Problem Solving and Algorithms

↓

Stage 4
Software Organization

↓

Stage 5
Object-Oriented Programming

↓

Stage 6
Data, Persistence and External Systems

↓

Stage 7
Software Engineering Practices

↓

Stage 8
Application Development

↓

Stage 9
Architecture and Advanced Development

↓

Stage 10
Independent Developer
```

The stages are conceptual rather than strictly sequential.

A student may work with material from several stages simultaneously once the necessary foundations have been established.

---

# Stage 0 — Computational Thinking

## Objective

Develop the ability to think in terms of problems, processes, states, constraints, and logical solutions.

---

## Core Competencies

The student can:

* describe a problem clearly;
* identify inputs, outputs, and constraints;
* divide a problem into smaller tasks;
* describe algorithms in natural language;
* identify repeated patterns;
* distinguish a problem from a particular implementation;
* understand automation as the transformation of a manual process into a repeatable procedure.

---

## Key Topics

* What programming is;
* How programs execute instructions;
* Algorithms;
* Problem decomposition;
* Logical reasoning;
* Abstraction;
* Program state.

---

## Completion Criteria

The student can take a simple real-world problem and describe a logical sequence of steps required to solve it, including relevant inputs, outputs, and state changes.

---

# Stage 1 — Programming Foundations

## Objective

Learn the fundamental building blocks common to most programming languages.

---

## Core Competencies

The student can:

* store and manipulate information;
* control program execution;
* create reusable logic;
* understand program state;
* distinguish expressions from actions that change state.

---

## Key Topics

* Variables;
* Assignment;
* Data types;
* Expressions;
* Conditions;
* Loops;
* Functions;
* Parameters and arguments;
* Return values;
* Basic debugging.

---

## Completion Criteria

The student can create small programs independently and explain their control flow and state changes.

---

# Stage 2 — Python Fundamentals

## Objective

Develop practical programming ability using Python.

Python remains the primary implementation language of the curriculum because it allows the student to focus on programming concepts while providing a practical path toward backend development.

---

## Core Competencies

The student can:

* write Python programs;
* use standard data structures;
* work with functions;
* organize code into modules;
* work with files and basic external data;
* use virtual environments and project dependencies;
* understand mutable and immutable objects at a practical level.

---

## Key Topics

* Python syntax;
* Lists;
* Dictionaries;
* Sets;
* Tuples;
* Functions;
* Modules;
* Packages;
* Virtual environments;
* Exceptions;
* File I/O;
* JSON;
* Basic dependency management.

---

## Completion Criteria

The student can independently create small Python applications and explain the main language constructs used in them.

---

# Stage 3 — Problem Solving and Algorithms

## Objective

Develop the ability to design solutions rather than only translate instructions into Python syntax.

---

## Core Competencies

The student can:

* analyze a problem;
* decompose it into smaller operations;
* select appropriate data structures;
* compare alternative solutions;
* reason about basic algorithmic complexity;
* debug incorrect logic systematically.

---

## Key Topics

* Algorithm design;
* Searching;
* Sorting;
* Iteration;
* Recursion;
* Complexity;
* Data structure selection;
* Edge cases;
* State transitions.

---

## Completion Criteria

The student can solve unfamiliar small and medium programming problems through structured reasoning and can explain why a chosen solution works.

Advanced algorithms are not considered a prerequisite for backend development at this stage.

---

# Stage 4 — Software Organization

## Objective

Move from isolated scripts toward organized software projects.

---

## Core Competencies

The student can:

* divide code into modules;
* separate responsibilities;
* distinguish business logic from input/output;
* identify dependencies;
* organize application flow;
* recognize when code structure makes change unnecessarily difficult.

---

## Key Topics

* Project structure;
* Modules and packages;
* Separation of concerns;
* Dependency management;
* Dependency injection;
* Pure functions and side effects;
* Error handling;
* Configuration;
* Documentation;
* Refactoring.

---

## Completion Criteria

The student can create a multi-module Python project whose responsibilities are understandable and whose components can be modified without unnecessarily affecting unrelated parts.

---

# Stage 5 — Object-Oriented Programming

## Objective

Understand when and how objects can be used to represent domain concepts and manage related state and behavior.

---

## Core Competencies

The student can:

* model domain entities;
* design classes;
* use dataclasses where appropriate;
* understand composition;
* understand inheritance and polymorphism at a practical level;
* distinguish domain objects from infrastructure concerns;
* recognize when object-oriented design is useful and when simpler structures are sufficient.

---

## Key Topics

* Classes;
* Objects;
* Attributes;
* Methods;
* Encapsulation;
* Dataclasses;
* Composition;
* Inheritance;
* Polymorphism;
* Abstract interfaces;
* Basic SOLID principles.

---

## Completion Criteria

The student can design and implement a small domain model and explain the responsibilities and relationships of its objects.

---

# Stage 6 — Data, Persistence and External Systems

## Objective

Learn how applications interact with persistent data and external resources.

---

## Core Competencies

The student can:

* read and write structured data;
* model relational data;
* work with SQLite;
* use SQL for common operations;
* separate persistence from business logic;
* implement repository-style persistence boundaries;
* coordinate changes across multiple repositories;
* understand the basic purpose of transactions and Unit of Work;
* consume external APIs at a basic level.

---

## Key Topics

* Files;
* JSON;
* Relational databases;
* Tables and relationships;
* SQL;
* SQLite;
* Repository pattern;
* Persistence boundaries;
* Transactions;
* Unit of Work;
* Historical snapshots;
* External APIs;
* Serialization.

---

## Completion Criteria

The student can build an application that stores domain data persistently while keeping business logic reasonably independent from the underlying storage mechanism.

The student is not expected to have deep database-engineering knowledge at this stage. PostgreSQL internals, advanced query optimization, migrations, locking, and production database operations remain areas for later development.

---

# Stage 7 — Software Engineering Practices

## Objective

Develop reliable development habits and the ability to change software safely.

---

## Core Competencies

The student can:

* use Git for normal development workflows;
* write automated tests;
* distinguish unit and integration tests;
* use test doubles where appropriate;
* debug failures systematically;
* refactor without unnecessarily changing behavior;
* evaluate the effect of architectural changes;
* use AI tools while retaining responsibility for understanding and validating the result.

---

## Key Topics

* Git;
* Testing;
* pytest;
* Fixtures;
* `pytest.raises`;
* Test doubles and in-memory fakes;
* Unit testing;
* Integration testing;
* API testing;
* Debugging methodology;
* Refactoring;
* Code review;
* Documentation;
* Development workflows;
* AI-assisted development.

---

## Completion Criteria

The student can add and modify functionality in an existing project while using tests and debugging tools to reduce regressions.

At the current stage, the student has practical experience with pytest, TestClient, fixtures, in-memory fakes, and API-level testing. Further work is required in integration testing, broader test coverage, and testing multi-component coordination.

---

# Stage 8 — Application Development

## Objective

Learn how separate components form a complete application with multiple interfaces and external boundaries.

---

## Core Competencies

The student can:

* structure an application into layers or meaningful boundaries;
* implement application use cases;
* connect domain logic with persistence;
* expose functionality through an HTTP API;
* understand HTTP methods and status codes;
* validate external input;
* separate presentation concerns from business logic;
* support multiple application entry points;
* write basic API tests.

---

## Key Topics

* Application architecture;
* Use Cases;
* Application Shell;
* Domain entities;
* Read Models;
* Repository boundaries;
* HTTP;
* REST-style APIs;
* FastAPI;
* Pydantic;
* HTTP status codes;
* Request and response models;
* API testing;
* Swagger/OpenAPI;
* Multiple entry points;
* Basic asynchronous programming;
* Concurrency for I/O-bound operations.

---

## Current Position

The student has completed the material through **Module 09**.

At this point the student has practical experience with:

* multi-module Python applications;
* domain entities and dataclasses;
* repositories;
* SQLite persistence;
* Unit of Work;
* multi-repository coordination;
* Use Cases;
* Application Shell;
* Read Model vs Domain Entity;
* pytest-based testing;
* FastAPI;
* Pydantic request/response validation;
* HTTP methods and status codes;
* API-level testing with TestClient;
* multiple entry points sharing the same application logic;
* basic `async`/`await` and `asyncio.gather`;
* the distinction between concurrency and parallelism;
* the distinction between I/O-bound and CPU-bound work.

The current development focus should therefore deepen these concepts rather than reintroduce them from zero.

---

## Current Learning Priorities

The next stage of development should emphasize:

* integration testing;
* test isolation;
* test doubles;
* testing multi-repository coordination;
* reliable error handling;
* deeper SQL and transaction understanding;
* API design;
* authentication and authorization;
* configuration and deployment;
* production application boundaries;
* continued independent implementation without relying on AI-generated code as a substitute for understanding.

---

## Completion Criteria

The student can independently implement a complete small application feature spanning:

```text
External Input
      ↓
Presentation Layer
      ↓
Use Case
      ↓
Domain Logic
      ↓
Repository
      ↓
Database
```

and can test the relevant parts at appropriate levels.

The student does not need to master every production technology before moving forward. The important criterion is the ability to understand the path of data and responsibility through the application.

---

# Stage 9 — Architecture and Advanced Development

## Objective

Develop the ability to reason about software architecture, trade-offs, system boundaries, and long-term maintainability.

---

## Core Competencies

The student should gradually become able to:

* identify architectural boundaries;
* make explicit design decisions;
* compare alternative architectures;
* understand trade-offs;
* recognize overengineering;
* design systems around changing requirements;
* reason about reliability and failure modes;
* work with unfamiliar existing codebases;
* understand the consequences of persistence, concurrency, and deployment decisions.

---

## Key Topics

* Layered architecture;
* Clean Architecture concepts;
* Hexagonal Architecture concepts;
* Repository pattern;
* Unit of Work;
* Application services and Use Cases;
* Domain vs infrastructure boundaries;
* Read Models;
* Dependency inversion;
* Design patterns;
* API architecture;
* Authentication and authorization;
* Transactions;
* Concurrency;
* Performance;
* Security basics;
* Deployment;
* Reverse proxies;
* HTTPS;
* PostgreSQL;
* Database migrations;
* Observability;
* System design;
* Working with existing codebases.

---

## Current Status

The student has begun working with architectural concepts in practical projects and can explain several common boundaries and patterns.

However, this stage is **in progress**.

The student should not yet be treated as having broad independent architecture expertise. Further evidence is needed through:

* independent design of unfamiliar systems;
* implementation without step-by-step guidance;
* evaluation of competing architectural approaches;
* production-oriented deployment;
* deeper database and concurrency work;
* maintenance of larger existing codebases.

---

## Completion Criteria

The student can design a moderately complex application, explain the major architectural decisions, identify meaningful trade-offs, and revise the design when requirements change.

---

# Stage 10 — Independent Developer

## Objective

Develop the ability to independently learn, design, implement, debug, deploy, and maintain software.

---

## Final Competencies

The student can:

* start a project from an ambiguous problem;
* clarify requirements;
* research unfamiliar technologies;
* choose appropriate tools;
* design an architecture proportional to the problem;
* implement features independently;
* write and maintain tests;
* debug complex problems;
* work with existing codebases;
* deploy applications;
* monitor and maintain software;
* evaluate technical trade-offs;
* effectively use AI as an engineering assistant without outsourcing understanding or decision-making.

---

## Completion Criteria

There is no single project or examination that permanently marks completion of this stage.

Evidence should come from repeated independent work across different problems and contexts.

The student should be able to move from:

```text
Problem
   ↓
Requirements
   ↓
Design
   ↓
Implementation
   ↓
Testing
   ↓
Debugging
   ↓
Deployment
   ↓
Maintenance
```

with progressively less external guidance.

---

# 4. Project Integration Strategy

Real projects should become increasingly important as the student's competencies develop.

The recommended progression is:

```text
Exercises

↓

Small Personal Programs

↓

Independent Features

↓

Project Modules

↓

Complete Applications

↓

Real-World Projects

↓

Independent Software Development
```

The student's existing projects should be used as learning environments whenever they provide realistic problems.

In particular, the QR Warehouse project can serve as a practical environment for studying:

* domain modeling;
* relational databases;
* persistence;
* application architecture;
* HTTP APIs;
* testing;
* authentication and authorization;
* integration with existing systems;
* deployment;
* real-world requirements;
* maintainability.

However, project development must not completely replace fundamental learning.

A real project is a learning environment, not proof that every underlying competency has already been mastered.

---

# 5. Progress Evaluation

Progress should be evaluated using multiple forms of evidence.

The mentor should consider whether the student can:

* explain a concept without reproducing memorized definitions;
* implement it in a known context;
* modify an existing implementation;
* debug a broken implementation;
* apply it in a slightly unfamiliar context;
* explain why one solution was chosen over another;
* recognize limitations of their own solution.

A concept should not be considered fully mastered merely because the student successfully implemented it once with substantial guidance.

---

# 6. Independence Model

The curriculum should gradually shift the student's role from following instructions toward making engineering decisions.

```text
Guided Implementation
        ↓
Implementation With Explanations
        ↓
Independent Feature Implementation
        ↓
Independent Design + Implementation
        ↓
Independent Problem Solving
```

AI assistance may be used throughout this progression.

However, the amount of AI-generated implementation should decrease when the educational objective is to develop independent programming ability.

The student should remain capable of explaining and modifying code produced with AI assistance.

---

# 7. Adaptation

This roadmap is not a rigid schedule.

The mentor may adjust:

* order of topics;
* depth of topics;
* practice volume;
* project integration;
* review frequency;
* difficulty of exercises;

based on demonstrated progress and unresolved gaps.

The roadmap defines direction, not a fixed timeline.

Current competency should always take precedence over assumptions based solely on completed module numbers.

---

# 8. Current Curriculum Position

**Completed through Module 09.**

The student has progressed beyond basic Python and introductory OOP into practical application development involving:

* modular architecture;
* domain modeling;
* persistence;
* repositories;
* transactions and Unit of Work;
* automated testing;
* HTTP APIs;
* FastAPI;
* API validation;
* multiple application entry points;
* basic asynchronous programming.

The next curriculum phase should consolidate these skills through testing, integration, reliability, deeper database work, security fundamentals, deployment, and increasingly independent implementation.

The curriculum should continue to expose gaps rather than hide them behind broad labels such as "advanced developer" or "software architect".

---

**End of Curriculum Roadmap v0.2**
