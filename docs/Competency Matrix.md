# Competency Matrix

**Framework:** AI Programming Mentor Framework (APMF)

**Version:** 0.2

**Status:** Active

---

# 1. Purpose

This document defines the competency model used to track the student's development within the AI Programming Mentor Framework.

The matrix is intended to answer three related questions:

1. What concepts has the student encountered?
2. What can the student currently do with those concepts?
3. How independently can the student apply them in a new situation?

The matrix measures **demonstrated capability**, not the number of completed modules.

Completion of a module does not automatically mean that every competency introduced in that module has reached an independent level.

---

# 2. Competency Philosophy

APMF evaluates three dimensions:

* **Knowledge** — does the student understand the concept?
* **Application** — can the student use it in code?
* **Independence** — can the student make appropriate decisions without step-by-step guidance?

The purpose is not to produce a permanent label.

A competency level is a snapshot of current ability and can change as the student gains experience.

A student may also have different levels in closely related competencies. For example, they may understand an architectural pattern well while still needing guidance when implementing it in an unfamiliar project.

---

# 3. Competency Levels

## Level 0 — Not Encountered

The student:

* has not meaningfully encountered the concept;
* cannot yet explain its purpose;
* cannot apply it.

---

## Level 1 — Familiarity

The student:

* recognizes the concept;
* understands basic terminology;
* can follow an explanation;
* can recognize a simple example.

The student still requires substantial guidance to apply the concept.

---

## Level 2 — Guided Application

The student:

* can apply the concept in familiar situations;
* can complete practical tasks with mentor guidance;
* understands the general purpose and basic trade-offs;
* can modify an existing example.

The student may still struggle when the problem is presented in an unfamiliar form.

---

## Level 3 — Independent Application

The student:

* can apply the concept independently in familiar problem domains;
* can implement common solutions without step-by-step instructions;
* can debug ordinary mistakes;
* can explain the main reasoning behind their decisions;
* can recognize when the concept is applicable.

This is the primary target for practical competency.

Level 3 does **not** mean expert knowledge.

---

## Level 4 — Transfer and Advanced Understanding

The student:

* can apply the concept in unfamiliar situations;
* understands important trade-offs and limitations;
* can compare several viable approaches;
* can identify inappropriate uses of a technique;
* can explain the concept clearly to another learner;
* can make design decisions involving the concept without relying on a recipe.

Level 4 is intentionally difficult to achieve and should not be assigned merely because the student has completed an advanced module.

---

# 4. Current Competency Snapshot

The following snapshot reflects the student's demonstrated learning after Module 09.

The levels are deliberately conservative. They describe the current learning state rather than an overall professional qualification.

---

# Area A — Computational Thinking

## CT-001 Problem Decomposition

**Current level:** 3 — Independent Application

The student can decompose practical programming problems into smaller components and has repeatedly used decomposition while designing project architecture and mini-projects.

Current limitation:

* decomposition of completely unfamiliar domains still benefits from discussion and review.

---

## CT-002 Algorithmic Thinking

**Current level:** 2–3 — Guided to Independent Application

The student can design step-by-step solutions for familiar problems and reason about program flow before implementation.

Further development is needed in:

* more complex algorithms;
* algorithmic efficiency;
* unfamiliar problem types.

---

## CT-003 Abstraction

**Current level:** 3 — Independent Application in familiar contexts

The student understands the purpose of abstraction and has applied it through:

* functions;
* repositories;
* use cases;
* domain objects;
* presentation boundaries.

Current limitation:

* distinguishing useful abstraction from premature abstraction still requires deliberate evaluation in unfamiliar situations.

---

# Area B — Programming Fundamentals

## PF-001 Variables and Data

**Current level:** 3 — Independent Application

The student understands:

* variable binding;
* assignment;
* basic types;
* mutable and immutable objects;
* references to objects.

---

## PF-002 Control Flow

**Current level:** 3 — Independent Application

The student can use:

* conditions;
* loops;
* iteration;
* `break`;
* `continue`;
* basic control-flow composition.

---

## PF-003 Functions

**Current level:** 3 — Independent Application

The student can:

* define functions;
* use parameters and arguments;
* return values;
* separate responsibilities between functions;
* reason about function contracts.

Further development:

* deeper understanding of advanced function behavior;
* decorators;
* more advanced functional patterns.

---

## PF-004 Debugging Fundamentals

