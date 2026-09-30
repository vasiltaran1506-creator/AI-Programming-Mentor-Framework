# Module 08 --- Database Fundamentals & SQL

**Framework:** AI Programming Mentor Framework (APMF)\
**Stage:** 2 --- Python Application Foundations / Data Persistence\
**Prerequisites:** Modules 00--07\
**Primary language:** Python 3\
**Teaching language:** English\
**Estimated difficulty:** Intermediate+\
**Estimated workload:** \~20--24 hours\
**Primary project:** QR Warehouse database layer\
**Module type:** Guided database fundamentals + practical SQL +
architectural integration

------------------------------------------------------------------------

# Module Overview

Module 07 established an important architectural boundary:

> **Business logic should not have to know how data is physically
> stored.**

You experienced this directly when QR Warehouse moved from JSON storage
to SQLite without rewriting the core business logic.

That was useful architecturally --- but it also exposed a major
knowledge gap. You could use SQLite and reproduce enough SQL to make the
repository work, but you could not yet confidently reason about
relational databases, schema design, joins, constraints, transactions,
indexes, and migrations.

Module 08 removes that black box.

The goal is **not** to make you a database administrator. The goal is to
make you capable of reasoning about persistent state as an engineer:
model it, query it, constrain it, change it safely, and integrate it
with Python without destroying the boundaries established in Module 07.

------------------------------------------------------------------------

# Central Principle

> **A database is not merely a place where data is stored. It is a
> system for representing, constraining, querying, and changing
> structured persistent state.**

The conceptual transition is:

``` text
"I save objects somewhere"
        ↓
"I model persistent facts and their relationships"
        ↓
"I define the rules under which that state may exist and change"
```

------------------------------------------------------------------------

# What This Module Is NOT

This module does not attempt to master:

-   database administration;
-   replication or sharding;
-   distributed databases;
-   advanced query optimization;
-   PostgreSQL administration;
-   NoSQL databases in depth;
-   distributed transactions;
-   advanced isolation anomalies;
-   ORM mastery;
-   cloud database infrastructure.

These become easier later because the relational foundation will already
be in place.

------------------------------------------------------------------------

# Learning Goals

By the end of Module 08, the student should be able to:

1.  explain what a database is;
2.  explain what a relational database is;
3.  distinguish tables, rows, columns, and values;
4.  explain primary keys and foreign keys;
5.  model one-to-one, one-to-many, and many-to-many relationships;
6.  write practical `SELECT`, `INSERT`, `UPDATE`, and `DELETE` queries;
7.  filter, sort, and limit results;
8.  use aggregates such as `COUNT`, `SUM`, and `AVG`;
9.  use `GROUP BY` and `HAVING`;
10. write ordinary `JOIN` queries;
11. understand `NULL`;
12. use `NOT NULL`, `UNIQUE`, `CHECK`, `PRIMARY KEY`, and `FOREIGN KEY`
    constraints;
13. use parameterized SQL from Python;
14. explain SQL injection;
15. explain transactions, atomicity, `commit()`, and `rollback()`;
16. explain indexes and their trade-offs;
17. design a reasonable small relational schema;
18. understand practical normalization;
19. explain what a migration is;
20. compare SQLite and PostgreSQL conceptually;
21. integrate SQLite cleanly behind a repository boundary;
22. write repository integration tests;
23. distinguish business tests from persistence tests;
24. recognize when historical data must be stored as a snapshot;
25. reason about database design before writing tables.

The strongest completion criterion is not "I know SQL syntax." It is:

> **"I can identify persistent state and its relationships, design a
> reasonable schema, express useful questions in SQL, and explain how
> the application should interact with the database safely."**

------------------------------------------------------------------------

# Methodological Context

## From Module 03

You already know JSON, serialization, validation, exceptions, data
boundaries, and filesystem persistence.

Now ask:

> What changes when persistence is handled by a database instead of a
> file?

## From Module 04

You already know contracts, explicit dependencies, business logic vs
I/O, dependency injection, testability, and refactoring.

The database remains an infrastructure concern.

