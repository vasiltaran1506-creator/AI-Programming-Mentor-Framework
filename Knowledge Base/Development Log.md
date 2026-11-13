---

# Development Log

**Version:** 3.1
**Status:** Active
**Maintained by:** AI Methodologist

---

## Purpose

The Development Log records the long-term evolution of the student's programming and software-engineering development.

Unlike the **Learning Journal**, which records individual learning experiences, and **Checkpoint Reports**, which evaluate modules, this document focuses on patterns that emerge across multiple modules.

Its purpose is to improve the educational process itself.

The student changes.
The mentor changes.
The methodology changes.

This document records those changes and uses new evidence to revise earlier assumptions.

---

# 1. Methodology

After each completed module, the mentor should consider:

1. What became stronger?
2. What remains weak or inconsistent?
3. What did the module reveal about the student's learning process?
4. How should future teaching adapt?

Older observations should not be treated as permanent diagnoses.

New evidence may:

* reinforce an existing observation;
* refine it;
* contradict it;
* show that a previously important difficulty has become less relevant.

The current state should always be based on the most recent demonstrated evidence.

---

# 2. Student Profile Evolution

## Initial Profile

| Field                 | Value                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Learning Stage**    | Beginning Programmer                                                                                                                                                        |
| **Primary Language**  | Python                                                                                                                                                                      |
| **Primary Goal**      | Become capable of designing, implementing, testing, and maintaining real software while using AI as an engineering assistant rather than as an substitute for understanding. |
| **Learning Strategy** | Project-based learning combined with structured curriculum and guided discovery.                                                                                            |

---

## Current Profile — After Module 09

| Field                 | Value                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Learning Stage**    | Intermediate learning stage: practical application development                                                                                                                          |
| **Current Focus**     | HTTP APIs, FastAPI, API testing, multiple application entry points, asynchronous programming, testing architecture, and continued database development                                  |
| **Primary Goal**      | Build sufficient independent engineering ability to develop real backend-oriented applications and gradually take responsibility for architecture, testing, deployment, and maintenance |
| **Learning Strategy** | Mental model → conceptual understanding → guided implementation → independent implementation → project integration → reflection                                                         |

The current description intentionally avoids labels such as "professional engineer", "senior engineer", or "architect".

The student has demonstrated several advanced concepts in guided project contexts, but broader independent experience across unfamiliar systems is still developing.

---

## Current Profile — After Module 11

> The Module 09 profile above is retained unchanged as a historical record.
> The following description supersedes it as the current assessment.

| Field                 | Value                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Learning Stage**    | Intermediate learning stage: application development with first operational deployment experience                                                                                       |
| **Current Focus**     | Linux server operation, SSH-based administration, Docker images and containers, persistent storage, Docker Compose, CI pipelines, and the boundary between application code and infrastructure |
| **Primary Goal**      | Develop QR Warehouse into a maintainable, deployable backend product; reach independent operational competence; prepare for PostgreSQL and commercial-grade deployment                  |
| **Learning Strategy** | Mental model → conceptual understanding → guided implementation → verification on real infrastructure → failure diagnosis → scope negotiation → reflection                                |

### What changed in Module 11

The student crossed a significant boundary:

```text
"An application that runs on my computer"
                 ↓
"A service that runs on a machine I operate"
```

This is not merely a new tool in the toolbox. It introduces an entirely new class of problems:

* state that survives process death;
* environment that differs from the development machine;
* code delivery between machines;
* authentication between systems rather than between a person and a site;
* automatic recovery after reboot;
* verification that happens independently of the developer.

### Calibration

The student successfully completed a guided end-to-end deployment and independently diagnosed several failures.

This does **not** yet constitute independent operational expertise. The student has not yet:

* deployed a service from scratch without dialogue;
* operated a multi-service system;
* configured reverse proxy, HTTPS, or authentication;
* administered PostgreSQL;
* performed a real backup-and-restore cycle;
* written a meaningful test suite autonomously.

The correct description remains **intermediate**, now with a first real deployment behind them.

---

## Current Profile — After Module 12

> The Module 09 and Module 11 profiles above are retained unchanged as historical records.
> The following description supersedes them as the current assessment.

| Field                 | Value                                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Learning Stage**    | Intermediate learning stage: application development with a first real database migration and a substantially redesigned domain model        |
| **Current Focus**     | PostgreSQL as a separate service, SQLAlchemy Core over an async driver, Alembic schema migrations, multi-table transactional workflows, repository boundaries under load |
| **Primary Goal**      | Complete the operational lifecycle of QR Warehouse on PostgreSQL and reach independent implementation ability in the persistence and application layers |
| **Learning Strategy** | Mental model → decomposition → implementation → review → correction → integration → reflection                                                |

### Context availability note

The retained dialogue covers Module 12 only from the middle of the repository-migration work onward.

The earlier phases — persistence audit, PostgreSQL fundamentals in Compose, the driver/interface decision, the isolated async experiment, and the test/CI work — are reported by the student as completed, and later work presupposes them. They are not directly observable in the retained context.

They are therefore recorded as **reported and indirectly corroborated**, not as mentor-observed demonstrations. Before a final module assessment is issued, the corresponding artifacts (notes, driver-decision record, test suite, CI workflow) should be inspected directly.

### What changed in Module 12

The student crossed a second boundary:

```text
"My application stores data in a file"
                 ↓
"My application coordinates state in a database server"
```

This introduced a new class of problem that did not exist with a single-file database:

* several tables that must change together or not at all;
* a distinction between retrieving data and deciding what the data means;
* schema evolution against a database that already contains rows;
* identifiers that refer to different entities and are easy to confuse;
* an asynchronous call chain in which a single missing `await` produces a runtime failure rather than a type error.

### Scope deviation and its consequences

Module 12 was specified as an infrastructure replacement: swap the SQLite adapter for PostgreSQL while preserving the domain model and business behavior. The final item of the planned scope was explicitly an architectural test — the boundaries built in Modules 07–09 should make the swap possible without touching business logic.

The student instead replaced the data model and rewrote most of the application. The simple early schema was replaced by a domain model covering equipment types with individual/bulk tracking, estimates with item snapshots, reservations, picking tasks, and item allocations.

This decision was reasoned: migrating disposable learning data into a schema that did not represent the real domain would have produced work with no product value.

The trade-off must be recorded honestly:

* the student gained substantially more domain-modelling and multi-entity workflow experience than the module planned;
* the specific claim the module was designed to test — **infrastructure replaced without disturbing business logic** — was not tested, because the business logic changed at the same time;
* the two changes were not separated by a verified working state, which is what Adjustment 015 exists to prevent.

This is not a failure of the module. It is a scope deviation whose cost is a missing piece of evidence, and it should be recorded as such rather than absorbed silently into "module completed".

### Calibration

Demonstrated in the retained portion of the module:

* implementing multi-table write workflows across several repositories with a single commit boundary;
* applying Alembic migrations against a live server database, including reading a generated revision before applying it;
* diagnosing a `NOT NULL` migration failure and correctly proposing the nullable → backfill → constrain sequence;
* independently designing a batch-retrieval availability algorithm, including the non-obvious case of two positions in the same estimate consuming each other's stock;
* independently designing an operator-facing response contract and an endpoint path based on how the client would actually be used;
* repeatedly identifying defects in the mentor's proposed solutions.

Not demonstrated:

* authoring a non-trivial migration independently — the three-step migration was written by the mentor, and the student explicitly noted this as a loss;
* reading a framework validation traceback without guidance;
* verifying rollback behavior through an induced failure;
* reasoning about concurrent execution — the race between availability check and reservation insert was noted and deferred, not resolved;
* transferring any of this to an unfamiliar codebase.

First-draft error rate remained high. Most slices required correction after review, and several corrections were repeats of errors already seen earlier in the module. The correct description is **reviewed implementation**, not independent implementation.

---

# 3. Learning Characteristics

These observations describe learning behavior rather than grades.

---

## 3.1 Strong Conceptual Curiosity

**Confidence:** High

The student frequently asks why a system should be designed in a particular way rather than merely asking how to implement it.

Examples include:

* questioning why Use Cases should exist separately from domain objects;
* asking why repositories should not own transaction commits;
* questioning whether a class should continue to exist when its behavior is no longer used;
* examining whether an abstraction solves a real problem;
* asking what happens when an infrastructure component changes;
* questioning how an HTTP API can coexist with the existing CLI.

### Additional evidence — Module 11

* asking why GitHub abolished passwords for Git operations;
* immediately challenging the answer: "but can't a key leak just like a password?";
* asking what a daemon actually is and why it is called a daemon;
* asking whether `0.0.0.0` is really necessary and what a specific IP would do instead;
* asking how Docker physically redirects a request from the host IP to the container IP;
* asking why `COPY . .` contains two dots;
* asking whether configuration files belong in a volume.

### Educational implication

New concepts should begin with the problem they solve.

The mentor should avoid presenting architectural patterns as arbitrary rules.

Module 11 additionally confirms that the student is not satisfied with a correct-looking command. They want the mechanism underneath it.

---

## 3.2 Architectural Intuition

**Confidence:** High

The student has repeatedly arrived at useful architectural solutions before learning their formal names.

Examples include:

* repository boundaries;
* dependency inversion;
* Strategy Pattern;
* composition over inheritance;
* Factory Pattern;
* Architectural Filter for Domain/Application/Infrastructure;
* Unit of Work;
* Historical Snapshot;
* Application Shell;
* Read Model recognition;
* multiple application entry points;
* separating HTTP translation from business logic.

