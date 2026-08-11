# Module 03 — Building Real Python Programs

**Stage:** 2 — Python Application Foundations
**Prerequisites:** Module 00, Module 01, Module 02
**Primary language:** Python 3
**Teaching language:** English
**Estimated difficulty:** Intermediate Beginner
**Purpose:** Move from writing individual scripts toward understanding the structure of real programs.

---

# Module Overview

In Module 02, you learned to work with Python's toolbox:

* lists;
* dictionaries;
* sets;
* strings;
* functions;
* files;
* `pathlib`;
* standard Python tools;
* basic data structure design.

However, most of these skills still exist inside relatively small programs.

The next step is to understand:

> **How are these elements combined into a program made of multiple parts?**

A real program rarely consists of one long file.

Instead, it usually consists of components, each responsible for a specific task:

```text
program
│
├── configuration
├── data access
├── business logic
├── validation
├── user interface
└── entry point
```

Module 03 is dedicated to this transition.

---

# Main Principle of the Module

> **Do not just learn to write working code — learn to organize working code.**

In Module 02, the main question was:

> "Which Python tool is appropriate for this task?"

In Module 03, another question appears:

> "Where exactly should this code live?"

And another:

> "What should happen if something goes wrong?"

---

# Learning Goals

By the end of the module, the student should be able to:

1. Work with the filesystem using `pathlib`.
2. Understand the difference between `Path` objects and string paths.
3. Import code from other modules.
4. Understand what happens during `import`.
5. Split a program across multiple `.py` files.
6. Define the responsibility of individual modules.
7. Understand the basic structure of a Python project.
8. Work with exceptions.
9. Distinguish an expected error from an actual program failure.
10. Design predictable functions.
11. Work with JSON.
12. Separate configuration data from program logic.
13. Use mock data during development.
14. Read and interpret tracebacks independently.
15. Debug a multi-file program.
16. Understand the flow of data through multiple components.

---

# Chapter 01 — Filesystem as a Data Structure

## 1.1. From Files to the Filesystem

Previously, a file was considered approximately like this:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

Now we need to look at the bigger picture.

A file is only one object inside a filesystem.

A filesystem contains:

```text
folder
├── file
├── file
├── folder
│   ├── file
│   └── file
└── folder
```

A program should be able to:

* find files;
* create directories;
* check whether objects exist;
* determine the type of an object;
* move files;
* copy files;
* delete files;
* retrieve information about files.

---

## 1.2. `pathlib.Path`

The primary tool is:

```python
from pathlib import Path
```

Creating a path:

```python
path = Path("data/example.txt")
```

Important:

```python
path
```

is a **`Path` object**, not simply a string.

Mental model:

> A string describes **how a path is written**.
> A `Path` represents that path as an **object that a program can work with**.

---

## 1.3. `Path` vs `str`

A string:

```python
path = "data/example.txt"
```

A `Path`:

```python
path = Path("data/example.txt")
```

A string can be displayed:

```python
print(path)
```

But a `Path` provides filesystem-related operations:

```python
path.exists()
path.is_file()
path.is_dir()
path.name
path.stem
path.suffix
path.parent
```

For example:

```python
path = Path("images/photo.png")

print(path.name)
print(path.stem)
print(path.suffix)
```

Result:

```text
photo.png
photo
.png
```

---

## 1.4. Building Paths

Do not manually write:

```python
"data/" + filename
```

Use:

```python
path = Path("data") / filename
```

For example:

```python
folder = Path("images")
filename = "photo.png"

path = folder / filename
```

This is an important habit when working with filesystems.

---

## 1.5. Checking Existence

```python
path.exists()
```

returns:

```python
True
```

or:

```python
False
```

Checking the object type:

```python
path.is_file()
```

```python
path.is_dir()
```

Remember the mistake from earlier modules:

```python
path.exists
```

and:

```python
path.exists()
```

are fundamentally different.

The first is a reference to the method.

The second actually calls the method.

---

## 1.6. Iterating Through a Directory

```python
folder = Path("images")

for item in folder.iterdir():
    print(item)
```

You can check each object:

```python
for item in folder.iterdir():
    if item.is_file():
        print(item)
```

---

## 1.7. Searching by Pattern

```python
for file in folder.glob("*.png"):
    print(file)
```

Recursive search:

```python
for file in folder.rglob("*.png"):
    print(file)
```

The important distinction is:

```text
glob  → searches the specified directory
rglob → also searches nested directories
```

---

## 1.8. Practice

The student should independently write a program that:

1. receives a directory path;
2. checks whether it exists;
3. determines whether it is a directory;
4. finds all `.txt` files;
5. prints their names;
6. separately counts the number of files found.

### Constraint

Do not use `os.walk()`.

The purpose of the task is to reinforce `pathlib`.

---

# Chapter 02 — Modules and Imports

## 2.1. The Problem with One File

Imagine a program:

```text
main.py
```

It contains:

* file reading;
* data processing;
* calculations;
* validation;
* menus;
* output;
* configuration.

At first, this is convenient.

Later, the file becomes:

```text
main.py
  1000 lines
  2000 lines
  3000 lines
```

The problem is not only its size.

The real problem is that different parts of the program become mixed together.

---

# 2.2. A Module

Any Python file can act as a module.

For example:

```text
math_tools.py
```

contains:

```python
def add(a, b):
    return a + b
```

Another file:

```text
main.py
```

can use this function:

```python
from math_tools import add

result = add(2, 3)
print(result)
```

---

# 2.3. `import`

You can import an entire module:

```python
import math_tools
```

and use:

```python
math_tools.add(2, 3)
```

Or import a specific object:

```python
from math_tools import add
```

Now:

```python
add(2, 3)
```

---

# 2.4. Why This Matters

`import` is not merely a syntax construct.

It means:

> "This part of the program uses functionality provided by another module."

This creates a dependency:

```text
main.py
   │
   ▼
math_tools.py
```

As programs grow, there may be many such dependencies.

---

# 2.5. Separation of Responsibility

Poor structure:

```text
main.py
├── file reading
├── calculations
├── validation
├── configuration
├── output
└── everything else
```

Better:

```text
project/
├── main.py
├── file_utils.py
├── data_processing.py
├── validation.py
└── config.py
```

Now each file has a more understandable responsibility.

---

# 2.6. Do Not Turn Every File into a Junk Drawer

Important:

> Splitting files is not an end in itself.

Do not create:

```text
print_helper.py
string_helper.py
number_helper.py
loop_helper.py
```

for every two-line function.

A module should group components that are **related in purpose**.

---

# 2.7. `if __name__ == "__main__"`

A very important construction:

```python
if __name__ == "__main__":
    main()
```

It allows Python to distinguish between:

```text
running a file directly
```

and:

```text
importing the file from another module
```

For example:

```python
def greet():
    print("Hello")


if __name__ == "__main__":
    greet()
```

When run directly:

```text
Hello
```

When imported:

```python
import greetings
```

`greet()` will not be called automatically.

---

# 2.8. Practical Task

Create a program consisting of three files:

```text
project/
├── main.py
├── calculations.py
└── data.py
```

`data.py` is responsible for data.

`calculations.py` is responsible for calculations.

`main.py` is responsible for starting the program and interacting with the user.

The main goal of the exercise is:

> to experience that a program can be one coherent organism even when its code is distributed across multiple files.

---

# Chapter 03 — Designing a Multi-File Program

Now we combine the previous knowledge.

Create an architecture such as:

```text
file_analyzer/
│
├── main.py
├── filesystem.py
├── analyzer.py
├── formatter.py
└── data/
```

Responsibilities:

### `filesystem.py`

Working with files and directories.

### `analyzer.py`

Analyzing the collected data.

### `formatter.py`

Preparing results for display.

### `main.py`

Orchestrating the program.

---

# 3.1. Data Flow

For example:

```text
Filesystem
     │
     ▼
raw data
     │
     ▼
Analyzer
     │
     ▼
results
     │
     ▼
Formatter
     │
     ▼
User
```

This is a very important concept.

Each component should have a clear input and output.

---

# 3.2. Function Contracts

For example:

```python
def find_files(folder):
    ...
```

We should understand:

### Input

```text
Path
```

### Output

```text
list[Path]
```

Not:

```text
sometimes list
sometimes None
sometimes string
```

If a function has an unpredictable contract, the rest of the program becomes fragile.

---

# 3.3. Architecture Exercise

The student will be given the task:

> Design a program for analyzing a directory.

Before writing code, the student must determine:

1. which components exist;
2. which file is responsible for what;
3. what data is passed between components;
4. which functions are needed;
5. what types of data they accept;
6. what they return.

**Code comes only after the design.**

This deliberately continues one of the student's strongest habits from Modules 00–02:

> architecture first, implementation second.

---

# Chapter 04 — Exceptions and Failure

Previously, programs were mainly considered under the model:

```text
Input → Processing → Output
```

But real programs constantly encounter situations such as:

```text
file does not exist
path is incorrect
JSON is corrupted
data has the wrong type
user entered invalid input
access is denied
```

A program must know how to deal with such situations.

---

# 4.1. What Is an Exception?

For example:

```python
number = int("hello")
```

Python cannot perform the requested operation.

A:

```text
ValueError
```

is raised.

---

# 4.2. Traceback

A traceback shows:

```text
where the error occurred
```

and:

```text
how the program reached that point
```

It is important to learn to read tracebacks **from the bottom upward**.

The bottom usually contains:

```text
error type
error message
```

The lines above show the chain of function calls that led to the error.

---

# 4.3. `try / except`

```python
try:
    number = int(user_input)
except ValueError:
    print("Enter a number")
```

Mental model:

> `try` — "attempt this operation."

> `except` — "if this specific expected error occurs, handle it here."

---

# 4.4. Do Not Catch Everything

Bad:

```python
try:
    ...
except:
    pass
```

This hides errors.

Better:

```python
except ValueError:
    ...
```

Handle the errors that the program actually expects.

---

# 4.5. `else`

```python
try:
    number = int(value)
except ValueError:
    print("Invalid number")
else:
    print(number)
```

`else` runs when no exception occurs.

---

# 4.6. `finally`

```python
try:
    ...
except SomeError:
    ...
finally:
    ...
```

`finally` is used for actions that should happen regardless of whether an exception occurred.

At this stage, the main goal is to understand the concept rather than memorize every possible use case.

---

# 4.7. An Error Is Not Automatically Something to Hide

A very important distinction:

```text
Expected situation
→ handle it

Unexpected program failure
→ investigate and fix it
```

For example:

The user enters:

```text
abc
```

instead of a number.

This is an expected input error.

But if:

```python
result = user["name"]["length"]
```

fails because the program unexpectedly produced the wrong data structure, this is a reason to investigate the underlying problem.

---

# 4.8. Practice

Create a program that:

* accepts a path;
* attempts to open a file;
* correctly reports a missing file;
* handles relevant reading or encoding errors where appropriate;
* does not hide unknown errors.

---

# Chapter 05 — JSON and Structured Data

## 5.1. The Problem of Data Persistence

Previously, data lived inside Python:

```python
students = {
    "Alice": 20,
    "Bob": 21
}
```

But after the program terminates, the data disappears.

We need to save it.

---

# 5.2. JSON

JSON is a simple text format for storing structured data.

For example:

```json
{
    "name": "Alice",
    "age": 20,
    "tags": ["python", "programming"]
}
```

---

# 5.3. Python ↔ JSON

Python:

```text
dict
list
str
int
float
bool
None
```

JSON:

```text
object
array
string
number
true
false
null
```

---

# 5.4. Writing JSON

```python
import json

data = {
    "name": "Alice",
    "age": 20
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
```

---

# 5.5. Reading JSON

```python
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

Now:

```python
data
```

is once again a Python data structure.

---

# 5.6. JSON as a Boundary

A very important engineering idea:

```text
File
  ↓
JSON
  ↓
Python data
  ↓
Business logic
```

Business logic should not constantly think:

> "How is this object represented in JSON?"

It should work with normal Python data structures.

---

# Chapter 06 — Configuration and Data Boundaries

Now another important separation appears.

Imagine:

```python
DATA_FOLDER = "data"
MAX_FILES = 100
OUTPUT_FORMAT = "json"
```

These are settings.

They are not business logic.

---

# 6.1. Configuration

Settings can be stored separately:

```text
project/
├── main.py
├── config.py
└── settings.json
```

For example:

```python
DATA_FOLDER = "data"
MAX_FILES = 100
```

---

# 6.2. Why This Matters

If the path to a directory is used in ten places:

```text
"data"
```

and the directory changes later, you need to change ten places.

If the value is centralized:

```python
DATA_FOLDER = "new_data"
```

the change happens in one place.

---

# 6.3. Data Boundaries

We introduce the principle:

> **External data should be converted into understandable internal structures as early as possible.**

For example:

```text
JSON
 ↓
validation
 ↓
Python data structures
 ↓
business logic
```

Do not force every component of the program to know how an external format is structured.

---

# Chapter 07 — Validation and Defensive Programming

Now we combine:

* functions;
* dictionaries;
* JSON;
* exceptions;
* file input.

Imagine:

```json
{
    "name": "Alice",
    "age": 20
}
```

But a user may provide:

```json
{
    "name": 123,
    "age": "hello"
}
```

The program needs to determine:

> "These data do not match the expected structure."

---

# 7.1. Validation

Validation is the process of checking whether data satisfies certain requirements.

For example:

```python
def validate_student(data):
    if not isinstance(data, dict):
        return False

    if "name" not in data:
        return False

    if "age" not in data:
        return False

    return True
