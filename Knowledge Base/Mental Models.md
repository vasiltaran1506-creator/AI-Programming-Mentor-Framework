# Mental Models

Version: 1.0

Status: Active

Last Updated: After Module 01

---

# Purpose

Programming is easier to learn when abstract concepts are connected to intuitive mental images.

This document collects those images.

A mental model is **not** a formal definition.

Instead, it is a simplified way of thinking that helps build intuition.

Some models may be technically incomplete.

That is acceptable.

Their purpose is understanding, not mathematical precision.

New mental models should be added whenever a concept becomes significantly easier to understand through an analogy.

---

# Variable

## Mental Model

A variable is a **label**, not a box.

Imagine a room full of objects.

You take a sticker and write:

```
score
```

Then you stick it onto an object.

```
score
 │
 ▼
10
```

Later you remove the sticker and place it on another object.

```
score
 │
 ▼
25
```

The sticker moved.

The object did not.

Always think about moving labels—not moving values.

---

# Assignment (=)

Assignment is **not equality**.

It is an instruction.

Think of it as:

> "Take the value on the right and attach the name on the left."

```
health = 100
```

means

```
health

↓

100
```

not

```
health equals 100 forever
```

---

# Data Types

Imagine different kinds of containers.

```
Text

↓

Words

```

```
Integer

↓

Whole numbers

```

```
Float

↓

Numbers with decimals

```

Every container has its own rules.

You cannot pour soup into an envelope.

Likewise, you cannot add a string to an integer.

---

# Input

Input is a conversation.

The computer stops speaking.

Now it waits.

Only after the user answers does the program continue.

```
Program

↓

Question

↓

Waiting...

↓

Answer

↓

Continue
```

---

# print()

Imagine a loudspeaker.

Whatever reaches the loudspeaker becomes visible to the user.

Nothing returns back into the program.

```
Program

↓

print()

↓

Screen
```

---

# return

Imagine a factory.

Raw materials enter.

Work happens inside.

A finished product leaves through the exit door.

```
Input

↓

Function

↓

return

↓

Result
```

The returned value continues travelling through the rest of the program.

---

# Function

A function is a machine.

You do not need to know how the gears work.

You only care about:

Input

↓

Machine

↓

Output

Good functions hide unnecessary complexity.

---

# Parameters and Arguments

Imagine writing instructions for assembling furniture.

The manual says:

```
Insert screw here.
```

It does not know which exact screw you will use.

```
screw

↓

Parameter
```

When someone actually builds the furniture:

```
Screw #A52

↓

Argument
```

Parameters are placeholders.

Arguments are real values.

---

# List

Imagine a bookshelf.

Every shelf position has a number.

```
0

1

2

3

4
```

Books occupy positions.

You access a book by its position.

Python starts counting from zero.

---

# Index

Think of apartment numbers.

The building contains many apartments.

You must specify which one you want.

```
students[3]
```

means

"The fourth apartment."

---

# Loop

Imagine walking through every room in a house.

```
Room 1

↓

Room 2

↓

Room 3

↓

Room 4
```

A loop simply repeats the same action.

The destination changes.

The action stays the same.

---

# while

Imagine waiting at a train station.

Every minute you ask:

```
Has the train arrived?
```

No?

Wait again.

Ask again.

Repeat.

When the answer becomes

```
Yes
```

you leave.

That is exactly how a while loop behaves.

---

# for

Imagine reading a guest list.

```
Alice

Bob

Charlie

David
```

You go through every name exactly once.

Nothing more.

Nothing less.

---

# Program State

Imagine freezing the program like a movie.

Everything that exists at that exact moment—

variables,

lists,

objects,

values—

forms the current state.

Programming is simply changing the state over time.

---

# Algorithm

An algorithm is a recipe.

The ingredients are the input.

The cooking process is the algorithm.

The finished meal is the output.

Different recipes can produce the same meal.

Some are simply better.

---

# Problem Decomposition

Imagine assembling a house.

Nobody starts with:

"Build house."

Instead:

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

Furniture

Large problems become easy once divided into smaller ones.

---

# Separation of Concerns

Imagine a restaurant.

The waiter does not cook.

The chef does not wash dishes.

The cashier does not prepare food.

Everyone has one responsibility.

Functions should work exactly the same way.

---

# Bug

A bug is not failure.

It is evidence that your mental model and the computer's model disagree.

The goal is not to eliminate bugs.

The goal is to discover where those models diverge.

---

# Debugging

Imagine being a detective.

The computer never lies.

Every incorrect result has a cause.

Your task is not guessing.

Your task is collecting evidence until only one explanation remains.

---

# Refactoring

Imagine cleaning a workshop.

No new tools appear.

Nothing new is built.

Everything simply becomes easier to find,

simpler to use,

and safer.

Refactoring does exactly the same for code.

---

# Good Code

Imagine explaining your solution to another engineer six months from now.

If Future You understands it immediately,

the code is good.

If Future You needs ten minutes,

the code needs improvement.

---

# AI Assistant

Think of AI as an experienced colleague.

The colleague can:

- explain;
- suggest;
- review;
- accelerate.

The colleague should not replace your thinking.

You remain the engineer responsible for the final solution.

---

# The Most Important Mental Model

Programming is **not writing code.**

Programming is the process of transforming an idea into an exact sequence of instructions that another entity can execute without ambiguity.

Code is only one possible language used to express those instructions.

Never confuse programming with typing syntax.

Understanding always comes first.

---

End of document.