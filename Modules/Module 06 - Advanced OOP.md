# Module 06 — Advanced Object-Oriented Python

**Framework:** AI Programming Mentor Framework (APMF)  
**Stage:** 2 — Python Application Foundations  
**Prerequisites:** Module 00, Module 01, Module 02, Module 03, Module 04, Module 05  
**Primary language:** Python 3  
**Teaching language:** English  
**Estimated difficulty:** Intermediate+  
**Purpose:** deepen practical object-oriented design through inheritance, method overriding, `super()`, polymorphism, interfaces, and introductory design patterns while preserving the architectural discipline established in Module 04 and Module 05.

---

# Module Overview

Module 05 established the foundations of object-oriented programming.

The student learned to:

- model meaningful entities as objects;
- distinguish classes from instances;
- represent object state;
- attach behavior to objects through methods;
- protect invariants through encapsulation;
- use composition;
- decide between `@dataclass` and regular classes;
- test object behavior with `pytest`;
- separate orchestration from domain logic.

The next problem is not:

> "How do I write more classes?"

The next problem is:

> **"What should I do when several objects are related, share some behavior, but differ in their implementation?"**

This is where inheritance and polymorphism become useful.

However, this module must not teach inheritance as a syntax trick.

The student should learn to answer:

```text
Do these objects really represent the same conceptual family?

What do they have in common?

What is different?

Should the common behavior live in a parent abstraction?

Would composition be clearer?

Would polymorphism actually remove conditional logic?

Is inheritance helping the design, or only reducing duplicated code?
```

The module therefore continues the central architectural progression:

```text
Module 03
Modules + Separation of Concerns
        ↓
Module 04
Contracts + Dependencies + Testing
        ↓
Module 05
Objects + State + Encapsulation + Composition
        ↓
Module 06
Inheritance + Polymorphism + Interfaces
        ↓
Larger Object-Oriented Systems
```

---

# Core Principle

> **Inheritance is a modeling tool, not a code-reuse shortcut.**

A second principle is equally important:

> **Prefer the simplest relationship that accurately represents the domain.**

Sometimes that relationship is:

```text
composition
```

Sometimes:

```text
inheritance
```

Sometimes:

```text
plain functions
```

Sometimes:

```text
independent classes with the same interface
```

The purpose of Module 06 is to learn how to tell the difference.

---

# Teaching Philosophy for This Module

The student has demonstrated strong architectural reasoning but sometimes receives enough guidance that there is less room to make independent decisions.

Module 06 should deliberately increase the amount of productive uncertainty.

The mentor should not remove every obstacle before the student encounters it.

Preferred progression:

```text
Problem
   ↓
Independent analysis
   ↓
Student proposes design
   ↓
Student attempts implementation
   ↓
Observe difficulty
   ↓
Minimal hint
   ↓
Another attempt
   ↓
Deeper hint if necessary
   ↓
Small code fragment if genuinely blocked
   ↓
Complete solution only when explicitly requested or educationally justified
```

The objective is not to make the student struggle for its own sake.

The objective is to create enough space for the student to make architectural decisions.

A useful rule:

> **Give the student the problem, not the solution path.**

Do not routinely provide:

```text
Step 1: create this class
Step 2: add this attribute
Step 3: inherit from this class
Step 4: write this method
```

unless the student is currently learning the syntax itself.

Instead provide:

```text
Goal
Constraints
Available concepts
Expected behavior
Acceptance criteria
```

and allow the student to design the solution.

---

# Calibrated Hint Policy

Hints remain an essential teaching tool.

The mentor should not interpret "more independence" as "never help."

Use a graduated hint system.

## Hint Level 0 — Question

Ask a question that points toward the relevant concept.

Example:

> What relationship exists between these two classes?

or:

> What part of the behavior is actually shared?

---

## Hint Level 1 — Direction

Identify the area of the problem without revealing the implementation.

Example:

> Look at the common interface rather than the internal implementation.

---

## Hint Level 2 — Structural Hint

Reveal the likely structural move.

Example:

> Consider whether both classes should provide the same method name while implementing it differently.

---

## Hint Level 3 — Minimal Code Fragment

Provide only the missing syntax or a very small fragment.

Example:

```python
class Camera(Equipment):
    ...
```

The student completes the rest.

---

## Hint Level 4 — Focused Implementation

Provide a substantial fragment when the student is genuinely blocked, then require the student to explain it and complete the remaining work.

---

## Hint Level 5 — Full Solution

Provide the complete implementation when:

- the student explicitly requests it;
- continued attempts are no longer producing learning;
- the syntax itself is the only remaining obstacle;
- comparing a correct implementation against the student's attempt has educational value.

After giving full code, the mentor must return to reasoning:

```text
Why does this design work?

Why is this inheritance relationship justified?

What alternatives were possible?

What would break if the abstraction changed?
```

---

# Testing Policy

Testing is important, but the student's primary career direction is backend/software development rather than dedicated test engineering.

Therefore, testing should remain a supporting engineering skill.

The mentor may provide partial or complete test scaffolding when that better supports learning the target programming concept.

For example, it is acceptable to provide:

```python
def test_camera_rental_cost():
    camera = Camera(...)
    # student writes the assertions
```

or:

```python
@pytest.mark.parametrize(...)
def test_calculate_cost(...):
    # student completes expected behavior
```

This is intentional.

The student should learn to:

- read tests;
- understand what behavior they protect;
- write assertions;
- interpret failures;
- modify tests when requirements change;
- use tests while refactoring.

The student does **not** need to spend disproportionate time manually writing large numbers of repetitive tests.

The target remains:

> **Build reliable software, using tests as an engineering safety net.**

---

# Module Learning Goals

By the end of Module 06, the student should be able to:

1. explain why inheritance exists;
2. distinguish inheritance from composition;
3. identify genuine `is-a` relationships;
4. create a subclass;
5. extend a parent class safely;
6. override a method;
7. use `super()` correctly;
8. understand method lookup at a practical level;
9. explain polymorphism;
10. recognize duck typing as an alternative to inheritance;
11. design and use a common interface;
12. recognize when conditional logic can be replaced by polymorphism;
13. identify inheritance by convenience;
14. understand why deep inheritance trees are difficult to maintain;
15. use abstract base classes at a practical introductory level;
16. understand the purpose of `ABC` and `@abstractmethod`;
17. compare composition and inheritance for a concrete problem;
18. recognize simple design patterns as reusable design ideas rather than recipes;
19. understand Factory and Strategy patterns conceptually;
20. write tests for polymorphic behavior;
21. use parameterized tests where repetition is meaningful;
22. use fixtures appropriately;
23. preserve Module 04 contracts and Module 05 encapsulation when using inheritance;
24. refactor object-oriented code without changing intended behavior;
25. make independent architectural decisions with limited mentor guidance.

---

# Section I — Why Inheritance Exists

## 1.1. The Problem

Suppose an application contains:

```text
Camera
Light
Cable
```

All three are pieces of rental equipment.

They may share:

```text
identity
name
category
rental-related behavior
availability
```

but their specialized behavior may differ.

The naive approach is to duplicate code.

The next approach is to ask:

> What is genuinely common?

This question is the beginning of inheritance.

---

## 1.2. Commonality vs Specialization

A useful conceptual model is:

```text
              Equipment
             /        \\
            /          \\
        Camera         Light
```

The parent represents the shared concept.

The child represents a specialization.

This should not be interpreted as:

> "Put anything reusable into a parent."

Instead:

> **The parent must represent a real conceptual abstraction.**

---

## 1.3. The "Is-a" Test

Inheritance often represents an `is-a` relationship.

Examples:

```text
Camera is equipment.
Light is equipment.
```

Potentially:

```text
Inventory is equipment.
```

The last statement is false.

Therefore inheritance would be a poor model.

This simple language test is useful, but it is not sufficient by itself.

Also ask:

```text
Does the child really specialize the parent?

Does the parent abstraction make sense on its own?

Does polymorphism become useful?

Would composition be clearer?
```

---

# Section II — A First Inheritance Model

## 2.1. Syntax

Basic inheritance:

```python
class Camera(Equipment):
    pass
```

The class in parentheses is the parent class.

`Camera` becomes a subclass of `Equipment`.

---

## 2.2. What the Subclass Gains

A subclass can reuse behavior from its parent.

Conceptually:

```text
Equipment
    ↓
shared behavior
    ↓
Camera
```

The subclass may then add or modify behavior.

---

## 2.3. First Exercise — Model a Family

Create a small domain with:

```text
Vehicle
Car
Truck
```

Before writing code, answer:

```text
What does Vehicle represent?

What does every Vehicle have?

What does Car add?

What does Truck add?

Is inheritance actually justified?
```

Do not implement immediately.

The mentor should review the reasoning first.

---

# Section III — Method Overriding

## 3.1. The Problem

Suppose the parent has:

```python
class Animal:
    def speak(self):
        return "Some sound"
```

A subclass may need specialized behavior:

```python
class Dog(Animal):
    def speak(self):
        return "Woof"
```

The child overrides the inherited method.

---

## 3.2. Why Override?

Method overriding allows a subclass to preserve a common interface while changing the implementation.

This becomes important for polymorphism.

The caller can work with:

```text
Animal-like object
```

without needing to know the concrete subclass.

