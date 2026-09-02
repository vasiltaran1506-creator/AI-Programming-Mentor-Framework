# Module 05 — Object-Oriented Python

**Framework:** AI Programming Mentor Framework (APMF)

**Stage:** 2 — Python Application Foundations  
**Prerequisites:** Module 00, Module 01, Module 02, Module 03, Module 04  
**Primary language:** Python 3  
**Teaching language:** Russian  
**Estimated difficulty:** Intermediate → Intermediate+  
**Purpose:** develop a practical understanding of Object-Oriented Programming and learn when objects, classes, methods, composition, and inheritance genuinely improve a Python program.

---

# Module Overview

Module 04 established an important engineering foundation.

The student learned to think about:

- responsibilities;
- explicit inputs and outputs;
- dependencies;
- side effects;
- separation of I/O and business logic;
- reusable components;
- `dataclass`;
- automated testing with `pytest`;
- refactoring.

The next natural question is:

> **What should we do when our program contains entities that have their own state, behavior, identity, and relationships with other entities?**

This is where Object-Oriented Programming becomes useful.

The purpose of Module 05 is **not** to teach the student to put every piece of code into a class.

Instead, the student should learn to recognize situations where an object is a useful model.

The central transition is:

```text
Module 02
Data + Functions
        ↓
Module 03
Modules + Architecture
        ↓
Module 04
Components + Contracts + Testing
        ↓
Module 05
Objects + State + Behavior + Relationships
        ↓
Larger Software Systems
```

---

# Core Principle

> **A class is a tool for modeling a meaningful concept, not a requirement for writing "professional" Python.**

The student should finish the module able to answer:

```text
What is the entity?

What state does it own?

What behavior belongs to it?

What should it expose?

What should remain an implementation detail?

What other objects does it depend on?

Would a class actually make this program easier to understand?
```

---

# Important Methodological Context

Module 04 deliberately postponed formal OOP until the student had experience with:

- functions;
- state;
- dependencies;
- modular architecture;
- interfaces;
- testing;
- `dataclass`;
- refactoring.

That decision should now pay off.

The student already encountered domain objects such as:

- `Equipment`;
- `EstimateItem`;
- `Estimate`.

The purpose of Module 05 is to deepen the understanding of what these objects mean and when it is useful to give an object behavior in addition to data.

Do not begin by presenting a large theoretical hierarchy of OOP concepts.

Prefer:

```text
problem
↓
identify entity
↓
identify state
↓
identify behavior
↓
try a simple class
↓
observe what the class gives us
↓
introduce terminology
```

---

# Learning Goals

By the end of Module 05, the student should be able to:

1. explain what an object is;
2. explain what a class is;
3. distinguish a class from an instance;
4. understand object identity;
5. create classes with `__init__`;
6. understand and correctly use `self`;
7. distinguish parameters from instance attributes;
8. model object state;
9. write instance methods;
10. understand how methods read and modify object state;
11. distinguish instance attributes from class attributes;
12. understand mutable object state;
13. recognize encapsulation as a design principle;
14. understand composition;
15. understand inheritance conceptually;
16. understand polymorphism and duck typing at a practical level;
17. use special methods such as `__str__`, `__repr__`, and `__eq__`;
18. understand when a `dataclass` is preferable to a normal class;
19. decide when a class is unnecessary;
20. refactor dictionary-based models into objects when meaningful behavior justifies it;
21. test stateful objects with `pytest`;
22. use tests while changing object design;
23. distinguish composition from inheritance;
24. recognize overengineered OOP;
25. design a small object-oriented subsystem independently.

---

# Competency Map

## PF-017 — Classes and Objects

Student can:

- explain class vs object;
- create instances;
- identify instance identity;
- initialize object state.

**Target:** Level 3 — Confident Application.

---

## PF-018 — Object State and Methods

Student can:

- define instance attributes;
- use `self`;
- write methods;
- modify and inspect object state.

**Target:** Level 3.

---

## PF-019 — Object-Oriented Design

Student can:

- identify meaningful entities;
- assign responsibilities to objects;
- keep responsibilities cohesive;
- avoid turning every concept into a class.

**Target:** Level 2–3.

---

## PF-020 — Composition and Relationships

Student can:

- make objects contain or use other objects;
- explain "has-a" relationships;
- prefer composition when it produces a clearer design.

