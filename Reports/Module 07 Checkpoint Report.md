# Checkpoint Report

**Framework:** AI Programming Mentor Framework (APMF)

**Version:** 0.1 Alpha

**Status:** Active

---

# 1. General Information

```text
Student: Vasily
Date: 2026-11-15
Checkpoint: Module 07 — Application Architecture & Software Design
Module / Stage: Stage 2 — Python Application Foundations / Architecture Transition
Teacher: AI Programming Mentor (Qwen)
```

---

# 2. Summary

The student completed Module 07 with a significant conceptual breakthrough: the transition from "engineer who designs flexible objects" to "engineer who designs maintainable application systems."

**Major achievements:**

* The student independently experienced Dependency Inversion through a real JSON → SQLite migration. The core business logic (`Inventory`, `Estimate`, `AddItemToEstimate`) remained completely unchanged during the storage replacement.
* The student independently formulated the "Architectural Filter" — a practical decision framework for classifying new features into Domain, Application, or Infrastructure.
* The student demonstrated mature pragmatic restraint by refusing to overengineer Use Cases when simple functions sufficed for the current project scale.
* The student successfully created three implementations of the Repository contract (JSON, SQLite, InMemory), proving the architecture works.

**Current challenges:**

* The student expressed intellectual humility regarding architectural decisions: "Я пока не чувствую, что понимаю архитектуру на уровне Senior." This is a healthy self-assessment but requires continued confidence building.
* SQLite syntax and database internals remain poorly understood. The student used SQLite as an infrastructure black box but explicitly stated desire to study databases fundamentally.
* The initial confusion between "Use Case" (Application Layer orchestrator) and "user scenario" (product management concept) required significant clarification.

**General recommendation:**

Continue architecture-first approach. Introduce a dedicated database module as the next major learning frontier. Continue validating the student's architectural instincts while building confidence through practical application.

---

# 3. Completed Learning Areas

```text
Completed:

- Software architecture as dependency management (not file organization)
- Architecture visibility through change scenarios ("What if JSON becomes SQLite?")
- Separation of Concerns at application scale (Presentation / Application / Domain / Infrastructure)
- Dependency direction reasoning (arrows between components)
- Dependency Inversion (practical, not theoretical)
- Dependency Injection at application scale (Composition Root wiring)
- Repository Pattern (contract + implementations)
- Application Services / Use Cases (conceptual understanding + practical extraction)
- Domain Rules vs Application Workflows distinction
- In-Memory Fakes for architecture-level testing
- Fakes vs Stubs vs Mocks (practical understanding)
- Architectural coupling identification
- Dependency leakage detection
- Incremental architectural refactoring (behavior preserved)
- Trade-offs and abstraction cost evaluation
- Overengineering avoidance (practical demonstration)
- SQLite integration (CREATE TABLE, SELECT, UPDATE, parameterized queries)
- Composition Root vs Use Case distinction
- Architecture debugging methodology
```

---

# 4. Competency Evaluation

```text
Competency:
SD-002 Architecture Basics

Current Level:
Level 3 → Level 4 (Independent Application → Advanced Understanding)

Evidence:
The student independently identified architectural boundaries in the QR Warehouse project, extracted the Repository pattern, created Use Cases, and performed a successful JSON → SQLite migration without touching business logic. The student formulated the "Architectural Filter" independently. The student compared simple, layered, and potentially overengineered designs and chose proportionally.

Confidence:
High

Notes:
The student can design sensible component structures for familiar applications. The transition to Level 4 is demonstrated by the ability to compare architectures and explain trade-offs, but the student has not yet designed architecture for a completely unfamiliar domain independently (Task F from Module 07 assessment). This remains the strongest measure of transfer.
```

```text
Competency:
SE-003 Refactoring

Current Level:
Level 3 — Independent Application

Evidence:
The student performed incremental architectural refactoring of QR Warehouse: extracted Repository from Inventory, extracted Use Case from main.py, replaced JSON with SQLite — all while preserving existing behavior and maintaining passing tests.

Confidence:
High

Notes:
The student demonstrated discipline in making one architectural improvement at a time. Tests were used as safety net during refactoring.
```

```text
Competency:
SD-003 Design Decisions

Current Level:
Level 3 — Independent Application

Evidence:
The student explicitly decided NOT to create complex Use Case classes when simple functions sufficed. The student identified that Factory for two if/elif branches would be overengineering. The student chose to defer database study rather than rushing into unfamiliar territory.

Confidence:
High

Notes:
The student demonstrates the rare ability to choose between adding, keeping, and removing abstractions based on cost and change pressure. This is Architectural Restraint at Level 3-4.
```