---

## 3.3. Exercise

Create:

```text
Notification
EmailNotification
SMSNotification
```

All should expose:

```python
send(message)
```

The implementation should differ.

The student decides:

- which state belongs to the parent;
- what belongs to each child;
- whether inheritance is actually the best solution.

Do not provide the class hierarchy unless the student asks.

---

# Section IV — `super()`

## 4.1. The Problem

Sometimes the child wants to extend parent behavior rather than replace it completely.

For example:

```python
class User:
    def __init__(self, name):
        self.name = name
```

A specialized user may need additional state.

The child can call:

```python
super().__init__(name)
```

This invokes the appropriate inherited implementation through the class hierarchy.

---

## 4.2. Mental Model

Think of:

```text
Child
  ↓
"Do the inherited initialization"
  ↓
Parent
  ↓
"Now let me add my specialized state"
```

`super()` is therefore not simply:

> "Call my parent."

A better mental model is:

> **"Continue the implementation through the inherited class relationship."**

The full details of Python's method resolution order are important later, but this module should first establish the practical use.

---

## 4.3. When Should `super()` Be Used?

Typical situations:

- extending parent initialization;
- extending inherited behavior;
- preserving existing parent logic while adding specialization.

Do not use `super()` merely because inheritance exists.

Ask:

> What parent behavior am I intentionally preserving?

---

## 4.4. Exercise

Create:

```text
Employee
Manager
```

The parent defines shared employee information.

The child adds manager-specific state.

Use `super()` only if your design actually requires inherited initialization.

Then explain why.

---

# Section V — Polymorphism

## 5.1. The Problem with Conditionals

Consider:

```python
if equipment.type == "camera":
    ...
elif equipment.type == "light":
    ...
elif equipment.type == "cable":
    ...
```

This can become difficult to extend.

Every new type may require modifying central code.

A different design is:

```text
Camera.calculate_cost()
Light.calculate_cost()
Cable.calculate_cost()
```

Then the caller can simply request:

```python
equipment.calculate_cost()
```

without deciding which concrete implementation should run.

---

## 5.2. Mental Model — One Question, Many Answers

Imagine a conductor asking:

> "Play your part."

Different instruments respond differently.

The conductor does not need separate instructions for every instrument.

Likewise:

```text
object.calculate_cost()
```

may produce different behavior depending on the object's concrete type.

This is polymorphism.

---

## 5.3. Formal Definition

Polymorphism means that different objects can be used through a common interface while providing different implementations of behavior.

At this stage, focus on practical polymorphism, not terminology memorization.

---

# Section VI — Duck Typing

## 6.1. Python's Flexible Model

Python often does not require objects to inherit from the same parent.

Suppose two unrelated classes both provide:

```python
render()
```

The caller can often use them in the same context.

The famous mental model is:

> "If it walks like a duck and quacks like a duck, treat it like a duck."

---

## 6.2. Inheritance Is Not Required

These may both work:

```text
Printer
PDFRenderer
HTMLRenderer
```

without sharing a parent class, provided they expose a compatible interface.

This leads to an important distinction:

```text
Inheritance:
"These objects are members of the same conceptual hierarchy."

Duck typing:
"I only care that this object provides the behavior I need."
```

---

## 6.3. Exercise — Common Interface Without Inheritance

Create three unrelated classes:

```text
ConsoleLogger
FileLogger
MemoryLogger
```

Each should support:

```python
log(message)
```

Use them through the same calling code.

Then answer:

```text
Did inheritance improve this problem?

Would a shared base class add anything useful?

What does the caller actually depend on?
```

---

# Section VII — Interface Thinking

## 7.1. Interface as a Contract

An interface is a promise about how a component can be used.

For example:

```text
calculate_cost()
```

means:

```text
"You can ask me for a cost."
```

The caller should care about the contract rather than the internal implementation.

This continues the contract thinking from Module 04.

---

## 7.2. Object-Oriented Interface

A useful mental model:

```text
Caller
  ↓
Interface
  ↓
Implementation
```

Different implementations can satisfy the same interface.

---

## 7.3. Interface Design Exercise

Design a small system for payments.

Possible implementations:

```text
CashPayment
CardPayment
OnlinePayment
```

The important operation is:

```text
pay(amount)
```

Before coding, define:

```text
Input:
Output:
State changes:
Errors:
External dependencies:
Responsibility:
```

This explicitly carries Module 04 contract discipline into Module 06.

---

# Section VIII — Abstract Base Classes

## 8.1. Why They Exist

Sometimes a developer wants to formalize:

> "Every subclass must provide this operation."

Python provides abstract base classes for this purpose.