## From Module 05

You already know objects, entities, state, behavior, and invariants.

Now learn that Python objects do not necessarily map one-to-one to
tables.

## From Module 06

You already know abstraction and pragmatic design.

Do not create abstractions merely because a database exists.

## From Module 07

You already know Domain, Application, Infrastructure, Repository, Use
Case, Dependency Inversion, Dependency Injection, and Composition Root.

A useful model is:

``` text
Presentation
      ↓
Application
      ↓
Domain
      ↑
Repository contract
      ↑
Infrastructure
      ↓
SQLite / PostgreSQL
```

The database belongs outside the domain --- but you will now understand
what happens inside that boundary.

------------------------------------------------------------------------

# Part I --- The Relational Model

## 1. Persistent State

A running Python program has in-memory state. When the process ends,
that state normally disappears.

Persistent storage lets state survive.

A database goes further than a plain file: it provides mechanisms for
organization, relationships, querying, integrity, transactions, and
efficient access.

## 2. Tables, Rows, Columns, Values

A simplified table:

``` text
equipment
+----+------------+--------------+-----------+
| id | sku        | name         | available |
+----+------------+--------------+-----------+
| 1  | LIGHT-001  | SkyPanel     | 3         |
| 2  | LIGHT-002  | Aputure 600D | 5         |
+----+------------+--------------+-----------+
```

A **table** is a collection of records of one modeled kind.

A **row** is one record.

A **column** describes one attribute.

A **value** is the actual data in one cell.

Do not confuse these levels.

------------------------------------------------------------------------

# Part II --- Identity and Relationships

## 3. Primary Keys

Names are often not unique. A primary key provides stable row identity.

``` sql
CREATE TABLE equipment (
    id INTEGER PRIMARY KEY,
    sku TEXT NOT NULL,
    name TEXT NOT NULL,
    available INTEGER NOT NULL
);
```

A practical system may use both:

``` text
id  → internal identity
sku → business identifier
```

For example:

``` sql
sku TEXT NOT NULL UNIQUE
```

This says that the business identifier must also be unique.

## 4. Foreign Keys

Suppose an estimate contains multiple items:

``` text
estimate
--------
id
client_name

estimate_item
-------------
id
estimate_id
equipment_id
quantity
```

`estimate_id` and `equipment_id` can be foreign keys.

A foreign key expresses a relationship between records.

``` sql
FOREIGN KEY (estimate_id) REFERENCES estimate(id)
```

## 5. Relationship Types

### One-to-one

``` text
User → UserProfile
```

### One-to-many

``` text
Estimate
  ├── Item
  ├── Item
  └── Item
```

### Many-to-many

Usually represented through a junction table:

``` text
order
product
order_product
```

The junction table represents the relationship itself.

------------------------------------------------------------------------

# Part III --- Schema Design and Normalization

## 6. Why Split Data Into Tables?

A design such as:

``` text
estimate_id | item1 | qty1 | item2 | qty2 | item3 | ...
```

does not scale naturally.

Repeated entities belong naturally in rows:

``` text
estimate
--------
id
client_id

estimate_item
-------------
id
estimate_id
equipment_id
quantity
```

A practical rule:

> **Rows represent repeated entities; columns represent attributes of
> one entity.**

## 7. Normalization

Normalization reduces unnecessary duplication and update anomalies.

Instead of repeatedly storing:

``` text
equipment_name
equipment_price
```

inside every historical item row, a design can reference an equipment
record.

However, normalization does not mean "split everything into as many
tables as possible."

The goal is to represent facts in appropriate places.

## 8. Historical Snapshots

Suppose equipment currently costs €100/day but an old estimate was
agreed at €80/day.

If `estimate_item` only refers to the current equipment price, the
historical estimate can become incorrect.

Therefore it may be appropriate to store:

``` text
estimate_item
-------------
equipment_id
quantity
price_per_day_at_estimate_time
```

This is a domain decision expressed through database design.

> **Schema design is part of domain modeling.**

------------------------------------------------------------------------

# Part IV --- SQL Fundamentals

