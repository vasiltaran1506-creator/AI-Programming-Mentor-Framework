# Module 02 — Python Toolbox

Version: 1.0

Stage: 2 — Python Fundamentals

Estimated duration: 8–12 lessons

Prerequisites:
- Module 00 — Computational Thinking
- Module 01 — Programming Foundations

---

# Introduction

Congratulations.

You have reached an important milestone.

During the previous module you learned how to write your first real Python programs.

You learned about variables.

You learned about conditions.

You learned about loops.

You learned about functions.

More importantly, you learned something much deeper.

You learned that programming is not about typing code.

Programming is about describing ideas so precisely that a computer can execute them.

Now another challenge appears.

Many beginners believe that becoming a better programmer means learning more syntax.

This is one of the biggest misconceptions in programming.

Professional developers rarely memorize everything.

Instead, they know something much more valuable.

They know what tools exist.

They know when to use them.

And, perhaps most importantly, they know how to discover new tools when necessary.

This module is about those tools.

---

# Learning Objectives

After completing this module you should be able to:

• understand the difference between functions and methods;

• confidently use the most common Python built-in functions;

• confidently use the most useful string methods;

• confidently use the most useful list methods;

• read simple Python documentation;

• use VS Code as a development tool instead of a text editor;

• choose appropriate built-in tools instead of reinventing existing solutions;

• build your first useful utility program.

---

# Before We Start

Imagine that someone gives you a giant toolbox.

Inside you find:

- hammers;
- screwdrivers;
- pliers;
- saws;
- measuring tape;
- drills;
- wrenches;
- dozens of other tools.

Would you try to memorize every single one on the first day?

Of course not.

Instead you would learn two things.

First:

"What problem does this tool solve?"

Second:

"When should I use it?"

Programming languages are exactly the same.

Python already contains hundreds of useful tools.

You do not need to create everything yourself.

One of the most important skills of an engineer is recognizing when a problem has already been solved.

Good programmers write less code than beginners.

Not because they know less.

Because they know the language better.

---

# Chapter 1

# Python Already Knows More Than You Think

Let's imagine a simple situation.

You have a list of numbers.

```python
scores = [75, 91, 68, 100, 82]
```

You want to know:

- how many numbers are inside;
- the largest number;
- the smallest number;
- the total sum;
- the average.

A beginner often starts thinking like this:

> "I'll write a loop."

Sometimes that's correct.

But experienced developers ask a different question.

> "Does Python already know how to do this?"

Most of the time...

Yes.

Python already knows.

This idea is one of the biggest mindset changes you will experience.

Programming is not:

"I write everything."

Programming is:

"I assemble existing tools into a solution."

---

# Mental Model

Imagine hiring employees.

You could personally do every task yourself.

You could answer emails.

Clean the office.

Prepare reports.

Pay salaries.

Design advertisements.

Repair computers.

Would that be efficient?

No.

Instead, companies hire specialists.

Python does exactly the same.

Instead of making you solve every problem manually,

it already hired specialists.

Some specialists count.

Some compare.

Some sort.

Some convert.

Some search.

Your job is knowing whom to ask.

---

# Toolbox Rule №1

Never ask:

"How do I write this myself?"

First ask:

"Does Python already have a tool for this?"

This single habit will improve your programming more than memorizing dozens of syntax rules.

---

# Chapter 2

# Built-in Functions

A built-in function is a function that already exists inside Python.

You do not need to install anything.

You do not need to write it yourself.

It is always available.

Think of built-in functions as the standard equipment included with every copy of Python.

We will study only the functions that beginners actually use frequently.

Learning every built-in function is unnecessary.

Learning the important ones is essential.

---

# len()

## Purpose

Returns the number of elements inside a collection.

## Mental Model

Imagine a librarian.

You hand them a shelf of books.

You ask:

"How many books are here?"

The librarian counts.

That librarian is `len()`.

---

```python
fruits = ["Apple", "Banana", "Orange"]

print(len(fruits))
```

Output

```text
3
```

---

Strings also have length.

```python
name = "Alexander"

print(len(name))
```

Output

```text
9
```

Because there are nine characters.

---

## Common Beginner Mistake

Many beginners think

```python
len(100)
```

should work.

It doesn't.

Why?

Because the number 100 is not a collection.

It contains no elements to count.

Python therefore raises an error.

---

# Practice