A simplified example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        ...
```

The abstract class defines the expected interface.

---

## 8.2. What This Means

The parent is saying:

```text
I know this operation must exist.

I do not provide the concrete implementation here.

Every concrete subclass must implement it.
```

---

## 8.3. Why Not Use ABC Everywhere?

Because not every interface needs formal machinery.

Python's duck typing is often enough.

Therefore ask:

```text
Do I need explicit enforcement?

Will the abstraction be shared by many implementations?

Does the interface communicate an important design boundary?
```

Do not use an abstract base class simply because it looks professional.

---

# Section IX — Composition vs Inheritance

This is one of the most important sections of Module 06.

## 9.1. Two Different Relationships

Composition usually expresses:

```text
has-a
```

Example:

```text
Inventory
    contains
        Equipment
```

Inheritance usually expresses:

```text
is-a
```

Example:

```text
Camera
    is-a
Equipment
```

---

## 9.2. Comparison

| Question | Composition | Inheritance |
|---|---|---|
| Main idea | has-a | is-a |
| Coupling | usually lower | usually higher |
| Flexibility | high | lower |
| Reuse mechanism | object collaboration | inherited behavior |
| Typical risk | too many collaborators | fragile hierarchy |
| Best use | assembling behavior | genuine specialization |

This is a guideline, not a law.

---

## 9.3. Design Exercise

Evaluate these relationships:

```text
Car → Engine
Camera → Battery
Manager → Employee
Inventory → Equipment
Square → Shape
```

For each, decide:

```text
composition
inheritance
neither
```

Then justify the decision.

The mentor should not reveal the answer immediately.

The goal is architectural reasoning.

---

# Section X — Inheritance by Convenience

A common beginner mistake is:

> "I already have useful code in this class, so I'll inherit from it."

This can produce relationships that are technically possible but conceptually wrong.

For example:

```text
Estimate
    inherits
Inventory
```

because both contain collections.

The fact that code can be reused does not mean the relationship is correct.

Ask:

```text
Is an Estimate an Inventory?

Does Estimate need the entire parent interface?

Would changes to Inventory unexpectedly affect Estimate?

Would composition be clearer?
```

---

# Section XI — Deep Inheritance Trees

Inheritance becomes harder to reason about as hierarchies grow.

Avoid building structures like:

```text
Entity
   ↓
Resource
   ↓
Equipment
   ↓
ElectronicEquipment
   ↓
ProfessionalElectronicEquipment
   ↓
Camera
   ↓
CinemaCamera
   ↓
DigitalCinemaCamera
```

unless the domain truly requires them.

The cost of a hierarchy includes:

- hidden inherited behavior;
- more complicated debugging;
- tighter coupling;
- harder refactoring;
- harder mental models.

Prefer shallow hierarchies.

---

# Section XII — Method Lookup

## 12.1. The Practical Question

When Python evaluates:

```python
obj.method()
```

where does it find `method`?

A useful beginner model is:

```text
instance
   ↓
class
   ↓
parent class
   ↓
higher parent classes
```

Python follows a method resolution order.

---

## 12.2. Why This Matters

Understanding lookup helps explain:

- inherited methods;
- overridden methods;
- `super()`;
- multiple inheritance later;
- surprising behavior in complex class hierarchies.

This module only requires a practical understanding.

Do not turn method resolution order into a memorization exercise.

---

# Section XIII — Polymorphism and Conditional Logic

## 13.1. The Architectural Opportunity

Sometimes code looks like:

```python
if type == "camera":
    ...
elif type == "light":
    ...
elif type == "cable":
    ...
```

If every branch exists because the objects have different implementations of the same conceptual operation, polymorphism may simplify the design.

The transformation is:

```text
Type checking
    ↓
Conditional branches
    ↓
Repeated modification of central code
```

toward:

```text
Common interface
    ↓
Object-specific behavior
    ↓
Simple caller
```

---

## 13.2. Important Warning

Not every `if` statement should become polymorphism.

Sometimes a simple conditional is the clearest solution.

Ask:

```text
Are these actually different objects?

Do they have meaningful behavior differences?

Will new variants appear?

Is the conditional growing?

Would polymorphism make the caller simpler?
```

---

# Section XIV — First Design Pattern: Factory

## 14.1. The Problem

Sometimes object creation itself requires decisions.

For example:

```text
"camera" → Camera
"light"  → Light
"cable"  → Cable
```

If this logic is repeated in many places, object creation becomes scattered.

A Factory can centralize the creation decision.

---

## 14.2. Mental Model

Think of a workshop:

```text
Request
   ↓
Factory
   ↓