**Target:** Level 2–3.

---

## PF-021 — Inheritance and Polymorphism

Student can:

- explain "is-a" relationships;
- create a simple subclass;
- override behavior;
- explain polymorphism;
- recognize when inheritance is inappropriate.

**Target:** Level 2.

---

## PF-022 — Special Methods

Student can:

- understand why Python calls special methods;
- implement simple `__str__`;
- understand `__repr__`;
- use `__eq__` appropriately;
- recognize that special methods are part of an object's interface.

**Target:** Level 2.

---

## PF-023 — Object Testing

Student can:

- test object initialization;
- test state transitions;
- test methods;
- test invalid state changes;
- use `pytest` to verify object behavior.

**Target:** Level 2–3.

---

# Chapter 01 — From Data Structures to Objects

## 1.1 The problem with unrelated data

Suppose a program represents equipment like this:

```python
equipment = {
    "name": "Aputure 600D",
    "category": "Light",
    "available": True,
}
```

This is completely valid.

We can write functions:

```python
def take_item(item):
    item["available"] = False


def return_item(item):
    item["available"] = True
```

This works.

But the knowledge about equipment is now distributed between:

- dictionaries;
- functions;
- callers;
- conventions about which keys exist;
- conventions about which functions are valid for which data.

As a program becomes larger, this can become difficult to reason about.

---

## 1.2 Objects

An object can combine:

```text
state
+
behavior
```

For example:

```python
class Equipment:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.available = True

    def take(self):
        self.available = False

    def return_item(self):
        self.available = True
```

Now the object owns:

- its state;
- behavior that belongs naturally to that state.

The important idea is not:

> "Classes are better than dictionaries."

The important idea is:

> **Sometimes the relationship between data and behavior is strong enough that an object becomes a clearer model.**

---

## 1.3 Class versus object

A class describes what objects of a particular type look like and what they can do.

An object is a concrete instance of that class.

```python
class Equipment:
    pass
```

`Equipment` is a class.

```python
light = Equipment()
camera = Equipment()
```

`light` and `camera` are two different objects.

Mental model:

```text
Class
  ↓
description / blueprint

Object
  ↓
concrete instance
```

Do not confuse:

```python
Equipment
```

with:

```python
equipment
```

This distinction is especially important because the student previously made the mistake of confusing class-level access with instance-level access.

---

## 1.4 Identity

Two objects can contain identical data and still be different objects.

```python
a = Equipment()
b = Equipment()
```

Conceptually:

```text
a ──→ Object A
b ──→ Object B
```

Even if their attributes later contain the same values, the objects themselves have different identities.

This connects directly to Python's model of objects and references.

---

## 1.5 Practice

Create a simple `Book` class.

It should represent:

- title;
- author;
- year.

Add one method that returns a readable description.

Before writing code, answer:

```text
What is the entity?
What state does it have?
What behavior belongs to it?
```

Do not introduce inheritance or advanced features.

---

# Chapter 02 — `self`, `__init__`, and Object State

## 2.1 Instance attributes

Consider:

```python
class Equipment:
    def __init__(self, name):
        self.name = name
```

After:

```python
item = Equipment("Aputure 600D")
```

the object contains:

```text
name → "Aputure 600D"
```

The attribute:

```python
item.name
```

belongs to that particular object.

---

## 2.2 Parameters versus attributes

These are different:

```python
name
```

and:

```python
self.name
```

In:

```python
def __init__(self, name):
    self.name = name
```

`name` is a parameter.

`self.name` is an attribute stored on the object.

Mental model:

```text
name
↓
temporary input to the method

self.name
↓
state stored by the object
```

This distinction must be explicitly reinforced because confusing parameter names and object attributes is a common source of errors.

---

## 2.3 What is `self`?

Consider:

```python
class Equipment:
    def describe(self):
        return self.name
```

When we write:

```python
item.describe()
```

`self` refers to `item`.

Conceptually, this is similar to:

```python
Equipment.describe(item)
```

The exact internal mechanics are less important than the mental model:

> **`self` is the particular object whose method is currently executing.**

---

## 2.4 `__init__`

`__init__` is commonly used to initialize the state of a newly created instance.

```python
class Equipment:
    def __init__(self, name, category):
        self.name = name
        self.category = category
```