This is useful evidence of developing architectural intuition.

However, these discoveries should not automatically be interpreted as broad architecture mastery. Most were developed within known project contexts and with some degree of guidance.

### Additional evidence — Module 11

* independently concluded that container-local data is disposable and must be externalized;
* correctly distinguished build-time configuration from run-time configuration;
* proposed separating client-side presentation (exports, charts, files) from server-side logic;
* proposed splitting CI into separate jobs by test category;
* recognized that hard-coded paths are a design problem, not only a Docker problem.

### Educational implication

Continue using discovery-based architecture exercises, but increasingly require the student to justify decisions independently and compare alternative designs.

---

## 3.3 Analytical Thinking

**Confidence:** High

The student regularly considers:

* edge cases;
* failure scenarios;
* state transitions;
* trade-offs;
* data integrity;
* dependency direction;
* information leakage;
* abstraction cost;
* future changes.

A recurring question is effectively:

> "What happens if this assumption stops being true?"

This is particularly visible in the QR Warehouse and Gaffer Sandbox projects.

### Additional evidence — Module 11

The student repeatedly reasoned correctly about lifecycle questions before being taught the terminology:

* what happens to the database when the container is deleted;
* what happens when the volume itself is deleted;
* what happens to configuration when a new empty volume replaces an old one;
* what happens to a foreground process when the SSH session closes;
* whether a test suite can be manipulated to produce a false green result.

### Educational implication

Prefer realistic problems with competing constraints over purely mechanical exercises.

Lifecycle and failure questions are now a particularly productive entry point for this student.

---

## 3.4 Understanding Before Memorization

**Confidence:** High

The student tends to resist terminology until its conceptual meaning is clear.

This was particularly visible with:

* Use Cases;
* Repository Pattern;
* Dependency Inversion;
* Unit of Work;
* Read Models;
* HTTP API architecture.

Mental models have consistently helped resolve these conceptual boundaries.

### Module 11 extension

The same pattern appeared with infrastructure terminology:

* daemon;
* image versus container;
* volume versus container;
* bind mount versus named volume;
* build-time versus run-time;
* port mapping;
* detached mode.

The student explicitly refused to proceed on the basis of unexplained flags:

> "Я не очень понимаю, что значит COPY . . и что значат все эти флаги"

### Educational implication

The preferred sequence remains:

```text
Problem
   ↓
Mental Model
   ↓
Concept
   ↓
Formal Terminology
   ↓
Implementation
   ↓
Practice
```

---

## 3.5 Pragmatic Judgment

**Confidence:** High, but still developing

The student has demonstrated awareness that additional abstraction is not automatically better.

Examples include:

* questioning unnecessary Factory classes;
* deciding that pervasive logging was not justified at the current project scale;
* removing dead code instead of preserving obsolete abstractions;
* simplifying `Estimate` after its behavior moved elsewhere;
* rejecting unnecessary architectural complexity;
* recognizing that synchronous SQLite does not need to be artificially converted into asynchronous code.

At the same time, independent architectural judgment across unfamiliar systems has not yet been sufficiently tested.

### Refinement after Module 11

The earlier judgment about synchronous SQLite has **evolved rather than been contradicted**.

In Module 09 the student concluded that async conversion was unnecessary. In Module 11 the student identified the synchronous driver as a genuine product limitation, connected it to their unused async/await knowledge, and connected PostgreSQL to both employability and commercial readiness.

The difference is context: the project is no longer framed as an exercise.

### Additional Module 11 evidence of pragmatism

* chose to keep SQLite for the first deployment rather than expand the module's scope;
* declined to add a coverage threshold while the suite is shallow;
* declined to implement backups for disposable test data on a capacity-constrained disk;
* justified backup frequency using actual business cadence rather than a generic rule;
* agreed to skip a redundant `--build` experiment after demonstrating understanding.

### Educational implication

Every architectural concept should include:

* when it is useful;
* when it is unnecessary;
* what it costs;
* what simpler alternative exists;
* what future change would justify introducing it.

Module 11 shows that the student can now participate in this trade-off discussion rather than only receive it.

---

## 3.6 Intellectual Humility

**Confidence:** High

The student regularly distinguishes between:

* understanding a concept;
* having implemented it;
* being comfortable applying it independently;
* having deep expertise.

This is important because the student has sometimes developed strong solutions while simultaneously recognizing gaps in knowledge.

The mentor should preserve this calibration rather than replacing it with exaggerated labels.

### Additional evidence — Module 11

The student openly stated:

* "Я пока не знаю, как устроена файловая система докера изнутри";
* "я не особо понимаю" regarding port redirection;
* "Я не знаю, что значит флаг -t";
* an explicit admission that they dislike writing tests and that existing tests were written formally rather than from conviction.

These are high-quality signals. The student does not manufacture confidence to satisfy the mentor.

### Educational implication

Preserve and reward explicit uncertainty. Never allow a green CI badge or a running container to be interpreted as proof of understanding.

---

## 3.7 Motivation Through Real Problems

**Confidence:** High

Engagement increases substantially when technical concepts are connected to real problems.

The strongest example is the Gaffer Sandbox, where database concepts were connected to the student's previous experience with equipment rental estimates.

The QR Warehouse project similarly provides a persistent real-world context for:

* inventory;
* equipment;
* estimates;
* QR codes;
* warehouse workflows;
* APIs;
* databases;
* integration;
* deployment.

### Educational implication

Whenever possible, introduce abstract concepts through realistic domain problems before moving to generalized exercises.

---

## 3.8 Transfer of Existing Mental Models

**Confidence:** Medium-High

**First clearly recorded in Module 11.**

The student repeatedly reused previously learned models to approach unfamiliar infrastructure:

* class versus object → image versus container;
* recipe → Dockerfile;
* isolated kitchen → virtual environment;
* hotel room versus bank safe → container versus volume;
* key versus spoken code → SSH key versus password.

Importantly, the student also transferred a **wrong** model initially:

* described an image as "a snapshot of a container";
* described a volume as "a separate container";
* assumed the base image should mirror the server's operating system;
* assumed `routes.py` was an executable file.

Each misconception was corrected through dialogue and did not persist.

### Educational implication

Elicit the student's existing model before introducing a new one.

Then explicitly test where the analogy breaks. Analogy-based learning is effective for this student, but broken analogies become durable misconceptions if left uncorrected.

---

## 3.9 Self-Diagnosis and Verification

**Confidence:** High

**First clearly demonstrated in Module 11.**

The student independently located and resolved several failures:

* identified that CI did not trigger because the workflow's branch filter did not match the working branch;
* recognized that `pip` had installed stale dependencies because `requirements.txt` had not been pushed;
* chose the Git-based repair path rather than editing the file directly on the server;
* noticed after reboot that data was absent and correctly traced it to an earlier volume reset.

This is a meaningful shift from "tell me what to do" to "here is what I observed, here is my hypothesis".

### Educational implication

Provide diagnostic space before supplying the answer.

Productive questions now include:

> What would you check first?

> Which part of this output actually failed?

> What evidence would confirm or refute your hypothesis?

---

## 3.10 Willingness to Question the Method Itself

**Confidence:** Medium, emerging

**First clearly recorded in Module 11.**

The student began questioning the educational structure, not only the technical content:

* "Чему у нас посвящен модуль? Если модуль чисто про докер, то я не вижу смысла изучать постгрес внутри него";
* asked whether test results can be falsified by rewriting the tests;
* proposed restructuring CI jobs by test category;
* declined an exercise that would add no new information.

This is a sign of growing ownership over the learning process.

### Educational implication

Answer scope questions explicitly and honestly.

Treat student criticism of an exercise as curriculum-design evidence, not as resistance.

---

## 3.11 Commercial and Product Awareness

**Confidence:** Medium-High, emerging

**First clearly recorded in Module 11.**

The student explicitly reframed the project:

> "я давно перестал думать об этом проекте как об учебном"

They articulated:

* an intended buyer (a company);
* an approximate customer and project cadence;
* a change frequency for the equipment catalog;
* a disk-capacity constraint on the current server;
* a career motivation for learning PostgreSQL;
* a future client/server split of the application.

### Educational implication

Use this as a source of realistic constraints.

At the same time, distinguish carefully between:

* a problem that exists now;
* a problem that will exist at commercial scale;
* a problem that belongs to a different module.

The student's commercial vision is an asset. It must not become a source of premature scope expansion.

---

## Additional evidence — Module 12

Mapped to the existing characteristics rather than replacing them.

**3.1 Strong Conceptual Curiosity**

* asked why an action endpoint uses `POST` rather than `PATCH`, given that a status field is being updated;
* asked what question the `reservation`, `picking_task`, and `item_allocation` tables each answer, and refused to proceed until the responsibilities were clear;
* asked whether `item_allocation` needs its own `asset_code`, which surfaced a normalization question rather than a schema defect.

**3.2 Architectural Intuition**

* decomposed the picking workflow into discrete operations before writing any code, and did so by drawing the state transitions on a refrigerator door when no whiteboard was available;
* independently reasoned that returning a whole `PickingTask` after each scan would transmit redundant data, that returning only an `ItemAllocation` would transmit too little, and arrived at a purpose-built response contract containing per-line and per-task progress;
* independently challenged the proposed endpoint path containing `estimate_item_id`, on the grounds that a scanner client cannot know that identifier in advance.

**3.3 Analytical Thinking**