Correct object
```

The caller says:

> "Give me a camera."

It does not need to know every detail of constructing that object.

---

## 14.3. Important Limitation

A Factory is useful when creation logic itself is meaningful.

Do not create:

```text
FactoryFactoryManager
```

for a simple constructor.

The pattern should remove complexity, not add it.

---

# Section XV — Second Design Pattern: Strategy

## 15.1. The Problem

Suppose one operation can be performed through different algorithms:

```text
standard pricing
discount pricing
premium pricing
```

Instead of a huge conditional:

```python
if mode == "standard":
    ...
elif mode == "discount":
    ...
elif mode == "premium":
    ...
```

we can represent the algorithm as an interchangeable object.

---

## 15.2. Mental Model

Think of changing a tool:

```text
Pricing Engine
      ↓
  Strategy
  /   |   \\
A     B     C
```

The surrounding system stays the same.

Only the strategy changes.

---

## 15.3. Why Strategy Matters

Strategy demonstrates a deeper idea:

> **Behavior itself can become a replaceable dependency.**

This connects directly to dependency injection from Module 04.

---

# Section XVI — Testing Polymorphism

Testing should verify behavior, not class hierarchy trivia.

Suppose several objects support:

```python
calculate_cost()
```

A useful test can focus on the contract:

```text
Given an object supporting calculate_cost
→ the result satisfies the expected contract.
```

---

## 16.1. Test Scaffolding

The mentor may provide:

```python
def test_camera_cost():
    camera = Camera(...)
    # student writes assertions
```

and:

```python
def test_light_cost():
    light = Light(...)
    # student writes assertions
```

The student's job is to identify:

```text
What behavior matters?

What should be asserted?

Which edge cases matter?
```

---

## 16.2. Parameterized Tests

When several cases share the same test structure, parameterization becomes useful.

Example:

```python
@pytest.mark.parametrize(
    "price, days, expected",
    [
        (100, 1, 100),
        (100, 3, 300),
        (250, 2, 500),
    ],
)
def test_rental_cost(price, days, expected):
    ...
```

The exact syntax should be taught when used.

The important concept is:

> **One behavior, many inputs.**

---

# Section XVII — Fixtures

Fixtures prepare reusable test state.

For example:

```python
@pytest.fixture
def inventory():
    ...
```

The purpose is not to make tests look advanced.

Fixtures are useful when the same setup appears repeatedly.

Ask:

```text
Is this setup genuinely shared?

Does a fixture make tests clearer?

Would local setup be simpler?
```

Avoid turning every piece of test data into a fixture.

---

# Section XVIII — Test-Driven Development

Module 05 introduced the Red-Green-Refactor idea.

Module 06 deepens it.

The cycle is:

```text
RED
Write a test that fails
        ↓
GREEN
Write the smallest code that passes
        ↓
REFACTOR
Improve the design
        ↓
Repeat
```

For this module, the cycle is especially useful when introducing polymorphic behavior.

---

## 18.1. Why TDD Helps OOP

Objects contain state and behavior.

That creates more possible interactions.

Tests provide a precise behavioral contract.

For example:

```text
Object creation
      ↓
Initial state
      ↓
Operation
      ↓
State transition
      ↓
Expected result
```

---

# Section XIX — Refactoring OOP Safely

A useful refactoring sequence is:

```text
Working implementation
       ↓
Tests
       ↓
Identify design problem
       ↓
Small change
       ↓
Run tests
       ↓
Repeat
```

Never refactor a large object hierarchy without behavioral protection.

---

# Section XX — QR Warehouse Integration

This section is mandatory.

The student must apply Module 06 ideas to the QR Warehouse Project.

However, the mentor must **not force inheritance into the existing architecture**.

The project already uses composition appropriately.

The purpose is to investigate whether polymorphism could solve a real problem.

---

## 20.1. Candidate Domain

Current conceptual model:

```text
Equipment
EstimateItem
Inventory
Estimate
```

Potential future extensions could include:

```text
Camera
Light
Cable
Stand
```

But these should not automatically become subclasses.

---

## 20.2. Investigation Task

Analyze the domain.

Ask:

```text
Do categories actually have different behavior?

Or are they only labels?

Does each category require specialized calculations?

Do categories have different validation rules?

Do categories have different rental workflows?

Would inheritance simplify anything?

Would it create unnecessary coupling?
```

The student must answer these questions before changing the code.

---

## 20.3. Polymorphism Challenge

Introduce a realistic requirement.

Example:

> Different equipment types may eventually calculate rental costs differently.

Possible future behavior:

```text
Camera
    base rental price + insurance

Light
    base rental price

Cable
    fixed package price