Then:

```python
item = Equipment("Aputure 600D", "Light")
```

initializes the object's attributes.

The student should understand the flow:

```text
Equipment(...)
      ↓
new instance
      ↓
__init__(self, ...)
      ↓
object state initialized
```

Do not describe `__init__` as "the constructor" without qualification if doing so creates confusion. It is more precise at this stage to say that it is the initialization method called during instance creation.

---

## 2.5 Mutable object state

Objects can change state:

```python
item.available = False
```

or through behavior:

```python
item.take()
```

This gives us:

```text
initial state
      ↓
method call
      ↓
new state
```

This is exactly the kind of state transition that should later be tested.

---

## 2.6 Practice — BankAccount

Design a `BankAccount` class with:

- owner;
- balance.

Possible behavior:

- `deposit(amount)`;
- `withdraw(amount)`;
- `get_balance()`.

Before implementation, decide:

- What state does the object own?
- Which operations are valid?
- What should happen if withdrawal exceeds the balance?
- Which errors are programming errors and which are normal business conditions?

The mentor should not immediately provide the implementation.

---

# Chapter 03 — Methods and Object Responsibility

## 3.1 Data versus behavior

A common beginner mistake is to create classes that contain only data while keeping all behavior elsewhere.

That is not automatically wrong.

The question is:

> **Does some behavior naturally belong to this object?**

For equipment:

```text
Equipment
├── name
├── category
├── available
├── take()
└── return_item()
```

This can be coherent because taking and returning equipment directly change the equipment's own state.

---

## 3.2 Cohesion

A useful object usually has related responsibilities.

Good:

```text
Equipment
    state about one piece of equipment
    +
    behavior directly related to that equipment
```

Less useful:

```text
Equipment
    +
    database connection
    +
    user interface
    +
    JSON file loading
    +
    network requests
```

The second design creates a "god object".

Module 04's separation-of-responsibilities principles still apply.

OOP does not replace good architecture.

---

## 3.3 Methods that return versus methods that mutate

A method can:

1. inspect state;
2. change state;
3. calculate something;
4. coordinate another object.

Examples:

```python
item.describe()
```

may return information.

```python
item.take()
```

may change state.

The student should learn to recognize the difference.

---

## 3.4 Practice

Given several operations on an equipment dictionary, decide:

- which operations belong to `Equipment`;
- which belong to an `Inventory`;
- which should remain ordinary functions.

The student must explain the reasoning before writing classes.

---

# Chapter 04 — Instance Attributes and Class Attributes

## 4.1 Instance attributes

An instance attribute belongs to a particular object.

```python
class Equipment:
    def __init__(self, name):
        self.name = name
```

Each object can have a different name.

---

## 4.2 Class attributes

A class attribute belongs to the class and may be shared conceptually across instances.

```python
class Equipment:
    category_name = "Equipment"
```

Then:

```python
Equipment.category_name
```

can access it.

The student should learn that:

```text
instance attribute
    ↓
belongs to one object

class attribute
    ↓
belongs to the class
```

Do not overemphasize advanced descriptor behavior or metaclasses.

---

## 4.3 A common trap

Do not use a mutable class attribute accidentally as shared instance state:

```python
class Inventory:
    items = []
```

This creates one shared list at the class level.

If every inventory should have its own list, initialize it per instance:

```python
class Inventory:
    def __init__(self):
        self.items = []
```

This is an important connection to the student's existing understanding of mutable objects.

---

## 4.4 Practice

Identify which of these should be instance state and which could reasonably be class-level information:

```text
equipment name
equipment availability
company name
maximum allowed quantity
inventory items
```

Explain why.

---

# Chapter 05 — Encapsulation and Interfaces

## 5.1 What encapsulation means here

At this stage, treat encapsulation primarily as a design idea:

> **An object should control and expose the state that belongs to its responsibility through a clear interface.**

For example, instead of allowing every part of a program to manipulate availability arbitrarily:

```python
item.available = False
```

we may provide:

```python
item.take()
```

The method can enforce rules.

---

## 5.2 Why this matters

Suppose equipment cannot be taken twice.

A direct assignment cannot enforce that rule.

A method can:

```text
take()
    ↓
is item available?
    ↓
yes → change state
no  → report failure
```

