# Mental Models

**Version:** 2.0

**Status:** Active

**Last Updated:** After Module 09

---

# Purpose

Programming is easier to learn when abstract concepts are connected to intuitive mental images.

This document collects the mental models that have become useful during the course of the APMF.

A mental model is **not a formal definition**.

It is a simplified way of thinking that helps build intuition and make technical decisions.

Some models are intentionally incomplete. Their purpose is to make relationships between concepts easier to see, not to replace precise technical definitions.

As the student's understanding develops, a mental model may be refined or replaced. A newer model should not automatically be considered "more correct"; it should simply explain the concept more accurately at the current level of understanding.

---

# Python Fundamentals

## Variable

A variable is a **label attached to an object**.

Imagine a room full of objects.

You take a sticker and write:

```text
score
```

Then you attach it to an object:

```text
score
  │
  ▼
 10
```

Later:

```text
score
  │
  ▼
 25
```

The label changed what it refers to.

The important idea is that the variable name itself is not the value.

This model becomes especially useful when thinking about mutable objects, references, and assignment.

---

## Assignment (`=`)

Assignment is **not equality**.

It is an instruction:

> Evaluate the expression on the right and bind the name on the left to the resulting object.

For example:

```python
health = 100
```

Think:

```text
evaluate 100
     ↓
bind "health"
     ↓
   object
```

Do not read `=` as:

> "health is permanently equal to 100."

A later assignment can bind the same name to another object.

---

## Data Types

Think of a type as a set of rules describing what kind of object something is and what operations are meaningful for it.

For example:

```text
int
 └── whole-number operations

str
 └── text operations

list
 └── ordered mutable collection operations
```

Different types support different operations.

The useful mental model is not simply "different containers", but:

> **A type tells Python how an object should behave under particular operations.**

---

## Mutable vs Immutable

Think of an object as a physical object.

An immutable object is like a document printed on paper.

If you want a different document, you create another one.

A mutable object is more like a whiteboard.

The same object can be changed while remaining the same object.

This distinction becomes important when several variables refer to the same object.

```text
a ──┐
    ├──> mutable object
b ──┘
```

If the object changes through `a`, `b` can observe the same change because both names refer to the same object.

---

## Input

Input is a conversation between the program and something outside the program.

For console input:

```text
Program
   ↓
Question
   ↓
Waiting
   ↓
Answer
   ↓
Program continues
```

More generally, input is any data entering the program from an external source:

* user input;
* a file;
* a database;
* an HTTP request;
* another service;
* a device.

---

## `print()`

Imagine a loudspeaker.

The program sends information to the loudspeaker:

```text
Program
   ↓
print()
   ↓
Screen
```

`print()` produces an observable side effect.

It does **not** return the displayed text to the caller.

This distinction is important:

```python
print("hello")
```

and

```python
return "hello"
```

serve different purposes.

---

## `return`

Imagine a factory.

```text
Input
  ↓
Function
  ↓
Processing
  ↓
Output
```

`return` is the mechanism by which a function gives a result back to its caller.

The returned value can continue through the rest of the program:

```python
result = calculate(...)
```

A useful distinction is:

```text
print  → communicate with an external observer

return → communicate with the caller
```

---

## Function

A function is a **named piece of behavior with a defined interface**.

The simplest model is:

```text
Input
  ↓
Function
  ↓
Output
```

But a real function may also:

* change state;
* perform I/O;
* call other functions;
* raise an exception.

Therefore the simple "machine" model is useful, but incomplete.

A good function interface makes it possible to understand how to use the function without immediately knowing every implementation detail.

---

## Parameters and Arguments

Parameters are placeholders in a function definition.

Arguments are the actual values supplied during a call.

```python
def greet(name):
    ...
```

Here `name` is a parameter.

```python
greet("Alice")
```

Here `"Alice"` is an argument.

Mental model:

```text
Function definition
       ↓
   parameter
       ↓
placeholder

Function call
       ↓
   argument
       ↓
actual value
```

---

## List

Imagine an ordered row of numbered storage compartments:

```text
0   1   2   3   4
│   │   │   │   │
A   B   C   D   E
```

A list preserves order and allows access by position.

Python uses zero-based indexing, so the first element is at index `0`.

---

## Index

An index identifies a position inside an ordered collection.

```python
students[3]
```