* the strongest single piece of evidence in the module: while checking availability, the student accounted not only for existing reservations but for other positions **in the same estimate** whose date ranges overlap. This case was not present in any mentor-supplied description;
* motivated defensive success checks by reasoning about a storage failure part-way through a transaction. The instinct was correct; the remedy belonged at a different layer, and the student accepted removing the checks once that was explained.

**3.5 Pragmatic Judgment**

* deferred the cross-task uniqueness check for scanned units after correctly estimating that it would not be a small change;
* declined scheduled reminders for stalled tasks as unnecessary for the current scope;
* chose strict completion validation now, with a separate confirmation-driven path deferred rather than bolted on;
* kept two input paths for bulk equipment (repeated scanning, or one scan plus an edited quantity) instead of forcing a single interaction model;
* chose `.returning()` with a row count over `rowcount` when the type checker objected, accepting slightly more work for a clearer contract.

**3.6 Intellectual Humility**

* stated plainly, before submitting a large slice, that they were not confident any of it would work;
* explicitly recorded that the migration file had been written by the mentor rather than by themselves, and named that as a gap;
* asked directly where in a long traceback the actual failure is described.

**3.10 Willingness to Question the Method Itself**

This characteristic strengthened considerably. The student rejected three successive mentor proposals for the availability check:

> the first required one query per estimate line;

> the second placed business decisions inside the repository;

> the third reintroduced the per-line query loop after the objection had already been made.

Each objection was correct. The student then stopped the exchange and asked to restart from the problem rather than from the proposed code.

---

## 3.12 Sustained Complexity — Tolerance and Limits

**Confidence:** High, first clearly recorded in Module 12.

The availability-checking problem required simultaneous reasoning over three collections — estimate lines, existing reservations, and physical stock — under a variable condition (date overlap) and two tracking modes.

The student reported approximately two days on this single use case, working late into the night, with reported frustration and disrupted sleep, and afterwards described the transition from linear operations to multi-entity coordination as the hardest thing they had encountered.

The outcome was correct and largely self-authored. The process was not sustainable.

Two contributing factors should be separated:

* the problem itself is genuinely a step change in difficulty, and this is expected;
* the mentor supplied three flawed approaches before the student restarted, which added avoidable cost.

### Educational implication

Multi-entity coordination work should be decomposed into independently verifiable steps before implementation begins, with explicit stopping points. Abstraction-heavy work should not be scheduled at night. When a student reports that an approach is confusing, treat that as a defect signal in the approach before treating it as a comprehension gap in the student.

---

# 4. Learning Preferences

| Aspect                       | Current Observation                                     |
| ---------------------------- | ------------------------------------------------------- |
| **Teaching Style**           | Guided discovery, questions, dialogue                   |
| **Concept Introduction**     | Mental model before terminology                         |
| **Examples**                 | Real engineering problems and personal projects         |
| **Architecture Learning**    | Refactoring and change scenarios                        |
| **Pattern Learning**         | Discover pattern → name pattern → examine alternatives  |
| **Practice**                 | Project integration after focused exercises             |
| **Testing**                  | Learn through behavior and failure cases                |
| **Least Effective Approach** | Memorization without context or unexplained terminology |

### Additional preferences observed in Module 11

| Aspect                       | Current Observation                                     |
| ---------------------------- | ------------------------------------------------------- |
| **Infrastructure Learning**  | Lifecycle and data-flow models before commands          |
| **Failure Analysis**         | Diagnose the actual failing component before fixing     |
| **Scope Negotiation**        | Explicit module boundaries and recorded deferrals       |
| **Exercise Selection**       | May skip a drill once reasoning is demonstrated         |
| **Pacing**                   | Wants to move to practice once the concept is clear     |

The student responds particularly well to questions such as:

> What happens if X changes?

> What responsibility actually belongs here?

> What would break if this dependency were replaced?

> Is this abstraction solving a real problem?

### Additional productive questions from Module 11

> What happens to this data when the container is deleted?

> Which layer owns this decision: build time or run time?

> Is this needed now, or in the next module?

> What would you check first?

> Where does this file physically live?

### Additional preferences observed in Module 12

| Aspect                     | Current Observation                                                          |
| -------------------------- | ---------------------------------------------------------------------------- |
| **Responsibility Boundaries** | Will stop implementation to settle which layer owns a decision            |
| **Data Retrieval**         | Rejects per-item query loops once the pattern is visible                     |
| **API Design**             | Reasons from what the operator sees on screen backwards to the contract      |
| **Migration Work**         | Prefers generating on the server against the real database, out of familiarity rather than efficiency |
| **Error Explanation**      | Wants to know where in a long traceback the failure is actually stated       |
| **Pace**                   | Wants a written plan of steps, checks, and inputs without complete code      |

The last item is a direct restatement of Adjustment 014 by the student:

> "Не пиши код за меня, просто опиши текстом, что и как я должен сделать."

---

# 5. Progress Timeline

## Module 00

The student began moving from thinking of programming as code writing toward structured problem solving.

### Methodology change

Emphasize:

* decomposition;
* state;
* algorithms;
* reasoning before syntax.

---

## Module 01

The student strengthened Python fundamentals and began treating functions and data structures as conceptual tools rather than isolated syntax.

### Methodology change

Continue connecting language constructs to the underlying computational model.

---

## Module 02

The student became more comfortable with Python's standard data structures and built-in operations.

A recurring improvement was learning to choose an appropriate data representation rather than relying on parallel structures.

### Methodology change

Emphasize:

* data representation;
* mutable vs immutable objects;
* choosing structures based on operations required.

---

## Module 03

The student developed multi-module applications and defensive data-processing workflows.

Important patterns included:

* separation of responsibilities;
* validation boundaries;
* configuration separation;
* data pipelines;
* defensive defaults.

### Methodology change

Move gradually from isolated Python exercises toward complete small applications.

---

## Module 04

The QR Warehouse project became a central practical learning environment.

The student worked with:

* configuration;
* file loading;
* validation;
* business logic;
* estimates;
* inventory;
* export;
* orchestration.

The project demonstrated that programming concepts became easier to understand when attached to a real domain.

### Methodology change

Use QR Warehouse for genuine integration needs while keeping experimental patterns in separate exercises or mini-projects.

---

## Module 05

The student developed practical OOP skills.

Important concepts included:

* encapsulation;
* composition;
* inheritance;
* polymorphism;
* dataclasses;
* object responsibilities;
* automated testing.

The student also began using pytest to protect business behavior.

### Methodology change

Introduce OOP through domain modeling rather than through isolated class exercises.

---

## Module 06

The student expanded from basic OOP toward reusable behavioral designs.

Important developments included:

* Strategy Pattern;
* polymorphism;
* Abstract Base Classes;
* `super()`;
* Factory Pattern;
* composition over inheritance;
* Liskov Substitution Principle;
* dependency injection.

The student repeatedly demonstrated an ability to discover a useful design before learning its formal name.

### Methodology change

Continue pattern discovery, but always include discussion of the cost and appropriate scope of the pattern.

---

## Module 07

The focus shifted from individual objects toward application architecture.

Major developments included:

* Repository Pattern;
* Dependency Inversion;
* Use Cases;
* Composition Root;
* In-Memory Fakes;
* separation of Domain, Application, and Infrastructure;
* SQLite as a persistence mechanism;
* JSON → SQLite refactoring.

The most important architectural insight was that architecture can be understood as **controlling dependencies and containing change**.

### Methodology change

Teach architecture primarily through change scenarios.

For example:

```text
What if JSON becomes SQLite?

What if CLI becomes HTTP?

What if another interface is added?

What if two repositories must participate in one operation?
```

---

## Module 08

The student deepened database and application-architecture knowledge.

Important developments included:

* relational schema design;
* foreign keys;
* constraints;
* indexes;
* SQL CRUD;
* Historical Snapshot;
* Unit of Work;
* multi-repository coordination;
* thick Use Cases;
* Application Shell;
* Read Model vs Domain Entity;
* nullable foreign-key design;
* idempotent seeding;
* feature-branch workflow.

The Gaffer Sandbox provided a domain-driven environment for learning relational modeling.

### Methodology change

Continue connecting database concepts to business invariants.

However, database knowledge should now be deepened rather than treated as complete. In particular:

* database internals;
* query planning;
* PostgreSQL;
* migrations;
* deeper transaction behavior

remain future topics.

---

## Module 09

The student moved from a primarily CLI-oriented application toward a multi-entry-point application with an HTTP API.

Major developments included:

* HTTP request/response model;
* FastAPI;
* Pydantic;
* HTTP methods;
* HTTP status codes;
* API validation;
* Swagger/OpenAPI;
* TestClient;
* API-level testing;
* structured `Result` values;
* separation of business results from HTTP translation;
* information-leakage considerations;
* CLI and HTTP API sharing the same Use Cases;
* basic `async`/`await`;
* `asyncio.gather`;
* concurrency vs parallelism;
* I/O-bound vs CPU-bound work.

The key conceptual shift was:

```text
CLI ───────
           ↓
     Presentation
           ↓
       Use Cases
           ↓
     Infrastructure
           ↓
        Database
           ↑
           │
HTTP API ──┘
```

The student demonstrated that a new presentation layer can be added without rewriting the business logic.

### Methodology change

The next stage should not simply introduce more frameworks.

It should consolidate application development through:

* integration testing;
* test isolation;
* Use Case testing;
* API design;
* authentication and authorization;
* deeper database work;
* deployment;
* independent implementation.

---

## Module 11

### Home Server, Linux, Docker, CI/CD

The student moved from developing an application to operating a service on a separate machine.