```

At this stage, there is no need to build a sophisticated validation system.

The main idea is to understand the boundary:

```text
data received
      ↓
validated
      ↓
used
```

---

# 7.2. Why Validation Should Be Separate

Poor approach:

```python
def calculate(data):
    if ...
    if ...
    if ...
    if ...
    # calculation
```

This mixes:

```text
validation
+
business logic
```

Better:

```python
if validate(data):
    calculate(data)
```

---

# 7.3. Contracts

A function:

```python
calculate(data)
```

may assume:

```text
data — a valid dictionary
```

Its responsibility is then to calculate the result, not to check every possible problem in the universe.

This allows us to gradually build a pipeline:

```text
Input
 ↓
Validation
 ↓
Processing
 ↓
Output
```

---

# Chapter 08 — The First Real Multi-File Project

The final chapter of the module combines everything studied.

The student receives a task to independently create a small program.

### Requirements

The program must:

* contain multiple Python files;
* use `pathlib`;
* read data from a file;
* use JSON;
* have a separate data-processing module;
* have validation;
* handle expected errors;
* contain understandable functions;
* have a single entry point.

---

# Recommended Structure

```text
project/
│
├── main.py
├── filesystem.py
├── data_loader.py
├── validator.py
├── processor.py
├── config.py
│
└── data/
    ├── input.json
    └── output.json
```

However, **do not give this structure to the student as a ready-made answer immediately**.

The student should first propose an architecture independently.

The mentor then analyzes it.

---

# Project Challenge

### Scenario

Imagine that you have a directory containing data about a collection of objects.

For example:

```json
[
    {
        "name": "Item A",
        "category": "tools",
        "price": 100
    },
    {
        "name": "Item B",
        "category": "books",
        "price": 20
    }
]
```

The program should:

1. load the data;
2. validate it;
3. process it;
4. perform several calculations;
5. produce a result;
6. save the result;
7. inform the user about the result.

---

# Constraints

The student **does not receive the finished architecture**.

Before writing code, the student must provide:

### 1. Problem Decomposition

What tasks exist?

### 2. Data Model

What data structures will be used?

### 3. Component Design

Which modules are needed?

### 4. Function Contracts

For each key function:

```text
Input:
Output:
Possible errors:
Responsibility:
```

### 5. Data Flow

For example:

```text
JSON
 ↓
Loader
 ↓
Validation
 ↓
Processor
 ↓
Result
 ↓
JSON
```

---

# Final Assessment

The final task should be completed **without step-by-step guidance**.

Qwen should not immediately correct mistakes.

If the student asks:

> "How do I write this function?"

the mentor should first determine whether the problem is actually a lack of knowledge, or whether the student is trying to skip the design stage.

If the architecture has not been defined:

> return to architecture first.

If the architecture is correct but the syntax is unknown:

> provide a minimal hint.

If an error occurs:

> ask the student to read the traceback independently and formulate a hypothesis.

---

# Module 03 — Required Competencies

## PF-004 — Filesystem Operations

The student can:

* create `Path` objects;
* check `exists()`;
* distinguish files from directories;
* use `iterdir()`;
* use `glob()` / `rglob()`;
* construct paths using `/`.

**Target:** Level 3 — Independent Application.

---

## PF-005 — Modules

The student understands:

* what a module is;
* why `import` exists;
* the difference between `import x` and `from x import y`;
* the basic role of `__name__`;
* why programs are divided into files.

**Target:** Level 3.

---

## PF-006 — Program Architecture

The student can:

* divide a program into components;
* define the responsibility of a module;
* describe data flow;
* formulate function contracts.

**Target:** Level 2–3.

This is one of the key competencies of Module 03.

---

## PF-007 — Exception Handling

The student can:

* read a traceback;
* understand `Exception`;
* use `try`;
* use specific `except` clauses;
* avoid hiding unknown errors.

**Target:** Level 3.

---

## PF-008 — Structured Data Persistence

The student can:

* read JSON;
* write JSON;
* convert JSON ↔ Python data;
* separate an external data format from internal program logic.

**Target:** Level 3.

---

## PF-009 — Validation

The student understands:

* what validation is;
* why data boundaries are important;
* why functions should receive expected data types;
* why validation and business logic should preferably be separated.

**Target:** Level 2–3.

---

# Module 03 Methodological Rules

These rules should be used by Qwen during the learning process.

### Rule 1 — Do Not Over-Explain Syntax

If the student already understands the concept but has forgotten the syntax, do not give another theoretical lecture.

Provide a minimal hint and allow the student to write the code independently.

---

### Rule 2 — Type Check

Whenever a method-related error occurs, ask:

> "What type of object is on the left side of the dot?"

For example:

```python
data.append(...)
```

Instead of immediately answering:

> "There is an error here."

First ask:

> "What is `data`? What type is it?"

---

### Rule 3 — Contract Check

When there is a problem with a function, ask:

```text
What does it accept?
What should it return?
What does it actually return?
```

---

### Rule 4 — Architecture Before Implementation

If a task requires multiple components:

> first the diagram → then the functions → then the code.

---

### Rule 5 — Failure Is Data

An error should be treated as information.

Not:

> "Wrong. Here is the corrected code."

Instead:

```text
What happened?
Where did it happen?
Why did it happen?
What hypothesis can you propose?
```

---

### Rule 6 — Preserve Independence

The student is already capable of solving reasonably complex problems independently.

Therefore, Qwen should not become a code autocomplete system.

Priority:

```text
student reasoning
        ↓