**Current level:** 3 — Independent Application

The student can investigate errors using evidence rather than relying only on guessing.

Further development is needed in:

* unfamiliar large codebases;
* more complex runtime failures;
* production-style debugging.

---

# Area C — Python Development

## PY-001 Python Syntax

**Current level:** 3 — Independent Application

The student can read and write ordinary Python programs and understands the syntax required for the concepts currently studied.

This does not imply complete knowledge of the Python language.

---

## PY-002 Data Structures

**Current level:** 3 — Independent Application

The student can use:

* lists;
* tuples;
* dictionaries;
* sets;
* strings.

The student can select between common collection types based on the required behavior.

---

## PY-003 Modules and Packages

**Current level:** 3 — Independent Application

The student can organize a multi-file Python project and understands why code is separated into modules.

Further development:

* packaging;
* distribution;
* dependency management at a larger scale.

---

## PY-004 Virtual Environments and Dependencies

**Current level:** 2 — Guided Application

The student understands the purpose of isolated project environments and can work with the development environment used by the project.

Further independent practice is needed with:

* dependency management;
* reproducible environments;
* package installation and version constraints;
* project packaging.

---

# Area D — Software Engineering

## SE-001 Code Organization

**Current level:** 3 — Independent Application in the current project context

The student can organize code into separate responsibilities and has worked with structures containing presentation, application, domain, and infrastructure concerns.

---

## SE-002 Readable and Maintainable Code

**Current level:** 2–3 — Guided to Independent Application

The student actively considers:

* naming;
* function responsibility;
* separation of concerns;
* duplication;
* readability.

Further practice is needed to apply these principles consistently without external review.

---

## SE-003 Refactoring

**Current level:** 3 — Independent Application in familiar contexts

The student understands refactoring as structural improvement while preserving intended behavior.

The student has used refactoring to improve project architecture and remove unnecessary code.

Further development:

* larger-scale refactoring;
* safely refactoring unfamiliar production code.

---

## SE-004 Documentation

**Current level:** 2–3 — Guided to Independent Application

The student can document project concepts, architectural decisions, and learning conclusions.

Further development is needed in writing concise documentation intended for other developers rather than primarily for personal learning.

---

# Area E — Development Tools

## DT-001 Git

**Current level:** 2–3 — Guided to Independent Application

The student understands version control and uses Git as part of project development.

Further development:

* more complex branching;
* conflict resolution;
* collaborative workflows;
* pull requests and code review workflows.

---

## DT-002 Development Environment

**Current level:** 3 — Independent Application

The student can configure and troubleshoot a Python development environment and has practical experience with:

* Windows;
* PowerShell;
* VS Code;
* Python;
* Neovim;
* project dependencies;
* command-line tooling.

---

## DT-003 Debugging Tools

**Current level:** 2 — Guided Application

The student can use ordinary debugging techniques and development tools.

Further development is needed in systematic use of:

* debuggers;
* profiling;
* logging;
* tracing;
* diagnosis of larger applications.

---

# Area F — Software Design

## SD-001 Object-Oriented Design

**Current level:** 2–3 — Guided to Independent Application

The student understands:

* classes;
* objects;
* dataclasses;
* domain objects;
* composition;
* basic interfaces and polymorphic behavior.

The student is still developing judgment about when object-oriented techniques are actually useful.

---

## SD-002 Architecture Basics

**Current level:** 3 — Independent Application in the current project context

The student understands and has applied concepts including:

* separation of responsibilities;
* presentation boundaries;
* application/use-case layer;
* repositories;
* infrastructure;
* dependency direction;
* multiple application entry points.

This is one of the student's stronger current areas.

The main remaining challenge is transferring these ideas to unfamiliar systems without overengineering.

---

## SD-003 Design Decisions

**Current level:** 2–3 — Guided to Independent Application

The student can compare alternatives and discuss trade-offs.

The student has also learned to question whether an abstraction is actually necessary.

Further development:

* making architectural decisions with less mentor assistance;
* evaluating operational and maintenance costs;
* recognizing when a simpler design is sufficient.

---

# Area G — Persistence and Databases

## DB-001 Relational Data Modeling

**Current level:** 2–3 — Guided to Independent Application

The student understands basic relational concepts and has worked with SQLite schemas and domain-oriented data models.

Further development:

* normalization;
* indexing;
* constraints;
* query planning;
* PostgreSQL.

---