This module was conducted on a real home server (`homelab`, Ubuntu 26.04 LTS), not in a simulated environment.

### Server and network foundations

* SSH access under a regular user rather than root;
* understanding of `sudo` and least privilege;
* interpretation of `ip addr` output;
* distinction between dynamic DHCP assignment and a stable address;
* creation of a DHCP reservation on the router;
* verification of reconnection after reboot.

### Code delivery between machines

* GitHub as a single source of truth;
* the local → staging → commit → push → remote model;
* generation of a server-side SSH key pair;
* understanding of why passwords were replaced by keys and tokens for Git operations;
* the distinction between a private key and a public key;
* cloning the repository over SSH;
* feature-branch isolation for infrastructure work.

### Baseline before containerization

* installation of `pip` and `venv`;
* creation of a virtual environment on the server;
* execution of the existing test suite as a known-working baseline;
* recovery from a stale `requirements.txt` caused by an unpushed local change;
* deliberate choice of the Git-based repair rather than server-side file editing.

### Docker concepts

* daemon versus client;
* image versus container;
* layers and build caching;
* `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`;
* dependency-first layer ordering;
* `.dockerignore` and defensive exclusion patterns;
* the relationship between build context and container filesystem;
* why existing relative paths in the application did not require rewriting.

### Persistence

* understanding that container-local state is disposable;
* named volumes as independent storage;
* volume mount points as "doors" rather than copies;
* volume population on first use;
* separation of code and configuration (image) from user data (volume);
* an explicit persistence test: create data → delete container → recreate container → verify data survived.

### Runtime and orchestration

* port mapping (`host:container`) and its relationship to `--host 0.0.0.0`;
* detached mode;
* image tagging;
* Docker Compose as Infrastructure as Code;
* service definitions, port mappings, volume declarations;
* `up`, `down`, `ps`, `logs`;
* the difference between `up -d` and `up -d --build`;
* restart policies;
* verification of automatic service startup after a full server reboot.

### Continuous Integration

* GitHub Actions as an independent verification environment;
* workflow triggers and branch filters;
* checkout → setup Python → install dependencies → run tests;
* diagnosis of a non-triggering workflow caused by a branch mismatch;
* generalization of the trigger to `feature/**`;
* discussion of what a failing check does and does not prevent;
* discussion of test falsification and defense in depth (review, coverage, security scanning, culture).

### Operational decisions made by the student

* **PostgreSQL deferred** to a dedicated module, with explicit reasoning about scope and depth of learning;
* **SQLite retained** for the first deployment;
* **Backups deferred** after reviewing the mechanism, with reasoning about data value, change cadence, and disk capacity;
* **Coverage thresholds deferred** until the test suite is meaningful;
* **Application rewrite refused as part of infrastructure work** after discussion of scope creep;
* **CI kept minimal** (one job) until the project justifies splitting it.

### Failures encountered and diagnosed

* a pre-existing broken `amneziawg-dkms` package blocked `apt`; the student learned to distinguish "my change failed" from "an unrelated system component was already broken";
* stale dependencies installed from an unpushed `requirements.txt`;
* CI did not trigger because of a branch filter mismatch;
* data was absent after the final reboot because a volume had been reset during an earlier exploratory step.

### Key conceptual shift

```text
Code on my machine
        ↓
Service on a machine I operate
        ↓
Infrastructure I can rebuild from a file
```

And, within that infrastructure:

```text
Image      = definition
Container  = ephemeral execution
Volume     = persistent state
Compose    = declared topology
CI         = independent verification
```

### Calibration: what was and was not demonstrated

**Demonstrated:**

* completing a guided end-to-end deployment;
* verifying persistence through a controlled experiment;
* verifying automatic startup after reboot;
* independently diagnosing branch, dependency, and package failures;
* making and justifying scope decisions.

**Not demonstrated:**

* deploying independently from an empty machine without dialogue;
* operating multiple interacting services;
* reverse proxy, HTTPS, authentication, or secrets management;
* PostgreSQL administration or migration;
* a real backup-and-restore cycle;
* autonomous authorship of a meaningful test suite.

**Important verification caveat:**

The final reboot verified **service recovery**, not **data survival**. The volume had been reset earlier during exploration, so the database was intentionally empty at that point. Persistence itself had been verified in a separate earlier test.

These are two different claims and must not be merged into one.

### Methodology change

The next stage should not add more frameworks.

It should:

* deepen one subsystem at a time (PostgreSQL as its own module);
* increase test depth and connect tests to their actual engineering purpose;
* progressively reduce guidance during operational work;
* preserve the distinction between "it ran" and "I can reproduce and explain it".

---

## Module 12

### PostgreSQL, Async Persistence, Schema Migrations, Multi-Entity Workflows

The student replaced SQLite with PostgreSQL and, in the same effort, replaced the application's data model.

### Context caveat

The retained record begins part-way through the repository migration. The audit, PostgreSQL fundamentals, interface decision, isolated async experiment, and test/CI phases are reported as completed and are presupposed by later work, but are not directly observable here. They are recorded as reported, not as observed.

### Persistence and interface

* PostgreSQL running as a separate Compose service with a named volume;
* SQLAlchemy Core over an async PostgreSQL driver, with SQL and driver-specific records confined to Infrastructure;
* an async call chain traced from endpoint through use case to repository;
* a session-per-request dependency, with a single commit performed at the presentation boundary;
* repositories split by aggregate: equipment, estimate, reservation, picking task.

### Domain model introduced by the student

* equipment types with individual and bulk tracking modes;
* estimates and estimate items carrying price and name snapshots;
* reservations representing committed quantity over a date range;
* picking tasks representing the warehouse's assembly job;
* item allocations binding an estimate line to specific physical units, or to a quantity for bulk stock.

### Workflows implemented

* create estimate, add and remove lines;
* submit for confirmation, with a non-empty check;
* confirm, which verifies availability, creates reservations, creates a picking task, and advances the estimate status;
* cancel, which releases reservations and cancels the picking task;
* accept a picking task, scan individual units or bulk quantities, complete the task;
* issue equipment, which fulfils reservations and marks allocations issued.

### Schema migrations

* Alembic revisions generated inside the running container, inspected, applied, then copied out and committed;
* a `NOT NULL` column added to a populated table, which failed and required a three-step revision;
* a `CHECK` constraint replaced to admit a new status value, which autogenerate does not emit;
* nullable timestamp columns added for issue and return events.

### Failures encountered and diagnosed

* a migration failed with a not-null violation on existing rows; the student correctly proposed making the column nullable, backfilling, then constraining;
* a framework validation error at startup was traced to a response model that did not inherit `BaseModel`;
* a response validation error at request time was traced to a dictionary key that did not match the declared field name;
* a type-checker objection to `rowcount` was resolved by choosing an explicit returning-based count.

### Design decisions made by the student

* availability computed from batched retrieval with the decision made in the use case;
* picking reads live catalog data rather than snapshots, on the grounds that the interval between estimate creation and assembly is short. This is defensible, but it rests on an assumption about catalog stability that should be recorded as an assumption rather than a fact;
* scanning endpoint takes the task identifier plus a scanned code, and the server determines which estimate line it belongs to;
* completion is an explicit operator action, not an automatic consequence of the progress flag, so that additional items can still be added;
* strict completion validation for now, with a forced path deferred behind a confirmation dialog.

### Deliberately deferred

* checking whether a scanned unit is already committed to another active task;
* adding estimate lines after assembly has started, described by the student as a real rental-counter scenario;
* forced completion of partial assembly;
* reminders for stalled tasks;
* the concurrency window between availability check and reservation insert.

### Calibration: what was and was not demonstrated

**Demonstrated:** implementing and correcting multi-table workflows under review; applying migrations to a live database; several genuinely independent design decisions; correctly rejecting flawed mentor proposals.

**Not demonstrated:** authoring a non-trivial migration unaided; independent reading of framework tracebacks; induced-failure rollback verification; concurrency correctness; transfer to an unfamiliar system.

The module's intended architectural test — replacing infrastructure while leaving business logic untouched — was not performed, because both changed together.

### Methodology change

The next stage should:

* name and reuse the retrieval/decision split deliberately rather than rediscovering it under pressure;
* bound multi-entity coordination work by session, not by feature;
* require the student to author non-trivial migrations;
* treat recurring mechanical error classes as a pre-submission checklist rather than a review finding;
* complete the remaining lifecycle (return and close) with reduced guidance.

---

# 6. Current Strengths

The strongest demonstrated areas are currently:

### Conceptual reasoning

The student usually seeks the underlying reason for a design rather than memorizing a rule.

### Application architecture

The student can work with:

* Domain;
* Application;
* Presentation;
* Infrastructure;
* repositories;
* Use Cases;
* dependency injection;
* Application Shell.

### Persistence architecture

The student has practical experience with:

* SQLite;
* relational schemas;
* SQL CRUD;
* repositories;
* transactions;
* Unit of Work;
* Historical Snapshot.

### Testing

The student has practical experience with:

* pytest;
* assertions;
* fixtures;
* `pytest.raises`;
* in-memory fakes;
* API tests;
* TestClient.

The remaining challenge is increasing test depth and independence.

**Module 11 addition:** the student now understands the *role* tests play in a delivery pipeline. This is a motivational and architectural advance, not yet a quantitative improvement in test coverage or test authorship skill.

### HTTP APIs

The student can build and reason about basic FastAPI endpoints and understands that endpoints should translate between HTTP and application-level operations.

### AI-assisted development