hint
        ↓
attempt
        ↓
feedback
        ↓
solution
```

not:

```text
question
 ↓
AI code
 ↓
copy
```

---

# Module 03 Practical Projects

The module should contain several small projects, not only one large project.

Recommended directions:

### Project A — File Analyzer

Work with:

```text
Path
iterdir
glob
file metadata
```

### Project B — JSON Data Processor

Work with:

```text
JSON
dict
list
validation
processing
```

### Project C — Multi-File Utility

Work with:

```text
imports
modules
functions
architecture
```

### Project D — Final Integrated Project

Combines everything.

---

# Open Questions Carried Forward

The following questions do not need to be artificially resolved at the beginning of Module 03.

### Q-0004

**How does hashing work inside sets and dictionaries?**

Status:

```text
Open
```

Return to this question after enough context has been introduced to study:

* hash functions;
* hash tables;
* collisions;
* average-case complexity;
* `O(1)` lookup.

---

### Q-0005

**What is the difference between `pathlib.Path` and string paths?**

Status:

```text
Open
```

This question should naturally be addressed during Chapter 01 of Module 03.

After completing the chapter, Qwen should verify whether the student can independently explain:

> how `Path` differs from `str` and why `Path` is preferable for filesystem operations.

---

# Expected Learning Journal Additions

After Module 03, Qwen should update `Learning Journal.md`.

It is especially important to record:

* what changed in the student's understanding of modules;
* what became clearer about `Path`;
* what was difficult about `import`;
* how the student learned to read tracebacks;
* which exceptions the student learned to handle;
* how the student understood JSON;
* how the student's understanding of boundaries between components changed;
* which architectural decisions the student made independently.

---

# Expected Development Log Additions

Qwen should track:

### Active Pattern

**Syntax vs Architecture Gap**

If the architecture of a solution is correct but the implementation contains syntax errors, do not treat this as an architectural failure.

---

### Active Pattern

**Type Awareness**

Continue tracking cases of:

```text
wrong method
wrong type
wrong return value
```

---

### New Pattern

**Module Responsibility**

Track whether the student attempts to put too many unrelated responsibilities into a single file.

---

### New Pattern

**Exception Overuse**

Track attempts such as:

```python
except:
    pass
```

or excessive use of `try/except` instead of fixing an underlying logical error.

---

# Completion Criteria

Module 03 is considered complete when the student can independently create a small multi-file program in which:

```text
             ┌──────────────┐
             │    Input     │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │  Validation  │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │  Processing  │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │    Output    │
             └──────────────┘
```

and:

* components are separated by responsibility;
* data has understandable types;
* functions have predictable contracts;
* the filesystem is handled through `pathlib`;
* external data is loaded separately from business logic;
* expected errors are handled;
* unexpected errors are not hidden;
* the student can explain **why the program is structured this way**.

The main criterion is:

> **The student must be able not only to run the program, but also to give a guided tour of its architecture: open each file and explain why it exists, what data it receives, what it does, and what it returns.**

---

# Final Idea of Module 03

Module 02 taught:

> **"Python has tools. Choose the right tool."**

Module 03 should teach:

> **"A program has parts. Distribute responsibility between them correctly."**

This is the next qualitative step from writing individual scripts toward real software engineering.