## DB-002 SQL

**Current level:** 2 — Guided Application

The student can work with common SQL operations required by the current projects.

Further development:

* more complex queries;
* joins;
* aggregation;
* indexes;
* transactions;
* query performance;
* database internals.

---

## DB-003 Repository and Persistence Architecture

**Current level:** 3 — Independent Application in the current project context

The student understands the repository boundary and its relationship with application logic and persistence infrastructure.

Further development is needed with more complex persistence scenarios and multiple concurrent operations.

---

## DB-004 Transactions and Unit of Work

**Current level:** 2–3 — Guided to Independent Application

The student understands the purpose of transactional boundaries and the basic Unit of Work pattern.

Further practical experience is needed with:

* transaction failures;
* multiple repositories;
* rollback behavior;
* concurrent operations;
* production database behavior.

---

# Area H — Testing and Quality

## TQ-001 Unit Testing

**Current level:** 2–3 — Guided to Independent Application

The student can write unit tests with pytest and understands the basic Arrange–Act–Assert structure.

---

## TQ-002 Integration Testing

**Current level:** 2 — Guided Application

The student understands the purpose of integration tests and has practical experience testing application components together.

Further development:

* database integration;
* transaction boundaries;
* multi-repository coordination;
* test isolation.

---

## TQ-003 API Testing

**Current level:** 2–3 — Guided to Independent Application

The student can test FastAPI endpoints using `pytest` and `TestClient`.

The student understands that API tests verify behavior across the HTTP boundary rather than only testing individual functions.

---

## TQ-004 Test Doubles

**Current level:** 2 — Guided Application

The student understands the purpose of fakes and has worked with in-memory alternatives to infrastructure dependencies.

Further development:

* choosing between fakes, mocks, and stubs;
* designing effective test boundaries;
* avoiding tests that reproduce implementation details.

---

# Area I — Web and API Development

## WEB-001 HTTP Fundamentals

**Current level:** 2–3 — Guided to Independent Application

The student understands:

* common HTTP methods;
* status codes;
* path parameters;
* query parameters;
* request bodies;
* response bodies.

---

## WEB-002 FastAPI

**Current level:** 2–3 — Guided to Independent Application

The student can create API endpoints and understands FastAPI's role as a presentation-layer technology.

---

## WEB-003 API Architecture

**Current level:** 3 — Independent Application in the current project context

The student understands the API as a translation layer between HTTP and application behavior.

The student has applied the idea of multiple entry points sharing the same application logic.

---

## WEB-004 Authentication and Authorization

**Current level:** 0–1 — Not Yet Developed

The concepts have been identified as future requirements, but they have not yet been developed to a practical level.

Future topics include:

* authentication;
* authorization;
* sessions or tokens;
* role-based access;
* API security.

---

# Area J — Asynchronous Programming

## AS-001 `async` / `await`

**Current level:** 2 — Guided Application

The student understands the basic purpose of asynchronous functions and can follow and implement simple asynchronous examples.

---

## AS-002 Concurrency

**Current level:** 2 — Guided Application

The student understands the difference between concurrency and parallelism and has used `asyncio.gather()` in a simple I/O-oriented example.

Further development is needed in real application scenarios.

---

## AS-003 I/O-Bound vs CPU-Bound Work

**Current level:** 2 — Guided Application

The student understands why asynchronous programming is primarily useful for I/O-bound workloads and why `async` does not automatically make CPU-bound computation faster.

---

# Area K — Project Development

## PD-001 Feature Implementation

**Current level:** 2–3 — Guided to Independent Application

The student can implement features in the current project context and has experience integrating multiple components.

Further development is needed to consistently implement larger features independently from a written specification.

---

## PD-002 Working With Existing Codebases

**Current level:** 2 — Guided Application

The student can understand and modify a project they have already been developing.

Working effectively in a completely unfamiliar production codebase remains a future competency target.

---

## PD-003 Software Planning

**Current level:** 2–3 — Guided to Independent Application

The student can break planned functionality into components, identify architectural concerns, and think about implementation before coding.

Further development:

* estimating work;
* managing scope;
* prioritizing requirements;
* planning changes in unfamiliar systems.

---

# Area L — AI-Assisted Development

## AI-001 AI Collaboration

**Current level:** 3 — Independent Application

The student can formulate technical questions, provide context, request explanations, and use AI as part of the development workflow.

---

## AI-002 Code Evaluation