The student increasingly treats AI as a tool whose output must be understood and evaluated rather than blindly copied.

This should continue to develop toward independent implementation and code review.

### Deployment and containerization

**Added after Module 11.**

The student can now work with:

* a Dockerfile and its layer ordering;
* `.dockerignore` and build context;
* images, containers, and their different lifecycles;
* named volumes and persistence requirements;
* port mapping and network exposure;
* Docker Compose as declarative infrastructure;
* restart policies and reboot recovery.

This competence was demonstrated on real hardware and was verified through observation, not only through explanation.

### Infrastructure debugging

**Added after Module 11.**

The student demonstrated the ability to:

* read a long package-manager log and identify the actually failing component;
* distinguish a local change from a remote state;
* trace a CI non-trigger to its configuration cause;
* reconnect to a server after reboot and verify service state;
* notice that an expected result was missing and propose a cause.

### Operational judgment

**Added after Module 11.**

The student can now participate in decisions about:

* what belongs in an image versus a volume;
* what belongs in this module versus the next one;
* what is required now versus at commercial scale;
* which verification is sufficient for which claim.

This is emerging judgment, still dependent on dialogue, but no longer purely receptive.

### Persistence and database work

**Added after Module 12.**

The student can now work with:

* PostgreSQL as a separate service reached by Compose service name;
* SQLAlchemy Core query construction, including joins, aggregation, and `RETURNING`;
* an async repository chain with a single transaction boundary at the presentation edge;
* Alembic revision generation, inspection, and application against a live database;
* coordinating writes across several repositories in one operation.

This was demonstrated in a working application, but with review. First drafts consistently required correction, and several error classes recurred across slices. The competence is real and is not yet independent.

### Contract and workflow design

**Added after Module 12.**

The student can reason from an operator's screen backwards to an API contract, and can decompose a multi-stage warehouse process into discrete operations with explicit state transitions before implementation.

This is emerging design ability inside a domain the student authored themselves. It is not yet evidence of design ability in an unfamiliar domain.

---

# 7. Current Gaps

The most important current gaps are:

## Python

* lambda and higher-order functions;
* deeper object/reference model;
* hashing and dictionary/set internals;
* deeper Python runtime knowledge.

## Databases

* systematic SQL depth;
* database internals;
* indexes and query planning;
* PostgreSQL;
* migrations;
* locking and concurrency;
* production database operations.

## Testing

* comprehensive Use Case unit tests;
* multi-repository integration tests;
* transaction/rollback tests;
* broader test isolation;
* testing unfamiliar systems.

## Web development

* authentication;
* authorization;
* security fundamentals;
* API versioning;
* production configuration.

## Deployment

* Linux server environment;
* Docker;
* reverse proxy;
* HTTPS;
* process management;
* logging;
* monitoring;
* backups;
* deployment workflows.

## Independent engineering

The student has demonstrated strong performance in known project contexts.

The next important progression is applying the same reasoning to unfamiliar requirements and codebases with progressively less guidance.

---

## Revision after Module 11

The lists above are retained as the historical gap assessment. The following table records the current state based on new evidence.

| Area                       | Previous status | Current evidence                                  | Remaining gap                                        |
| -------------------------- | --------------- | ------------------------------------------------- | ---------------------------------------------------- |
| Linux server environment   | Unaddressed     | SSH, users, sudo, packages, reboot, service checks | Independent administration of an unfamiliar system   |
| Docker                     | Unaddressed     | Image, container, volume, Compose, restart policy  | Multi-service topology, networking, production hardening |
| Deployment workflows       | Unaddressed     | Git → build → run → verify; CI pipeline            | End-to-end independent deployment without guidance   |
| Process management         | Unaddressed     | Detached containers, restart policies             | systemd, resource limits, health checks              |
| Backups                    | Unaddressed     | Mechanism discussed and understood conceptually   | No implemented backup; no restore drill              |
| Reverse proxy / HTTPS      | Unaddressed     | Not attempted                                     | Entirely open                                        |
| Logging / monitoring       | Unaddressed     | Container logs read and interpreted               | Structured logging, aggregation, alerting            |
| PostgreSQL                 | Unaddressed     | Deliberately deferred by agreement                | Entirely open; next dedicated module                 |
| Testing                    | Shallow         | CI now executes the existing suite automatically  | Suite depth, autonomy of authorship, coverage        |
| Async programming          | Conceptual only | Synchronous driver identified as a real limitation| No applied async database work                       |

### Interpretation

Several items previously listed as gaps are now **partially addressed**, not closed.

The distinction matters:

* the student has seen and operated a mechanism;
* the student cannot yet reproduce it independently under unfamiliar conditions.

### Testing motivation — explicit observation

Module 11 produced an unusually clear self-report:

> the student dislikes writing tests; existing tests were written formally, without understanding their role in a delivery pipeline.

The student now articulates the correct purpose of tests:

* they protect behavior across changes;
* they run independently of the author;
* they serve the future maintainer, including the future self.

This is a genuine conceptual shift. It has not yet produced a larger or deeper suite.

**Agreed approach:**

* keep CI running the existing suite;
* do not impose a coverage threshold while the suite is shallow;
* grow tests incrementally when real change or real risk justifies them;
* do not treat a green badge as evidence of product quality.

### Deployment gaps that remain open

* reverse proxy and TLS termination;
* authentication and authorization;
* secrets management;
* structured logging and observability;
* health checks and monitoring;
* backup and restore drills;
* multi-container networking;
* database migrations and schema versioning;
* zero-downtime or controlled-update deployment.

---

## Revision after Module 12

The Module 11 table above is retained as the historical assessment. The following records movement observed or reported during Module 12.

| Area | Previous status | Current evidence | Remaining gap |
| --- | --- | --- | --- |
| PostgreSQL | Deliberately deferred | Running as a distinct service; application connects and operates against it | Roles and privileges, locking, isolation levels, `EXPLAIN`, administration |
| Migrations | Unaddressed | Revisions generated, inspected, applied on a live server; a failed `NOT NULL` migration repaired; a `CHECK` constraint replaced | Authoring non-trivial revisions independently; downgrade rehearsal; migration testing |
| Async programming | Conceptual only | Full async chain in production code; missing-`await` failures diagnosed | Cancellation, concurrent execution, connection lifecycle under load |
| Transactions | Basic Unit of Work understanding | Multi-repository writes committed once at the presentation boundary | Induced-failure rollback verification; concurrent confirmation race |
| SQL depth | Guided application | Multi-table joins, aggregation, `RETURNING`, batch retrieval | Query planning, indexes, aggregation semantics still error-prone |
| Data modelling | Guided to independent | Designed a multi-table rental domain including snapshots, reservations, and allocations | Normalization judgement under change; constraint design for concurrency |
| Testing | Shallow | No new evidence in the retained context | Suite depth, autonomy, rollback and migration tests |
| Concurrency | Unaddressed | Race condition identified and named | Entirely open; deferred by decision |
| Backup and restore | Conceptual only | Not attempted in the retained context | No dump, no restore drill |

### Interpretation

Several areas moved from unaddressed to operational-with-review. None moved to independent.

Testing is the clearest unchanged gap. The module specification required PostgreSQL integration tests and an isolated CI database; the student reports these phases were covered earlier, but no test artifacts appear in the retained context. This must be verified against the repository before the module is assessed, and must not be assumed in either direction.

---

# 8. Recurring Difficulties

These are recurring implementation difficulties, not fundamental conceptual weaknesses.

---

## 8.1 Syntax and Small Implementation Errors

**Status:** Improving

Examples observed across modules include:

* missing parentheses when calling methods;
* missing `return` statements;
* incorrect SQL syntax;
* incorrect `break` placement;
* occasional tuple/argument mistakes;
* minor path/configuration mistakes.

These errors sometimes interrupt otherwise correct architectural reasoning.

### Action

Continue separating:

```text
Design correctness
        ↓
Implementation correctness
        ↓
Syntax correctness
```

The student should increasingly use tests, linters, IDE diagnostics, and small verification steps to catch these errors independently.

---

## 8.2 SQL Syntax Fluency

**Status:** Developing

The student can now use common SQL operations but still occasionally confuses similar statements.

Examples from Module 08 included confusion between:

```text
INSERT
UPDATE
DELETE
DROP
```

and occasional `fetchone()` / `fetchall()` mistakes.

### Action

Continue systematic SQL practice rather than assuming that practical SQLite exposure equals full SQL fluency.

---

## 8.3 `fetchone()` and `fetchall()` Mental Model

**Status:** Improving

The student understands the distinction but occasionally needs to explicitly reason about the return type.

Preferred mental model:

```text
fetchone()
    ↓
one row or None

fetchall()
    ↓
collection of rows
```

The `None` case should become an automatic part of database code review.

---

## 8.4 Return-Path Completeness

**Status:** Improving

The student has occasionally created functions where one branch does not return the expected value.

### Action

When a function has a meaningful return contract, mentally check:

```text
Can every possible execution path reach a valid return?
```

This is particularly important for Use Cases.

---

## 8.5 Index vs Value

**Status:** Improving

The student has occasionally confused:

```text
list position
```

with:

```text
value stored at that position
```

This appeared in database-driven selection menus.

### Action

Continue using the distinction:

```text
index = position

value = thing stored there
```

and use explicit mappings when user-facing numbers represent database identifiers.

---

## 8.6 Local vs Remote State Synchronization

**Status:** New, observed in Module 11

The student repeatedly encountered a gap between what exists locally and what exists remotely:

* an edited `requirements.txt` was committed or present locally but not pushed, so the server cloned an outdated version;
* a CI workflow was written for one branch while the actual work moved to another.

In both cases the reasoning was correct; the **state assumption** was wrong.

### Action

Before building or deploying, explicitly verify:

```text
Which branch am I on?
What is actually on the remote?
Which revision will the server receive?
```

Useful habits:

* `git status`;
* `git log --oneline`;
* `git remote -v`;
* checking the remote file tree after a push.

This difficulty is procedural, not conceptual, and is highly trainable.

---

## 8.7 Environment Parity Assumptions

**Status:** Improving

The student initially assumed that the server environment would resemble the development machine.

Observed gaps included:

* `pip` not installed;
* no virtual environment;
* no project dependencies;
* a different package set than expected.

By the end of the module the student understood why the container must carry its own environment rather than rely on the host.

### Action

Continue framing deployment as:

```text
Do not assume the target machine.
Declare it.
```

Docker and Compose are the current instruments for that declaration.

---

## 8.8 Reading System-Level Failure Output

**Status:** Improving

During Module 11 the student faced a long `apt`/`dpkg` log in which the requested packages installed successfully but an unrelated pre-existing package failed to configure.

The initial reading was that the installation had failed.

After guidance, the student could identify:

* which packages were actually set up;
* which component failed;
* why an unrelated broken package blocks future operations.

### Action

Teach a consistent reading order for long logs:

```text
What was requested?
What succeeded?
What actually failed?
Is this failure caused by my change or by pre-existing state?
```

This is a transferable operational skill, not a one-off fix.

---

## 8.9 Command and Flag Fluency

**Status:** Improving

The student did not initially recognize:

* `-t`, `-d`, `-p` in Docker commands;
* the two-argument form of `COPY`;
* the module-object syntax used by uvicorn;
* the meaning of `0.0.0.0`.

Each was resolved through explicit explanation rather than memorization.

### Action

Continue Adjustment 002. Never introduce an unexplained flag into an instruction for this student.

---

## 8.10 Missing `await` on Asynchronous Repository Calls

**Status:** Recurring, observed in Module 12

The same omission appeared in several separate slices: an asynchronous repository method called without `await`, producing a coroutine object that was then handed to the response serializer.

The reasoning about the workflow was correct in every case; the failure was mechanical.

### Action

Treat the async boundary as a checklist item rather than a review item:

```text
Is this method async?
        ↓
Is it awaited?
        ↓
Is its caller async?
        ↓
Is that caller awaited?
```

The student should be able to run this check without prompting before submitting a slice.

---

## 8.11 Enum and Database Value Boundary

**Status:** Recurring, observed in Module 12

Reads correctly converted a stored string into an enum; writes sometimes passed the enum object where the stored string was required.

### Action

Name the boundary explicitly and keep it symmetric:

```text
database string  →  Enum(value)   on read
Enum member      →  .value        on write
```

---

## 8.12 Identifier Confusion Across Related Tables

**Status:** New, observed in Module 12, and the most consequential error class in the module

Several distinct failures share one cause — an identifier belonging to one entity used where another was required:

* a primary key column filtered against a list of foreign keys, in two separate repositories;
* an update addressed to the estimate-item table when the estimate table was intended;
* a method named for a task identifier that accepted an estimate identifier;
* a list built to hold item identifiers populated with estimate identifiers instead.

This is the relational form of the difficulty already recorded in 8.5.

### Action

Before writing a `WHERE` clause, state in words which entity the column identifies and which entity the supplied value identifies. If those differ, the query is wrong regardless of whether it executes.

---

## 8.13 `RETURNING` Omitted Before Row Fetch

**Status:** Recurring, observed in Module 12

An `UPDATE` was executed without `.returning()`, after which a row fetch returned nothing and the use case reported a failure that had not occurred.

### Action

Bind the two together as a single habit: if a row will be read back from a write statement, the statement must return it.

---

## 8.14 Response Contract Mismatches

**Status:** New, observed in Module 12

Startup and request-time failures traced to:

* a response model that did not inherit the framework base model, twice;
* a configuration attribute name misspelled, so it was silently ignored;
* a single-object response model declared for a list;
* a returned dictionary key that did not match the declared field name.

The student also asked where in a long validation traceback the actual defect is described, which indicates that framework error output is not yet read independently.

### Action

Teach a fixed reading order for validation errors, mirroring 8.8:

```text
What kind of error is this — request, response, or startup?
        ↓
Which field or model is named?
        ↓
What was expected?
        ↓
What was actually supplied?
        ↓
Which of my two declarations disagrees with the other?
```

---

## 8.15 Aggregation Semantics

**Status:** New, observed in Module 12

Progress calculations were sometimes taken from a single row, or from the length of a collection, where a sum over rows was required. A completeness check inspected record status instead of comparing accumulated quantity against requested quantity.

### Action

Before computing a total, ask explicitly: is the answer one row, a count of rows, or a sum across rows? For bulk equipment in particular, several partial allocations may exist for one estimate line.

---

# 9. Methodology Adjustments

## Adjustment 001 — Mental Models First

**Status:** Active

Every major new concept should begin with a useful mental model before formal terminology.

---

## Adjustment 002 — Introduce New Syntax Explicitly

**Status:** Active

Unknown language features should not appear unexpectedly in exercises.

The student should first understand what a new feature does and why it exists.

---

## Adjustment 003 — Project Integration

**Status:** Active

Major concepts should eventually be connected to a real project.

The connection should be meaningful rather than forced.

---

## Adjustment 004 — Separate Design From Syntax

**Status:** Active

The student often understands architecture before implementation details.

Teaching should allow conceptual design before requiring syntactically perfect code.

---

## Adjustment 005 — Discover Patterns Before Naming Them

**Status:** Active

When practical circumstances allow, the student should first attempt to solve the design problem.

The formal pattern name can then be introduced as vocabulary for an already-understood idea.

---

## Adjustment 006 — Socratic Exploration

**Status:** Active

Complex topics should use questions that encourage the student to derive conclusions rather than simply receiving them.

---

## Adjustment 007 — Teach When Not to Use a Pattern

**Status:** Active

Every significant abstraction should be discussed in terms of:

* benefits;
* costs;
* simpler alternatives;
* appropriate scale;
* signs of overengineering.

---

## Adjustment 008 — Separate Experimental and Production Code

**Status:** Active

Mini-projects are appropriate for exploring patterns that may not yet be justified in the main project.

Real projects should receive abstractions when they solve actual problems.

---

## Adjustment 009 — Calibrated Feedback

**Status:** Active

The mentor should distinguish between:

* correct intuition;
* successful implementation;
* demonstrated competence;
* independent competence;
* broad expertise.

Praise should reinforce concrete evidence rather than use inflated professional labels.

---

## Adjustment 010 — Architecture Through Change

**Status:** Active

Architecture should frequently be taught through questions such as:

> What happens if X changes?

This is more useful for the student than memorizing architectural diagrams.

---

## Adjustment 011 — Domain-Driven Learning

**Status:** Active

When possible, use real domains familiar to the student to make abstract concepts concrete.

The Gaffer Sandbox demonstrated the effectiveness of this approach.

---

## Adjustment 012 — Testing as an Engineering Tool

**Status:** Active

Testing should not be treated as a separate topic that happens after programming.

Tests should increasingly be used to:

* specify behavior;
* detect regressions;
* validate architectural boundaries;
* support refactoring;
* investigate failures.

---

## Adjustment 013 — Increase Independence Gradually

**Status:** Active

As concepts become familiar, guidance should decrease.

The intended progression is:

```text
Explanation
    ↓
Guided implementation
    ↓
Partial guidance
    ↓
Independent implementation
    ↓
Independent design
```

---

## Adjustment 014 — AI as Assistant, Not Substitute

**Status:** Active

When the educational goal is implementation skill, the mentor should avoid unnecessarily providing complete solutions.

The student should be encouraged to:

* reason first;
* write code;
* encounter errors;
* debug;
* compare alternatives;
* explain AI-generated code when AI assistance is used.

---

## Adjustment 015 — One Subsystem at a Time

**Status:** Active, added after Module 11

Infrastructure work must not become an excuse for an application rewrite.

When the student proposes simultaneous changes to code architecture and deployment architecture, separate them into distinct stages with a verified working state between them.

Module 11 demonstrated the value of this constraint: the existing application was containerized without modification, which made every failure attributable to infrastructure rather than to a rewrite.

---

## Adjustment 016 — Establish a Baseline Before Containerizing

**Status:** Active, added after Module 11

Before packaging an application, verify that it runs in a plain environment on the target machine.

This separates two questions that are otherwise conflated:

```text
Does the application work here?
Does the container work?
```

---

## Adjustment 017 — Persistence Must Be Demonstrated, Not Assumed

**Status:** Active, added after Module 11

For any stateful service, require an explicit survival test:

```text
Create data
    ↓
Destroy the container
    ↓
Recreate the container
    ↓
Verify the data
```

Reading an explanation of volumes is not equivalent to observing persistence.

Equally, verify **which claim** a test supports. A reboot test that shows a running service does not prove data survival if the volume was reset beforehand.

---

## Adjustment 018 — Treat Failures as Diagnostic Material

**Status:** Active, added after Module 11

Broken packages, stale remote files, and non-triggering workflows are not interruptions to the lesson. They are the lesson.

The mentor should resist immediately supplying the fix and instead guide the student through:

```text
Observation
    ↓
Hypothesis
    ↓
Verification
    ↓
Repair
    ↓
Re-verification
```

