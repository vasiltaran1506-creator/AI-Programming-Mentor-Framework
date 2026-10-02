# APMF Knowledge Base Specification

**Version:** 2.1
**Status:** Active
**Author:** AI Programming Mentor Framework

---

# 1. Purpose

The Knowledge Base (KB) is the long-term memory of the student's learning process.

Unlike modules, which teach concepts, or checkpoint reports, which evaluate progress, the Knowledge Base stores knowledge, observations, questions, and development patterns that should remain useful after individual modules have been completed.

Its primary goals are:

* reduce forgetting;
* improve long-term retention;
* preserve important discoveries;
* maintain a coherent picture of the student's development;
* provide a personal engineering reference tailored to the student's actual experience.

The Knowledge Base is not a textbook.

It is a living collection of documents that evolves throughout the student's learning journey.

---

# 2. Design Principles

## 2.1 Student-Oriented

Every explanation should be written for the student who owns the repository.

The goal is understanding, not completeness.

If a concept can be explained using terminology the student already understands, that explanation should be preferred over unnecessary formal terminology.

---

## 2.2 Incremental Growth

Knowledge is accumulated gradually.

Existing documents should normally be updated incrementally rather than rewritten without reason.

Updates may include:

* adding new concepts;
* refining explanations;
* correcting factual inaccuracies;
* adding examples;
* recording newly discovered relationships;
* moving questions between knowledge states;
* updating the student's current development picture.

Historical material should be preserved when it still accurately represents the student's learning process.

---

## 2.3 Evidence-Based Development Tracking

The Knowledge Base should distinguish between:

* something the student has encountered;
* something the student can explain;
* something the student has implemented successfully;
* something the student can apply independently;
* something that has been demonstrated repeatedly in unfamiliar contexts.

Completing an exercise or understanding a concept once should not automatically be described as mastery.

Statements about the student's abilities should be grounded in observed work, explanations, decisions, or repeated practice.

Avoid inflated professional labels such as "architect", "senior developer", or "professional engineer" unless they are explicitly justified by the evidence and the context requires such a description.

---

## 2.4 Mental Models Before Formal Definitions

Concepts should first be introduced through intuition whenever this helps understanding.

Formal definitions should follow the intuitive model.

Example:

Instead of immediately presenting a formal definition of a variable, begin with an intuitive model such as putting a label on an object.

After the intuition is understood, formal terminology can be introduced.

This approach is especially useful for abstract concepts such as:

* dependency inversion;
* transactions;
* repositories;
* concurrency;
* architectural boundaries.

---

## 2.5 Engineering Focus

The purpose of the Knowledge Base is practical engineering.

Whenever appropriate, a concept should answer one or more of the following questions:

* What is it?
* Why does it exist?
* What problem does it solve?
* When should I use it?
* When should I not use it?
* How does it work?
* What mistakes are common?
* How does it appear in a real project?
* What trade-offs does it introduce?

The Knowledge Base should not accumulate concepts merely because they are considered important in textbooks.

---

## 2.6 No Duplicate Canonical Knowledge

Every substantial piece of information should have one canonical location.

For example:

Detailed explanation of Python lists
→ `Programming Handbook`

Reflection about finally understanding lists
→ `Learning Journal`

Personal analogy for lists
→ `Mental Models`

Open question about list internals
→ `Questions`

Long-term observation that the student repeatedly confuses list and set methods
→ `Development Log`

Other documents should reference or summarize the canonical information rather than unnecessarily reproducing it.

Some controlled overlap is acceptable when it is required for context.

---

# 3. Components

The Knowledge Base consists of five living documents.

---

## 3.1 Programming Handbook

**Purpose:** Permanent engineering reference.

Contains:

* concepts;
* syntax;
* examples;
* best practices;
* common mistakes;
* relationships between topics;
* practical implementation notes.

This document answers:

> "What technical knowledge should I be able to refer back to?"

The Handbook should contain stable technical knowledge rather than personal reflections or progress assessments.

---

## 3.2 Learning Journal

**Purpose:** Chronological record of important learning experiences.

Contains:

* discoveries;
* conceptual breakthroughs;
* difficult topics;
* changes in understanding;
* useful mistakes;
* important personal observations;
* reflections on the learning process.

This document answers:

> "How did my understanding develop?"

Historical entries should normally remain intact.

Corrections are appropriate when an entry contains a factual inconsistency, incorrect date, or materially misleading statement.

The journal should not become a detailed diary of every exercise.

---

## 3.3 Mental Models

**Purpose:** Collection of analogies, visualizations, simplified explanations, and intuitive models.

Contains:

* metaphors;
* comparisons;
* diagrams;
* simplified conceptual models;
* memorable explanations.

This document answers:

> "How should I think about this concept?"

Mental models should support understanding rather than replace technical definitions.

---

