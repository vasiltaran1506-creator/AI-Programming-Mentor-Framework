# Questions

Version: 1.0

Status: Active

Maintained by: AI Programming Mentor

---

# Purpose

Questions are one of the most valuable learning resources.

Every unanswered question reveals the boundary between current knowledge and future understanding.

This document exists to preserve curiosity.

A question should never be considered a distraction.

Instead, it becomes part of the learning roadmap.

Questions should not disappear.

They move through different stages as understanding develops.

---

# Workflow

Every question belongs to exactly one state.

```
Open
    ↓
Discussing
    ↓
Answered
    ↓
Mastered
```

---

## Open

The question has been asked.

The student does not yet understand the answer.

---

## Discussing

The topic is currently being studied.

The answer may be incomplete.

Further clarification may be needed.

---

## Answered

The student understands the concept.

However, additional practical experience is still recommended.

---

## Mastered

The student has successfully applied the concept in real code.

The knowledge is considered stable.

Mastered questions remain in this document as part of the learning history.

---

# Rules

Questions are never deleted.

Questions may move between states.

A previously answered question may become Open again if later topics reveal a deeper misunderstanding.

This is considered normal.

---

# Open Questions

## Q-0001

Title

Why does Python start indexing at zero?

Reason

The student understands that indexing starts at zero but wants to understand the historical and technical reasons behind this design.

Related Topics

- Lists
- Memory
- Arrays

Priority

Medium

Status

Open

---

## Q-0002

Title

What actually happens inside memory when variables change?

Reason

The student has a good intuitive understanding of state but wants to understand how Python stores and updates objects internally.

Related Topics

- Variables
- Assignment
- Objects
- References

Priority

High

Status

Open

---

## Q-0004
Title
How does hashing work inside sets and dictionaries?
Reason
The student understands that sets provide instant lookup and that dictionaries use keys for fast access.
However, the underlying mechanism — hashing — has not been explored.
The student asked why `in` works instantly for sets but requires iteration for lists.
Related Topics
Sets
Dictionaries
Hash Tables
Performance
Priority
Medium
Status
Open

## Q-0005
Title:
What is the difference between pathlib.Path and string paths?

Reason:
The student used pathlib.Path during the Tag Library Manager project and encountered confusion between Path objects and string paths.
The student understood the basic usage but wants a deeper understanding of when to use Path objects versus plain strings.

Related Topics:
pathlib
File I/O
Object-Oriented Design

Priority:
Medium

Status:
Mastered

---

# Discussing

(No questions currently in this state.)

---

# Answered

(No questions yet.)

---

# Mastered

Q-0003
Title
Why do some functions return values while others only modify existing objects?
Reason
This question naturally follows the discussion about `print()`, `return()`, and methods such as `append()`.
Resolution
Студент глубоко усвоил разницу между неизменяемыми (immutable) и изменяемыми (mutable) типами данных. Он понял, что строки (камни) требуют `return`, потому что методы создают новые объекты. В то время как списки и словари (корзины) передаются в функции по ссылке, и их можно модифицировать на месте без `return`. Концепция закреплена на практике при написании парсера тегов.


---

# Mentor Responsibilities

The mentor should review this document at the beginning of every new module.

If today's lesson naturally answers one of the Open questions, the mentor should explicitly reference it.

Example:

"This lesson answers Question Q-0002."

This helps the student connect new knowledge with previous curiosity.

---

# Student Responsibilities

The student should add new questions whenever they appear.

Questions do not need to be well written.

Even incomplete thoughts deserve to be recorded.

Examples:

"Why?"

"How?"

"What if...?"

The mentor is responsible for refining them into proper engineering questions.

---

# Quality Rules

A good question is:

- specific;
- motivated by curiosity;
- connected to programming;
- possible to answer.

Poor example:

"How does Python work?"

Better example:

"Why are strings immutable in Python?"

---

# Long-Term Vision

Over time this document should become a map of the student's intellectual journey.

Many questions that once seemed impossible will eventually become obvious.

New questions will replace them.

This continuous cycle of asking, understanding and applying is one of the defining characteristics of professional engineers.

---

End of document.