# Student Principles

**Version:** 1.1

**Status:** Active

**Owner:** Student

**Maintained by:** Student and AI Methodologist

---

# Purpose

This document defines the principles that guide my development as a software engineer.

Programming languages will change.

Frameworks will change.

AI models will change.

My engineering principles should remain stable.

This constitution is not a set of rules imposed from outside.

It is a commitment I make to myself.

Whenever I feel lost, frustrated, uncertain, or tempted to choose convenience over understanding, I should return to this document.

---

# My Goal

I do not want to become someone who merely writes code.

I want to become a developer who can understand problems, design solutions, build useful software, and gradually take responsibility for the systems I create.

Code is one of my tools.

Thinking is my primary skill.

My goal is not to know everything.

My goal is to become increasingly capable of finding out what I do not know and using that knowledge effectively.

---

# Core Principles

## 1. Understanding Comes Before Memorization

I do not aim to memorize syntax.

I aim to understand ideas.

If I understand the concept, syntax can be looked up.

I should distinguish between:

* knowing how something works;
* knowing how to use it;
* remembering its exact syntax.

Forgetting syntax is normal.

Not understanding what the code is supposed to do is a more important problem.

---

## 2. Thinking Comes Before Coding

I will not immediately begin writing code.

Before touching the keyboard, I will ask:

* What problem am I solving?
* What information do I have?
* What result do I expect?
* What rules must remain true?
* What edge cases should I consider?
* What is the simplest reasonable solution?

Only after I understand the problem sufficiently will I begin implementing it.

I do not need a perfect design before writing any code.

The goal is to think enough to avoid solving the wrong problem.

---

## 3. Curiosity Is More Valuable Than Speed

Learning quickly is not my only goal.

Learning deeply enough to use knowledge independently is more important.

If I do not understand something, I will slow down instead of pretending I understand.

Questions are progress.

Not weakness.

At the same time, I should not demand complete understanding of every detail before moving forward.

Some concepts become clear only after practical experience.

---

## 4. Mistakes Are Data

An error message is not a failure.

It is information.

Every bug teaches me something about how the computer, language, library, or my own assumptions actually work.

Instead of asking only:

> "Why doesn't this work?"

I will also ask:

> "What assumption of mine turned out to be incorrect?"

I should distinguish between:

* a syntax mistake;
* an implementation mistake;
* a misunderstanding of a concept;
* an incorrect architectural decision;
* insufficient information.

Different problems require different responses.

---

## 5. Readability Is a Feature

Code is read far more often than it is written.

Future Me is also another programmer.

I write code that Future Me can understand.

If I need to choose between cleverness and clarity,

I choose clarity.

Names, structure, and predictable behavior are part of software quality.

---

## 6. Simplicity Wins

I prefer the simplest solution that correctly solves the problem.

Complexity must justify its existence.

I should not add:

* abstractions;
* design patterns;
* layers;
* frameworks;
* asynchronous code;
* configuration systems;

merely because they are available.

A more sophisticated design is not automatically a better design.

The right amount of architecture depends on the problem, requirements, and expected change.

---

## 7. Refactoring Is Improvement

Rewriting code is not admitting failure.

It is part of engineering.

Every version of my code teaches me something that the previous version could not.

I should be willing to improve code when:

* its responsibilities have become unclear;
* requirements have changed;
* duplication creates problems;
* tests expose a design weakness;
* a simpler structure has become apparent.

At the same time, refactoring should have a reason.

I do not need to constantly rewrite working code merely to make it look different.

---

## 8. One Responsibility at a Time

Every function, module, and class should have a clear purpose appropriate to its role.

"One responsibility" does not necessarily mean "one line of work."

A Use Case may legitimately coordinate several operations.

A repository may legitimately contain several persistence methods.

A class may legitimately contain several related behaviors.

The important question is whether the responsibilities belong together and can be explained coherently.

If something is difficult to explain because it is doing unrelated things,

it probably needs to be reconsidered.

---

## 9. I Learn by Building

Theory matters.

Practice matters too.

Whenever possible, I connect new knowledge to real projects.

Every project becomes part of my education.

But building is not enough by itself.

After implementing something, I should ask:

* Why does this design work?
* What would break if the requirements changed?
* What could be simpler?
* What did I misunderstand?
* What did I learn that can be reused elsewhere?

The goal is not merely to finish projects.

The goal is to become better through them.

---

## 10. AI Is My Mentor, Not My Brain

AI is one of the most powerful tools available to me.

I use it to:

* learn;
* explore;
* ask questions;
* review;
* debug;
* compare approaches;
* accelerate development;
* discover things I would otherwise overlook.

I do not outsource my thinking.

When the purpose is learning, I should implement important parts of the solution myself whenever reasonably possible.

I should be able to explain code before treating it as knowledge.

If AI writes an implementation for me, copying it is not the same as learning it.

I should use AI to increase my capabilities, not to replace them.

The final responsibility for my technical decisions remains mine.

---

## 11. I Accept Not Knowing

No developer knows everything.

I do not need to know everything before building useful software.

When I encounter an unfamiliar topic, I treat it as something to investigate.

A useful response to not knowing is:

1. identify exactly what I do not understand;
2. reduce the question to a manageable size;
3. learn enough to continue;
4. practice it;
5. return to the deeper details when they become relevant.

Not knowing something is normal.

Pretending to know something is much more dangerous.

---

## 12. Every Module Is a Step Forward

Progress is not measured by perfection.

It is measured by understanding something today that I did not understand before.

Some topics will become clear quickly.

Others will require several encounters.

A temporary difficulty does not erase previous progress.

Likewise, completing a module does not mean that every concept in it has been mastered.

The goal is cumulative development.

Small improvements accumulate.

---

## 13. Independence Is the Direction

The purpose of learning is not to remain dependent on a mentor, course, or AI.

Whenever possible, I should gradually move through this cycle:

```text
Understand with help
        ↓
Practice with guidance
        ↓
Implement with less guidance
        ↓
Solve familiar problems independently
        ↓
Solve unfamiliar problems independently
        ↓
Know when and how to ask for help
```

Asking for help is not the opposite of independence.

Knowing what help I need, evaluating it critically, and continuing afterward is part of independence.

---

## 14. Architecture Must Serve the Problem

I am interested in software architecture, but architecture is not a competition to see who can create the most layers.

I should ask:

* What problem does this abstraction solve?
* What change does it protect against?
* What dependency does it isolate?
* Does the added complexity pay for itself?

I should prefer architecture that makes real changes safer and the system easier to understand.

A pattern is a tool.

A layer is a tool.

An abstraction is a tool.

None of them is automatically valuable simply because it is considered "professional."

---

## 15. Real Problems Matter

Whenever possible, I should connect programming to real problems.

Real requirements contain ambiguity, constraints, existing systems, imperfect data, human behavior, and changing priorities.

These are not distractions from programming.

They are part of software development.

My projects should therefore teach me not only how to write code, but also how to understand the problem that the code is supposed to solve.

---

# My Responsibilities

As a student I commit to:

* asking questions;
* writing important code myself whenever possible;
* reading and explaining my own code;
* reviewing mistakes honestly;
* testing what I build;
* learning to use documentation and other technical sources;
* questioning unnecessary complexity;
* keeping my Knowledge Base useful and accurate;
* connecting theory to practical projects;
* gradually increasing my independence;
* treating programming as a craft rather than simply a school subject.

---

# Definition of Success

Success is not simply finishing a curriculum.

Success is gradually reaching the point where I can independently:

* understand a problem;
* identify important constraints;
* decompose the problem;
* design a reasonable solution;
* evaluate alternatives;
* implement the solution;
* test and debug it;
* recognize what I do not know;
* find the information necessary to continue;
* improve the solution when requirements change.

I do not need to achieve all of this perfectly or all at once.

The important direction is increasing independence.

When I can reliably do these things, the particular language or framework I am using becomes much less important.

---

# Long-Term Vision

My goal is not simply to become a Python developer.

I want to become a developer capable of learning new languages, frameworks, tools, and technologies when the problem requires them.

Python is my current primary tool.

Backend development is my current direction.

Software engineering is the broader discipline I am learning.

Programming is only the beginning.

Engineering thinking is the destination.

---

# Personal Motto

> **Understanding creates independence.**

Everything else follows.

---

End of document.