```text
Competency:
Dependency Reasoning (Module 07 specific)

Current Level:
Level 3 — Independent Application

Evidence:
The student can deliberately control dependencies using interfaces and injection. The student traced dependency arrows, identified dependency leakage (Inventory storing catalog internally), and designed a better boundary (EquipmentRepository contract). The student explained why Dependency Inversion works in practical terms.

Confidence:
High

Notes:
The student can diagnose dependency direction as a source of maintenance cost. The remaining gap is applying this reasoning to completely unfamiliar domains without mentor guidance.
```

```text
Competency:
Architectural Restraint (Module 07 specific)

Current Level:
Level 3 → Level 4

Evidence:
The student deliberately chose NOT to introduce Use Case classes when unnecessary. The student resisted the temptation to create abstractions "because they look professional." The student asked "Is this abstraction solving a real problem right now?" before introducing new architectural layers.

Confidence:
High

Notes:
This is a rare and valuable trait. Most students either overengineer or underengineer. The student naturally finds the middle ground.
```

---

# 5. Strengths

## Conceptual Understanding

The student demonstrated deep conceptual understanding of architecture as dependency management. The insight "Architecture is about controlling dependencies so that changes remain local, safe, and predictable" was not memorized — it was experienced through the JSON → SQLite migration.

## Engineering Intuition

The student independently invented the "Architectural Filter" (Domain / Application / Infrastructure classification) before being given the formal framework. This continues the pattern from previous modules where the student invents professional patterns before learning their names.

## Pragmatic Judgment

The student demonstrated mature engineering restraint. When the mentor introduced Use Cases, the student correctly identified that creating complex classes was unnecessary for the current project scale but understood WHEN they would become mandatory. This is rare and valuable.

## Problem Solving Through Change

The student learns architecture most effectively through change scenarios. The question "What if JSON becomes SQLite?" motivated the entire Repository extraction. The student experienced the pain of tight coupling before the solution was introduced.

## Intellectual Humility

The student explicitly stated: "Я пока не чувствую, что понимаю архитектуру на уровне Senior, и не могу с уверенностью принимать архитектурные решения." This is not weakness — it is accurate self-assessment combined with correct instincts. The student does not pretend to know what they do not know.

---

# 6. Weaknesses and Knowledge Gaps

## Database Fundamentals

The student used SQLite successfully as an infrastructure detail but has no systematic understanding of:

* SQL syntax beyond basic SELECT/UPDATE
* Relational database internals (B-trees, pages, indexing)
* Transactions and atomicity
* Schema design principles
* Migrations
* Query optimization

The student explicitly stated: "Никакого системного понимания синтаксиса, внутреннего устройства базы данных и прочего у меня пока нет. Хочется изучать это в будущих модулях."

## Architectural Terminology Confusion

The student initially confused "Use Case" (Application Layer orchestrator) with "user scenario" (e.g., "using the app on Windows 10"). This was a terminology collision between software architecture and product management/QA contexts. Resolved through mental models, but indicates that architectural vocabulary needs explicit grounding before introduction.

## SQLite Syntax Patterns

The student encountered several SQLite-specific difficulties:

* Confused `fetchone()` (returns one tuple) with `fetchall()` (returns list of tuples)
* Forgot to pass parameters as tuples to `cursor.execute()`
* Initially thought SQL code should be in a separate `.sql` file
* Was surprised by the binary nature of `.db` files

These were resolved during the module but indicate that database work requires more systematic attention to syntax patterns.

## Confidence Gap

The student's architectural instincts are correct, but the student does not yet trust them fully. The student seeks validation before making architectural decisions. This is appropriate at the current level but should gradually decrease as the student accumulates more independent design experience.

---

# 7. Common Mistakes Pattern

```text
- Terminology confusion when architectural terms collide with product management terms
  (e.g., "Use Case" vs "user scenario").
  
- SQLite syntax patterns: forgetting parameter tuples in execute(), confusing
  fetchone() with fetchall(), trying to iterate over a single row tuple.

- Placing conn.commit() and conn.close() inside loops instead of after them
  (variable scope pattern continuing from previous modules).

- Seeking validation before committing to architectural decisions, even when
  the instinct is correct. This is not a mistake per se but a confidence
  pattern that should be gradually addressed.

- The missing-parentheses issue from previous modules did NOT appear in
  Module 07 architectural work, suggesting it is primarily a syntax-level
  pattern that decreases when the student is focused on design rather
  than implementation details.
```

