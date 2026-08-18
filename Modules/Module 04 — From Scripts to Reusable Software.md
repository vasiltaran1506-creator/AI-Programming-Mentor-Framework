# Module 04 — From Scripts to Reusable Software

**Stage:** 2 — Python Application Foundations  
**Prerequisites:** Module 00, Module 01, Module 02, Module 03  
**Primary language:** Python 3  
**Teaching language:** English  
**Estimated difficulty:** Intermediate Beginner → Intermediate  
**Purpose:** move from organizing multi-file programs to designing reusable, testable, maintainable components.

---

# Module Overview

Module 03 taught how to organize a real Python program:

- filesystem operations;
- `pathlib`;
- modules and imports;
- multi-file programs;
- exceptions;
- JSON;
- configuration;
- validation;
- data boundaries;
- separation of responsibilities.

The next problem appears naturally.

A program can be divided into files and still be difficult to reuse, test, or extend.

For example, a module may contain functions that:

- depend directly on global state;
- read files while performing business logic;
- print results instead of returning them;
- mix validation, transformation, and output;
- are difficult to test without creating real files;
- duplicate the same logic in several places.

Module 04 introduces the next level of software design:

> **How do we design components that are independent, reusable, predictable, and easy to test?**

The central transition is:

```text
Module 02
Use the right Python tool
        ↓
Module 03
Put responsibilities in the right components
        ↓
Module 04
Design components that cooperate through clear interfaces
```

---

# Core Principle

> **A good component should do one thing clearly, depend on as little as possible, and communicate through explicit inputs and outputs.**

The goal is not to create complicated architecture.

The goal is to make simple programs remain understandable as they grow.

---

# Learning Goals

By the end of Module 04, the student should be able to:

1. distinguish pure functions from functions with side effects;
2. identify hidden dependencies;
3. understand local, global, and passed state;
4. design functions around explicit inputs and outputs;
5. understand dependency injection at a beginner/intermediate level;
6. distinguish business logic from I/O;
7. separate transformation from persistence;
8. design reusable components;
9. recognize duplicated logic and unnecessary coupling;
10. understand basic interfaces and abstractions;
11. use type hints to communicate intended contracts;
12. understand `None` as an intentional return value;
13. use `dataclass` for simple structured domain objects;
14. write basic automated tests with `pytest`;
15. design code so that important logic can be tested without external resources;
16. debug failing tests systematically;
17. refactor working code without changing its behavior;
18. recognize when abstraction improves a program and when it only adds complexity.

---

# Methodological Direction

Module 04 should **not** begin with a formal lecture on Object-Oriented Programming.

Classes and OOP may appear later in the module as a tool for solving a concrete design problem.

The student should first experience the limitations of tightly coupled procedural code.

The intended progression is:

```text
Functions
    ↓
State and side effects
    ↓
Dependencies
    ↓
Separation
    ↓
Interfaces
    ↓
Testing
    ↓
Refactoring
    ↓
Simple domain objects
```

The student should discover why these ideas are useful before being asked to memorize terminology.

---

# Chapter 01 — Pure Functions and Side Effects

## 1.1. Two kinds of work

Consider:

```python
def calculate_total(prices):
    return sum(prices)
```

The function receives data and returns a result.

Now compare:

```python
def save_total(total):
    with open("total.txt", "w", encoding="utf-8") as file:
        file.write(str(total))
```

The second function changes something outside itself.

It performs a **side effect**.

---

## 1.2. Pure functions

A pure function has an important property:

> Given the same input, it produces the same output and does not modify external state.

Example:

```python
def add_tax(price, rate):
    return price * (1 + rate)
```

This is easy to reason about.

---

## 1.3. Side effects

Common side effects include:

- writing files;
- reading user input;
- printing;
- modifying external mutable state;
- network requests;
- database operations;
- changing global variables.

Side effects are not bad.

Real programs need them.

The important question is:

> **Where should side effects happen?**

---

## 1.4. The boundary pattern

Instead of:

```text
load file
parse data
calculate
print
save
```

