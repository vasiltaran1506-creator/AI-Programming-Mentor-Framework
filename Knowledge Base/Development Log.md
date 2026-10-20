# Development Log

**Version:** 3.0
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

*End of Development Log v3.0*