The object can therefore protect an invariant.

---

## 5.3 Invariants

An invariant is a condition that should remain true for a valid object.

For example:

```text
equipment.quantity >= 0
```

or:

```text
account.balance >= 0
```

if negative balances are forbidden.

The student should learn to ask:

> What must always be true about this object?

This question is more important than memorizing the word "encapsulation".

---

## 5.4 Practice

Design rules for an `Equipment` object:

- Can unavailable equipment be taken again?
- Can returned equipment be returned again?
- What happens on an invalid transition?

Write the rules before writing code.

---

# Chapter 06 — Composition: Objects Working Together

## 6.1 The "has-a" relationship

Suppose we have:

```text
Inventory
    contains
Equipment objects
```

This is composition.

An inventory is not an equipment item.

It **has** equipment items.

Example conceptually:

```python
class Inventory:
    def __init__(self):
        self.items = []
```

The inventory can manage objects.

---

## 6.2 Why composition is important

Large programs are usually built from objects that collaborate.

For example:

```text
Inventory
    ↓
Equipment

Estimate
    ↓
EstimateItem

Warehouse
    ↓
Equipment
    ↓
Scan
```

The goal is not to put everything into one class.

The goal is to give each object a meaningful responsibility.

---

## 6.3 Composition versus inheritance

This distinction is fundamental:

```text
Inventory has Equipment
        ↓
composition
```

versus:

```text
Camera is Equipment
        ↓
potential inheritance
```

A useful beginner heuristic:

> **"has-a" often suggests composition.  
> "is-a" may suggest inheritance.**

This is a heuristic, not a mathematical rule.

---

## 6.4 Practice

Design an `Inventory` that manages `Equipment` objects.

Before coding, describe:

- what `Inventory` owns;
- what `Equipment` owns;
- what operations belong to each;
- how they communicate.

---

# Chapter 07 — Inheritance

## 7.1 Why inheritance exists

Suppose several objects share common behavior.

Example:

```text
Equipment
├── Camera
├── Light
└── Microphone
```

A subclass can reuse or specialize behavior from a base class.

Example:

```python
class Equipment:
    def describe(self):
        return self.name


class Camera(Equipment):
    pass
```

The `Camera` class inherits from `Equipment`.

---

## 7.2 Inheritance is not automatically better

Do not teach inheritance as:

> "How professional programmers avoid duplication."

That leads to bad designs.

Inheritance should represent a meaningful relationship.

If two objects merely happen to share some code, inheritance may be the wrong solution.

---

## 7.3 Method overriding

A subclass can provide specialized behavior:

```python
class Equipment:
    def describe(self):
        return self.name


class Camera(Equipment):
    def describe(self):
        return f"Camera: {self.name}"
```

The subclass overrides the inherited method.

---

## 7.4 `super()`

Introduce `super()` only when a practical example requires it.

Example:

```python
class Camera(Equipment):
    def __init__(self, name, sensor_size):
        super().__init__(name)
        self.sensor_size = sensor_size
```

The student should understand the purpose:

> `super()` allows the subclass to use behavior from the parent class without duplicating it.

Do not turn `super()` into a memorization exercise.

---

## 7.5 Practice

Given a domain containing:

```text
Equipment
Camera
Light
Microphone
```

decide whether inheritance actually improves the model.

The student must be allowed to conclude:

> "No inheritance is necessary."

That is a valid answer.

---

# Chapter 08 — Polymorphism and Duck Typing

## 8.1 The basic idea

Polymorphism means that different objects can respond to the same operation in their own way.

Suppose:

```python
class Camera:
    def describe(self):
        return "Camera"


class Light:
    def describe(self):
        return "Light"
```

Then code can operate on both through the common behavior:

```text
object.describe()
```

without needing to know the exact concrete type in advance.

---

## 8.2 Duck typing

Python often uses duck typing:

> **If an object supports the operation you need, you can often use it without caring about its exact class.**

Conceptually:

```python
def print_description(item):
    print(item.describe())
```

The function does not necessarily need:

```python
item: Equipment
```

if all it requires is that `item` has a suitable `describe()` method.

---

## 8.3 Why this connects to Module 04

This is another example of an interface.

Module 04 taught:

```text
component
    ↓
explicit interface
```

OOP adds another form:

```text
object
    ↓
supported behavior
```

The important engineering question remains:

> What does this component promise to provide?

---

## 8.4 Practice

Create several objects with the same method name but different implementations.

Then write one function that works with all of them.

Do not introduce abstract base classes yet.

---

# Chapter 09 — Special Methods

Python objects can participate naturally in Python syntax by implementing special methods.

Examples:

```text
__str__
__repr__
__eq__
```

---

## 9.1 `__str__`

Used for a human-readable representation.

Example:

```python
class Equipment:
    def __str__(self):
        return self.name
```

Then:

```python
print(item)
```

can use that representation.

---

## 9.2 `__repr__`

`__repr__` is intended to provide a useful representation of an object, especially for debugging.

The student should understand the practical difference:

```text
__str__
    ↓
human-oriented display

__repr__
    ↓
developer/debug-oriented representation
```

Do not require memorization of every convention around `repr`.

---

## 9.3 `__eq__`

Objects can define what equality means for their domain.

For example, two objects might be considered equal when they have the same identifier.

The student should understand that object identity and equality are different concepts.

```text
identity
    ↓
are these the same object?

equality
    ↓
should these objects be considered equivalent?
```

---

## 9.4 Practice

Add a meaningful `__str__` to a domain object.

Then investigate what happens when the object is printed before and after implementing it.

---

# Chapter 10 — Dataclass versus Normal Class

Module 04 introduced `dataclass` as a structured data model.

Module 05 should deepen that understanding.

---

## 10.1 Dataclass for data-oriented objects

Example:

```python
from dataclasses import dataclass


@dataclass
class Equipment:
    name: str
    category: str
    available: bool = True
```

This is excellent when the object is primarily a structured bundle of data.

---

## 10.2 Normal class for richer behavior

If the object has substantial behavior and invariants, a normal class may communicate the design more clearly.

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        ...
```

The point is not that normal classes are "more advanced".

The point is that the representation should match the problem.

---

## 10.3 Decision rule

Ask:

```text
Is this mostly structured data?
    ↓
dataclass may be appropriate.

Does this object own meaningful behavior,
state transitions, or invariants?
    ↓
a normal class may be more appropriate.
```

A dataclass can also contain methods, so this is not an absolute distinction.

---

## 10.4 Practice

Take one dictionary-based domain model.

Create:

1. a dictionary version;
2. a dataclass version;
3. a normal class version.

Compare them.

Explain which version is most appropriate and why.

---

# Chapter 11 — Testing Stateful Objects with pytest

Module 04 introduced automated testing.

Now apply the same principles to objects.

---

## 11.1 Testing initial state

Example concept:

```text
Create equipment
    ↓
expected initial state
```

Test:

- name;
- category;
- availability.

---

## 11.2 Testing state transitions

Think:

```text
initial state
      ↓
operation
      ↓
expected state
```

For example:

```text
available
    ↓
take()
    ↓
unavailable
```

and:

```text
unavailable
    ↓
return_item()
    ↓
available
```

---

## 11.3 Testing invalid transitions

If the domain says:

```text
unavailable equipment cannot be taken
```

that rule should have a test.

This is where OOP and testing reinforce each other:

```text
Object
  ↓
owns state
  ↓
owns rules for changing state
  ↓
tests verify those rules
```

---

## 11.4 Test behavior, not implementation

Avoid tests that merely verify internal implementation details.

Prefer:

```text
When I perform operation X,
the object should behave like Y.
```

This keeps tests useful during refactoring.

---

## 11.5 Practical Exercise

Write `pytest` tests for a stateful object.

Required:

- initial state;
- normal state transition;
- second transition;
- invalid operation;
- at least one edge case.

The student should intentionally break one method and diagnose the failing test.

---

# Chapter 12 — Refactoring Dictionaries into Objects

This chapter connects Module 04 directly with Module 05.

Start with:

```python
equipment = {
    "name": "Aputure 600D",
    "category": "Light",
    "available": True,
}
```

and functions:

```python
def take_item(item):
    item["available"] = False


def return_item(item):
    item["available"] = True
```

Ask:

```text
Is there meaningful behavior belonging to the entity?

Does the entity have state?

Would combining state and behavior make the system clearer?
```

If yes, an object may be justified.

---

## 12.1 Refactoring process

Use:

```text
existing working code
        ↓