```

The student should design a solution that allows:

```python
equipment.calculate_rental_cost(...)
```

without requiring the caller to inspect the equipment category.

The exact architecture is intentionally left open.

---

## 20.4. Integration Constraints

The student should preserve:

- existing encapsulation;
- explicit responsibilities;
- object invariants;
- test coverage;
- simple orchestration in `main.py`;
- composition where it remains appropriate.

Do not rewrite the entire project merely to demonstrate inheritance.

---

# Section XXI — Architecture Review

At the end of the module, the student should be able to review an object-oriented system and answer:

```text
What classes exist?

Why does each class exist?

Which objects own state?

Which methods protect invariants?

Where is composition used?

Where is inheritance used?

Why?

Where is polymorphism used?

What interface does it provide?

Could any inheritance relationship be removed?

Would removing it improve the design?

Where are the external dependencies?

How are important behaviors tested?
```

---

# Practical Projects

## Project A — Animal Behaviors

Build:

```text
Animal
Dog
Cat
Bird
```

Focus:

- inheritance;
- overriding;
- polymorphism.

Do not spend excessive time on advanced details.

---

## Project B — Notification System

Build:

```text
EmailNotification
SMSNotification
PushNotification
```

All should support:

```text
send(message)
```

Focus:

- common interface;
- polymorphism;
- testing.

The student decides whether inheritance is needed.

---

## Project C — Payment System

Build:

```text
CashPayment
CardPayment
OnlinePayment
```

Focus:

- interface thinking;
- optional abstract base class;
- dependency boundaries;
- error handling.

---

## Project D — Strategy Pricing

Build several pricing strategies.

Possible strategies:

```text
RegularPricing
WeekendPricing
CorporatePricing
```

Focus:

- replaceable behavior;
- composition;
- dependency injection;
- Strategy pattern.

---

## Project E — Factory

Create a small object factory.

Input:

```text
"camera"
"light"
"cable"
```

Output:

```text
corresponding object
```

Focus:

- centralized creation;
- abstraction;
- avoiding unnecessary complexity.

---

## Project F — QR Warehouse

Apply the module to the real project.

The student chooses whether inheritance or polymorphism solves a real requirement.

The mentor must not dictate the hierarchy.

---

# Independent Design Challenges

These challenges are intentionally less guided.

## Challenge 1 — The Wrong Hierarchy

A system contains:

```text
Database
File
API
```

and someone proposes:

```text
Database
   ↓
File
   ↓
API
```

Determine whether this hierarchy makes sense.

Explain why or why not.

---

## Challenge 2 — Reuse Trap

A developer wants:

```text
Estimate
    inherits
Inventory
```

because both contain collections and methods for adding/removing things.

Evaluate the design.

---

## Challenge 3 — Growing Conditional

A program contains:

```python
if item.category == "camera":
    ...
elif item.category == "light":
    ...
elif item.category == "cable":
    ...
elif item.category == "stand":
    ...
elif item.category == "monitor":
    ...
```

Determine whether polymorphism would improve the design.

Do not assume that it must.

---

## Challenge 4 — Composition or Inheritance?

Evaluate:

```text
Car / Engine
Dog / Animal
Order / Customer
Manager / Employee
Report / Formatter
```

Choose:

```text
composition
inheritance
association
function
```

and justify each decision.

---

# Debugging Method for Module 06

When inheritance-related code fails, do not jump directly to the solution.

First identify:

```text
What is the actual object?

What is its concrete class?

What is its parent class?

Which method is being called?

Is the method overridden?

Which implementation is Python using?

Does super() participate?

What state exists before the call?

What state exists after the call?

What does the traceback say?
```

When polymorphism fails, ask:

```text
What interface did the caller expect?

Does the object provide that interface?

Is the method name correct?

Are the arguments compatible?

Is the problem actually caused by inheritance?
```

---

# Common Mistakes to Track

Continue tracking previous patterns:

- type confusion;
- tuple trap;
- label-vs-value confusion in `isinstance`;
- variable scope;
- inconsistent return contracts;
- premature coding;
- syntax mistakes;
- object reference confusion.

New Module 06 patterns:

## OOP-008 — Inheritance by Convenience

Using inheritance purely because it allows code reuse.

---

## OOP-009 — False Is-a Relationship

Creating inheritance where composition or association better describes the domain.

---

## OOP-010 — Parent Class Overload

Putting too much behavior into a parent class because several subclasses currently share it.

---

## OOP-011 — Deep Hierarchy

Creating many inheritance levels without a strong domain reason.

---

## OOP-012 — Conditional Polymorphism Missed

Repeatedly checking concrete types instead of using a common behavior interface when polymorphism would simplify the design.

---

## OOP-013 — Polymorphism Overengineering

Replacing a simple conditional with a complicated hierarchy when no real benefit exists.

---

## OOP-014 — Incorrect `super()`

Using `super()` without understanding which inherited behavior is intentionally being preserved.

---

# Mentor Behavior for Module 06

The mentor should continue the teaching philosophy of previous modules.

## Rule 1 — Do Not Start With the Inheritance Syntax

Start with the modeling problem.

Preferred:

```text
problem
↓
identify relationships
↓
identify shared behavior
↓
compare composition vs inheritance
↓
choose design
↓
learn syntax needed
```

---

## Rule 2 — Make Inheritance Earned

Before approving inheritance, ask:

```text
What is the parent abstraction?

