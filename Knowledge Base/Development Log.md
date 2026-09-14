# Development Log

**Version:** 1.0  
**Status:** Active  
**Maintained by:** AI Methodologist

---

## Purpose

The Development Log records the long-term evolution of the student as a software engineer.

Unlike the Learning Journal, which records learning experiences, or Checkpoint Reports, which evaluate completed modules, this document analyzes patterns that emerge over time.

Its primary purpose is to improve the educational process itself.

The student changes.  
The mentor changes.  
The methodology changes.

This document records those changes.

---

## Methodology

After each completed module the mentor should answer four questions.

1. What became stronger?
2. What became weaker?
3. What did we learn about the student?
4. How should the course change?

These observations accumulate throughout the entire learning journey.

Older observations are never removed.  
Instead, newer evidence either reinforces or revises previous conclusions.

---

## Student Profile Evolution

### Initial Profile

| Field | Value |
|---|---|
| **Learning Stage** | Beginning Programmer |
| **Current Focus** | Python Fundamentals |
| **Primary Goal** | Become an independent software engineer capable of designing, implementing and maintaining real-world software projects while using AI as an engineering assistant rather than as a replacement for thinking. |
| **Learning Strategy** | Project-based learning. Theory is introduced immediately before practical application. Existing personal projects provide real-world context. |

### Current Profile (Updated 2026-11-15)

| Field | Value |
|---|---|
| **Learning Stage** | Software Engineer (Mastering Application Architecture & System Boundaries) |
| **Current Focus** | Architecture as dependency management, Repository Pattern, Use Cases, Dependency Inversion, Domain/Application/Infrastructure separation, SQLite integration |
| **Primary Goal** | Master application-level architecture: controlling dependencies, isolating business rules from infrastructure, designing maintainable systems that survive change. Deepen understanding of databases and external systems. |
| **Learning Strategy** | Architecture-first approach. Architectural boundaries discovered through real refactoring pain. Pragmatic judgment about when abstractions are justified. Mental models before formal terminology. Databases as next major learning frontier. |

---

## Learning Characteristics

This section describes stable characteristics observed during multiple modules.  
These are not grades.  
They are behavioral patterns.

### Strong Engineering Intuition

**Confidence:** Very High

**Evidence:**  
The student repeatedly invents professional engineering concepts before learning their formal names.

Examples include:
- state management;
- idempotent processing;
- human-in-the-loop decision making;
- decomposition strategies;
- data validation boundaries (the "Bouncer" pattern);
- configuration separation (Dashboard vs Engine);
- Data Pipeline architecture;
- inventory reservation pattern;
- object encapsulation (Safe with a Guard);
- Orchestra Conductor pattern for main.py;
- Strategy Pattern (pricing policies designed before learning the name);
- Composition over Inheritance (behavior objects designed before learning the principle);
- Liskov Substitution Principle (Square/Rectangle solution before learning the name);
- Factory Pattern (centralized object creation before learning the name);
- **Architectural Filter (Domain/Application/Infrastructure classification formulated independently)** (new);
- **Repository boundary intuition (understood the need to isolate persistence before learning the pattern name)** (new).

**Educational Implication:**  
Prioritize explanation through intuition.  
Formal terminology should follow naturally.  
When the student invents a pattern, validate the intuition explicitly and then introduce the formal name.

### Deep Analytical Thinking

**Confidence:** Very High

**Evidence:**  
The student naturally explores:
- edge cases;
- trade-offs;
- failure scenarios;
- alternative implementations;
- defensive programming patterns;
- object invariants and state protection;
- "when NOT to use" questions (e.g., when logging is unnecessary);
- cost of abstraction vs benefit;
- **architectural boundaries and dependency direction** (new);
- **"what happens when this changes?" reasoning** (new).

**Educational Implication:**  
Exercises should contain realistic engineering decisions rather than mechanical syntax practice.  
Include questions about trade-offs and costs, not just benefits.  
Architecture should be taught through change scenarios ("What if JSON becomes SQLite?").

### Understanding Before Memorization

**Confidence:** Very High