identify domain entity
        ↓
identify state
        ↓
identify behavior
        ↓
design class
        ↓
write tests
        ↓
refactor
        ↓
run tests
        ↓
compare behavior
```

Do not rewrite the entire project simply to "make it OOP."

---

# Chapter 13 — When NOT to Use OOP

This chapter is essential.

The student must learn that:

> **Using a class is not automatically an improvement.**

A simple function may be better:

```python
def calculate_total(prices):
    return sum(prices)
```

There is usually no reason to create:

```python
class TotalCalculator:
    ...
```

for such a simple operation.

---

## 13.1 Warning signs of unnecessary OOP

Examples:

```text
class StringFormatter
class NumberHelper
class FilePathManager
class CalculationService
```

These names are not automatically bad, but they should trigger a question:

> What state, identity, or meaningful responsibility does this object actually own?

---

## 13.2 Avoid class explosion

Bad architecture:

```text
UserManager
UserService
UserFactory
UserRepository
UserValidator
UserFormatter
UserHelper
```

created before there is a real problem.

Module 04's rule still applies:

> **Abstract because a real problem exists, not because abstraction is possible.**

---

# Chapter 14 — Integrated Project: Warehouse Domain Model

The final project should connect OOP with the student's existing warehouse / QR-code project.

The objective is **not** to rewrite the entire warehouse application.

Instead, identify one meaningful domain subsystem and model it using objects.

Possible entities:

```text
Equipment
Inventory
Scan
Estimate
EstimateItem
```

The student should decide which entities genuinely deserve classes.

---

## Stage 1 — Domain Analysis

Describe:

```text
What entities exist?

What state does each entity own?

What behavior belongs to each entity?

Which entities interact?

Which things should remain simple functions or data structures?
```

---

## Stage 2 — Object Design

For each proposed class:

```text
Class:
Responsibility:
State:
Methods:
Dependencies:
Invariants:
```

---

## Stage 3 — Relationships

Describe relationships such as:

```text
Inventory
    has many
Equipment

Estimate
    has many
EstimateItem
```

Determine whether each relationship is:

- composition;
- simple association;
- inheritance;
- or not actually an object relationship.

---

## Stage 4 — Contracts

For important methods:

```text
Input:
Output:
State changes:
Normal absence:
Possible errors:
Responsibility:
```

Module 04's contract discipline must continue.

---

## Stage 5 — Implementation

Implement the smallest useful object-oriented subsystem.

Do not rewrite unrelated parts of the warehouse project.

---

## Stage 6 — Tests

Use `pytest` to test:

- object creation;
- initial state;
- important methods;
- state transitions;
- invalid operations;
- edge cases.

---

## Stage 7 — Refactoring

After tests exist:

- identify one design problem;
- improve it;
- run the tests;
- verify that intended behavior remains unchanged.

---

## Stage 8 — Architectural Review

The student must explain:

```text
Why does this class exist?

Why does it own this state?

Why does this method belong here?

Why is this relationship composition/inheritance?

Why are some things still functions?