Module 11 produced some of the strongest independent reasoning during exactly these moments.

---

## Adjustment 019 — Separate Build Time From Run Time Explicitly

**Status:** Active, added after Module 11

For infrastructure topics, maintain a visible boundary between:

* what is baked into an artifact;
* what is decided when the artifact is executed.

Confusion between these two layers was a recurring source of questions in Module 11 and was resolved whenever the boundary was named explicitly.

---

## Adjustment 020 — Verify Remote State Before Assuming Deployment Correctness

**Status:** Active, added after Module 11

Before issuing build or deploy instructions, confirm:

* the current branch;
* the remote URL;
* whether local changes have been pushed;
* which revision the target machine will receive.

Two separate Module 11 failures originated from incorrect state assumptions rather than incorrect technical understanding.

---

## Adjustment 021 — Negotiate and Record Scope Explicitly

**Status:** Active, added after Module 11

When a student asks whether a technology belongs in the current module, answer directly.

Then record:

* the decision;
* the reasoning;
* what is deliberately deferred;
* where the deferred work will appear.

Module 11's decisions to defer PostgreSQL and backups were sound and should be preserved as decisions, not forgotten as omissions.

---

## Adjustment 022 — Connect Testing to Its Actual Engineering Purpose

**Status:** Active, added after Module 11

For this student, abstract arguments for testing were insufficient.

The effective reframing was:

```text
A test is a contract with the future maintainer.
CI enforces that contract independently of the author.
```

Continue connecting test authorship to real change and real risk rather than to coverage quotas.

---

## Adjustment 023 — Allow the Student to Decline a Redundant Exercise

**Status:** Active, added after Module 11

When the student demonstrates correct reasoning about a mechanism, an additional confirming drill may add little value.

Module 11 included a justified decision to skip a planned `--build` experiment. This should be treated as evidence of efficiency, not as avoidance.

The mentor should distinguish:

* "I don't want to do the work" — investigate;
* "I already understand this mechanism" — verify the reasoning and move on.

---

## Adjustment 024 — Pace Theory Against demonstrated Readiness

**Status:** Active, added after Module 11

The student signals clearly when a concept has landed and wants to proceed to practice.

Extended Socratic sequences remain valuable for genuinely difficult concepts, but should not be prolonged once the student can already predict the behavior correctly.

---

## Adjustment 025 — Validate the Mentor's Proposal Against Stated Constraints Before Presenting It

**Status:** Active, added after Module 12

Three successive approaches to the availability check were supplied and three were correctly rejected by the student: a per-line query loop, business logic placed inside the repository, and then the per-line loop again after the objection had already been raised.

The cost was approximately two days and visible distress.

Before proposing an approach, verify it against the constraints already established in the conversation — query count, layer responsibility, and the student's stated objections. A rejected constraint must not reappear in the next proposal.

---

## Adjustment 026 — Name the Retrieval / Decision Split Explicitly

**Status:** Active, added after Module 12

The student arrived at the correct structure under pressure:

```text
Repository  →  delivers sets of data, batched
Use Case    →  decides what the data means
```

This should now be named, written down, and reused deliberately rather than rediscovered. It is the concrete form of the repository boundary the student already understands in the abstract.

---

## Adjustment 027 — Bound Complexity by Session, Not by Feature

**Status:** Active, added after Module 12

A use case that coordinates several collections under variable conditions is not one working session. It is a plan with independently verifiable steps and stopping points.

Before implementation of such a slice, agree:

* what data must be retrieved, and in how many queries;
* what will be decided in memory;
* what will be written, and in what order;
* how each step will be checked before the next begins.

Abstraction-heavy work should not be scheduled at night.

---

## Adjustment 028 — Migration Files Are Code, and the Student Should Write Them

**Status:** Active, added after Module 12

Autogenerate produces a draft, not a finished revision. It does not emit constraint replacements, and it does not handle adding a non-null column to a populated table.

When a generated revision is insufficient, the mentor should guide the student to author the upgrade path rather than supply it. In Module 12 the mentor wrote the three-step revision, and the student explicitly recorded this as a missed learning opportunity:

> "Жалко, конечно, что файл миграции я написал не сам, но я зато понял, что файл миграции нужно писать самостоятельно."

The insight landed. The practice did not.

---

## Adjustment 029 — Record Scope Deviations at the Moment They Occur

**Status:** Active, added after Module 12

Adjustment 021 already required explicit scope negotiation. It was not applied when the data model was replaced during a module specified as an adapter swap.

The deviation was reasonable. The absence of a record was not: it removed the module's central architectural test without noting that the test would no longer be run.

When scope changes mid-module, record immediately what evidence is lost and where it will be recovered.

---

## Adjustment 030 — Design the Response Contract Before the Endpoint

**Status:** Active, added after Module 12

The student's strongest API reasoning came from asking what the warehouse operator needs to see after a scan. Make that an explicit step:

```text
What does the operator do next?
        ↓
What must be on screen for them to do it?
        ↓
What is the smallest contract that carries it?
```

This produced a better result than returning either a whole aggregate or a bare record, and it should be applied before writing the endpoint rather than after.

---

# 10. Mentor Notes — Current State

The student has now moved beyond introductory Python and OOP into practical application development.

The most important development is not the number of technologies learned.

It is the change in the student's mental model of software.

The student increasingly sees software as:

```text
Requirements
     ↓
Responsibilities
     ↓
Boundaries
     ↓
Dependencies
     ↓
Data
     ↓
Behavior
     ↓
Interfaces
     ↓
Tests
     ↓
Deployment
```

rather than as a collection of Python files.

At the same time, this development should not be overstated.

The student still needs substantial practice with:

* unfamiliar codebases;
* independent architecture;
* production deployment;
* authentication;
* advanced testing;
* PostgreSQL and database operations;
* real-world operational constraints.

The next phase should therefore focus less on accumulating design patterns and more on **independent application of existing knowledge**.

---

## Revision after Module 11

The deployment node in the diagram above is no longer abstract.

The student has now stood on the other side of it: they have operated a machine, moved code between machines, packaged an application, externalized its state, and observed it recover after a reboot.

This produces a new kind of learning material. From now on, architectural questions can be grounded in operational consequences:

> What happens to this abstraction when it runs inside a container?

> Which layer should own configuration if the environment changes?

> What does this design cost when we need to migrate databases?

> What breaks if two instances share one file?

### Observations about the mentor's own practice

Module 11 also produced evidence about the teaching process itself.

**1. Confirm state before issuing commands.**

The CI branch mismatch and the stale `requirements.txt` were partly enabled by the mentor generating instructions against an assumed branch and an assumed remote state. Future instructions should begin from verified state.

**2. Separate exploration from verification artifacts.**

An exploratory volume reset during the module destroyed the data that would later have served as evidence in the reboot test. Experimental destruction should use a separate, clearly disposable volume so that the primary verification artifact remains intact.

**3. Do not let an example silently define the scope.**

A mentor's illustration can become an implicit commitment. When PostgreSQL was raised, the student rightly asked whether it belonged in this module at all. Scope must be negotiated explicitly.

**4. Accept calibrated refusal.**

The student's decisions to defer PostgreSQL, backups, and coverage thresholds were better reasoned than a default "do everything" approach. The mentor should support such decisions and record their trade-offs rather than pushing for completeness.

**5. Distinguish execution from understanding.**

A running container and a green CI check are weak evidence on their own. The stronger evidence in Module 11 was the student's ability to predict what would happen to data under deletion, and to diagnose why a pipeline did not run.

### Current positioning

The student is an application developer with a first real deployment behind them.

They are not yet an independent operator, and should not be described as one.

The next meaningful progression is not "learn another tool". It is:

```text
Guided deployment
        ↓
Reproducible deployment
        ↓
Independent deployment
        ↓
Independent operational design
```

---

## Revision after Module 12

The persistence node in the student's mental model is no longer a file.

The student has now operated a database server, changed its schema while it held data, coordinated writes across several tables in one transaction, and reasoned about what a warehouse operator needs from an API in order to do their job.

Architectural questions can now be grounded in data consequences as well as operational ones:

> Which entity does this identifier actually identify?

> How many queries will this decision cost?

> What must be atomic here, and what happens if it is not?

> Who owns this decision — the thing that fetches the data, or the thing that interprets it?

### Observations about the mentor's own practice

Module 12 produced uncomfortable but useful evidence about the teaching process.

**1. The mentor's proposals were wrong three times in a row, and the student was right three times.**

The availability check was proposed with a per-line query loop, then with business logic inside the repository, then with the loop again. Each objection came from the student. Future proposals must be checked against constraints already stated in the conversation before being presented.

**2. Supplying the migration removed the learning.**

The three-step revision was written by the mentor. The student noticed and said so. Adjustment 014 was not honoured at the moment it mattered most.

**3. Assessment was generated from retained context instead of from artifacts.**

The mentor reported several module phases as incomplete when they had been completed earlier and the context had been lost. The student had to correct this. An assessment of module completion must begin from repository artifacts and the student's own records, not from what happens to remain in the conversation window.

**4. Complete implementations were supplied repeatedly despite an explicit request not to.**

The student asked for plans, checks, and inputs without code. Several responses still contained full use-case and repository implementations. Where the educational objective is implementation ability, the default should be specification plus review.

**5. Recurring error classes were treated as individual review findings.**

Missing `await`, enum value conversion, omitted `RETURNING`, and identifier confusion each appeared multiple times across separate slices. Reviewing each instance did not stop the next one. These should have been consolidated into a short pre-submission checklist the student applies themselves.