inside one giant function, prefer:

```text
I/O boundary
    ↓
Python data
    ↓
pure processing
    ↓
Python result
    ↓
I/O boundary
```

This makes the central logic easier to understand and test.

---

## 1.5. Practical Exercise

The student receives a program that:

- reads prices from a file;
- calculates totals;
- prints the result;
- writes the result back to another file.

The task is to identify:

1. which operations are pure;
2. which operations have side effects;
3. which parts should be separated.

Do not refactor immediately.

First describe the existing data flow.

---

# Chapter 02 — State and Hidden Dependencies

## 2.1. State

State is information that can change while a program runs.

Examples:

```python
current_user
cart_items
settings
cache
```

The problem is not state itself.

The problem is **uncontrolled state**.

---

## 2.2. Global state

Example:

```python
tax_rate = 0.2

def calculate(price):
    return price * (1 + tax_rate)
```

The function appears to take one argument.

But it actually depends on two pieces of information:

```text
price
tax_rate
```

The second dependency is hidden.

---

## 2.3. Explicit dependencies

Prefer:

```python
def calculate(price, tax_rate):
    return price * (1 + tax_rate)
```

Now the contract is visible.

This leads to a central rule:

> **If a function needs information, prefer passing that information explicitly rather than hiding it in global state.**

---

## 2.4. Why explicit dependencies help

Explicit dependencies make code:

- easier to understand;
- easier to test;
- easier to reuse;
- easier to modify.

For example:

```python
calculate(100, 0.2)
calculate(100, 0.1)
```

The behavior is obvious.

---

## 2.5. Practical Exercise

Given several functions using global variables, identify:

- hidden dependencies;
- state that should remain local;
- state that should be passed as an argument;
- state that genuinely belongs to a broader application component.

The student must explain the reasoning before changing the code.

---

# Chapter 03 — Designing Function Contracts

Module 02 introduced predictable return contracts.

Module 04 extends this idea.

A function should communicate:

```text
What do I give you?
What do you give me?
What assumptions do you make?
What can go wrong?
```

---

## 3.1. Example contract

```python
def find_user(users, user_id):
    ...
```

Possible contract:

```text
Input:
    users — dictionary
    user_id — string

Output:
    user dictionary or None

Errors:
    invalid input structure is not handled here

Responsibility:
    find one user by ID
```

---

## 3.2. `None` as an intentional result

Sometimes absence is a normal result.

Example:

```python
def find_user(users, user_id):
    return users.get(user_id)
```

Possible results:

```python
{"name": "Alice"}
```

or:

```python
None
```

This is different from an unexpected exception.

The important thing is that the contract explicitly defines the behavior.

---

## 3.3. Avoid ambiguous returns

Do not create functions whose result changes shape unpredictably:

```python
# Bad contract
return user
```

in one case and:

```python
return user, metadata
```

in another.

Instead, design one predictable return shape.

---

## 3.4. Type hints

Introduce type hints as communication tools.

Example:

```python
def calculate_total(prices: list[float]) -> float:
    return sum(prices)
```

The annotation communicates intent.

It does not replace validation or runtime reasoning.

---

## 3.5. Type hints are not magic

The student should understand:

```python
def greet(name: str) -> str:
```

does not automatically prevent:

```python
greet(123)
```

Type hints primarily help:

- humans;
- IDEs;
- static analysis;
- documentation.

---

## 3.6. Practical Exercise

Given several poorly specified functions, the student must write:

- input contract;
- output contract;
- possible normal absence;
- possible errors;
- responsibility.

Then add appropriate type hints.

---

# Chapter 04 — Dependency Injection and Testable Design

## 4.1. The problem

Consider:

```python
def load_users():
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)
```

This function is tightly coupled to:

```text
a specific filename
+
the filesystem
+
JSON
```

Testing it requires interacting with the filesystem.

---

## 4.2. Separate acquisition from processing

Instead of:

```python
def get_average_age():
    with open("users.json", ...) as file:
        users = json.load(file)

    return calculate_average(users)
```