## 9. SELECT

``` sql
SELECT *
FROM equipment;
```

Specific columns:

``` sql
SELECT sku, name, available
FROM equipment;
```

Prefer selecting what the application actually needs rather than using
`*` everywhere.

## 10. WHERE

``` sql
SELECT sku, name
FROM equipment
WHERE available > 0;
```

Conditions can be combined:

``` sql
WHERE available > 0
  AND price_per_day < 10000
```

## 11. ORDER BY and LIMIT

``` sql
SELECT *
FROM equipment
ORDER BY name ASC
LIMIT 10;
```

Descending:

``` sql
ORDER BY price_per_day DESC
```

## 12. INSERT

``` sql
INSERT INTO equipment (sku, name, available)
VALUES ('LIGHT-00001', 'SkyPanel', 3);
```

Use explicit column names.

## 13. UPDATE

``` sql
UPDATE equipment
SET available = 2
WHERE sku = 'LIGHT-00001';
```

The `WHERE` clause is critical.

Never casually execute:

``` sql
UPDATE equipment
SET available = 2;
```

unless changing every row is explicitly intended.

## 14. DELETE

``` sql
DELETE FROM equipment
WHERE sku = 'LIGHT-00001';
```

Again, know exactly which rows are selected.

## 15. NULL

`NULL` means absence of a value. It is not the same as `0`, `False`, or
an empty string.

Use:

``` sql
IS NULL
IS NOT NULL
```

not:

``` sql
= NULL
```

------------------------------------------------------------------------

# Part V --- JOINs and Aggregation

## 16. JOIN

Suppose:

``` text
estimate_item
-------------
equipment_id
quantity
```

references:

``` text
equipment
---------
id
name
price
```

You can combine them:

``` sql
SELECT
    estimate_item.quantity,
    equipment.name,
    equipment.price
FROM estimate_item
JOIN equipment
    ON estimate_item.equipment_id = equipment.id;
```

The important question is not "Which JOIN syntax do I memorize?"

It is:

> Which records are related, and what information do I need from each
> side?

## 17. INNER JOIN vs LEFT JOIN

A normal `JOIN` is usually an `INNER JOIN`: only matching records are
returned.

A `LEFT JOIN` keeps every row from the left table and attaches matching
rows from the right table when available.

Mental model:

``` text
INNER JOIN → matching intersection
LEFT JOIN  → all left records + matches when available
```

## 18. Aggregate Functions

``` sql
SELECT COUNT(*) FROM equipment;
```

``` sql
SELECT SUM(quantity) FROM estimate_item;
```

``` sql
SELECT AVG(price_per_day) FROM equipment;
```

Also:

``` sql
MIN(...)
MAX(...)
```

## 19. GROUP BY

``` sql
SELECT category, COUNT(*)
FROM equipment
GROUP BY category;
```

This creates one result per category.

## 20. HAVING

`WHERE` filters rows; `HAVING` filters groups.

``` sql
SELECT category, COUNT(*)
FROM equipment
GROUP BY category
HAVING COUNT(*) > 10;
```

Useful conceptual order:

``` text
FROM
 ↓
WHERE
 ↓
GROUP BY
 ↓
HAVING
 ↓
SELECT
 ↓
ORDER BY
```

------------------------------------------------------------------------

# Part VI --- Python and SQL Safely

## 21. Parameterized Queries

Never build SQL by interpolating untrusted input.

Bad:

``` python
sku = input("SKU: ")
query = f"SELECT * FROM equipment WHERE sku = '{sku}'"
```

Better:

``` python
query = """
SELECT *
FROM equipment
WHERE sku = ?
"""

cursor.execute(query, (sku,))
```

This separates SQL structure from data.

## 22. SQL Injection

SQL injection occurs when external data is allowed to alter the SQL
command itself.

Parameterized queries create a boundary:

``` text
SQL structure + parameter value
```

The driver treats the parameter as data rather than SQL syntax.

This is a fundamental security practice.

## 23. sqlite3

Python includes SQLite support:

``` python
import sqlite3

connection = sqlite3.connect("warehouse.db")
cursor = connection.cursor()
```

Query:

``` python
cursor.execute("SELECT sku, name FROM equipment")
```

Read one row:

``` python
row = cursor.fetchone()
```

Read all rows:

``` python
rows = cursor.fetchall()
```

Remember:

``` text
fetchone() → one row or None
fetchall() → collection of rows
```

A row is commonly represented as a tuple:

``` python
(1, "LIGHT-00001", "SkyPanel", 3)
```

------------------------------------------------------------------------

# Part VII --- Constraints and Integrity

A database can enforce rules.

## NOT NULL

``` sql
name TEXT NOT NULL
```

## UNIQUE

``` sql
sku TEXT UNIQUE
```

## CHECK

``` sql
available INTEGER CHECK (available >= 0)
```

## PRIMARY KEY

Provides row identity.

## FOREIGN KEY

Protects relationships between tables.

Application validation and database constraints serve different
purposes.

Python validation can provide friendly messages and business-specific
checks. Database constraints protect persistent integrity even if data
reaches the database through another path.

A useful principle is:

> **Validate where useful; enforce critical persistence invariants at
> the persistence boundary too.**

------------------------------------------------------------------------

# Part VIII --- Transactions

## 24. What Is a Transaction?

A transaction groups related database operations into one logical unit.

For example:

``` text
create estimate
add estimate items
reserve inventory
```

If reservation fails after the first two operations, you may not want a
half-created business operation.

Conceptually:

``` text
BEGIN
  A
  B
  C
COMMIT
```

or, after failure:

``` text
BEGIN
  A
  B
  C ← failure
ROLLBACK
```

## 25. Atomicity

Atomicity means the logical transaction is treated as all-or-nothing.

A classic example is a bank transfer:

``` text
remove €100 from A
add €100 to B
```

You do not want only the first change to survive.

The four ACID concepts should be understood at a practical level:

``` text
Atomicity  → all or nothing
Consistency → valid state remains valid
Isolation   → concurrent work is appropriately separated
Durability  → committed state survives appropriate failures
```

## 26. commit() and rollback()

``` python
try:
    cursor.execute(...)
    cursor.execute(...)
    connection.commit()
except Exception:
    connection.rollback()
    raise
```

Do not memorize this as a ritual. Understand what logical operation the
transaction represents.

## 27. Transaction Scope

This:

``` python
for item in items:
    cursor.execute(...)
    connection.commit()
```

commits each item separately.

Sometimes that is correct. Sometimes the entire loop represents one
atomic operation:

``` python
for item in items:
    cursor.execute(...)

connection.commit()
```

Transaction boundaries should follow business meaning.

------------------------------------------------------------------------

# Part IX --- Indexes

## 28. What Is an Index?

Suppose a table contains millions of rows and the application repeatedly
asks:

``` sql
SELECT *
FROM equipment
WHERE sku = ?;
```

An index provides a specialized lookup structure that can help the
database find relevant rows efficiently.

Example:

``` sql
CREATE INDEX idx_equipment_sku
ON equipment(sku);
```

Mental model:

``` text
without index → inspect many rows
with index    → use lookup structure → find candidates
```

## 29. Index Trade-offs

Indexes are not free.

They consume storage and must be maintained when data changes.

Therefore:

> **Index for real access patterns, not because indexes sound fast.**

Good candidates often include frequently searched identifiers and
columns heavily used in joins, filtering, or sorting. Actual usefulness
depends on workload and query shape.

------------------------------------------------------------------------

# Part X --- Migrations

## 30. Schema Changes

Schemas evolve.

Version 1:

``` text
equipment
---------
id
sku
name
```

Later:

``` text
price_per_day
```

A migration describes the transition:

``` sql
ALTER TABLE equipment
ADD COLUMN price_per_day REAL NOT NULL DEFAULT 0;
```

A migration answers:

> How do we move an existing database from schema version A to schema
> version B?

Real projects normally maintain ordered migrations rather than manually
editing production databases.

You do not need to build a migration framework yet.