What does every child genuinely share?

What makes each child a specialization?

Why is composition not better?

Where will polymorphism be useful?
```

---

## Rule 3 — Increase Independent Reasoning

Do not automatically give the student the class hierarchy.

First ask for:

```text
Entities
Relationships
Shared behavior
Specialized behavior
Candidate abstraction
Alternative design
Decision
```

Then discuss the student's reasoning.

---

## Rule 4 — Do Not Confuse Difficulty With Learning

Allow productive struggle.

But if the student repeatedly fails to progress, increase assistance.

The goal is:

```text
independent reasoning
```

not:

```text
maximum frustration
```

---

## Rule 5 — Code Can Be a Teaching Tool

A complete implementation is allowed.

When code is provided, it must be used as an object of analysis.

Ask:

```text
Why is this class here?

Why this parent?

Why this method?

Why super()?

Why composition?

What would happen if we removed inheritance?
```

---

## Rule 6 — Testing Supports Engineering

Tests should reinforce:

- contracts;
- behavior;
- state transitions;
- refactoring;
- polymorphism.

Do not turn the module into a test-writing marathon.

Providing test scaffolding is acceptable when it keeps focus on the main programming concept.

---

## Rule 7 — Preserve the Student's Architecture

Do not replace the student's design merely because another OOP architecture looks more sophisticated.

Evaluate:

- cohesion;
- coupling;
- responsibility;
- testability;
- clarity;
- maintainability;
- complexity.

---

# Design Review Checklist

Before approving an inheritance hierarchy:

```text
[ ] Is there a genuine is-a relationship?
[ ] Does the parent represent a meaningful abstraction?
[ ] Do subclasses share a stable interface?
[ ] Does polymorphism provide a real benefit?
[ ] Is composition clearly worse?
[ ] Is the hierarchy shallow?
[ ] Is the parent small and coherent?
[ ] Are invariants still protected?
[ ] Are dependencies explicit?
[ ] Can the behavior be tested easily?
```

---

# Module 04 + Module 05 Continuity

Module 06 does not replace previous principles.

Inheritance must still respect:

```text
Module 04
    ↓
explicit dependencies
clear contracts
separation of concerns
testability
refactoring discipline
    +
Module 05
    ↓
encapsulation
composition
object responsibility
state protection
```

This means:

> **Advanced OOP is still software architecture.**

A sophisticated class hierarchy with poor responsibilities is still poor architecture.

---

# Practical Testing Strategy

For each important polymorphic behavior, prefer a small number of meaningful tests.

Example conceptual structure:

```text
Behavior
   ↓
multiple implementations
   ↓
same contract
   ↓
test each implementation
```

The test should focus on observable behavior.

Do not write tests that merely confirm:

```python
isinstance(obj, Camera)
```

unless the type itself is genuinely part of the contract.

Prefer:

```text
Does the object calculate the correct cost?

Does the object reject invalid state?

Does the object preserve its invariant?

Does the caller work with every supported implementation?
```

---

# Final Integrated Project

## Project — QR Warehouse Advanced OOP Extension

The student must extend the existing QR Warehouse Project with one meaningful polymorphic feature.

The requirement should be realistic.

Possible examples:

```text
different rental pricing policies
different equipment cost calculations
different reservation rules
different export formats
different notification mechanisms
```

The student must choose the feature.

---

## Stage 1 — Requirement

Describe:

```text
What new business requirement exists?

Who needs it?

What behavior changes?
```

---

## Stage 2 — Domain Analysis

Identify:

```text
objects
responsibilities
shared behavior
specialized behavior
relationships
```

---

## Stage 3 — Architecture Proposal

Write at least two possible designs.

For example:

```text
Design A — conditional logic
Design B — polymorphism
```

Then compare:

```text
clarity
coupling
extensibility
testability
complexity
```

Choose one.

---

## Stage 4 — Contracts

For important methods:

```text
Input:
Output:
State changes:
Normal absence:
Possible errors:
Side effects:
Responsibility:
```

---

## Stage 5 — Tests

Write or extend tests before or alongside the implementation.

The mentor may provide test scaffolding.

At least:

```text
normal behavior
boundary behavior
failure behavior
multiple implementations
```

---

## Stage 6 — Implementation

Implement the smallest useful design.

Do not refactor unrelated parts of QR Warehouse.

---

## Stage 7 — Refactoring

After the feature works:

```text
identify one design problem
↓
make one meaningful improvement
↓
run tests
↓
verify behavior
```

---

## Stage 8 — Architecture Review

The student must explain:

```text
Why was inheritance used?

