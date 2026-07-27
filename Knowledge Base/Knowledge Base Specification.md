# APMF Knowledge Base Specification

Version: 2.0

Status: Active

Author: AI Programming Mentor Framework

---

# 1. Purpose

The Knowledge Base (KB) is the long-term memory of the student's learning process.

Unlike modules, which teach concepts, or checkpoints, which evaluate progress, the Knowledge Base stores knowledge that should remain useful long after a module has been completed.

Its primary goal is to reduce forgetting, improve long-term retention, and create a personal engineering reference tailored to the student.

The Knowledge Base is not a textbook.

It is a living collection of documents that evolves throughout the student's journey.

---

# 2. Design Principles

The Knowledge Base follows several fundamental principles.

## 2.1 Student-Oriented

Every explanation must be written for the student who owns the repository.

The goal is understanding, not completeness.

If a concept can be explained using terminology the student already knows, that explanation should be preferred over a formal definition.

---

## 2.2 Incremental Growth

Knowledge is accumulated gradually.

Existing documents should rarely be rewritten from scratch.

Instead:

- new sections are added;
- explanations are improved;
- examples are expanded;
- relationships between concepts are strengthened.

The Knowledge Base should continuously grow alongside the student's experience.

---

## 2.3 Engineering Focus

The purpose of the Knowledge Base is practical engineering.

Every concept should answer at least one of the following questions:

- What is it?
- Why does it exist?
- When should I use it?
- How does it work?
- What mistakes are common?
- How is it used in real projects?

Concepts that cannot answer these questions should not be included.

---

## 2.4 Mental Models Before Formal Definitions

Concepts should first be introduced through intuition.

Formal definitions come afterwards.

Example:

Incorrect:

Variable is a named reference to an object.

Correct:

Imagine putting a label on an object.

You can replace the label.

You can move the label.

The object itself continues to exist.

Only after the intuition is established should formal terminology be introduced.

---

## 2.5 No Duplicate Knowledge

Every piece of information must have exactly one canonical location.

Example:

Detailed explanation of lists

→ Programming Handbook

Reflection about finally understanding lists

→ Learning Journal

Personal analogy

→ Mental Models

Progress assessment

→ Checkpoint Report

Documents must reference each other instead of duplicating information.

---

# 3. Components

The Knowledge Base consists of five living documents.

---

## Programming Handbook

Purpose:

Permanent engineering reference.

Contains:

- concepts;
- syntax;
- examples;
- best practices;
- common mistakes;
- relationships between topics.

This document answers:

"What do I know?"

---

## Learning Journal

Purpose:

Chronological learning diary.

Contains:

- discoveries;
- reflections;
- surprising moments;
- difficult topics;
- personal observations.

This document answers:

"What did I learn today?"

---

## Mental Models

Purpose:

Collection of analogies, visualizations and intuitive explanations.

Contains:

- metaphors;
- diagrams;
- comparisons;
- simplified models.

This document answers:

"How should I think about this concept?"

---

## Questions

Purpose:

Knowledge backlog.

Contains:

- unanswered questions;
- partially answered questions;
- future research topics.

Questions are never deleted.

Instead, they move through three states:

Open

↓

Answered

↓

Mastered

---

## Development Log

Purpose:

Track changes in the student's development.

Unlike the Learning Journal, this document focuses on long-term patterns rather than daily learning.

Contains:

- strengths;
- weaknesses;
- changes in learning strategy;
- recurring mistakes;
- methodology improvements.

This document answers:

"How am I changing as an engineer?"

---

# 4. Update Policy

After every completed module the mentor must update the Knowledge Base.

Required updates:

Programming Handbook

✓

Learning Journal

✓

Mental Models

✓

Questions

✓

Development Log

✓

Skipping Knowledge Base updates is considered an incomplete module.

---

# 5. Writing Guidelines

Every document should be written:

- in English;
- using clear technical language;
- without unnecessary academic terminology;
- using Markdown.

Whenever possible, include:

- diagrams;
- tables;
- bullet lists;
- code examples.

Large paragraphs should be avoided.

---

# 6. Relationship with Curriculum

Modules introduce new knowledge.

The Knowledge Base preserves it.

Checkpoint Reports evaluate it.

Together they create a complete learning cycle.

Teaching

↓

Practice

↓

Reflection

↓

Evaluation

↓

Knowledge Base Update

↓

Next Module

---

# 7. Mentor Responsibilities

The mentor is responsible for maintaining the Knowledge Base.

The mentor should never ask the student to manually rewrite or reorganize these documents.

The student may contribute additional notes, but the mentor owns the overall structure and consistency.

---

# 8. Long-Term Vision

The Knowledge Base should continue growing throughout the student's engineering career.

Although the first learning track focuses on Python, the Knowledge Base is language-independent.

Future sections may include:

- Git
- SQL
- Qt
- Docker
- Linux
- Networking
- Software Architecture
- Testing
- AI Engineering

The Knowledge Base is intended to become the student's personal engineering encyclopedia.

---

End of document.