means:

> Give me the element at position `3`.

Because Python starts counting from zero, this is the **fourth** element.

---

## Dictionary

Think of a dictionary as a collection of labeled drawers.

Instead of asking:

> "Give me item number 3."

you ask:

> "Give me the item associated with this key."

```text
"name"  ──> "Alice"
"age"   ──> 21
"role"  ──> "worker"
```

The key provides a way to locate the associated value.

This makes dictionaries especially useful when data is naturally described by names rather than positions.

---

## Set

Think of a set as a collection where membership matters more than position.

```text
{"red", "green", "blue"}
```

The central question is:

> "Is this element a member of the collection?"

Sets are therefore useful for membership checks and operations such as union, intersection, and difference.

---

# Control Flow

## Loop

Imagine walking through every room in a building.

```text
Room 1
  ↓
Room 2
  ↓
Room 3
  ↓
Room 4
```

A loop repeatedly performs some operation while moving through a sequence or while a condition remains true.

The exact stopping rule depends on the kind of loop.

---

## `for`

A `for` loop is useful when you want to process the elements of an iterable.

```python
for item in items:
    process(item)
```

Mental model:

> Take the next item, perform the action, then continue with the next item.

```text
item 1 → action
item 2 → action
item 3 → action
...
```

---

## `while`

Imagine waiting at a train station.

Every cycle you ask:

```text
Has the train arrived?
```

If not:

```text
wait
↓
check again
↓
wait
↓
check again
```

A `while` loop repeats while its condition remains true.

The important question when designing one is:

> **What changes between iterations so that the condition eventually becomes false?**

---

# Program State

Imagine freezing a running program at one exact moment.

Everything that currently exists and matters to the program forms its state:

* variable bindings;
* object contents;
* collection contents;
* application data;
* external resources and their relevant state.

Programming can often be understood as:

```text
State A
   ↓
operation
   ↓
State B
   ↓
operation
   ↓
State C
```

This model becomes especially useful when thinking about databases, transactions, tests, and bugs.

---

# Algorithm

An algorithm is a **procedure for transforming inputs into a desired result**.

The recipe analogy is useful:

```text
Ingredients → Recipe → Meal
Input       → Algorithm → Output
```

Different algorithms can solve the same problem.

They may differ in:

* clarity;
* correctness;
* performance;
* memory usage;
* complexity;
* suitability for the particular context.

---

# Problem Decomposition

Imagine building a house.

Instead of thinking:

```text
Build house
```

break the problem down:

```text
Foundation
   ↓
Walls
   ↓
Roof
   ↓
Windows
   ↓
Doors
   ↓
Interior
```

Software problems work similarly.

A large problem becomes manageable when divided into smaller problems with clear responsibilities.

A useful decomposition question is:

> **What smaller thing can I understand, implement, and test independently?**

---

# Separation of Concerns

Imagine a restaurant.

```text
Customer
   ↓
Waiter
   ↓
Kitchen
   ↓
Chef
```

The waiter does not need to cook the food.

The chef does not need to manage every customer interaction.

Different parts of the system have different responsibilities.

In software, separation of concerns means keeping conceptually different responsibilities from becoming unnecessarily mixed together.

It does **not** mean that every function, class, or file must contain exactly one tiny responsibility.

The goal is to make responsibilities understandable and changeable.

---

# Pure Function

Imagine a calculator.

You give it:

```text
2 + 3
```

and it produces:

```text
5
```

It does not modify the outside world.

If you call it again with the same inputs, you get the same result.

Mental model:

```text
Input
  ↓
Pure Function
  ↓
Output
```

Pure functions are useful because they are easy to reason about and test.

Not every useful function needs to be pure. Applications inevitably contain side effects.

---

# Side Effect

A side effect is an interaction with state or the outside world beyond simply producing a returned value.

Examples:

* writing to a file;
* modifying a database;
* printing;
* sending an HTTP request;
* changing a mutable object;
* modifying application state.

Mental model:

```text
Function
   ↓
Result

and/or

Function
   ↓
Change outside itself
```

A useful architectural goal is not to eliminate side effects, but to **keep them in understandable places**.

---

# Dependency

Imagine a restaurant dish that requires a particular ingredient.

The dish depends on that ingredient.

Software components similarly depend on other components.

For example:

```text
Use Case
   ↓
Repository
   ↓
Database
```

The use case depends on something that can provide repository behavior.

Making dependencies explicit makes a system easier to understand, replace, and test.

---

# Dependency Injection

Imagine a coffee machine that does not go to the warehouse itself to buy coffee beans.

Instead, someone gives it the beans.

The machine can then operate without knowing where they came from.

In software:

```text
Application
    ↑
dependency supplied from outside
```

This is the basic intuition behind dependency injection.

It is particularly useful when production code needs a real dependency while tests need a fake or in-memory one.

---

# Business Logic vs I/O

Imagine a warehouse worker deciding:

> "Can this equipment be issued?"

That is a business decision.

Now imagine actually recording the issue in SQLite.

That is I/O.

Mental model:

```text
Business decision
       ↓
Application logic
       ↓
I/O boundary
       ↓
Database / File / HTTP / etc.
```

Keeping these concerns distinguishable makes business rules easier to test and change.

---

# Repository

Imagine a warehouse clerk who knows how to retrieve and store equipment records.

The rest of the application does not need to know whether the clerk stores the records:

* in SQLite;
* PostgreSQL;
* memory;
* or somewhere else.

The repository is the boundary through which application code accesses persisted data.

Mental model:

```text
Application
    ↓
Repository interface / contract
    ↓
Persistence implementation
    ↓
Database
```

A repository is not "the database".

It is an abstraction around the application's interaction with persisted data.

---

# Use Case

Imagine a worker receiving a request:

> "Issue these pieces of equipment for this order."

The worker must coordinate several steps:

```text
Receive request
     ↓
Check conditions
     ↓
Load required data
     ↓
Apply business rules
     ↓
Coordinate changes
     ↓
Return result
```

A **Use Case** represents an application-level action that produces a meaningful outcome.

It is more useful to think of a use case as a unit of application behavior than simply as "a function with a fancy name."

---

# Thick Use Case

A use case should not necessarily be a thin proxy that simply forwards a call to a repository.

When an operation contains meaningful application rules or coordinates several components, the use case can act as the place where that orchestration lives.

For example:

```text
Issue Equipment
      ↓
Load equipment
      ↓
Check availability
      ↓
Create movement
      ↓
Update required state
      ↓
Commit
```

The exact distribution of logic depends on the domain.

The important question is:

> **Where should this decision live so that the application remains understandable and the rule is not duplicated?**

---

# Domain Entity vs Read Model

Imagine two different views of the same warehouse.

One view is designed to **change equipment state**.

Another view is designed to **show a convenient report**.

They may contain overlapping information without serving the same purpose.

```text
Domain Entity
    ↓
represents something the application operates on

Read Model
    ↓
represents data shaped for reading
```

The same real-world concept can therefore have different representations for different tasks.

This distinction becomes useful when a database query returns a convenient reporting structure that should not automatically become the application's domain object.

---

# Transaction

Imagine a warehouse operation that consists of several changes:

```text
Remove equipment from available stock
        ↓
Create movement record
        ↓
Update order state
```

Suppose the second operation succeeds but the third fails.

The database could be left in an inconsistent intermediate state.

A transaction provides the mental model:

```text
Start
  ↓
Change A
  ↓
Change B
  ↓
Change C
  ↓
Commit
```

or, if something fails:

```text
Start
  ↓
Change A
  ↓
Change B
  ↓
Failure
  ↓
Rollback
```

The purpose is to make a group of changes behave as one atomic unit according to the database's transaction semantics.

---

# Unit of Work

Imagine a coordinator responsible for a single business operation.

Several repositories may participate:

```text
Equipment Repository
        \
         \
          → Unit of Work → Transaction
         /
        /
Order Repository
```

The Unit of Work mental model is:

> Several related persistence operations belong to one application-level operation and should share one transactional boundary.

It becomes particularly useful when a use case coordinates changes across multiple repositories.

---

# Application Shell

Imagine a building with one internal system and several entrances.

The building contains the actual application behavior.

Different entrances provide different ways to interact with it.

```text
CLI ─────────┐
             │
HTTP API ────┼──→ Application
             │
Other UI ────┘
```

The "shell" or entry-point layer handles interaction with the outside world.

The core application logic should not need to know whether the request originally came from a CLI command or an HTTP request.

---