Why was composition rejected or retained?

Where is the common interface?

Where does polymorphism happen?

Why does each class own its behavior?

What would become difficult if five more equipment types were added?

What would happen if the feature were removed?
```

---

# Module Completion Criteria

Module 06 is complete when the student can independently:

- explain inheritance without relying on memorized definitions;
- identify genuine `is-a` relationships;
- distinguish inheritance from composition;
- create and extend subclasses;
- override methods;
- use `super()` intentionally;
- explain polymorphism;
- implement a common interface;
- use duck typing appropriately;
- recognize when inheritance should not be used;
- use abstract base classes at a basic practical level;
- recognize simple use cases for Factory and Strategy;
- test polymorphic behavior;
- use tests as protection during refactoring;
- make an architectural decision and defend it.

Most importantly, the student should be able to say:

> **"I could use inheritance here, but I chose not to because..."**

and have a technically sound reason.

That is a stronger skill than simply knowing how to write:

```python
class Child(Parent):
```

---

# Final Conceptual Transition

Module 04 taught:

> **Good structure makes change safer.**

Module 05 taught:

> **Objects can own state and behavior.**

Module 06 teaches:

> **Related objects can share interfaces without losing specialized behavior — but the relationship must be modeled deliberately.**

The progression is:

```text
Functions
    ↓
Components
    ↓
Objects
    ↓
Composition
    ↓
Inheritance
    ↓
Polymorphism
    ↓
Interchangeable behavior
    ↓
Larger maintainable systems
```

The final instinct should not be:

> "Where can I use inheritance?"

It should be:

> **"What relationship actually exists between these things, and which design expresses that relationship with the least unnecessary complexity?"**

That question is the real goal of Module 06.

---

# Self-Check Questions

Before declaring the module complete, the student should be able to answer these in their own words:

1. What problem does inheritance solve?
2. What is the difference between `is-a` and `has-a`?
3. Why is inheritance not simply a code reuse mechanism?
4. What does method overriding do?
5. Why does `super()` exist?
6. What is polymorphism?
7. How is duck typing different from inheritance?
8. What is an interface?
9. When is an abstract base class useful?
10. When is a plain class with duck typing enough?
11. Why can deep inheritance trees be dangerous?
12. What is inheritance by convenience?
13. How can polymorphism reduce conditional logic?
14. When should a simple conditional remain a conditional?
15. What is the role of Factory?
16. What problem can Strategy solve?
17. How does Strategy connect to dependency injection?
18. How should polymorphic behavior be tested?
19. Why should tests focus on behavior rather than class names?
20. How would you decide between inheritance and composition in a new project?

---

# Recommended Learning Journal Questions

After completing the module, reflect on:

```text
What changed in my understanding of inheritance?

Did I begin to see inheritance as modeling rather than code reuse?

Which inheritance relationship felt genuinely useful?

Which inheritance relationship looked attractive but was actually wrong?

Did polymorphism change how I think about conditionals?

Did I become more comfortable deciding not to use inheritance?

When did composition feel like the better solution?

Which concept required the most reasoning?

Did the increased independence in exercises help me think more clearly?

When did I actually need a hint?

Was the hint level appropriate?

Which part of the module would I want to practice again?
```

---

# Knowledge Base Integration

After Module 06, update:

```text
Programming Handbook
Learning Journal
Questions
Development Log
Mental Models
Checkpoint Report
```

The updates should preserve the historical development of the student rather than rewriting previous learning.

The Programming Handbook should store technical knowledge.

The Learning Journal should store personal learning experience.

The Development Log should record methodology changes.

Questions should preserve unresolved and resolved curiosity.

The Checkpoint Report should evaluate demonstrated competence.

---

# Final Mentor Note

The student has demonstrated strong architectural intuition in previous modules.

Module 06 should not reward the student for building the most elaborate hierarchy.

It should reward:

```text
good modeling
+
clear reasoning
+
appropriate abstraction
+
simple interfaces
+
testable behavior
+
independent decisions
```

The mentor's goal is to gradually reduce unnecessary guidance without reducing the quality of support.

The student should leave this module not thinking:

> "I know inheritance."

but:

> **"I can look at a software design, identify the relationships between objects, compare possible abstractions, and choose one deliberately."**

That is the engineering skill Module 06 is designed to develop.