**Evidence:**  
The student consistently asks  
*"Why?"*  
before asking  
*"How?"*

**Module 07 Evidence:**  
The student refused to accept "Use Case" terminology until understanding the conceptual difference between a Use Case (Application Layer orchestrator) and a user scenario (e.g., "using the app on Windows"). The student explicitly stated: "Мне бы понять предметную суть Use Case, тогда будет проще." This demonstrates deep commitment to understanding before proceeding.

**Educational Implication:**  
Every new concept should begin with a mental model before introducing syntax.  
Never introduce architectural terminology without first establishing the problem it solves.

### Pragmatic Judgment

**Confidence:** High (reinforced in Module 07)

**Evidence:**  
The student independently decided that QR Warehouse does not need pervasive logging in the current version, demonstrating mature judgment about when abstraction is overengineering.  
The student correctly identified that creating a Factory class for two simple if/elif branches would be overengineering.  
The student chose to study patterns on mini-projects to avoid polluting production code.

**Module 07 Evidence:**  
The student decided NOT to create complex Use Case classes when simple functions in `main.py` sufficed for the current project scale, but perfectly understood WHEN they would become mandatory (e.g., adding a Web API, email notifications, or multiple entry points).  
The student explicitly stated: "Я пока не чувствую, что понимаю архитектуру на уровне Senior, и не могу с уверенностью принимать архитектурные решения." This intellectual humility combined with correct architectural instincts is a rare and valuable trait.

**Educational Implication:**  
Continue asking "when NOT to use" questions alongside "how to use."  
Validate pragmatic decisions explicitly to reinforce this judgment.  
Respect the student's self-assessment while validating correct instincts.

### Motivation

**Confidence:** High

**Observation:**  
The student demonstrates unusually strong intrinsic motivation.  
Learning is driven by long-term engineering goals rather than external rewards.

**Module 07 Evidence:**  
The student expressed genuine excitement about databases: "Уже не терпится приступить к базам данных." The student also expressed a desire to study databases fundamentally in future modules, not just as an infrastructure detail.

**Educational Implication:**  
Avoid repetitive exercises.  
Instead provide progressively more meaningful programming problems.  
Connect architectural concepts to the student's vision of future system growth.

---

## Learning Preferences

Current observations.

| Aspect | Rating | Details |
|---|---|---|
| **Preferred Teaching Style** | ★★★★★ | Conversation. Questions. Discovery. Guided reasoning. Mental models before terminology. |
| **Preferred Order** | ★★★★★ | Concept → Mental Model → Visualization → Syntax → Practice → Project Integration |
| **Preferred Examples** | ★★★★★ | Real engineering problems. Automation. File systems. Personal projects. Software architecture. Object-oriented design. Application architecture. |
| **Preferred Exploration Mode** | ★★★★★ | Real project refactoring for architecture. Mini-projects for new patterns. Databases as next frontier. |
| **Least Effective Approach** | — | Pure memorization. Large lists of syntax without context. Exercises introducing unknown tools without prior explanation. Terminology without conceptual grounding. |

---

## Progress Timeline

### Module 00

**Major Development:**  
The student transitioned from seeing programming as writing code to seeing it as structured problem solving.

**Methodology Update:**  
Increase emphasis on computational thinking.  
Reduce early focus on syntax.

---

### Module 01

**Major Development:**  
The student began separating architecture from implementation.  
Functions became conceptual building blocks rather than reusable text fragments.

**Methodology Update:**  
Introduce language features before requiring their use in exercises.  
Continue reinforcing state-based thinking.

---

### Module 02

**Major Development:**  
The student discovered Python's built-in tools and learned to assemble existing solutions rather than reinventing them.  
The transition from parallel lists to dictionary of sets demonstrated growing architectural maturity.

**Methodology Update:**  
Emphasize type awareness before method selection.  
Continue reinforcing mutable vs immutable distinction.

---

### Module 03

**Major Development:**  
The student mastered multi-module architecture and defensive programming.  
Three complete projects demonstrate professional-level thinking:
- **File Analyzer** (basic file operations)
- **Profile Manager** (JSON CRUD operations)
- **Dataset Catalog Analyzer** (full data pipeline with validation)