------------------------------------------------------------------------

# Part XI --- SQLite and PostgreSQL

## SQLite

SQLite is an embedded relational database engine. The database commonly
lives in a file and the application connects directly to it.

Advantages:

-   simple deployment;
-   no separate database server;
-   excellent for local applications and many small systems;
-   real SQL;
-   constraints, transactions, and indexes.

## PostgreSQL

PostgreSQL is a client-server relational database system. A dedicated
database server accepts connections from applications and other clients.

It is a strong choice when requirements call for centralized access,
many concurrent clients/writers, remote connections, operational
tooling, high availability, or larger workloads.

The important lesson is not:

> "PostgreSQL is professional and SQLite is not."

It is:

> **Choose the database according to workload, concurrency, deployment,
> operational, and reliability requirements.**

Both are relational databases and both support tables, relationships,
constraints, joins, indexes, and transactions.

------------------------------------------------------------------------

# Part XII --- Database Architecture Boundary

Module 07's architecture should remain intact:

``` text
Presentation
      ↓
Application / Use Cases
      ↓
Domain
      ↑
Repository contract
      ↑
SQLite Repository
      ↓
SQLite
```

Domain code should not contain:

``` python
sqlite3.connect(...)
```

or know about:

``` text
cursor
SQL strings
commit()
warehouse.db
```

Those are infrastructure concerns.

The repository contract provides the application-facing abstraction. SQL
remains real and important, but it lives at the correct boundary.

------------------------------------------------------------------------

# Part XIII --- ORM: First Introduction

An ORM (Object-Relational Mapper) maps database concepts to
programming-language objects.

An ORM may let an application perform an operation conceptually like:

``` python
equipment = session.get(Equipment, 1)
```

instead of explicitly writing SQL.

ORMs can be extremely useful, but they do not remove the underlying
concepts:

``` text
tables
joins
constraints
indexes
transactions
queries
relationships
```

Therefore:

> **Learn SQL and relational modeling before depending heavily on an
> ORM.**

ORMs will be studied later.

------------------------------------------------------------------------

# Part XIV --- Testing Database Code

Not every test should start a real database.

A useful separation is:

``` text
Domain tests
    no database

Application tests
    fake repository

Repository integration tests
    real SQLite
```

Repository integration tests should verify things such as:

-   saving equipment;
-   finding by SKU;
-   updating persisted values;
-   missing-record behavior;
-   uniqueness constraints;
-   foreign-key enforcement;
-   transaction rollback;
-   schema behavior.

These tests verify the integration of:

``` text
Python + SQL + SQLite + schema
```

That is precisely where integration tests belong.

------------------------------------------------------------------------

# Part XV --- Database Design Through Change Scenarios

Reuse Module 07's strongest technique: design through change.

Ask:

### Scenario 1

Equipment names can change.

Where is equipment identity represented?

### Scenario 2

Estimate prices must remain historically correct.

Where is the agreed price stored?

### Scenario 3

An estimate can contain the same equipment twice.

Should the database permit this, or should application logic merge the
items?

### Scenario 4

Equipment moves between shelves.

Do you need only current location, or location history too?

### Scenario 5

Multiple warehouses are introduced.

Where does warehouse identity enter the model?

### Scenario 6

Inventory quantity must never be negative.

Which layer enforces that invariant?

These questions reveal the schema's relationship to the domain.

------------------------------------------------------------------------

# Part XVI --- Practical Exercise Sequence

## Exercise 1 --- Table Anatomy

Create a `books` table with:

``` text
id
title
author
year
```

Insert several rows and inspect the table.

**Goal:** become comfortable with the relational model.

## Exercise 2 --- CRUD

Implement create, read, update, and delete operations.

**Goal:** understand persistent state changes.

## Exercise 3 --- Constraints