Without running the program,

predict the output.

```python
animals = ["Cat", "Dog", "Fox", "Wolf"]

print(len(animals))
```

Explain why.

---

# sum()

## Purpose

Adds together all numeric values.

---

Instead of writing

```python
total = 0

for value in numbers:
    total += value
```

Python already provides

```python
total = sum(numbers)
```

Much shorter.

Much easier to read.

---

## Mental Model

Imagine an accountant.

You place invoices on the table.

The accountant adds everything together.

That accountant is `sum()`.

---

```python
prices = [120, 450, 80]

print(sum(prices))
```

Output

```text
650
```

---

## Important

`sum()` only works with numbers.

It cannot add text.

---

Incorrect

```python
names = ["Alice", "Bob"]

sum(names)
```

Python raises an error.

---

# Reflection

Notice something interesting.

You already knew how to write a loop.

But using `sum()` is better.

Why?

Not because it is shorter.

Because anyone reading your code immediately understands your intention.

Good code communicates ideas.

Not effort.


# min()

## Purpose

Returns the smallest value.

---

## Mental Model

Imagine that five athletes have finished a race.

You ask the judge:

"Who finished first?"

The judge doesn't care about every participant.

He simply tells you the best result.

That judge is `min()`.

---

```python
temperatures = [18, 24, 15, 27, 21]

print(min(temperatures))
```

Output

```text
15
```

---

Works with text as well.

```python
names = ["Charlie", "Alice", "Bob"]

print(min(names))
```

Output

```text
Alice
```

Why?

Because strings are compared alphabetically.

---

# max()

## Purpose

Returns the largest value.

---

## Mental Model

If `min()` finds the smallest mountain,

then `max()` finds the tallest one.

---

```python
scores = [84, 95, 71, 100, 89]

print(max(scores))
```

Output

```text
100
```

---

# Reflection

Notice that Python already knows how to compare values.

You don't need to write a loop every time.

Instead of asking

> "How can I find the largest number?"

start asking

> "Does Python already know how?"

Usually the answer is yes.

---

# sorted()

## Purpose

Creates a new sorted collection.

---

Suppose you have

```python
numbers = [8, 3, 6, 1, 9]
```

If you call

```python
print(sorted(numbers))
```

Python returns

```text
[1, 3, 6, 8, 9]
```

---

Something very important happened.

Look carefully.

```python
numbers = [8, 3, 6, 1, 9]

new_numbers = sorted(numbers)
```

After this,

```python
numbers
```

is still

```text
[8, 3, 6, 1, 9]
```

while

```python
new_numbers
```

became

```text
[1, 3, 6, 8, 9]
```

The original list was not changed.

Python created another one.

This distinction will become extremely important later.

---

## Mental Model

Imagine making a photocopy of a document.

You sort the copy.

The original document stays untouched.

That is exactly what `sorted()` does.

---

# Practice

Predict the result.

```python
cities = ["Tokyo", "Amsterdam", "Berlin"]

print(sorted(cities))
```

Why?

---

# range()

## Purpose

Produces a sequence of numbers.

---

At first glance this function seems strange.

In reality,

it solves an incredibly common problem.

Suppose you want to repeat something five times.

Instead of writing

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

Python lets you say

```python
for i in range(5):
    print("Hello")
```

Output

```text
Hello
Hello
Hello
Hello
Hello
```

---

But why five?

Let's investigate.

```python
for i in range(5):
    print(i)
```

Output

```text
0
1
2
3
4
```

---

Notice something surprising.

It stops before reaching five.

This often confuses beginners.

---

## Mental Model

Imagine climbing stairs.

You start on stair zero.

To reach stair five,

you step on

0

1

2

3

4

The fifth step is where you stop.

Python thinks in exactly the same way.

---

## Three Forms of range()

### One argument

```python
range(5)
```

Produces

```text
0 1 2 3 4
```

---

### Two arguments

```python
range(3, 8)
```

Produces

```text
3 4 5 6 7
```

---

### Three arguments

```python
range(2, 12, 2)
```

Produces

```text
2 4 6 8 10
```

The third value is called the step.

---

# Toolbox Rule №2

Whenever you need to repeat an action a fixed number of times,

think about `range()`.

---

# enumerate()

This function is one of the first things that separates beginners from experienced Python programmers.

To understand why it exists,

let's first look at a common beginner solution.