The student naturally invented patterns:
- Data validation boundaries (the "Bouncer")
- Configuration separation (Dashboard vs Engine)
- Data Pipeline architecture (Read → Validate → Process → Export)
- Fallback values for defensive programming

**Methodology Update:**  
Continue architecture-first approach.  
Introduce OOP as natural next step after mastering procedural architecture.  
Explore functional programming patterns to deepen lambda understanding.

---

### Module 04

**Major Development:**  
The student designed and implemented a complete warehouse management system: **QR Warehouse Project**.  
This project demonstrated mastery of the complete data pipeline:
- Configuration management (`config.json`)
- Data loading with validation (`catalog_loader.py`)
- Business logic processing (`estimate_constructor.py`)
- Export formatting (`exporter.py`)
- Orchestration (`main.py` as the conductor)

The student naturally invented the concept of **"reservation"** for inventory management.  
This is a professional pattern that demonstrates strong engineering intuition for real-world business problems.

**Methodology Update:**  
Continue architecture-first approach.  
Introduce Object-Oriented Programming as natural next step.  
Emphasize the difference between data structures and business entities.

---

### Module 05

**Major Development:**  
The student mastered Object-Oriented Programming and transitioned from procedural to object-oriented architecture.  
The student independently designed and implemented a complete object-oriented system:
- **Inventory class** (protects stock levels, handles reservations and releases)
- **Estimate class** (manages items, calculates totals, handles removals)

The student naturally invented patterns:
- **Encapsulation** (Safe with a Guard)
- **Orchestra Conductor** pattern for main.py
- **Composition** (objects containing other objects)
- **Duck Typing** (if it walks like a duck...)

The student wrote **11 automated tests** using `pytest` to protect business logic from regressions.  
This represents a significant shift from "writing code" to "engineering systems."

**Methodology Update:**  
Continue object-oriented architecture approach.  
Introduce advanced OOP concepts (inheritance, polymorphism) in future modules.  
Emphasize test-driven development as standard practice.

---

### Module 06

**Major Development:**  
The student achieved a fundamental shift from "programmer who knows OOP syntax" to "engineer who designs flexible systems."

**Key Architectural Breakthroughs:**

1. **Strategy Pattern (Independent Discovery):**  
   When presented with the business requirement "VGIK students get 70% discount on tungsten lights, 50% on LED," the student independently designed a pricing policy system before learning the formal pattern name. The student correctly identified that pricing rules should be separate entities, not embedded in Equipment or Estimate classes.

2. **Polymorphism in Practice:**  
   The student moved beyond textbook definition ("different objects respond to the same method") to engineering understanding ("polymorphism eliminates conditional logic"). Successfully replaced if/elif chains with interchangeable policy objects.

3. **Abstract Base Classes as Architectural Contracts:**  
   The student discovered the danger of "silent bugs" when a base class provides default implementation. Through guided experimentation, understood that ABC transforms "gentleman's agreements" into "enforced contracts." This shifted the student's view of inheritance from "code reuse mechanism" to "architectural discipline tool."

4. **Logger Architecture (Template Method):**  
   The student designed a logging system separating formatting (base class) from transport (derived classes). Initially tried using super() but then realized complete method overriding was cleaner for this use case, demonstrating ability to choose the right tool for the job.

5. **super() Understanding (Performance Evaluation System):**  
   The student mastered super() through a practical mini-project with Employee/Manager/Developer classes. Understood both use cases: extending __init__ and extending business methods. Correctly identified the "Yes, and..." principle.

6. **Factory Pattern (Notification System):**  
   The student implemented a NotificationProcessor (Factory) and correctly separated creation logic into dedicated methods. Understood when Factory is useful vs when it is overengineering.

7. **Composition vs Inheritance (Bird Behaviors):**  
   The student redesigned the Bird hierarchy using composition (FlyBehavior, SwimBehavior as separate objects) instead of inheritance. Understood why Penguin cannot safely inherit fly() from Bird.