Create a table using `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, and `CHECK`.
Attempt invalid operations and observe the database rejecting them.

**Goal:** understand database-enforced integrity.

## Exercise 4 --- Relationships

Create `authors` and `books`, with one author having many books. Write
JOIN queries.

**Goal:** understand relationships instead of nesting everything like
JSON.

## Exercise 5 --- Aggregation

Create sales data and answer:

``` text
How many sales?
Total revenue?
Average sale?
Revenue per product?
Products with more than 10 sales?
```

**Goal:** learn to ask questions of data using SQL.

## Exercise 6 --- Transactions

Implement a transfer or reservation scenario demonstrating successful
commit and failed rollback.

**Goal:** understand atomicity.

## Exercise 7 --- Index Investigation

Create enough records for lookup performance to become measurable.
Compare a lookup before and after an index.

Do not obsess over benchmark precision. Explain why the index can help
and what it costs.

## Exercise 8 --- Schema Design

Design a database for a small rental company with equipment, clients,
estimates, and estimate items. Design the schema before writing SQL.

**Goal:** demonstrate modeling rather than syntax memorization.

------------------------------------------------------------------------

# Part XVII --- QR Warehouse Database Challenge

Do not rewrite the entire project.

## Step 1 --- Inspect

Identify:

``` text
What data exists?
What is persistent?
What is derived?
What belongs to the domain?
What belongs to the database?
```

## Step 2 --- Design

At minimum consider:

``` text
equipment
estimate
estimate_item
```

Do not add tables automatically.

## Step 3 --- Schema

Write the schema manually with appropriate constraints.

## Step 4 --- Seed Data

Create representative records.

## Step 5 --- Repository

Implement repository operations against SQLite.

## Step 6 --- Integration Tests

Test persistence behavior using the real database.

## Step 7 --- Transaction

Introduce at least one transaction where a real multi-step operation
requires atomicity.

## Step 8 --- Index

Add at least one index justified by an actual access pattern.

## Step 9 --- Migration

Perform at least one controlled schema change through a migration.

## Step 10 --- Explain

For every table, constraint, transaction, and index, explain why it
exists.

The challenge is not "make SQLite work."

> **Design persistent state so that the database itself participates in
> protecting the application's correctness.**

------------------------------------------------------------------------

# Part XVIII --- Independent Design Challenge

Do not use QR Warehouse.

Choose an unfamiliar domain such as:

``` text
library
music collection
small online store
cinema ticketing
task management
photo archive
rental car system
```

Identify independently:

``` text
entities
attributes
identifiers
relationships
constraints
likely queries
transactions
possible indexes
```

Then explain:

``` text
Why is this table separate?
Why is this a foreign key?
Why is this value unique?
Why can this value be NULL?
Why does this operation need a transaction?
Why is this column indexed?
What would change if the business rule changed?
```

This is the strongest test of transfer.

------------------------------------------------------------------------

# Part XIX --- Common Mistakes to Track

Continue previous patterns:

-   type confusion;
-   inconsistent contracts;
-   scope mistakes;
-   architecture vs syntax gap;
-   dependency leakage;
-   abstraction judgment;
-   premature coding;
-   overengineering;
-   method-call mistakes.

Add:

## DB-001 --- SQL-as-Magic

Copying SQL without explaining which rows and columns it operates on.

## DB-002 --- SELECT \* Everywhere

Using `SELECT *` without considering what data is actually required.

## DB-003 --- Missing WHERE

Executing `UPDATE` or `DELETE` without deliberately selecting the target
rows.

## DB-004 --- String-Built SQL

Inserting external values directly into SQL strings.

## DB-005 --- Constraint-Free Design

Relying entirely on Python validation for invariants the database can
enforce.

## DB-006 --- Table Explosion

Creating tables without a real modeling reason.

## DB-007 --- JSON-in-SQL

Putting a relational structure into one large JSON blob when relational
querying is required.

## DB-008 --- Over-Normalization

Splitting data into excessive tables without meaningful benefit.

## DB-009 --- Missing Transaction Boundary

Performing logically inseparable changes without considering atomicity.

## DB-010 --- Commit Everywhere

Committing after every tiny operation without understanding transaction
scope.

## DB-011 --- Index Everything

Adding indexes indiscriminately without considering access patterns and
write cost.

## DB-012 --- ORM Before SQL

Trying to avoid learning SQL by immediately learning an ORM.

## DB-013 --- Database in Domain

Putting `sqlite3` or SQL details into domain logic.

## DB-014 --- Current State Replaces Historical State

Storing only current values when historical snapshots are required.

## DB-015 --- Schema-First Without Domain Thinking

Creating tables before identifying persistent entities, relationships,
and invariants.

------------------------------------------------------------------------

# Part XX --- Mental Models

## 1. Database as a Librarian

A JSON file is like a box of documents.

A database is like a librarian who knows:

``` text
where things are
what they are
how they relate
which rules they must obey
```

## 2. Table as a Spreadsheet With Rules

A table resembles a spreadsheet, but the database adds identity,
constraints, relationships, transactions, queries, and indexes.

## 3. Primary Key as Passport Number

Names can change. Stable identifiers provide identity.

``` text
name → descriptive
id   → identity
```

## 4. Foreign Key as an Address

A foreign key tells you that one record refers to another record.

## 5. JOIN as Connecting Ledgers

Two ledgers can be connected using a shared identifier.

## 6. Transaction as a Package

A transaction is a package of changes. Either the logical package
succeeds or it is rolled back.

## 7. Index as a Book Index

A book index points toward relevant pages instead of forcing a scan from
the beginning. A database index provides a similar lookup aid.

## 8. Constraint as a Security Guard

Python may request valid state. A database constraint can reject invalid
state at the persistence boundary.

------------------------------------------------------------------------

# Part XXI --- Self-Check Questions

Before declaring Module 08 complete, answer these in your own words:

1.  What is a database?
2.  What makes a database relational?
3.  What is a table?
4.  What is a row?
5.  What is a column?
6.  What is a primary key?
7.  What is a foreign key?
8.  Why are relationships represented explicitly?
9.  What is one-to-many?
10. How is many-to-many usually represented?
11. What problem does normalization address?
12. What does `SELECT` do?
13. What does `WHERE` do?
14. What does `ORDER BY` do?
15. Why is `WHERE` important for `UPDATE` and `DELETE`?
16. What is `NULL`?
17. What does `JOIN` do?
18. What is the practical difference between INNER JOIN and LEFT JOIN?
19. What does `GROUP BY` do?
20. What does `HAVING` do?
21. Why are parameterized queries important?
22. What is SQL injection?
23. What does `fetchone()` return?
24. What does `fetchall()` return?
25. What is a transaction?
26. What does atomicity mean?
27. Why does `commit()` exist?
28. Why does `rollback()` exist?
29. What is an index?
30. Why can an index improve performance?
31. Why can too many indexes be harmful?
32. What is a database constraint?
33. Why use both application validation and database constraints?
34. What is a migration?
35. What is the practical difference between SQLite and PostgreSQL?
36. Why should domain code not know about SQL?
37. What belongs in a Repository?
38. Why should repository integration tests use a real database?
39. When should a schema store a historical snapshot?
40. How would you decide whether a concept deserves a new table?
41. What makes a transaction boundary meaningful?
42. How would you decide which column to index?
43. What is the simplest database design that satisfies the
    requirements?

The final question is the most important.

------------------------------------------------------------------------

# Part XXII --- Completion Criteria

Module 08 is complete when the student can independently:

-   create a relational schema;
-   define primary and foreign keys;
-   use practical constraints;
-   perform CRUD operations;
-   write filtered queries;
-   write ordinary joins;
-   use aggregation;
-   use parameterized queries;
-   explain SQL injection;
-   create and use transactions;
-   explain commit and rollback;
-   create an index for a justified access pattern;
-   explain index trade-offs;
-   design a small normalized schema;
-   perform a basic migration;
-   use SQLite from Python;
-   keep SQL inside the infrastructure boundary;
-   write repository integration tests;
-   distinguish business tests from persistence tests;
-   explain SQLite vs PostgreSQL conceptually;
-   integrate the database into QR Warehouse without leaking database
    details into domain logic;
-   design a small unrelated database without copying QR Warehouse
    blindly.

Most importantly:

> **The student can explain what persistent facts exist, how they
> relate, which rules protect them, which queries the application needs,
> and why the database design represents the domain correctly.**

------------------------------------------------------------------------

# Final Conceptual Transition

Module 04 taught:

> **Good structure makes change safer.**

Module 05 taught:

> **Objects can own state and behavior.**

Module 06 taught:

> **Relationships, interfaces, and polymorphism allow related components
> to vary without unnecessary coupling.**

Module 07 taught:

> **A maintainable application is a system of components whose
> responsibilities and dependencies are deliberately controlled.**

Module 08 teaches:

> **Persistent state is part of the system's model, and a database can
> actively enforce and query that model.**

The progression becomes:

``` text
Data
  ↓