# HTTP API

An HTTP API is another **entrance into the application**.

Think of a building:

```text
CLI entrance ──┐
               │
HTTP entrance ─┼──→ Application
               │
Other entrance ┘
```

The API does not need to become the application's business logic.

Its main job is to translate between HTTP and application-level concepts.

```text
HTTP Request
     ↓
Presentation Layer
     ↓
Use Case
     ↓
Application Result
     ↓
Presentation Layer
     ↓
HTTP Response
```

This mental model is central to the current architecture understanding.

---

# HTTP Endpoint as Translator

An endpoint can be viewed as a translator.

It translates:

```text
HTTP world
    ↓
Path
Query
Body
Headers
    ↓
Application world
```

and then translates the result back:

```text
Application result
    ↓
HTTP status
JSON response
    ↓
HTTP world
```

The endpoint should therefore not automatically become the place where business rules live.

---

# Path, Query and Body

Think of an HTTP request as arriving with three different baskets of information.

### Path

Identifies **which resource** is being addressed.

```text
/equipment/42
```

Here `42` identifies a particular equipment item.

### Query

Modifies or describes the request.

```text
/equipment?status=available
```

### Body

Contains data being submitted as part of the operation.

```json
{
    "quantity": 3
}
```

A useful question is:

> Is this value identifying the resource, filtering the request, or supplying the data of the operation?

That question often reveals where the value belongs.

---

# HTTP Methods

Think of HTTP methods as expressing the intention of a request.

```text
GET
  → retrieve

POST
  → create / trigger an operation

PATCH
  → partially modify

DELETE
  → remove
```

These are semantic conventions, not Python functions.

The application layer should not become tightly coupled to the HTTP method itself.

---

# HTTP Status Codes

Think of an HTTP response as a compact description of what happened.

Examples:

```text
200 → successful request

201 → resource successfully created

204 → successful request with no response body

404 → requested resource was not found

409 → request conflicts with current state

422 → request data failed validation

500 → unexpected server-side failure
```

The exact status code should communicate the outcome of the HTTP operation without exposing unnecessary internal implementation details.

---

# Pydantic at the HTTP Boundary

Think of Pydantic as a **bouncer at the entrance**.

External data arrives:

```text
HTTP Request
     ↓
Pydantic validation
     ↓
Accepted structured data
     ↓
Application
```

The boundary validates the shape and basic constraints of incoming data before that data enters deeper layers.

This helps keep malformed external input from spreading through the application.

Pydantic validation is not a replacement for business rules.

For example:

```text
Pydantic:
"quantity is an integer"

Business logic:
"this quantity cannot exceed available stock"
```

Those are different responsibilities.

---

# Result Pattern

Imagine a use case returning a structured report instead of speaking HTTP directly.

```text
Use Case
   ↓
Result
   ├── success
   ├── status
   └── details
```

For example:

```text
equipment_not_found
not_enough_stock
success
```

The HTTP layer can then translate the application result into an appropriate HTTP response.

Mental model:

```text
Use Case
   ↓
Application Result
   ↓
CLI / HTTP / other presentation layer
```

This helps prevent application logic from becoming dependent on one particular presentation mechanism.

---

# Multiple Entry Points

A useful architecture model is:

```text
                 ┌── CLI
                 │
External Input ──┼── HTTP API
                 │
                 └── Other UI
                       │
                       ▼
                 Application
                       │
                ┌──────┴──────┐
                ▼             ▼
           Repositories    Services
                │
                ▼
             Database
```

The important idea is that multiple entry points can lead to the same application behavior.

Adding an API therefore does not automatically mean rewriting the business logic.

---

# Testing

Think of tests as **controlled experiments**.

Instead of asking:

> "Does this code look correct?"

you construct a situation where the expected behavior is known.

```text
Arrange
   ↓
Act
   ↓
Assert
```

A test is an executable statement about expected behavior.

---

# Unit Test

Imagine testing one component in isolation.

```text
Input
  ↓
Component
  ↓
Expected result
```

Dependencies that are not relevant to the behavior under test can sometimes be replaced with fakes or other test doubles.

The goal is fast, focused feedback.

---

# Integration Test

An integration test checks how multiple real components work together.

For example:

```text
Use Case
   ↓
Repository
   ↓
SQLite
```