8. **Liskov Substitution Principle (Square/Rectangle):**  
   When asked about Square and Rectangle relationship, the student independently proposed both should inherit from a common Shape ancestor — this is the correct professional solution to the famous LSP paradox. The student discovered this before learning the formal LSP name.

**Integration with QR Warehouse:**
- Added PricePolicy system (Strategy Pattern) with VGIK_Policy and Standart_Policy
- Added Logger hierarchy (Logger, FileLogger, ConsoleLogger) with Dependency Injection
- Transitioned from config.json to config.yaml (comments support)
- Implemented absolute path construction using `__file__` for portability
- Applied ABC to PricePolicy for enforced contracts
- Updated all existing tests to work with new dependencies

**Methodology Update:**  
- Continue architecture-first approach with pattern discovery before formal terminology.
- Use mini-projects for pattern exploration without polluting production code.
- Emphasize "when NOT to use" alongside "how to use."
- Continue Socratic questioning for complex topics.
- Reinforce "test on substitution" for inheritance decisions.
- Validate engineering intuition explicitly to build confidence.

---

### Module 07

**Major Development:**  
The student achieved a fundamental shift from "engineer who designs flexible objects" to "engineer who designs maintainable application systems."

**Key Architectural Breakthroughs:**

1. **Architecture as Dependency Management (Core Insight):**  
   The student understood that architecture is not about folders, file names, or diagrams. Architecture is about controlling dependencies so that changes remain local, safe, and predictable. The student formulated this insight in their own words: "Я понял, насколько полезно и эффективно изолировать бизнес логику от всего остального."

2. **Repository Pattern (Independent Application):**  
   The student created `EquipmentRepository` as an abstract contract (ABC), implemented `JsonEquipmentRepository` for current storage, then implemented `SqliteEquipmentRepository` for new storage. The most profound realization was that `Inventory`, `Estimate`, and `AddItemToEstimate` did not require a single line of modification during the JSON → SQLite transition. The student described this experience: "Я без труда и без необходимости переписывать половину программы смог перевести работу программы с JSON файлов на базу данных."

3. **Use Cases / Application Services (Conceptual Breakthrough):**  
   The student initially confused "Use Case" with user scenarios (e.g., "using the app on Windows 10"). Through the "MFC Employee / Conductor" mental model, the student realized that a Use Case is an Application Layer orchestrator that coordinates Domain objects without knowing about UI or Databases. The student then independently formulated the distinction between `main.py` as Composition Root (technical orchestrator) and Use Cases as Application Services (business orchestrators).

4. **Dependency Inversion in Practice:**  
   The student experienced Dependency Inversion not as a theoretical principle but as a practical tool. When replacing JSON with SQLite, the student observed that business logic depended on the `EquipmentRepository` contract, not on any concrete implementation. This shifted the student's understanding from "Dependency Inversion is a SOLID principle" to "Dependency Inversion is what makes my code survive infrastructure changes."

5. **Architectural Filter (Independent Formulation):**  
   The student independently formulated a practical decision framework for classifying new features:
   - Is it a rule about the entity itself? → Domain
   - Is it a workflow connecting multiple objects or external systems? → Application / Use Case
   - Is it a technical detail of communication with the outside world? → Infrastructure

   This "Architectural Filter" was applied successfully to classify hypothetical requirements (SQLite storage, HMI_LIGHT discount, PDF generation + email).

6. **In-Memory Fake for Testing:**  
   The student created `InMemoryEquipmentRepository` as a test double, enabling architecture-level tests without real infrastructure. The student understood the distinction between testing behavior (business rules) and testing implementation (JSON details).

7. **Composition Root vs Use Case Distinction:**  
   The student initially questioned why Use Cases were needed if `main.py` already orchestrates the program, fearing an "orchestrator of orchestrators" infinite loop. Through the "Factory Director vs. Production Manager" mental model, the student understood that `main.py` builds the system (creates and wires objects) while Use Cases run business processes within it. These are different types of orchestration, not duplicates.