```python
fruits = ["Apple", "Orange", "Banana"]

for i in range(len(fruits)):
    print(i, fruits[i])
```

This works.

But it is not the best solution.

Python already has a tool made specifically for this task.

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output

```text
0 Apple

1 Orange

2 Banana
```

Cleaner.

More readable.

Less chance of mistakes.

---

## Mental Model

Imagine a teacher reading the attendance list.

Instead of saying

"Student"

she says

"Student number 12."

Every student automatically receives both

their number

and

their name.

That is exactly what `enumerate()` does.

---

# zip()

This function combines multiple collections.

Suppose you have

```python
students = ["Alice", "Bob", "Charlie"]

scores = [95, 88, 100]
```

These lists are related.

The first student has the first score.

The second student has the second score.

Instead of using indexes,

Python lets you write

```python
for student, score in zip(students, scores):
    print(student, score)
```

Output

```text
Alice 95

Bob 88

Charlie 100
```

---

## Mental Model

Imagine a zipper on a jacket.

One side contains names.

The other contains scores.

The zipper connects matching pairs.

That is why the function is called `zip()`.

---

# Chapter Summary

Today you met several specialists already working inside Python.

They each solve one specific problem.

| Function | Responsibility |
|------------|----------------|
| len() | Count elements |
| sum() | Add numbers |
| min() | Find the smallest value |
| max() | Find the largest value |
| sorted() | Create a sorted copy |
| range() | Produce a sequence of numbers |
| enumerate() | Provide index and value together |
| zip() | Combine multiple collections |

Notice something important.

None of these functions introduced a new programming concept.

They introduced better tools.

This is how professional developers become productive.

Not by writing more code.

But by recognizing that someone has already written the right code for them.

---

# Knowledge Check

Without writing any code, answer the following questions.

## Question 1

You need to know how many images are inside a dataset folder.

Which built-in function immediately comes to mind?

Explain why.

---

## Question 2

You have collected 200 quality scores.

You need the highest one.

Which tool would you choose?

Why is it better than writing your own loop?

---

## Question 3

You have two lists.

One contains image filenames.

The other contains ratings.

Which built-in function naturally combines them?

Why is it safer than using indexes manually?

---

Do not continue to the next chapter until you can confidently answer every question without looking back.

# Chapter 3

# Functions vs Methods

This chapter is one of the most important in the entire beginner course.

Many new programmers become confused here.

Not because the topic is difficult.

Because nobody explains *why* Python has two different ways of calling code.

For example,

sometimes you write

```python
len(text)
```

but sometimes you write

```python
text.lower()
```

Why?

Why isn't it

```python
lower(text)
```

or

```python
text.len()
```

Understanding the answer means understanding one of the foundations of Python.

---

# Mental Model

Imagine that you own a smartphone.

Some things happen **to** the phone.

Some things happen **using** the phone.

These are different ideas.

For example

The phone can

- turn on;
- turn off;
- change its brightness;
- take a picture.

Those are actions performed by the phone itself.

You naturally think

> "Phone, take a picture."

not

> "Take a picture using this phone."

Now imagine another situation.

You place the phone on a scale.

The scale tells you its weight.

The scale isn't part of the phone.

It is an external tool.

The phone does not weigh itself.

Someone else measures it.

Python makes exactly the same distinction.

---

# External Tools

Some operations make sense for many different kinds of data.

For example

How many elements are inside?

That question can be asked about

- text;
- lists;
- tuples;
- dictionaries;
- many other collections.

Since counting is useful everywhere,

Python created one universal tool.

```python
len(...)
```

Notice that the object does not count itself.

Python counts it.

---

Another example

```python
type(...)
```

A string does not determine its own type.

Python does.

---

# Object Abilities

Now imagine something different.

Suppose you have text.

Text knows how to become lowercase.

Text knows how to become uppercase.

Text knows how to replace characters.

Text knows how to split itself.

Those actions belong to the text itself.

Therefore we write

```python
text.lower()

text.upper()

text.replace()

text.split()
```

The action belongs to the object.

---

# The Restaurant Analogy

Imagine entering a restaurant.

Some services belong to the restaurant.

For example

You ask

> Bring me today's menu.

The restaurant already has one.

Now imagine you ask

> Count how many customers are inside.

The restaurant usually doesn't do that itself.

A manager counts them.

Notice the difference.