How would the design change if the application became much larger?
```

---

# Practical Projects

## Project A — Book

Create a minimal `Book` class.

Learn:

- class;
- object;
- `__init__`;
- attributes;
- method.

---

## Project B — Bank Account

Model:

- owner;
- balance;
- deposit;
- withdrawal;
- invalid operations.

Focus on:

- state;
- invariants;
- methods;
- tests.

---

## Project C — Equipment

Model equipment with:

- identity;
- availability;
- take;
- return;
- description.

Focus on:

- domain behavior;
- state transitions;
- `pytest`.

---

## Project D — Inventory

Create an `Inventory` that manages equipment objects.

Focus on:

- composition;
- collections of objects;
- responsibilities;
- object collaboration.

---

## Project E — Polymorphism

Create several objects supporting the same operation.

Focus on:

- common interfaces;
- duck typing;
- polymorphism.

---

## Project F — Warehouse Domain

Apply the ideas to the student's actual warehouse / QR-code project.

The student chooses the architecture.

---

# Development Process Rules

## Rule 1 — Design Before Code

Before creating a class, ask:

```text
What problem does this class solve?
```

If there is no clear answer, do not create the class yet.

---

## Rule 2 — Preserve the Student's Architecture

The mentor should not automatically replace the student's design with a preferred OOP architecture.

The student makes the architectural decision.

The mentor evaluates:

- cohesion;
- coupling;
- responsibility;
- clarity;
- testability;
- unnecessary complexity.

---

## Rule 3 — Do Not Turn Everything Into a Class

A pure function can remain a pure function.

A dictionary can remain a dictionary.

A dataclass can remain a dataclass.

A class should exist because it improves the model.

---

## Rule 4 — Experience Before Terminology

Whenever possible:

```text
problem
↓
attempt
↓
observe limitation
↓
introduce concept
↓
apply concept
```

Do not begin with memorization of OOP vocabulary.

---

## Rule 5 — Keep Module 04 Principles

OOP does not invalidate:

- separation of concerns;
- explicit dependencies;
- predictable contracts;
- pure functions;
- testability;
- small interfaces;
- refactoring discipline.

Instead:

> **OOP is another design tool inside the architecture learned in Module 04.**

---

## Rule 6 — Do Not Immediately Introduce Advanced OOP

Do not introduce as core material:

- metaclasses;
- descriptors;
- multiple inheritance;
- abstract base classes in depth;
- complex design patterns;
- SOLID as a memorization exercise;
- dependency injection frameworks;
- decorators for OOP machinery;
- advanced magic methods.

These may be mentioned only when a concrete problem makes them relevant.

---

## Rule 7 — Inheritance Must Be Earned

Before using inheritance, ask:

```text
Is there a genuine "is-a" relationship?

Would composition be clearer?

Does the subclass really specialize the parent concept?

Will polymorphism actually be useful?
```

If the answer is unclear, prefer a simpler design.

---

## Rule 8 — Tests Are Part of the Design

When designing a stateful object, ask:

> How would I test this object's behavior?

If the answer is extremely difficult, reconsider the design.

---

# Debugging Method

When the student encounters an object-related error, the mentor should first ask the student to identify:

```text
What is the object?

What is its type?

What value is stored in the relevant attribute?

What method was called?

What should `self` refer to?

What state existed before the call?

What state existed after the call?

What did the traceback say?
```

Particular attention should be paid to:

```python
Equipment.name
```

versus:

```python
equipment.name
```

and:

```python
Equipment.method(...)
```

versus:

```python
equipment.method(...)
```

because the student previously demonstrated confusion between class and instance access.

---

# Common Mistakes to Track

Continue tracking previous patterns:

- type confusion;
- tuple trap;
- label-vs-value confusion in `isinstance`;
- variable scope;
- inconsistent return contracts;
- architecture vs syntax gap;
- premature coding.

New OOP patterns:

## OOP-001 — Class/Instance Confusion

Does the student confuse:

```python
Equipment
```

with:

```python
equipment
```

?

---

## OOP-002 — Parameter/Attribute Confusion

Does the student confuse:

```python
name
```

with:

```python
self.name
```

?

---

## OOP-003 — Incorrect `self`

Does the student understand which object `self` represents?

---

## OOP-004 — Class Explosion

Does the student create classes where simple functions or data structures would be clearer?

---

## OOP-005 — Inheritance by Convenience

Does the student use inheritance merely to reuse code?

---

## OOP-006 — Missing Object Responsibility

Does the student create data-only objects while placing all domain behavior elsewhere without a reason?

---

## OOP-007 — Mutable Class Attribute

Does the student accidentally share mutable state between instances through class attributes?

---

# AI Mentor Behavior

Qwen should continue following the teaching philosophy established in Module 04.

When the student asks:

> "How should I write this class?"

First determine whether the student has identified:

1. the entity;
2. its state;
3. its responsibility;
4. its behavior;
5. its dependencies;
6. its invariants.

If these are unclear:

> return to design.

If the design is clear but syntax is unfamiliar:

> provide a minimal hint.

If the student has written code and it fails:

> ask the student to inspect the traceback and formulate a hypothesis before giving the solution.

Do not immediately provide complete implementations.

---

# Questions to Track

Add questions to `Questions.md` when they genuinely arise.

Potential questions:

### Q-0010

**What exactly is the difference between a class and an object?**

Status:

```text
Open
```

---

### Q-0011

**What exactly does `self` represent?**

Status:

```text
Open
```

---

### Q-0012

**When should behavior belong to an object instead of a function?**

Status:

```text
Open
```

---

### Q-0013

**What is encapsulation actually solving?**

Status:

```text
Open
```

---

### Q-0014

**When should I use composition instead of inheritance?**

Status:

```text
Open
```

---

### Q-0015

**What is polymorphism in Python?**

Status:

```text
Open
```

---

### Q-0016

**When should I use a dataclass versus a normal class?**

Status:

```text
Open
```

---

These questions must not be marked as mastered merely because the topic was explained.

Close them only when the student can explain and apply the concept independently.

---

# Learning Journal Additions

After Module 05, update `Learning Journal.md`.

Record:

- the student's first clear understanding of class vs object;
- how the student understood `self`;
- the student's understanding of object state;
- examples where behavior naturally belonged to an object;
- whether composition became intuitive;
- first experience with inheritance;
- first experience with polymorphism;
- understanding of special methods;
- whether the student can distinguish dataclasses from richer classes;
- examples where the student correctly rejected OOP;
- examples of overengineering;
- the most important OOP-related breakthrough;
- how OOP changed the student's understanding of the warehouse project.

---

# Development Log Additions

Continue tracking:

- type confusion;
- method-call mistakes;
- scope issues;
- inconsistent returns;
- architecture vs syntax gap;
- dependency awareness;
- testability awareness;
- abstraction judgment;
- refactoring discipline.

Add:

```text
Object Modeling
    Can the student identify meaningful entities?