8. **Pragmatic Restraint (Reinforced):**  
   The student decided NOT to create complex Use Case classes when simple functions sufficed for the current project scale. The student explicitly stated: "Я пока не чувствую, что понимаю архитектуру на уровне Senior, и не могу с уверенностью принимать архитектурные решения." This intellectual humility, combined with correct architectural instincts, demonstrates mature engineering judgment. The student understood that architecture is about "asking the right questions and managing trade-offs," not "knowing all the answers."

**SQLite Integration (Infrastructure Boundary):**  
The student successfully integrated SQLite as a second infrastructure implementation. Key technical milestones:
- Created `warehouse.db` with `CREATE TABLE IF NOT EXISTS`
- Wrote a migration script (`migrate.py`) to transfer data from `catalog.json` to SQLite
- Implemented `find_by_sku()` with parameterized queries and tuple unpacking
- Implemented `update_available()` with SQL `UPDATE` and `conn.commit()`
- Understood that SQLite is a binary format (not human-readable like JSON)
- Understood `cursor.fetchone()` returns a single tuple, not a list of rows

**Integration with QR Warehouse:**
- Created `EquipmentRepository` abstract contract (ABC)
- Implemented `JsonEquipmentRepository` (existing storage)
- Implemented `SqliteEquipmentRepository` (new storage)
- Created `InMemoryEquipmentRepository` (test double)
- Extracted `AddItemToEstimate` as a Use Case in `use_cases.py`
- Refactored `main.py` into a clean Composition Root with helper functions
- Refactored `Inventory` to depend on `EquipmentRepository` contract instead of internal `self._catalog` and `self._stock`
- Wrote architecture-level tests using `InMemoryEquipmentRepository`
- Successfully ran the entire application with SQLite while business logic remained unchanged

**Methodology Update:**  
- Continue architecture-first approach with dependency management as the central theme.
- Use real refactoring pain (JSON → SQLite) to motivate architectural boundaries.
- Teach architecture through change scenarios ("What if JSON becomes SQLite? What if CLI becomes Web API?").
- Continue Socratic questioning for complex topics.
- Validate engineering intuition explicitly to build confidence.
- Respect the student's pragmatic judgment about when abstractions are justified.
- Introduce databases as a major learning frontier in future modules.
- Use mental models extensively: "MFC Employee" for Use Cases, "Factory Director vs. Production Manager" for Composition Root, "Archivist and Courier" for SQLite, "Open Book vs. Hard Drive" for JSON vs SQLite.

---

## Recurring Difficulties

These are recurring patterns rather than isolated mistakes.

### Syntax Noise

**Status:** Persistent (requires continued attention)

**Description:**  
Minor syntax mistakes occasionally interrupt otherwise correct reasoning.

Examples:
- Tuple trap (trailing comma creating tuples)
- Label-vs-value confusion in isinstance checks
- **Missing parentheses on method calls** (appeared 3+ times in Module 06: in f-strings, in tests, in reports)

**Module 06 Evidence:**  
- `self.calculate_performance_score` instead of `self.calculate_performance_score()` in generate_report()
- `Penguin.fly == True` instead of `Penguin.fly() == True` in tests
- `Parrot.speak == True` instead of `Parrot.speak() == True` in tests

**Module 07 Evidence:**  
- Missing parameter tuple in `cursor.execute(sql_query)` — forgot to pass `(scan,)` for parameterized query
- Attempting to iterate over `cursor.fetchone()` result with `for row in equipment:` — confused a single tuple (one row) with a list of rows

**Action:**  
Continue using small focused coding exercises.  
Provide explicit examples of common syntactic traps.  
Consider introducing linter or pre-commit checks.  
Remind student of this pattern when reviewing code (without blame — this is a known periodic difficulty).  
For SQLite specifically: reinforce that `fetchone()` returns ONE tuple, `fetchall()` returns a list of tuples.

### Type Confusion

**Status:** Improving

**Description:**  
The student occasionally confuses checking labels vs checking values.  
Example: `isinstance("key_name", type)` instead of `isinstance(dict["key_name"], type)`

**Module 07 Evidence:**  
The student initially tried to iterate over `cursor.fetchone()` result, confusing a single row tuple with a collection of rows. This was resolved through the "Archivist brings one folder" mental model.