The important difference from a unit test is not simply the number of lines or classes involved.

It is the fact that real component boundaries are being exercised together.

---

# Test Isolation

Imagine running an experiment in a clean laboratory.

Each experiment should start from a known state.

If one test leaves behind database records that affect the next test, the results become difficult to trust.

Mental model:

```text
Test A
  ↓
cleanup / isolated state
  ↓
Test B
  ↓
cleanup / isolated state
  ↓
Test C
```

Isolation makes failures easier to reproduce and understand.

---

# Fake

A fake is a simplified working implementation used in place of a real dependency.

For example:

```text
Production:
Use Case → SQLite Repository

Test:
Use Case → In-Memory Fake Repository
```

The fake should reproduce the relevant behavior required by the test.

A fake is not merely "mock data"; it is a substitute implementation.

---

# Refactoring

Imagine cleaning a workshop.

No new product is being created.

The goal is to improve the organization of the existing workshop so that future work becomes easier and safer.

Refactoring changes the internal structure while preserving the intended external behavior.

Mental model:

```text
Same behavior
      +
better structure
      =
refactoring
```

---

# Dead Code

Imagine a warehouse shelf containing boxes that nobody uses.

They occupy space, create confusion, and make it harder to understand what is actually important.

Dead code is similar.

Examples include:

* unused functions;
* obsolete classes;
* abandoned abstractions;
* unreachable branches;
* old compatibility code that is no longer needed.

Removing dead code is not merely cosmetic. It reduces the number of things a developer must understand.

---

# Overengineering

Imagine building a complex industrial machine to solve a problem that could be handled by a simple hand tool.

The complex solution may be technically impressive while still being inappropriate for the actual problem.

The mental model is:

```text
Problem
  ↓
Required complexity
```

not:

```text
Available technology
  ↓
Find a place to use it
```

A pattern, abstraction, framework, or architecture should solve a real problem.

Useful questions:

* What problem does this abstraction solve?
* What complexity does it introduce?
* Is the problem actually present?
* Will the design make the next change easier?
* Is the added flexibility worth its cost?

---

# Architecture

Architecture can be viewed as the **structure of responsibilities and dependencies in a system**.

A useful high-level model is:

```text
External world
      ↓
Presentation / Entry Point
      ↓
Application behavior
      ↓
Domain rules
      ↓
Infrastructure
      ↓
External systems
```

The exact number and names of layers can vary.

The important question is:

> **Where does a particular responsibility belong, and what would have to change if that responsibility changed?**

---

# Change as an Architectural Test

One of the most useful architecture questions is:

> **What changes if this requirement changes?**

For example:

```text
CLI → HTTP
```

If adding HTTP requires rewriting business rules, the boundary between presentation and application behavior may be too weak.

If changing SQLite to another persistence technology requires rewriting business logic, the persistence boundary may be too weak.

Architecture can therefore be evaluated not only by diagrams, but by the changes the system allows without unnecessary modification elsewhere.

---

# Error

An error is information about a mismatch between the expected and actual state of the program.

A useful mental model is:

```text
Expected
   ↓
Actual
   ↓
Difference
   ↓
Evidence
```

Not every error should be treated as an exceptional catastrophe.

Some errors are normal outcomes of application operations:

```text
equipment_not_found
not_enough_stock
invalid_input
```

The application should represent such outcomes deliberately when appropriate.

---

# Exception

An exception is a mechanism for interrupting the normal flow when an operation cannot continue through its ordinary path.

The useful mental model is:

```text
Normal flow
    ↓
operation
    ↓
result
```

versus:

```text
Normal flow
    ↓
unexpected / exceptional condition
    ↓
exception
    ↓
handled at an appropriate boundary
```

Exceptions should not automatically be used for every condition that is merely an expected business outcome.

---

# Debugging

Imagine being a detective.

The computer does not "randomly" produce an incorrect result.

There is a chain of causes.

The debugging process is:

```text
Symptom
  ↓
Observation
  ↓
Hypothesis
  ↓
Experiment
  ↓
Evidence
  ↓
Narrower hypothesis
  ↓
Cause
```

The important habit is to replace guessing with evidence.

---

# AI Assistant

Think of AI as an experienced technical colleague.

It can:

* explain;
* suggest;
* review;
* compare alternatives;
* find mistakes;
* accelerate routine work.

