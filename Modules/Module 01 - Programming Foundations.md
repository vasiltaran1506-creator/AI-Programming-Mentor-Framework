# Module 01 - Programming Foundations

**Framework:** AI Programming Mentor Framework (APMF)

**Version:** 0.1 Alpha

**Stage:** Stage 1 — Programming Foundations

**Status:** Active

---

# 1. Module Purpose

This module introduces the fundamental building blocks of programming through the Python language.

The main objective is not memorizing Python syntax.

The objective is to understand how abstract programming ideas become concrete instructions executed by a computer.

The student should learn to translate:

```
Problem

↓

Algorithm

↓

Program Structure

↓

Python Code
```

---

# 2. Learning Objectives

After completing this module, the student should understand:

* how programs store information;
* how data exists inside a computer program;
* how instructions are executed sequentially;
* how programs make decisions;
* how repeated actions are automated;
* how reusable logic is created with functions;
* how Python syntax represents programming concepts.

---

# 3. Core Learning Principles

The mentor should follow these principles:

## Understanding Before Syntax

Do not introduce Python syntax without explaining the underlying concept.

Example:

Before teaching:

```python
counter = 0
```

Explain:

* programs need memory;
* information must have a place where it is stored;
* variables provide names for stored values.

---

## Code Is a Representation of Thought

Every code example should begin with:

1. What problem are we solving?
2. What information do we need?
3. What steps should happen?
4. How does Python express those steps?

---

## Small Programs First

The student should create many small programs.

The goal is developing confidence with programming mechanics.

---

# 4. Concept 1 — Variables and State

## Objective

Understand how programs store and update information.

---

## Core Idea

A variable is a named reference to a value.

Programs constantly work with changing information.

Example:

A program tracking a player's score:

```
Initial state:

score = 0


After gaining points:

score = 10


After another action:

score = 25
```

The important concept is not the syntax.

The important concept is:

> A program has a state that changes over time.

---

## Python Introduction

Example:

```python
score = 0

score = score + 10

print(score)
```

The student should understand:

* where the value is stored;
* why the second assignment changes the state;
* why the previous value is replaced.

---

# 5. Concept 2 — Data Types

## Objective

Understand that different kinds of information require different representations.

---

## Core Idea

Computers need to know what kind of data they are working with.

Examples:

Numbers:

```
10
3.14
```

Text:

```
"Python"
```

Logical values:

```
True
False
```

---

## Important Concepts

The student should understand:

* integers;
* floating-point numbers;
* strings;
* booleans.

---

## Example

```python
age = 21
name = "Vasily"
is_student = True
```

The important question:

Not:

> "How do I write a string?"

But:

> "What type of information does my program need to represent?"

---

# 6. Concept 3 — Input and Output

## Objective

Connect programs with external information.

---

## Core Idea

Programs usually follow the model:

```
Input

↓

Processing

↓

Output
```

---

## Example

A simple greeting program:

Input:

```
User name
```

Processing:

```
Create greeting message
```

Output:

```
Hello, Vasily!
```

---

## Python Introduction

```python
name = input("Your name: ")

print("Hello,", name)
```

---

# 7. Concept 4 — Conditions

## Objective

Teach programs to make decisions.

---

## Core Idea

Programs often need different behavior depending on circumstances.

Example:

Problem:

```
If a user has permission:
    allow access

Otherwise:
    deny access
```

---

## Python Introduction

```python
age = 18

if age >= 18:
    print("Access allowed")
else:
    print("Access denied")
```

---

## Important Understanding

The student should understand:

A condition is not just syntax.

It is a formal representation of a decision.

---

# 8. Concept 5 — Loops

## Objective

Understand automation of repeated actions.

---

## Core Idea

Computers are good at repeating predictable operations.

Example:

Problem:

```
Check every file in a folder.
```

Human approach:

```
Open file 1
Check file 1

Open file 2
Check file 2

...
```

Program approach:

```
Repeat the same operation for every item.
```

---

## Python Introduction

```python
files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    print(file)
```

---

# 9. Concept 6 — Functions

## Objective

Understand how programs are divided into reusable components.

---

## Core Idea

Functions allow programmers to package logic.

Instead of:

```
Repeat the same instructions everywhere
```

we create:

```
Reusable operation
```

---

## Example

```python
def greet(name):
    print("Hello,", name)


greet("Anna")
```

---

## Important Understanding

A function should represent a clear responsibility.

The student should avoid creating large functions that do everything.

---

# 10. Practical Exercises

---

# Exercise 1 — State Tracking

Create a small program that tracks changing information.

Examples:

* player health;
* bank balance;
* task progress;
* inventory quantity.

Requirements:

* create initial state;
* modify state;
* display result.

---

# Exercise 2 — Data Classification

Take a real-world object.

Example:

A character in a game.

Identify:

* text data;
* numeric data;
* logical data.

Example:

```
Character:

Name:
Health:
Level:
Is_alive:
```

---

# Exercise 3 — Decision Program

Create a program that makes a simple decision.

Examples:

* check password length;
* determine access permission;
* calculate discount.

---

# Exercise 4 — Automation

Take a repetitive task and describe:

Before:

```
Manual process
```

After:

```
Automated algorithm
```

Then implement the simplest Python version.

---

# Exercise 5 — Translation Exercise

Take one algorithm from Module 00.

Example:

"Process files in a folder."

Do not build a complete application.

Only translate the logical structure into Python concepts:

* variables;
* conditions;
* loops;
* functions.

---

# 11. Knowledge Verification Questions

The student should be able to answer:

1. What is the difference between a value and a variable?

2. Why do programs need different data types?

3. What does changing a variable represent?

4. How does an `if` statement relate to human decision making?

5. Why are loops useful?

6. Why should logic be placed inside functions?

7. How does Python code represent an algorithm?

---

# 12. Common Difficulties Expected

The mentor should expect:

## Syntax Frustration

The student may understand the idea but make syntax errors.

This is normal.

Focus on understanding, not memorization.

---

## Confusing Code and Logic

The student may believe:

"I wrote incorrect Python, therefore my idea was wrong."

The mentor should separate:

* algorithm errors;
* implementation errors.

---

## Overengineering

Because the student has strong analytical thinking, there is a risk of designing overly complex solutions.

The mentor should teach:

> The simplest working solution is often the best first solution.

---

# 13. Completion Criteria

The module is completed when the student can:

* explain the role of variables;
* work with basic Python data types;
* create simple programs with input and output;
* use conditions;
* use loops;
* create simple functions;
* translate simple algorithms into Python code;
* explain their own code.

---

# 14. Mentor Notes

This module is a transition point.

The student already understands many abstract programming concepts.

The main challenge is connecting those concepts with the strict rules of a programming language.

The mentor should repeatedly reinforce:

```
Python is not programming itself.

Python is a tool for expressing programming ideas.
```

---

**End of Module 01 - Programming Foundations**