separate:

```python
def calculate_average(users):
    ...
```

from:

```python
def load_users(path):
    ...
```

Now the calculation does not care where the users came from.

---

## 4.3. Dependency injection

Dependency injection means, at its simplest:

> **Give a component the things it needs instead of making it find them itself.**

Example:

```python
def save_report(writer, report):
    writer(report)
```

The function does not decide how the report is saved.

Another component provides that dependency.

---

## 4.4. Beginner mental model

Think of a component as a machine.

Bad design:

```text
Machine
 ├── builds its own tools
 ├── finds its own data
 ├── decides where files live
 └── performs the task
```

Better:

```text
Tools ──────┐
Data ───────┼──→ Machine ──→ Result
Settings ───┘
```

The machine focuses on its actual responsibility.

---

## 4.5. Do not overuse dependency injection

Dependency injection is useful when a dependency:

- varies between environments;
- makes testing difficult;
- represents an external resource;
- needs to be replaced or mocked.

Do not create elaborate injection systems for trivial functions.

---

## 4.6. Practical Exercise

Refactor a function that:

- reads a JSON file;
- processes the data;
- saves the result.

The student should separate:

```text
loading
processing
saving
```

Then explain which dependencies remain external.

---

# Chapter 05 — Automated Testing with pytest

## 5.1. Why tests?

A program can appear to work while still containing bugs.

Manual testing repeatedly requires:

```text
run
enter input
observe
repeat
```

Automated tests allow the computer to repeat known checks.

---

## 5.2. The basic test

Example:

```python
def add(a, b):
    return a + b
```

Test:

```python
def test_add():
    assert add(2, 3) == 5
```

The important idea is:

```text
Arrange
Act
Assert
```

---

## 5.3. What makes a good first test?

A beginner test should:

- test one behavior;
- use predictable inputs;
- have a clear expected result;
- fail when the behavior is broken.

---

## 5.4. Testing pure functions

Pure functions are particularly easy to test.

Example:

```python
def normalize_name(name):
    return name.strip().title()
```

Tests can cover:

```python
assert normalize_name(" alice ") == "Alice"
assert normalize_name("BOB") == "Bob"
```

---

## 5.5. Edge cases

Testing should not only cover the happy path.

Consider:

```python
def average(numbers):
    return sum(numbers) / len(numbers)
```

What happens with:

```python
[]
```

The student should identify the edge case before writing the test.

---

## 5.6. Testing failure behavior

If a function is designed to raise an exception, test that contract explicitly.

Example:

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

The exact testing syntax should be taught when needed rather than memorized without context.

---

## 5.7. Practical Exercise

Create a small module containing several pure functions.

Write tests for:

- normal cases;
- boundary cases;
- invalid inputs where the contract specifies an error.

The student should run the test suite and intentionally introduce one bug to observe a failing test.

---

# Chapter 06 — Testing Components with External Dependencies

Pure functions are easy.

Real programs interact with:

- files;
- environment variables;
- clocks;
- network services;
- databases.

The question becomes:

> How can we test our logic without depending on the entire external world?

---

## 6.1. Test the boundary separately

For example:

```text
File loader
     ↓
Python data
     ↓
Processor
```

Test the processor with ordinary Python data.

Test the loader separately.

This is often simpler than mocking everything.

---

## 6.2. Mock data

Module 02 introduced mock data as an engineering practice.

Module 04 extends it:

```python
users = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 30},
]
```

The processor can be tested without creating real application files.

---

## 6.3. Temporary resources

When filesystem behavior itself must be tested, tests can use temporary files and directories.

The student should learn the principle:

> Tests should create and clean up their own temporary environment.

The exact `pytest` fixtures can be introduced when the need arises.

---

## 6.4. Practical Exercise

Take the file analyzer from Module 03.

Create two layers:

```text
filesystem layer
processing layer
```

Write tests for the processing layer without reading real files.

Then add a small integration test for the filesystem layer.

---