## 3.4 Questions

**Purpose:** Knowledge backlog.

Contains:

* unanswered questions;
* partially answered questions;
* questions requiring deeper practice;
* future research topics;
* concepts that the student understands only superficially.

Questions move through knowledge states rather than simply disappearing.

A practical lifecycle is:

```text
Open
  ↓
Answered
  ↓
Practiced
  ↓
Mastered
```

"Mastered" should be used conservatively.

A question should normally remain in `Practiced` or an equivalent intermediate state when the student understands the concept but has not demonstrated reliable independent application across different contexts.

---

## 3.5 Development Log

**Purpose:** Track long-term changes in the student's learning and engineering development.

Unlike the Learning Journal, this document focuses on patterns across multiple modules.

Contains:

* strengths;
* current gaps;
* recurring mistakes;
* changes in learning strategy;
* changes in problem-solving behavior;
* methodology improvements;
* observations about increasing independence.

This document answers:

> "How am I changing as a developer?"

It should describe development patterns rather than assign broad professional status.

---

# 4. Update Policy

The Knowledge Base should be reviewed after every completed module.

However, **review does not mean that every document must be rewritten after every module**.

The mentor should update a document only when the completed module provides information that materially belongs there.

Typical updates include:

| Document             | Typical reason to update                                                |
| -------------------- | ----------------------------------------------------------------------- |
| Programming Handbook | New stable technical knowledge                                          |
| Learning Journal     | New important learning experience                                       |
| Mental Models        | New useful analogy or conceptual model                                  |
| Questions            | New questions, answers, or changes in knowledge state                   |
| Development Log      | Meaningful change in skills, habits, difficulties, or learning strategy |

If a module does not provide meaningful new information for a particular document, that document may remain unchanged.

The purpose of this policy is to keep the Knowledge Base useful rather than turning maintenance into a mechanical documentation task.

---

# 5. Writing Guidelines

Knowledge Base documents should normally be written:

* in English;
* using clear technical language;
* with terminology appropriate to the student's current level;
* using Markdown;
* without unnecessary academic language;
* without overstating the student's competence.

Whenever useful, include:

* diagrams;
* tables;
* bullet lists;
* short code examples;
* concrete project examples.

Large paragraphs should be avoided when a structured format would communicate the idea more clearly.

---

## 5.1 Appropriate Level of Detail

The Knowledge Base should reflect the student's current learning stage.

It should not artificially simplify concepts that the student already understands.

At the same time, it should not imply knowledge that has not yet been demonstrated.

For example:

> "The student understands the basic purpose of dependency inversion and has applied it through repository abstractions."

is preferable to:

> "The student has mastered software architecture."

The first statement describes observable knowledge.

The second makes a much broader claim than the evidence supports.

---

## 5.2 Practical Context

When possible, new concepts should be connected to projects the student has actually worked on.

Examples include:

* QR Warehouse;
* database-backed inventory;
* equipment estimates;
* repository abstractions;
* FastAPI interfaces;
* API testing;
* small experimental projects.

Practical context should clarify the concept, not turn every document into a project diary.

---

# 6. Relationship with the Curriculum

Modules introduce and practice new knowledge.

The Knowledge Base preserves the knowledge that is worth carrying forward.

Checkpoint Reports evaluate progress.

The Development Log tracks longer-term development.

The Learning Journal preserves important learning experiences.

Together they form a learning cycle:

```text
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
```

The Knowledge Base is therefore a **memory system**, not a replacement for the curriculum or checkpoint reports.

---

# 7. Relationship with Projects

Projects are an important source of evidence for the Knowledge Base.

When a project reveals a useful architectural principle, implementation pattern, recurring mistake, or learning breakthrough, the relevant information should be extracted into the appropriate Knowledge Base document.

For example:

```text
Project experience
      ↓
What was learned?
      ↓
┌───────────────┬──────────────────────┐
│ Technical     │ Programming Handbook │
│ Insight       │                      │
├───────────────┼──────────────────────┤
│ Personal      │ Learning Journal     │
│ Breakthrough  │                      │
├───────────────┼──────────────────────┤
│ Mental Model  │ Mental Models        │
├───────────────┼──────────────────────┤
│ Open Question │ Questions            │
├───────────────┼──────────────────────┤
│ Long-term     │ Development Log      │
│ Pattern       │                      │
└───────────────┴──────────────────────┘
```

This prevents the Knowledge Base from becoming dependent on the continued existence of a particular project.

---

# 8. Mentor Responsibilities

The mentor is responsible for maintaining the Knowledge Base structure and consistency.

The mentor should:

* identify which information belongs in the Knowledge Base;
* choose the appropriate canonical document;
* preserve useful historical information;
* correct factual inconsistencies when necessary;
* avoid duplicating information unnecessarily;
* keep descriptions aligned with the