---

# 8. Independence Assessment

## Semi-Independent → Independent

The student demonstrates the following independence profile:

* **Familiar architectural problems** (Repository extraction, Use Case identification, dependency direction): The student can solve these independently. The JSON → SQLite migration was performed with minimal mentor intervention.

* **Unfamiliar architectural problems** (designing architecture for a completely new domain, Web API integration, database schema design): The student requires guidance and would benefit from mentor scaffolding.

* **Architectural reasoning and trade-off evaluation**: The student can independently compare designs and explain why one is more appropriate than another. This is the strongest indicator of growing independence.

* **Implementation details** (SQLite syntax, parameterized queries): The student requires hints and guided practice. This is expected given that databases were not a focus of Module 07.

The student is transitioning from "Assisted" to "Semi-Independent" in architecture and approaching "Independent" in architectural reasoning for familiar domains.

---

# 9. AI Usage Assessment

## Prompting Ability

The student describes architectural problems clearly and asks specific, well-formed questions. Examples:

* "Кто будет оркестрировать оркестраторов?"
* "Почему зашить это действие как метод в Estimate?"
* "Как мне обновить строчку available в json файле, не загружая его полностью?"

The student uses AI as a thinking partner, not as a code generator.

## Code Evaluation

The student can review AI-suggested architecture critically. The student rejected overengineered suggestions and proposed simpler alternatives. The student questioned the need for Use Case classes before accepting them.

## Decision Making

The student determines when AI assistance is appropriate and when independent reasoning is required. The student chose to write the SQLite implementation independently after understanding the pattern, rather than asking AI to generate it.

---

# 10. Project Integration

The QR Warehouse project underwent significant architectural evolution during Module 07:

**Implemented changes:**

* Created `EquipmentRepository` abstract contract (ABC) with `find_by_sku()` and `update_available()` methods
* Implemented `JsonEquipmentRepository` (existing storage)
* Implemented `SqliteEquipmentRepository` (new storage)
* Created `InMemoryEquipmentRepository` (test double)
* Extracted `AddItemToEstimate` as a Use Case in `use_cases.py`
* Refactored `main.py` into a clean Composition Root with helper functions (`read_config`, `create_logger`, `create_repository`, `input_info`, `decide_price_policy`, `enter_scan`, `save_and_exit`, `display_estimate`, `clear_console`)
* Refactored `Inventory` to depend on `EquipmentRepository` contract instead of internal `self._catalog` and `self._stock`
* Wrote architecture-level tests using `InMemoryEquipmentRepository`
* Created migration script to transfer data from `catalog.json` to SQLite
* Successfully ran the entire application with SQLite while business logic remained unchanged

**Architectural changes:**

* Dependency direction reversed: business logic now depends on contracts, not implementations
* Persistence isolated behind Repository boundary
* Presentation separated from Application logic
* Domain objects (`Inventory`, `Estimate`) no longer know about storage mechanism

**Discovered problems:**

* SQLite `fetchone()` returns a single tuple, not a list — caused initial confusion
* Parameterized queries require tuples — student initially forgot the parameter
* Binary `.db` files cannot be read in text editors — surprised the student

---

# 11. Recommended Next Steps

## Immediate (before next module)

* Complete the presentation layer feedback: add status handling (print/logging) in `main.py` for the Use Case results
* Run all tests to confirm the refactored architecture is stable

## Next Learning Objectives

* **Database Fundamentals Module**: SQL syntax systematically, relational database internals (B-trees, indexing), transactions, migrations, schema design. This is the student's explicitly stated desire and the natural next step after Repository Pattern.
* **Second Presentation Layer**: Introduce a Web API (Flask/FastAPI) alongside CLI to demonstrate that Use Cases remain reusable across different entry points.
* **Independent Design Challenge**: Give the student an unfamiliar domain (e.g., delivery company) and require independent architecture design before coding. This is the strongest measure of transfer.

## Concepts Requiring Reinforcement

* SQLite syntax patterns (parameterized queries, fetchone vs fetchall)
* Architectural terminology (explicitly distinguish from similar-sounding terms in other domains)
* Confidence in independent architectural decisions

## Recommended Exercises