# Chapter 07 — Dataclasses and Domain Objects

Only after the student has experienced increasingly complex dictionaries should structured domain objects be introduced.

## 7.1. The problem with large dictionaries

A dictionary can represent:

```python
user = {
    "name": "Alice",
    "age": 21,
    "email": "alice@example.com",
}
```

This is useful.

But in a larger program, repeated knowledge about the required keys becomes fragile.

---

## 7.2. `dataclass`

Introduce:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str
```

Now:

```python
user = User(
    name="Alice",
    age=21,
    email="alice@example.com",
)
```

---

## 7.3. What a dataclass provides

At this stage, focus on:

- named fields;
- clearer structure;
- readable representation;
- convenient initialization;
- type annotations.

Do not yet turn the class into a large collection of methods.

---

## 7.4. Dataclass vs dictionary

Use a dictionary when:

- the structure is flexible;
- keys are dynamic;
- the data is naturally map-like.

Consider a dataclass when:

- the structure is known;
- fields have stable meanings;
- the same domain object appears throughout the program.

---

## 7.5. Practical Exercise

Convert a small dictionary-based data model into a dataclass.

Then identify:

- what became clearer;
- what became less flexible;
- whether the conversion is actually justified.

The student must understand that dataclasses are a tool, not a mandatory replacement for dictionaries.

---

# Chapter 08 — Refactoring Without Changing Behavior

## 8.1. What is refactoring?

Refactoring means:

> changing the internal structure of code without intentionally changing its externally observable behavior.

Example:

```text
Before
one large function
        ↓
After
three focused functions
```

The program should still produce the same result.

---

## 8.2. Why tests matter

Tests provide a safety net.

```text
Working program
      ↓
Write tests
      ↓
Refactor
      ↓
Run tests
      ↓
Behavior preserved
```

This connects two major ideas:

```text
design
+
testing
=
safer change
```

---

## 8.3. Refactoring targets

The student should learn to recognize:

- duplicated logic;
- functions doing too many things;
- hidden global dependencies;
- unclear names;
- unnecessary nesting;
- mixed I/O and business logic;
- overly large modules;
- functions with unclear contracts.

---

## 8.4. Do not refactor for aesthetics alone

Not every repeated line needs a new abstraction.

A useful question:

> **Does this change make the program easier to understand, test, or modify?**

If not, leave it alone.

---

# Chapter 09 — Abstraction Without Overengineering

This chapter is deliberately conceptual.

The student has now encountered:

- functions;
- modules;
- dependencies;
- interfaces;
- dataclasses;
- tests;
- refactoring.

The danger is learning the wrong lesson:

> “Good programmers create lots of classes and abstractions.”

That is not the goal.

---

## 9.1. Abstraction

An abstraction hides unnecessary implementation details behind a simpler interface.

Example:

```python
users = load_users(path)
```

The caller does not need to know:

- how the file is opened;
- how JSON is parsed;
- how encoding is handled.

---

## 9.2. Good abstraction

A good abstraction:

- hides complexity;
- has a clear purpose;
- reduces duplication;
- makes the caller simpler.

---

## 9.3. Bad abstraction

A bad abstraction:

- adds layers without reducing complexity;
- exists only because “professional code needs it”;
- makes simple operations difficult to follow;
- requires understanding many files for a trivial task.

---

## 9.4. Rule

> **Do not abstract because you can. Abstract because the abstraction solves a real problem.**

---

# Chapter 10 — Final Integrated Project

The final project combines Module 03 and Module 04.

## Scenario

Build a small data-processing application.

The exact domain should be selected by the student.

Possible domains:

- inventory;
- books;
- tasks;
- datasets;
- image metadata;
- equipment;
- expenses.

The domain should preferably be relevant to the student's own projects.

---

# Required Architecture

The student must design the architecture independently.

The final program should contain clear separation between:

```text
Input / I/O
      ↓
Validation
      ↓
Domain data
      ↓
Business logic
      ↓