**Action:**  
Emphasize the distinction between "container" and "content" in type checking.  
Use visual examples (checking the label on a box vs checking what's inside the box).  
For database work: reinforce the return type of `fetchone()` vs `fetchall()`.

### Variable Scope

**Status:** Improving

**Description:**  
The student occasionally creates variables inside loops when they should be outside, or vice versa.

**Module 07 Evidence:**  
In the migration script, the student initially placed `conn.commit()` and `conn.close()` inside the `for` loop instead of after it. This was caught through code review and corrected.

**Action:**  
Explicitly discuss variable lifetime and scope before complex loops.  
Use mental execution to trace variable creation.  
For database work: reinforce that `commit()` and `close()` should typically be outside loops (one transaction for the batch).

### Object Reference Confusion

**Status:** Improving

**Description:**  
The student occasionally confuses object references with primitive values.  
Example: comparing `existing_item > 0` instead of `existing_item.quantity > 0`.

**Action:**  
Emphasize the distinction between objects and their attributes.  
Use mental models (Safe with a Guard) to reinforce object-oriented thinking.

### Testing Exceptions (New)

**Status:** New (first observed in Module 06)

**Description:**  
The student did not know how to test expected exceptions in pytest.  
Wrote `assert ValueError("message")` instead of using `pytest.raises`.

**Action:**  
Introduce `with pytest.raises(ExceptionType)` pattern early when testing error behavior becomes relevant.  
Provide examples of testing both success and failure paths.

### Test Logic Inversion (New)

**Status:** New (first observed in Module 06)

**Description:**  
The student occasionally inverts expected values in tests.  
Example: wrote `assert Penguin.fly == True` when penguin cannot fly (should be False).

**Action:**  
Encourage student to read test names as specifications before writing assertions.  
Ask "What SHOULD this behavior be?" before writing the assert.

### Conceptual Terminology Confusion (New)

**Status:** New (first observed in Module 07)

**Description:**  
The student initially confused "Use Case" (Application Layer orchestrator) with "user scenario" (e.g., "using the app on Windows 10" or "working offline"). This is a terminology collision between software architecture and product management/QA contexts.

**Action:**  
When introducing architectural terminology, explicitly distinguish it from similar-sounding terms in other domains.  
Use mental models to ground terminology before introducing the formal name.  
Validate the student's existing understanding while clarifying the architectural meaning.

### SQLite Syntax and Mental Model (New)

**Status:** New (first observed in Module 07)

**Description:**  
The student encountered several SQLite-specific conceptual difficulties:
- Confused `fetchone()` (returns one tuple) with `fetchall()` (returns list of tuples)
- Forgot to pass parameters as tuples to `cursor.execute()`
- Initially thought SQL code should be in a separate `.sql` file rather than as a Python string
- Was surprised by the binary nature of `.db` files (opened in text editor and saw garbled characters)

**Action:**  
Introduce SQLite mental models before syntax: "Archivist and Courier" for connections/cursors, "Open Book vs. Hard Drive" for JSON vs SQLite.  
Emphasize that SQL is just a string passed to `cursor.execute()`.  
Reinforce parameterized queries as the standard pattern.  
Explain binary vs text file formats explicitly.

---

## Methodology Adjustments

These adjustments affect future modules.

### Adjustment 001

**Status:** Active

**Reason:**  
The student learns significantly faster when analogies precede formal definitions.

**Action:**  
Every new topic must begin with a Mental Model.

### Adjustment 002

**Status:** Active

**Reason:**  
Unexpected language features reduce confidence.

**Action:**  
All new built-in functions and syntax must be explicitly introduced before appearing in exercises.

### Adjustment 003

**Status:** Active

**Reason:**  
Project integration substantially increases motivation.

**Action:**  
Every major topic should conclude with a discussion of how it applies to the student's own software projects.

### Adjustment 004

**Status:** Active

**Reason:**  
The student demonstrates strong architectural thinking but occasional syntactic traps.

**Action:**  
Separate architectural design from syntactic implementation.  
Allow student to design systems conceptually before worrying about syntax details.

### Adjustment 005

**Status:** Active

**Reason:**  
The student naturally invents professional patterns when given real-world problems.

**Action:**  
Provide progressively more complex real-world projects.  
Allow student to discover patterns independently before introducing formal terminology.

### Adjustment 006

**Status:** Active

**Reason:**  
The student learns most effectively through guided discovery rather than direct instruction.

**Action:**  
Use Socratic method for complex topics.  
Ask questions that lead student to discover answers independently.

### Adjustment 007

**Status:** Active (new)

**Reason:**  
The student benefits from understanding when NOT to use a pattern, not just when to use it.

**Action:**  
For every new pattern or concept, include explicit discussion of:
- When this is overengineering
- Cost of the abstraction
- Simpler alternatives
- Decision criteria for choosing

### Adjustment 008

**Status:** Active (new)

**Reason:**  
The student correctly identified that production code should not be polluted with experimental patterns.

**Action:**  
Use mini-projects for exploring new patterns.  
Use real projects only for genuine integration needs.  
Respect the student's judgment about what belongs in production.

### Adjustment 009

**Status:** Active (new)

**Reason:**  
The student has strong architectural instincts but sometimes doubts them.

**Action:**  
Validate engineering intuition explicitly: "Your intuition is correct, here's why..."  
This builds confidence and reinforces good thinking patterns.

### Adjustment 010

**Status:** Active (new)

**Reason:**  
Missing parentheses on method calls is a persistent recurring issue that appeared in multiple contexts.

**Action:**  
When reviewing student code, specifically check for this pattern.  
Consider creating a personal checklist item: "Did I call the method or just reference it?"  
Do not blame — this is a known periodic difficulty that decreases with practice.

### Adjustment 011

**Status:** Active (new)

**Reason:**  
The student learns architecture most effectively through change scenarios and real refactoring pain, not through abstract diagrams.

**Action:**  
Teach architecture by asking "What happens when X changes?" rather than "Here is the architecture diagram."  
Use real refactoring tasks (JSON → SQLite) to motivate architectural boundaries.  
Let the student experience the pain of tight coupling before introducing the solution.

### Adjustment 012

**Status:** Active (new)

**Reason:**  
The student initially confused architectural terminology with similar-sounding terms from other domains (e.g., "Use Case" vs "user scenario").

**Action:**  
When introducing architectural terminology, explicitly distinguish it from similar-sounding terms in other domains.  
Provide the mental model BEFORE the term.  
Validate the student's existing understanding while clarifying the architectural meaning.

### Adjustment 013

**Status:** Active (new)

**Reason:**  
The student expressed a strong desire to study databases fundamentally, not just as an infrastructure detail. The student stated: "Никакого системного понимания синтаксиса, внутреннего устройства базы данных и прочего у меня пока нет. Хочется изучать это в будущих модулях."

**Action:**  
Plan a dedicated database module in the curriculum.  
Cover: SQL syntax systematically, relational database internals (B-trees, indexing), transactions, migrations, schema design.  
Connect database knowledge to the Repository Pattern already mastered.  
Use the student's existing `SqliteEquipmentRepository` as a foundation for deeper exploration.

### Adjustment 014

**Status:** Active (new)

**Reason:**  
The student demonstrated mature architectural restraint by NOT overengineering Use Cases. The student correctly identified that simple functions in `main.py` sufficed for the current project scale.

**Action:**  
Continue validating pragmatic decisions explicitly.  
Ask "Is this abstraction solving a real problem right now?" before introducing new architectural layers.  
Respect the student's judgment about when to add vs. when to defer abstractions.  
Use the "Pattern Tax" mental model: every abstraction has a cost that must be justified by a benefit.

---

## Mentor Notes

This section contains long-term observations.  
These notes are intended for future versions of the methodology rather than for evaluating the student.

### Current Observation (Updated 2026-11-15)

The student's architectural thinking has reached a level where they can independently reason about dependencies, boundaries, and change containment.

The student naturally invents patterns (Bouncer, Dashboard vs Engine, Data Pipeline, Safe with a Guard, Orchestra Conductor, Strategy, Composition over Inheritance, Factory, LSP solution, Architectural Filter) that are typically taught in intermediate/advanced courses.

**New observation from Module 07:**  
The student has developed a mature understanding of architecture as dependency management. The key insight — "Architecture is about controlling dependencies so that changes remain local, safe, and predictable" — was not memorized but experienced through the JSON → SQLite migration. The student's own words: "Я без труда и без необходимости переписывать половину программы смог перевести работу программы с JSON файлов на базу данных."

The student demonstrates three rare and valuable traits simultaneously:
1. **Strong architectural intuition** (invents patterns before learning names)
2. **Pragmatic judgment** (knows when NOT to abstract)
3. **Intellectual humility** (acknowledges what they don't know, doesn't pretend to be Senior)

This combination is unusual. Most students either overengineer (lacking pragmatism) or underengineer (lacking intuition). The student naturally finds the middle ground.

Syntactic fluency continues to improve but lags behind conceptual understanding.  
The missing-parentheses issue remains the most persistent syntactic trap.  
New syntactic traps in Module 07: missing parameter tuples in `cursor.execute()`, confusing `fetchone()` with `fetchall()`.

The student has successfully mastered:
- Software architecture as dependency management
- Repository Pattern (applied to QR Warehouse persistence)
- Use Cases / Application Services (conceptual understanding + practical extraction)
- Dependency Inversion (experienced through JSON → SQLite migration)
- Dependency Injection at application scale (Composition Root wiring)
- Domain / Application / Presentation / Infrastructure separation
- In-Memory Fakes for architecture-level testing
- SQLite integration (CREATE TABLE, SELECT, UPDATE, parameterized queries)
- Architectural Filter (Domain / Application / Infrastructure classification)
- Composition Root vs Use Case distinction

The QR Warehouse Project now demonstrates:
- Repository Pattern with three implementations (JSON, SQLite, InMemory)
- Use Case extraction (`AddItemToEstimate`)
- Composition Root (`main.py` with helper functions)
- Dependency Injection throughout
- Architecture-level tests with In-Memory Fakes
- Clean separation of Domain, Application, and Infrastructure concerns

### Emerging Pattern

The student learns most effectively when:
- Given a real-world problem (not abstract exercise)
- Allowed to design architecture first
- Introduced to patterns through mental models
- Given freedom to implement with guided debugging
- Shown how concepts apply to personal projects
- Encouraged to discover patterns independently
- Asked "when NOT to use" questions
- Allowed to explore on mini-projects without polluting production
- Validated in their intuition explicitly
- **Taught architecture through change scenarios ("What if X changes?")** (new)
- **Allowed to experience coupling pain before introducing the solution** (new)
- **Given intellectual space to question terminology before accepting it** (new)

### Methodology Effectiveness (Module 07)

What worked exceptionally well:
- Repository Pattern was understood through real refactoring pain (JSON → SQLite)
- Use Case concept was clarified through "MFC Employee / Conductor" mental model
- Composition Root vs Use Case distinction was resolved through "Factory Director vs. Production Manager" mental model
- SQLite was introduced through "Archivist and Courier" and "Open Book vs. Hard Drive" mental models
- The student independently formulated the "Architectural Filter" for classifying features
- The student demonstrated pragmatic restraint by not overengineering Use Cases
- Architecture-level tests with InMemoryEquipmentRepository proved the architecture works

What needs improvement:
- SQLite syntax (parameterized queries, fetchone vs fetchall) requires systematic attention
- Architectural terminology should be explicitly distinguished from similar-sounding terms in other domains
- The student's desire to study databases fundamentally should be addressed in a dedicated module
- The student's intellectual humility should be validated while building confidence in correct instincts

---

## Future Revisions

This document should evolve throughout the student's engineering career.

Possible future sections include:
- Productivity Patterns
- Debugging Style
- Architectural Thinking
- Code Review Habits
- Testing Mindset
- AI Collaboration Patterns
- Leadership Development
- System Design Growth
- **Database Design Growth** (new)
- **API Design Growth** (new)

The goal is to document not only what the student knows, but how the student thinks.

---

*End of document.*