One action belongs naturally to the restaurant.

The other belongs to an outside observer.

Python works exactly the same way.

---

# Rule of Thumb

Ask yourself one question.

> "Does this action belong naturally to the object?"

If yes,

it is probably a method.

If not,

it is probably a function.

---

# Examples

Text becoming lowercase

belongs to text.

```python
text.lower()
```

---

A list sorting itself

belongs to the list.

```python
numbers.sort()
```

---

Finding the largest number

does not belong to any particular list.

Python simply examines values.

Therefore

```python
max(numbers)
```

---

Counting elements

does not belong to the list.

Python counts.

Therefore

```python
len(numbers)
```

---

# Toolbox Rule №3

Methods describe

"What this object knows how to do."

Functions describe

"What Python knows how to do."

---

# Objects

We have already used objects without realizing it.

Consider this variable.

```python
name = "Alexander"
```

Many beginners think

"name contains text."

This is only partially true.

A more accurate statement is

"name refers to a string object."

That object already contains many useful abilities.

For example

```python
name.upper()

name.lower()

name.replace()

name.strip()

name.split()
```

The string already knows how to perform these operations.

You are simply asking it to do so.

---

# Chapter 4

# String Methods

Strings are one of the most frequently used data types in programming.

Almost every program works with text.

Names.

Paths.

Messages.

Commands.

File extensions.

Dates.

User input.

Configuration files.

Learning string methods is therefore one of the highest-return investments you can make.

---

# lower()

Converts all characters to lowercase.

```python
name = "Alexander"

print(name.lower())
```

Output

```text
alexander
```

---

Useful for comparisons.

Instead of

```python
if answer == "yes":
```

you can safely write

```python
if answer.lower() == "yes":
```

Now

YES

Yes

yEs

all become

```text
yes
```

---

# upper()

Converts all letters to uppercase.

```python
code = "abc123"

print(code.upper())
```

Output

```text
ABC123
```

---

# strip()

This method quietly solves one of the most common beginner problems.

Suppose the user types

```text
      apple
```

or

```text
apple
```

with accidental spaces.

Those spaces are part of the string.

They may break comparisons.

```python
answer = input()

if answer == "yes":
```

The comparison fails if the user typed

```text
 yes
```

Notice the leading space.

Instead

```python
answer = input().strip()
```

Now unnecessary spaces disappear.

---

## Mental Model

Imagine cleaning dirty shoes before entering your house.

The shoes remain the same.

Only the dirt around them disappears.

That is exactly what `strip()` does.

---

# replace()

One of the most useful methods in everyday programming.

```python
text = "cat"

print(text.replace("c", "b"))
```

Output

```text
bat
```

---

Another example.

Suppose users enter decimal numbers using commas.

```text
15,75
```

Python expects

```text
15.75
```

You already solved this problem in Module 01.

```python
number = number.replace(",", ".")
```

Now the value can be converted into a float.

---

# split()

Suppose you have

```python
text = "Apple,Banana,Orange"
```

This is still one string.

Sometimes you want three separate values.

```python
fruits = text.split(",")
```

Result

```python
["Apple", "Banana", "Orange"]
```

---

## Mental Model

Imagine cutting a loaf of bread.

Originally

one loaf.

After cutting

many slices.

`split()` cuts one string into many smaller strings.

---

# join()

This method performs the opposite operation.

Suppose you have

```python
words = ["Python", "is", "fun"]
```

You want one sentence.

```python
sentence = " ".join(words)
```

Result

```text
Python is fun
```

---

## Mental Model

If `split()` is scissors,

then `join()` is glue.

One separates.

The other combines.

---

# startswith()

Sometimes you only care about the beginning.

```python
filename = "image_0001.png"

print(filename.startswith("image"))
```

Output

```text
True
```

Very useful for checking filenames.

---

# endswith()

Likewise,

```python
filename.endswith(".png")
```

checks whether the filename ends with

```text
.png
```

This becomes extremely useful when processing datasets.

---

# Reflection

Notice something interesting.

Every method we learned today answers a question beginning with

"What can this string do?"

A string can

become lowercase.

Become uppercase.

Split itself.

Join with others.

Replace characters.

Remove surrounding spaces.

Check how it starts.

Check how it ends.

This way of thinking will become even more important when we later study lists,

dictionaries,

Path objects,

and eventually classes.