* Design architecture for an unfamiliar problem (delivery company, appointment system) without mentor guidance
* Replace SQLite with PostgreSQL in the QR Warehouse (theoretical exercise to reinforce Repository boundary)
* Add a second Use Case (`RemoveItemFromEstimate` or `CreateEstimate`) independently

---

# 12. Curriculum Adjustment Recommendation

**Recommendation: Continue as planned with one adjustment.**

The current roadmap remains appropriate. However, the following adjustment is recommended:

* **Add a dedicated Database Module** between the current Architecture module and the next planned module. The student has explicitly expressed desire to study databases fundamentally, and the Repository Pattern provides a natural foundation for this. The student's existing `SqliteEquipmentRepository` can serve as a starting point for deeper exploration.

* **Increase confidence-building exercises**: The student's architectural instincts are correct but the student does not yet trust them fully. Provide opportunities for independent design followed by validation, rather than guided design.

* **Do NOT increase difficulty prematurely**: The student's intellectual humility is a strength. Do not push toward enterprise architecture, microservices, or distributed systems before the student has consolidated current understanding and gained confidence.

---

# 13. Final Mentor Assessment

The student has completed a transformative module. The transition from "engineer who designs flexible objects" to "engineer who designs maintainable application systems" is the most significant conceptual leap in the entire learning journey so far.

The student's strongest quality remains the combination of three rare traits:

1. **Strong architectural intuition** — invents patterns before learning names
2. **Pragmatic judgment** — knows when NOT to abstract
3. **Intellectual humility** — acknowledges what they do not know

This combination is unusual. Most students either overengineer (lacking pragmatism) or underengineer (lacking intuition). The student naturally finds the middle ground.

The next focus should be:

* Building confidence in independent architectural decisions
* Systematic database education (the student's explicitly stated desire)
* Transfer of architectural principles to unfamiliar domains
* Continued reinforcement of the "change scenario" approach to architecture

The student is not yet ready for enterprise architecture, distributed systems, or advanced design patterns. The student IS ready for deeper database work, second presentation layers, and independent design challenges.

---

# 14. Student Reflection

*The student answered the following questions after Module 07 completion:*

**What concepts became clearer?**

> "Я понял, насколько полезно и эффективно изолировать бизнес логику от всего остального."

The student understood that architecture is about controlling dependencies, not about file organization. The Repository Pattern made this tangible through the JSON → SQLite migration.

**What remains confusing?**

> Я пока не чувствую, что понимаю архитектуру на уровне Senior, и не могу с уверенностью принимать архитектурные решения, мне так или иначе нужно советоваться по этим вопросам.

**What was the most difficult part?**

> Я пока совершенно не знаю синтаксиса SQL. Я смог повторить пару строчек из предложенного учителем кода, но сам я пока, думаю, не в состоянии написать полноценный SQL запрос и сказать, что я полностью его понимаю. 

The conceptual distinction between Composition Root (`main.py`) and Use Cases (Application Services) was initially confusing. The student questioned why Use Cases were needed if `main.py` already orchestrates the program, fearing an "orchestrator of orchestrators" infinite loop. This was resolved through the "Factory Director vs. Production Manager" mental model.

The terminology collision between "Use Case" (architecture) and "user scenario" (product management) also required significant clarification.

**What would you like to explore further?**

> Во-первых, хочется получше изучить базы данных. Виды, синтаксис, назначение и прочее. Также хочется продолжать работу над проектом QR Warehouse, постепенно доводя его до состояния полноценного коммерческого продукта. 

The student expressed strong interest in:

* SQL syntax systematically
* Relational database internals
* Indexing and query performance
* Transactions
* Schema design
* The difference between SQLite, PostgreSQL, and other databases

---

# 15. Report Usage

This checkpoint report should be used by:

## AI Teacher

To adapt daily learning: introduce database fundamentals as the next major topic, continue validating architectural instincts, use change scenarios to motivate architectural boundaries, and provide opportunities for independent design.

## Student

To understand progress: the student has made a significant conceptual leap from object-oriented design to application architecture. The remaining gaps (databases, confidence) are clearly identified and addressable.

## Educational Architect

To evaluate and improve the learning system: Module 07 methodology was highly effective. The "change scenario" approach (JSON → SQLite) proved to be the strongest motivator for architectural boundaries. The "Architectural Filter" formulated independently by the student confirms that discovery-based learning produces deeper understanding than direct instruction.

---

**End of Checkpoint Report — Module 07**

**Date:** 2026-11-15

**Next checkpoint:** After Database Fundamentals Module