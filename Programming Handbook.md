# Programming Handbook

Version: 1.0

Status: Active

Last Updated: After Module 01

---

# Purpose

The Programming Handbook is the student's permanent engineering reference.

Unlike the Learning Journal, which records personal experiences, this document stores technical knowledge.

Unlike course modules, this document is not intended to teach new topics.

Instead, it explains concepts that have already been learned.

Every topic should be understandable months or years after it was first studied.

This document grows throughout the student's entire programming journey.

---

# How to Use This Handbook

This handbook is not meant to be read from beginning to end.

Instead:

- Search for a concept you have forgotten.
- Review syntax before writing code.
- Refresh your understanding of a topic.
- Connect related concepts together.

Whenever a new concept is learned, a new section should be added.

Existing sections may be improved but should never lose useful information.

---

# Variables

## What is a Variable?

A variable is a name that refers to a value.

The variable is **not** the value itself.

It simply allows the program to access that value later.

---

## Mental Model

Imagine putting a sticker with a name onto an object.

The sticker is the variable.

The object is the value.

You can move the sticker to another object.

The objects themselves do not move.

---

## Example

```python
name = "Alice"
age = 20
price = 15.5
```

---

## Assignment

The assignment operator (`=`) does not mean equality.

It means:

"Store the value on the right and make the variable on the left refer to it."

```python
score = 10
score = score + 5
```

After execution:

```
score

↓

15
```

---

## Common Mistakes

Thinking that `=` means mathematical equality.

Trying to use a variable before assigning a value.

Using unclear variable names.

---

## Best Practices

Use descriptive names.

Bad:

```python
x = 10
```

Better:

```python
student_age = 10
```

---

# Data Types

Python values have types.

The type determines:

- what operations are allowed;
- how the value is stored;
- how Python interprets it.

---

## str

Text.

```python
name = "Alice"
```

Common operations:

```python
.upper()

.lower()

.strip()

.replace()
```

---

## int

Whole numbers.

```python
age = 25
```

---

## float

Decimal numbers.

```python
price = 12.5
```

---

## Type Conversion

Sometimes data must be converted.

```python
age = int(input())
```

```python
price = float(input())
```

```python
text = str(number)
```

---

## Common Mistakes

Trying to add strings and numbers.

```python
"5" + 5
```

This produces an error.

Convert first.

```python
int("5") + 5
```

---

# Input and Output

Programs communicate with users.

Input:

```python
input()
```

Output:

```python
print()
```

---

## Example

```python
name = input("Name: ")

print(name)
```

---

## f-Strings

Recommended way to build text.

```python
print(f"Hello, {name}")
```

---

# Conditions

Programs make decisions using conditions.

```python
if

elif

else
```

---

## Example

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## Comparison Operators

```
==

!=

>

<

>=

<=
```

---

## Logical Operators

```
and

or

not
```

---

# Lists

A list stores multiple values.

Example:

```python
grades = [5, 4, 3]
```

---

## Mental Model

A numbered shelf.

Each item occupies a numbered position.

The numbering starts at **0**.

---

## Index

```python
grades[0]
```

returns

```
5
```

---

## Common Operations

```python
append()

remove()

len()

sort()
```

---

## Common Mistakes

Forgetting that indexing starts from zero.

Trying to access an index that does not exist.

---

# Loops

Loops repeat work.

Python has two main loop types.

---

## for

Used when iterating over a collection.

```python
for item in items:
    print(item)
```

---

## while

Used while a condition remains true.

```python
while True:
    ...
```

Often combined with

```
break
```

---

## Choosing Between Them

Use

```
for
```

when iterating over existing data.

Use

```
while
```

when waiting for something to happen.

---

# Functions

Functions group reusable logic.

Instead of repeating code:

```python
print("Hello")
print("Hello")
print("Hello")
```

Create a function.

---

## Syntax

```python
def greet(name):
    print(f"Hello {name}")
```

---

## Calling

```python
greet("Alice")
```

---

## Parameters

Names inside the function.

```python
def add(a, b):
```

---

## Arguments

Actual values passed into the function.

```python
add(5, 3)
```

---

## Return

A function may return a result.

```python
def square(x):
    return x * x
```

---

## print vs return

This is one of the most important concepts in Python.

```
print()

↓

Shows information.

```

```
return

↓

Gives a value back to the program.
```

If another part of the program needs the result,

use

```
return
```

---

## Mental Model

A factory.

Input enters.

Work happens.

Finished product leaves through the exit.

That exit is

```
return
```

---

# Program State

Every running program has a current state.

Variables change.

Lists change.

Objects change.

The state changes over time.

Programming is largely the process of managing state safely.

---

# Problem Decomposition

Large problems should never be solved all at once.

Instead:

Large Problem

↓

Smaller Problems

↓

Even Smaller Problems

↓

Simple Tasks

Only then should code be written.

---

# Separation of Concerns

Each part of the program should have one responsibility.

Example:

One function:

Collect user input.

Another:

Perform calculations.

Another:

Display results.

Mixing all responsibilities together makes programs difficult to maintain.

---

# Common Beginner Mistakes

Trying to memorize syntax instead of understanding concepts.

Writing everything inside one large function.

Using meaningless variable names.

Copying code without understanding it.

Ignoring error messages.

Being afraid to refactor.

---

# Engineering Principles Learned So Far

Always understand before coding.

Design algorithms before writing syntax.

Functions should have one responsibility.

Readable code is more valuable than clever code.

Small improvements accumulate over time.

Understanding is more important than memorization.

---

# Topics Planned for Future Updates

- Dictionaries
- Tuples
- Sets
- Files
- Modules
- Imports
- Exceptions
- Classes
- Objects
- OOP
- pathlib
- JSON
- Qt
- Git
- Testing
- Debugging
- Software Architecture

---

End of document.