State Ownership
    Does the student know which object should own which state?

Behavior Ownership
    Does the student place behavior where it conceptually belongs?

Composition Judgment
    Does the student recognize "has-a" relationships?

Inheritance Judgment
    Does the student avoid inheritance when composition is clearer?

Encapsulation Awareness
    Does the student recognize invariants and state-changing operations?

OOP Restraint
    Does the student know when NOT to create a class?
```

---

# Completion Criteria

Module 05 is complete when the student can independently design and implement a small object-oriented subsystem that:

- contains meaningful classes;
- distinguishes classes from instances;
- initializes object state correctly;
- uses `self` correctly;
- defines coherent methods;
- assigns responsibilities appropriately;
- uses composition when appropriate;
- understands simple inheritance;
- demonstrates basic polymorphism;
- uses special methods where they genuinely improve the interface;
- chooses between a dictionary, dataclass, function, and normal class based on the problem;
- contains automated tests;
- tests object state transitions;
- handles defined invalid states;
- can refactor object-oriented code without changing intended behavior;
- avoids unnecessary class hierarchies.

Most importantly, the student must be able to explain:

> **What objects exist, what state each object owns, what behavior belongs to each object, how objects interact, and why the chosen design is simpler than the alternatives.**

---

# Final Conceptual Transition

Module 03 taught:

> **A real program needs structure.**

Module 04 taught:

> **Good structure makes change safer.**

Module 05 teaches:

> **Objects can model state, behavior, identity, and relationships when the problem calls for them.**

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
Object collaboration
  ↓
Larger domain models
```

The student should not finish the module thinking:

> "Everything should be a class."

The desired conclusion is:

> **"I now have another tool for deciding how to model a program."**

The most important engineering question of the module is:

> **"Does introducing an object make the problem clearer, or am I adding complexity just because I learned OOP?"**

---

# Final Assessment

At the end of Module 05, Qwen should produce the usual:

- Checkpoint Report;
- Learning Journal update;
- Programming Handbook update;
- Questions update;
- Development Log update.

The Checkpoint Report should explicitly evaluate:

1. class/object understanding;
2. `self` and instance state;
3. methods and responsibility;
4. composition;
5. inheritance;
6. polymorphism;
7. special methods;
8. dataclass vs normal class judgment;
9. testing of stateful objects;
10. OOP restraint and avoidance of overengineering;
11. independence level;
12. architectural decision-making.

The report should distinguish between:

```text
memorized syntax
        vs
conceptual understanding
        vs
independent design judgment
```

A student should not be considered to have mastered OOP merely because they can write:

```python
class Something:
    ...
```

The stronger criterion is:

> **Given a new problem, can the student decide whether an object is appropriate, identify its state and responsibilities, design its interface, and explain why?**

That is the actual objective of Module 05.