**Current level:** 2–3 — Guided to Independent Application

The student can identify problems in AI-generated code and does not automatically treat generated code as correct.

The student has explicitly adopted the principle that understanding should precede accepting generated implementation.

---

## AI-003 Independent Decision Making

**Current level:** 3 — Independent Application

The student can decide when AI assistance is useful and when a problem should be solved or reasoned through independently.

A current learning priority is preventing AI from replacing the student's own implementation practice.

---

# 5. Current Strengths

The current competency profile shows several areas that have developed substantially through practical work:

* Python fundamentals;
* decomposition of practical problems;
* modular code organization;
* separation of responsibilities;
* repository-based persistence boundaries;
* application/use-case thinking;
* basic software architecture;
* refactoring;
* pytest fundamentals;
* HTTP and API fundamentals;
* FastAPI presentation-layer concepts;
* AI-assisted development with active evaluation of generated material.

These strengths should be used as foundations for later modules.

They should not be interpreted as evidence that the corresponding subjects are complete.

---

# 6. Current Development Gaps

The main areas requiring further development include:

* deeper SQL and relational database knowledge;
* database transactions and concurrency;
* integration testing;
* test doubles and test isolation;
* independent work in unfamiliar codebases;
* production deployment;
* authentication and authorization;
* HTTP security;
* PostgreSQL;
* migrations;
* observability and logging;
* more advanced Git workflows;
* deeper Python language features;
* algorithmic problem solving;
* asynchronous programming in realistic applications.

These gaps are normal for the current stage and should be addressed progressively rather than all at once.

---

# 7. Junior-Level Competency Model

APMF should **not** treat "Junior Developer" as a single binary achievement determined by completion of a fixed list.

Instead, readiness for junior-level work should be evaluated from a combination of demonstrated abilities.

Relevant evidence includes:

* ability to build and modify small applications;
* understanding of Python fundamentals;
* ability to decompose practical problems;
* ability to work with existing code;
* ability to debug ordinary problems;
* ability to write and run tests;
* understanding of basic software architecture;
* ability to use Git and development tools;
* ability to communicate technical decisions;
* ability to learn unfamiliar technologies;
* ability to work with AI without surrendering responsibility for the resulting code.

The student does not need Level 3 in every possible software-engineering topic before beginning practical junior-level work.

Conversely, completing an advanced topic does not compensate for a major weakness in a foundational skill.

---

# 8. Assessment Rules

## 8.1 Demonstration over exposure

The mentor should distinguish:

```text
"I have seen this"
```

from:

```text
"I understand this"
```

and:

```text
"I can use this independently"
```

These are different states.

---

## 8.2 Do not infer mastery from project size

A large project can contain code written with substantial assistance.

Project size alone is therefore not evidence of independent competency.

Assessment should consider:

* what the student implemented;
* what they can explain;
* what they can modify;
* how they respond when something breaks;
* whether they can reproduce the reasoning independently.

---

## 8.3 Competency is contextual

A student may be Level 3 in a familiar context and Level 2 in an unfamiliar one.

For example:

```text
FastAPI + SQLite + known project
        ↓
higher demonstrated independence

FastAPI + PostgreSQL + unfamiliar architecture
        ↓
lower demonstrated independence
```

This is expected.

---

## 8.4 Advanced topics should not hide foundational gaps

The student may work with advanced architecture or frameworks while still strengthening basic Python or database knowledge.

However, unresolved foundational gaps should eventually be addressed.

The mentor should return to them when they begin to interfere with more advanced work.

---

## 8.5 Reassessment

Competency levels should be updated when new evidence appears.

Useful evidence includes:

* independent exercises;
* project implementations;
* debugging sessions;
* code reviews;
* refactoring tasks;
* tests written without step-by-step instructions;
* explanations of design decisions;
* successful transfer of knowledge to a new problem.

The matrix should therefore be treated as a **living snapshot**, not a permanent record of ability.

---

# 9. Recommended Interpretation

The matrix should answer:

> **"What can the student currently demonstrate, and what should be strengthened next?"**

It should not answer:

> **"What kind of programmer is the student?"**

The purpose of the matrix is to guide learning decisions and expose gaps.

The ultimate objective is not to maximize competency scores.

The objective is to develop the ability to understand problems, design reasonable solutions, implement them, verify their behavior, and improve them through experience.

---

**End of Competency Matrix v0.2**