Functions
  ↓
Modules
  ↓
Components
  ↓
Objects
  ↓
Object Collaboration
  ↓
Polymorphism
  ↓
Application Boundaries
  ↓
Controlled Dependencies
  ↓
Persistent State
  ↓
Relational Models
  ↓
Queries + Constraints + Transactions
  ↓
Reliable Applications
```

The final instinct should not be:

> "What SQL syntax do I need?"

It should be:

> **"What persistent state exists, what relationships and invariants
> define it, and how should the database represent and protect them?"**

That is the core engineering skill of Module 08.

------------------------------------------------------------------------

# Recommended Time Budget

``` text
Database fundamentals                 ~1.5–2 h
Relational modeling                   ~2 h
SQL CRUD                              ~2 h
Filtering / sorting / aggregation     ~2 h
JOINs                                 ~2 h
Constraints / normalization           ~2 h
Python sqlite3                        ~1.5 h
Transactions                          ~2 h
Indexes                               ~1.5 h
Migrations                            ~1 h
SQLite vs PostgreSQL                  ~1 h
QR Warehouse integration              ~4–5 h
Independent design challenge           ~2 h
```

Expected total:

``` text
~20–24 hours
```

Do not optimize for consuming the estimate. Optimize for independent
reasoning and reproducibility.

------------------------------------------------------------------------

# Final Mentor Note

Module 07 deliberately exposed a gap rather than hiding it.

The student successfully used SQLite as infrastructure but explicitly
recognized that SQL syntax and database internals were not yet
understood deeply.

That is not a failure of Module 07. It is exactly why Module 08 exists.

The mentor should reward:

``` text
correct data modeling
+
clear SQL reasoning
+
understanding of constraints
+
transaction awareness
+
security awareness
+
justified indexing
+
schema judgment
+
architectural boundaries
+
independent problem solving
```

Do not reward:

``` text
memorizing SQL syntax
+
creating many tables
+
adding indexes everywhere
+
using an ORM to avoid SQL
+
database complexity for its own sake
```

The student should leave this module not thinking:

> "I know SQLite."

but:

> **"I understand what my application is asking the database to
> represent, protect, and retrieve --- and I can reason about the
> database rather than treating it as magic."**

------------------------------------------------------------------------

# Knowledge Base Integration

After Module 08, update:

``` text
Programming Handbook
Learning Journal
Questions
Development Log
Mental Models
Checkpoint Report
```

The Programming Handbook should store durable technical knowledge such
as:

``` text
relational databases
tables / rows / columns
primary keys
foreign keys
relationships
normalization
SQL
CRUD
WHERE / ORDER BY / LIMIT
JOIN
GROUP BY / HAVING
NULL
constraints
parameterized queries
SQL injection
transactions
atomicity
commit / rollback
indexes
schema design
migrations
SQLite
PostgreSQL comparison
repository/database boundary
database testing
```

The Learning Journal should preserve the learning experience rather than
duplicate the Handbook.

The Development Log should preserve methodology changes.

The Questions document should preserve unresolved curiosity.

The Checkpoint Report should distinguish:

``` text
SQL syntax recall
        vs
relational understanding
        vs
database design judgment
        vs
independent persistence architecture
```

------------------------------------------------------------------------

*End of Module 08 --- Database Fundamentals & SQL*