But the student remains responsible for understanding the resulting system.

The most important boundary is:

```text
AI generates information
        ↓
Student evaluates it
        ↓
Student understands it
        ↓
Student makes the decision
```

For learning, copying a complete implementation from AI can bypass the exact thinking that the exercise is intended to develop.

The useful question is therefore not:

> "Can AI write this?"

but:

> **"What part of this problem do I need to understand and be able to solve myself?"**

---

# Programming as Translation

A recurring mental model across the entire curriculum is **translation between levels of abstraction**.

For example:

```text
Real-world problem
       ↓
Conceptual model
       ↓
Application behavior
       ↓
Python objects/functions
       ↓
Database / HTTP / OS operations
```

Each layer expresses the same underlying problem in a different language.

Good engineering often means keeping those translations explicit instead of allowing one layer's concepts to leak uncontrollably into another.

---

# Async and Concurrency

Imagine a cook preparing several independent orders.

If the cook waits doing nothing while water boils, other useful work can be performed.

```text
Task A ── waiting ────────── done
Task B ───── work ─── done
Task C ───────── work ─── done
```

Asynchronous programming is particularly useful when tasks spend significant time **waiting for I/O**.

For example:

* network requests;
* waiting for external services;
* other asynchronous I/O operations.

---

# Concurrency vs Parallelism

Concurrency is about **making progress on multiple tasks during overlapping periods**.

Parallelism is about **executing multiple computations at the same time**, typically using multiple CPU cores or execution units.

Mental model:

```text
Concurrency:
A → wait → B → wait → A → B

Parallelism:
A →→→
B →→→
at the same time
```

`asyncio.gather()` can provide concurrency for independent asynchronous tasks.

It does not automatically make CPU-bound Python code execute in parallel.

---

# I/O-Bound vs CPU-Bound

Imagine two different kinds of work.

### I/O-bound

The program spends much of its time waiting:

```text
Start
  ↓
Waiting for network
  ↓
Continue
  ↓
Waiting for database
  ↓
Continue
```

Async concurrency can be useful here.

### CPU-bound

The processor itself must perform a lot of computation:

```text
Start
  ↓
Heavy calculation
  ↓
Heavy calculation
  ↓
Result
```

Simply converting the function to `async def` does not make CPU-bound work faster.

The distinction should therefore be:

> **What is the program spending most of its time doing: computing or waiting?**

---

# Synchronous Database Driver in an Async Application

An async application does not mean every operation must become asynchronous.

For example, if the selected SQLite driver is synchronous, it can remain synchronous when the workload and architecture make that choice reasonable.

The useful mental model is:

```text
Async HTTP layer
       ↓
Application logic
       ↓
Synchronous SQLite operation
       ↓
SQLite
```

The important question is not:

> "Can this technically be made async?"

but:

> **"Would making this operation asynchronous provide a meaningful benefit for this application?"**

Avoid adding asynchronous complexity merely because the surrounding application uses `async`.

---

# The Most Important Mental Model

Programming is **not primarily typing code**.

Programming is the process of:

```text
Problem
   ↓
Understanding
   ↓
Decomposition
   ↓
Model
   ↓
Algorithm / Architecture
   ↓
Implementation
   ↓
Verification
   ↓
Refactoring
```

Code is the executable expression of that reasoning.

At the current stage of learning, the most important progression is therefore not:

```text
learn more syntax
```

but:

```text
understand the problem
        ↓
choose appropriate abstractions
        ↓
define clear responsibilities
        ↓
implement
        ↓
test
        ↓
observe what becomes difficult
        ↓
refactor
```

The purpose of the mental models in this document is to support that process without replacing precise technical knowledge.

---

# Evolution of Mental Models

Mental models are expected to evolve.

A model that was useful during the first Python modules may later become incomplete.

For example:

```text
Function = machine
```

is useful for understanding input and output.

Later, it must be expanded to account for:

```text
side effects
dependencies
state
exceptions
I/O
contracts
```

Similarly:

```text
API = another entrance
```

is useful for understanding multiple entry points.

Later, it can be expanded into:

```text
HTTP
  ↓
Presentation translation
  ↓
Application use case
  ↓
Infrastructure
```

This evolution is not a contradiction.

It is a normal part of developing a more accurate mental model.

---

**End of document.**