Output / persistence
```

The exact number of modules is **not prescribed**.

---

# Required Features

The project must demonstrate:

- `pathlib`;
- JSON or another simple persistence format already studied;
- multiple modules;
- explicit function contracts;
- validation;
- appropriate exception handling;
- at least several pure functions;
- separation of I/O and processing;
- type hints on important functions;
- automated tests;
- at least one edge-case test;
- at least one failure-path test;
- at least one refactoring step after tests exist.

A `dataclass` should be used if the domain model genuinely benefits from one.

It should not be added merely to satisfy a checklist.

---

# Development Process

The student must work through these stages:

## Stage 1 — Problem Definition

Describe:

- what the program does;
- who uses it;
- what data enters it;
- what output it produces.

## Stage 2 — Data Model

Identify:

- entities;
- collections;
- relationships;
- persistent data.

## Stage 3 — Component Design

Describe:

- modules;
- responsibilities;
- dependencies.

## Stage 4 — Function Contracts

For important functions:

```text
Input:
Output:
Normal absence:
Possible errors:
Side effects:
Responsibility:
```

## Stage 5 — Implementation

Write the smallest working version.

## Stage 6 — Tests

Test important behavior.

## Stage 7 — Refactoring

Identify at least one real design problem and improve it.

## Stage 8 — Review

The student explains the final architecture without reading prepared notes.

---

# Final Assessment

The final project should be completed with limited mentor intervention.

Qwen should not immediately provide implementation code when the student asks:

> “How should I write this?”

Instead, determine whether the student has:

1. defined the responsibility;
2. defined the input;
3. defined the output;
4. identified dependencies;
5. chosen the appropriate data structure.

If those are unclear, return to design.

If they are clear and the issue is syntax, provide a small hint.

---

# Module 04 Competencies

## PF-010 — Pure Functions and Side Effects

Student can:

- identify side effects;
- write simple pure functions;
- separate pure processing from I/O.

**Target:** Level 3.

---

## PF-011 — Explicit Dependencies

Student can:

- identify hidden dependencies;
- pass important dependencies explicitly;
- avoid unnecessary global state.

**Target:** Level 3.

---

## PF-012 — Function Contracts

Student can:

- define inputs;
- define outputs;
- use predictable return shapes;
- use `None` intentionally;
- add useful type hints.

**Target:** Level 3.

---

## PF-013 — Testable Design

Student can:

- separate external dependencies from core logic;
- design code that can be tested with mock data;
- distinguish unit-level and integration-level testing conceptually.

**Target:** Level 2–3.

---

## PF-014 — Automated Testing

Student can:

- write basic `pytest` tests;
- use assertions;
- test normal behavior;
- test edge cases;
- test defined failure behavior;
- interpret test failures.

**Target:** Level 3.

---

## PF-015 — Domain Modeling

Student understands:

- when dictionaries are sufficient;
- when a `dataclass` provides clearer structure;
- that domain objects should represent meaningful concepts.

**Target:** Level 2–3.

---

## PF-016 — Refactoring

Student can:

- identify duplicated or overly coupled code;
- refactor incrementally;
- use tests as a safety net;
- explain what behavior should remain unchanged.

**Target:** Level 2–3.

---

# Module 04 Methodological Rules

## Rule 1 — Experience Before Terminology

When possible, let the student encounter the problem first.

Example:

```text
large function
↓
hard to test
↓
separate logic
↓
discover pure functions
```

Only then formalize the concept.

---

## Rule 2 — Do Not Turn OOP Into Memorization

Classes should be introduced as a response to a modeling problem.

Do not begin with:

- inheritance;
- polymorphism;
- design patterns;
- abstract base classes.

Those topics are outside the core purpose of this module.

---

## Rule 3 — Test the Reasoning, Not Just the Code

When a test fails, ask:

```text
What behavior did you expect?
What actually happened?
What does the failure tell you?
```

Do not immediately reveal the corrected code.

---

## Rule 4 — Prefer Small Interfaces

If a component can have:

```python
process(data) -> result
```

do not introduce five parameters and three global variables without a reason.

---

## Rule 5 — Keep Dependencies Visible

When reviewing code, repeatedly ask:

> “Where does this function get the information it needs?”

---

## Rule 6 — Refactor Only With a Reason

A refactor should solve a real problem:

- duplication;
- coupling;
- unclear responsibility;
- difficult testing;
- difficult modification.

---

## Rule 7 — Preserve the Student's Architecture

The student should make architectural decisions.

Qwen should evaluate them, not automatically replace them with its preferred design.

---

# Practical Projects

## Project A — Pure Data Processor

Build a small library of pure functions that:

- filter;
- transform;
- aggregate;
- sort;
- validate data.

No file I/O inside the processing functions.

---

## Project B — Testable File Processor

Build:

```text
loader
processor
writer
```

Then test the processor independently.

---

## Project C — Domain Model

Represent a small real-world domain using dictionaries first.

Then determine whether a `dataclass` improves the design.

---

## Project D — Refactoring Challenge

Qwen provides a deliberately messy but functioning program containing:

- global state;
- duplicated logic;
- mixed I/O and processing;
- unclear function contracts.

The student must diagnose and refactor it without changing its behavior.

---

# Expected Learning Journal Additions

After Module 04, Qwen should update `Learning Journal.md`.

The journal should record:

- the student's first clear understanding of pure functions;
- how the student learned to identify side effects;
- examples of hidden dependencies;
- whether dependency injection became intuitive;
- first experiences writing automated tests;
- important debugging discoveries;
- whether `dataclass` genuinely improved understanding of domain models;
- the student's attitude toward refactoring;
- examples of overengineering or unnecessary abstraction;
- the most important architectural breakthrough of the module.

---

# Expected Development Log Additions

Qwen should continue tracking previous patterns:

- type confusion;
- missing method parentheses;
- indentation;
- inconsistent return contracts;
- architecture vs syntax gap.

New patterns:

## Dependency Awareness

Does the student recognize when a function depends on external state?

## Testability Awareness

Does the student naturally ask:

> “How would I test this?”

## Abstraction Judgment

Does the student distinguish useful abstraction from unnecessary complexity?

## Refactoring Discipline

Does the student change code incrementally and verify behavior after each meaningful change?

---

# Questions to Track

New questions should be added to `Questions.md` when they genuinely arise.

Potential questions that may naturally emerge:

### Q-0006
**What exactly makes a function pure?**

Status:

```text
Open
```

---

### Q-0007
**What is dependency injection really solving?**

Status:

```text
Open
```

---

### Q-0008
**How does pytest discover and execute tests?**

Status:

```text
Open
```

---

### Q-0009
**When should I use a dataclass instead of a dictionary?**

Status:

```text
Open
```

These questions should **not** be marked as mastered merely because the topic was mentioned.

They should be closed only when the student can explain and apply the concept independently.

---

# Completion Criteria

Module 04 is complete when the student can independently design and implement a small Python application that:

- contains multiple modules;
- has clear component responsibilities;
- keeps important business logic independent from I/O;
- uses explicit dependencies;
- has predictable function contracts;
- uses type hints appropriately;
- contains automated tests;
- handles defined failure cases;
- tests edge cases;
- uses a structured domain model when justified;
- can be refactored safely;
- avoids unnecessary abstraction.

Most importantly, the student must be able to explain:

> **What depends on what, why those dependencies exist, where side effects occur, and how the program can be tested.**

---

# Final Conceptual Transition

Module 03 taught:

> **A real program needs structure.**

Module 04 teaches:

> **Good structure makes change safer.**

The student should finish the module understanding this progression:

```text
Working code
    ↓
Understandable code
    ↓
Separated responsibilities
    ↓
Explicit dependencies
    ↓
Testable components
    ↓
Safe refactoring
    ↓
Maintainable software
```

The objective is not to produce “professional-looking” architecture.

The objective is to develop the engineering instinct to ask:

> **“If I need to change this tomorrow, how difficult will that be?”**

That question should become one of the student's core programming habits.