### Current positioning

The student is an application developer who has completed a real database migration and substantially redesigned the application on top of it.

They are not yet an independent implementer. Most slices required correction, several corrections were repeats, and the module's intended test of architectural isolation was not run.

The next meaningful progression is not another technology. It is:

```text
Guided implementation
        ↓
Reviewed implementation
        ↓
Independent implementation in a familiar domain
        ↓
Independent implementation in an unfamiliar domain
```

---

# 11. Emerging Learning Pattern

The student learns most effectively when:

* the problem is realistic;
* the reason for a concept is clear;
* a mental model precedes terminology;
* the student is allowed to reason before receiving the answer;
* implementation follows conceptual understanding;
* mistakes are treated as debugging opportunities;
* the concept is integrated into a project;
* the student is asked when the solution should **not** be used;
* the student can compare alternatives;
* AI assistance does not remove the student's responsibility for understanding.

The student also benefits from revisiting concepts at increasing levels of abstraction.

For example:

```text
Repository
   ↓
Why persistence should be isolated
   ↓
Dependency direction
   ↓
Architecture
   ↓
System boundaries
```

This recursive deepening should remain a central feature of the curriculum.

---

## Additional patterns observed in Module 11

The student learns particularly well when:

* the consequence of a lifecycle event can be predicted before it is demonstrated;
* a familiar model can be transferred to an unfamiliar domain and then explicitly corrected;
* the failure is real rather than simulated;
* the student is allowed to challenge the premise of a question;
* the boundary of the current learning unit is stated explicitly;
* the student can connect a technical decision to a business or career consequence.

A second recursive deepening sequence is now available:

```text
Container
   ↓
Why the environment must be isolated
   ↓
Image versus container
   ↓
Build time versus run time
   ↓
Where state belongs
   ↓
System lifecycle and recovery
```

A third, still emerging:

```text
Test
   ↓
Behavior contract
   ↓
Automated enforcement
   ↓
Independent verification
   ↓
Trust in a delivery process
   ↓
Limits of that trust
```

### A new characteristic of the student's questions

Earlier modules produced questions of the form:

> Where should this responsibility live?

Module 11 added questions of the form:

> What happens to this when the thing that owns it disappears?

And, at the methodological level:

> Why is this topic in this module at all?

Both are signs of progressing from component-level reasoning to system-level and process-level reasoning.

---

## Additional patterns observed in Module 12

The student learns particularly well when:

* the responsibility boundary is settled before implementation begins;
* a proposed approach can be challenged on stated grounds rather than accepted on authority;
* the shape of the data flow is drawn before it is coded;
* a contract is derived from what a real operator needs to see;
* a failure is attributable to a specific layer rather than to the system as a whole.

A fourth recursive deepening sequence is now available:

```text
Table
   ↓
What question does this table answer
   ↓
Which entity owns which decision
   ↓
Where retrieval ends and interpretation begins
   ↓
What must change together
   ↓
What the operator needs to see
```

### A further characteristic of the student's questions

Module 09 produced questions of the form:

> Where should this responsibility live?

Module 11 added:

> What happens to this when the thing that owns it disappears?

Module 12 added:

> Does this belong in the repository or in the use case?

> Why does this endpoint need this identifier at all?

> How many queries will this actually make?

And, directed at the mentor:

> Your proposed solution does not satisfy the constraint I just gave you.

The last form is new. It is the student exercising technical authority over the teaching material rather than only over the learning process. It should be treated as a correctness signal, not as resistance.

---

# 12. Future Development Areas

The next major development areas should include:

1. **Testing depth**

   * Use Case unit testing;
   * integration testing;
   * transaction testing;
   * test isolation.

2. **Database depth**

   * SQL fluency;
   * indexes;
   * query planning;
   * PostgreSQL;
   * migrations;
   * transactions and concurrency.

3. **Web application depth**

   * authentication;
   * authorization;
   * API security;
   * API design.

4. **Deployment**

   * Linux;
   * Docker;
   * reverse proxy;
   * HTTPS;
   * configuration;
   * monitoring.

5. **Independent development**

   * unfamiliar requirements;
   * unfamiliar codebases;
   * architectural trade-offs;
   * implementation with reduced guidance.

6. **AI-assisted engineering**

   * code review of generated code;
   * debugging AI-generated implementations;
   * deciding when AI should and should not be used;
   * maintaining independent technical judgment.

### Status of these areas after Module 11

Area 4 has been partially addressed: Linux fundamentals, Docker, Compose, and a first deployment workflow are now demonstrated.

Still open within area 4:

* reverse proxy;
* HTTPS;
* secrets management;
* monitoring and structured logging;
* backup and restore drills.

Area 2 remains the next major focused effort.

### Status of these areas after Module 12

Area 2 has been substantially addressed, but not closed.

Now demonstrated: PostgreSQL as a service, async persistence through SQLAlchemy Core, multi-repository transactions, Alembic schema evolution against populated tables.

Still open within area 2:

* indexes and query planning;
* locking, isolation levels, and correctness under concurrent requests;
* PostgreSQL roles, privileges, and administration;
* backup and a verified restore drill;
* authoring non-trivial migrations without mentor-supplied code.

Area 1 remains the largest open gap. No new testing evidence appears in the retained context. The module required PostgreSQL integration tests and an isolated CI database; these are reported as completed earlier and must be verified against the repository rather than assumed.

A new area has surfaced and should be tracked explicitly:

**Correctness under concurrency.** The window between checking availability and inserting a reservation is known and was deliberately deferred. It is a real defect at multi-user scale and should not be forgotten as an omission.

Two product-lifecycle items also remain open and were deferred by decision:

* returning issued equipment and closing the estimate;
* adding estimate lines after assembly has begun.

---

## 7. Database migration — next agreed module

**Explicitly deferred from Module 11 by student decision.**

Planned scope:

* PostgreSQL as a second service in a Compose topology;
* Docker networking between application and database;
* connection configuration through environment variables;
* `asyncpg` and genuine async database access;
* connection pooling;
* schema migrations with Alembic;
* transaction behavior and concurrency;
* indexes and query planning;
* PostgreSQL backup and restore (`pg_dump`, recovery procedures);
* replacement of the SQLite infrastructure adapter without rewriting the domain layer.

The last item is a deliberate architectural test: the boundaries established in Modules 07–09 should make this migration possible without touching business logic.

### Status after Module 12

This module was executed, with a recorded scope deviation: the student replaced the data model rather than preserving the domain layer, so the architectural test above was not run as designed. PostgreSQL, Compose networking, environment-based connection configuration, async persistence, pooling, and Alembic migrations were all put into practice. Transaction behavior was demonstrated through multi-step write workflows; concurrency remains open. Indexes, query planning, and backup/restore were not addressed in the retained context.

---

## 8. Operational depth

After the database migration:

* reverse proxy and TLS termination;
* authentication and authorization;
* secrets management;
* structured logging;
* health checks and monitoring;
* scheduled backup with a verified restore procedure;
* controlled application updates.

---

## 9. Testing as a product requirement

Reframe test work from "an exercise I dislike" to "a maintenance asset a buyer will inspect":

* Use Case tests that protect business invariants;
* API contract tests;
* repository and transaction tests;
* migration tests;
* a coverage threshold introduced only once the suite is meaningful.

---

# 13. Long-Term Principle

The purpose of the framework is not to produce a student who can recite a large number of programming concepts.

The desired progression is:

```text
"I know the syntax."

        ↓

"I understand what the code does."

        ↓

"I understand why it is designed this way."

        ↓

"I can modify it safely."

        ↓

"I can design a solution myself."

        ↓

"I can evaluate competing solutions."

        ↓

"I can learn whatever the next problem requires."
```

The student's current position is somewhere in the middle of this progression.

The curriculum should continue moving toward independent problem solving without pretending that the final stages have already been reached.

---

## Position update after Module 11

Module 11 provides the first concrete evidence for the stage:

> "I can modify it safely."

The student containerized a working application without rewriting it, externalized its state, verified persistence, verified recovery, and added an independent verification pipeline.

The following stage remains open:

> "I can design a solution myself."

In the deployment domain this means being able to look at an unfamiliar service and independently decide:

* how it should be packaged;
* where its state belongs;
* how it should be exposed;
* how it should be verified;
* how it should be backed up and recovered;
* what should be deferred and why.

Module 11 moved the student from having never performed these actions to performing them with guidance. The next modules should move them toward performing them without it.

---

## Position update after Module 12

Module 12 strengthens the evidence for:

> "I can modify it safely."

The student changed the persistence mechanism, evolved the schema of a live database, and coordinated multi-table writes without losing data.

It also produces the first partial evidence for:

> "I can design a solution myself."

The workflow decomposition, the operator-facing response contract, the endpoint path decision, and the availability algorithm were the student's own. Each was reached by reasoning about the problem rather than by adapting a supplied example.

That evidence is bounded in three ways, and the bounds matter more than the achievement:

* it was produced inside a domain the student authored themselves;
* it was produced with review, and first drafts contained significant defects;
* the module's designed test of architectural isolation — infrastructure replaced without touching business logic — was not run, because both changed together.

The following stage therefore remains open, and its first concrete test is now available:

> Complete the remaining lifecycle — return and close — without mentor-supplied implementations, and verify rollback behavior with an induced failure rather than by inspection.

Module 12 moved the student from never having changed a database to changing one deliberately. The next module should move them from changing it correctly under review to changing it correctly on their own.

---

*End of Development Log v3.1*