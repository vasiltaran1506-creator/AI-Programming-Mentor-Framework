# Module 10 — Testing, Quality & Reliability

**Framework:** AI Programming Mentor Framework (APMF)  
**Version:** 0.1 Alpha  
**Status:** Proposed next module after Module 09  
**Stage:** Backend Foundations / Application Reliability  
**Estimated effort:** 22–30 focused hours  
**Primary project:** QR Warehouse  
**Communication language:** Russian (the student communicates with the mentor in Russian)  
**Curriculum language:** English

---

# 1. Why Module 10 Exists

QR Warehouse now has two entry points: a CLI and an HTTP API built with FastAPI. Both use the same application logic and repositories. The project also contains multiple Use Cases that coordinate repositories and manage database transactions.

This is an important milestone, but an application that works in a few manual checks is not yet an application whose behavior is reliably protected against regressions.

The previous modules introduced `pytest`, and Module 09 added API-level tests using FastAPI's `TestClient`. However, an important gap remains: the newer, database-backed Use Cases—especially those that coordinate multiple repositories and transactions—need focused tests of their own.

Module 10 addresses that gap. It teaches the student to make behavior observable, build deterministic tests, distinguish test layers, and verify both successful and failing operations. The goal is not to maximize the number of tests or achieve an arbitrary coverage percentage. The goal is to protect the application's important behavior with tests that are understandable, trustworthy, and useful during future refactoring.

> **The central idea of Module 10:** Tests are executable examples of expected behavior. They help us discover when the system stops keeping its promises.

This module should strengthen the existing QR Warehouse architecture, not replace it with a new one.

---

# 2. The Main Mindset Shift

Before this module, the student often verified behavior by running the application and checking the result manually:

```text
Run the program
      ↓
Perform an operation
      ↓
Look at the output
      ↓
Decide whether it seems correct
```

After this module, the student should be able to express important expectations as repeatable checks:

```text
Define the expected behavior
          ↓
Prepare a controlled starting state
          ↓
Execute one operation
          ↓
Observe the result and state changes
          ↓
Assert that the contract still holds
```

A test is not merely a way to prove that today's implementation works. It is a way to preserve an important behavior when tomorrow's implementation changes.

The student should begin asking:

- What behavior must never break?
- What can fail, and what should happen if it does?
- Which layer should a test exercise?
- What state must be isolated between tests?
- Does this test verify an externally meaningful behavior, or does it merely repeat implementation details?

---

# 3. Prerequisites

The module assumes the student has completed Modules 00–09 and can work with the following concepts:

- Python functions, classes, exceptions, collections, and modules;
- basic object-oriented design, composition, and dependency injection;
- Domain, Application, Presentation, and Infrastructure responsibilities;
- Repository interfaces and concrete repository implementations;
- Use Cases that coordinate repositories;
- relational tables, foreign keys, constraints, and parameterized SQL;
- SQLite connections and the project's current transaction approach;
- HTTP methods, status codes, request validation, and FastAPI endpoints;
- basic `pytest` tests and FastAPI `TestClient` usage.

The student does not need to know advanced pytest plugins, mocking frameworks, CI/CD, Docker, PostgreSQL, or async database drivers before starting.

---

# 4. Learning Outcomes

By the end of Module 10, the student should be able to:

1. Explain the difference between unit, integration, and API tests, and select a test type based on the behavior being verified.
2. Write tests using a clear Arrange–Act–Assert structure.
3. Use pytest fixtures to create predictable test contexts and clean them up safely.
4. Use parametrization when several inputs should verify the same behavioral rule.
5. Distinguish a fake, a stub, and a mock, and use test doubles only when they simplify a meaningful test.
6. Test Use Cases independently from FastAPI and the real database by supplying suitable fake repositories.
7. Verify successful operations, expected business failures, and important state transitions.
8. Test transaction outcomes using the real SQLite implementation, recognizing that fake repositories cannot prove real database atomicity.
9. Test HTTP contracts separately from business logic, including status codes, response bodies, and validation failures.
10. Keep tests isolated from the user's working database and from one another.
11. Diagnose a failing test systematically rather than changing assertions until the test passes.
12. Review test quality: identify brittle assertions, duplicated setup, misleading test names, and missing failure-path coverage.
13. Explain what the test suite does and does not establish about the reliability of QR Warehouse.

These outcomes describe practical competence in a small application. They do not imply production-level expertise in testing or reliability engineering.

---

# 5. Scope and Non-Goals

## Included

- `pytest` fundamentals needed for a maintainable project test suite;
- test anatomy and behavioral assertions;
- fixtures, parametrization, and exception assertions;
- test doubles, especially in-memory fake repositories;
- unit tests for the existing QR Warehouse Use Cases;
- integration tests for real SQLite repositories and transaction behavior;
- API tests using FastAPI's `TestClient`;
- deterministic test-data setup and cleanup;
- basic test organization and failure diagnosis;
- a small, evidence-based review of test coverage.

## Explicitly Out of Scope

Do not turn this module into a broad course on every testing tool. The following topics are deferred:

- PostgreSQL migration and database-driver selection;
- SQLAlchemy and Alembic;
- async database access and advanced `asyncio` testing;
- authentication and authorization;
- load, stress, soak, and performance testing;
- browser end-to-end testing;
- contract-testing frameworks and consumer-driven contracts;
- property-based testing with Hypothesis;
- mutation testing;
- CI/CD pipelines and deployment automation;
- a large test-factory or dependency-container redesign.

Some of these subjects may be mentioned when useful, but they must not become prerequisites for completing Module 10.

---

# 6. Mentor Operating Instructions

These instructions are part of the module and must be followed throughout it.

## 6.1 Language

- Communicate with the student in Russian unless the student explicitly requests another language.
- The curriculum and any requested learning artifacts remain in English.
- Explain new concepts in Russian, using English technical terms where they are standard.

## 6.2 The Student Must Write the Implementation

**Critical rule: do not write complete implementation code or complete test solutions for the student.**

The student explicitly established this boundary during Module 09. Respect it.

The mentor may:

- explain concepts and mental models;
- inspect the existing project and identify relevant files;
- describe behavioral requirements and test cases;
- ask guiding questions;
- point to a specific failing assertion or suspicious line;
- provide a small syntax example when it teaches a general mechanism and does not solve the current task;
- review code written by the student;
- suggest a next debugging step;
- explain a completed solution after the student has made a genuine attempt.

The mentor must not:

- generate an entire test file for the student to copy;
- rewrite a Use Case or repository without the student's request and a clear learning reason;
- silently fix the student's code;
- replace a meaningful exercise with a ready-made solution;
- claim independent mastery when the work was completed through substantial guidance.

If the student is stuck, use a gradual hint sequence:

1. Ask the student to restate the expected behavior.
2. Ask which layer should be tested and what state is relevant.
3. Give a conceptual hint.
4. Point to the specific function, return value, or test assertion involved.
5. Show a tiny, unrelated syntax example if syntax is the actual obstacle.
6. Only after a genuine attempt, explain the solution path. Keep the student responsible for writing the final code.

## 6.3 Calibrate Praise and Competency Claims

- Praise specific decisions and evidence, not presumed traits.
- Do not use labels such as “professional-level,” “exceptional,” or “senior-level” based on a single exercise.
- Distinguish independent work, work completed after hints, and conceptual understanding demonstrated only in discussion.
- A passing test suite is evidence that tested expectations hold for the tested cases; it is not proof that the application is bug-free.
- Treat the student's self-assessment as important evidence, but not as the only evidence.

## 6.4 Inspect Before Prescribing

At the beginning of the practical work, inspect the current QR Warehouse structure and the actual code. Do not assume class names, method signatures, return values, database lifecycle, or transaction implementation from an older report.

Before proposing a test seam or refactoring:

1. Identify how the current Application object and Use Cases are constructed.
2. Identify repository contracts and concrete SQLite repositories.
3. Identify who owns the connection and who calls `commit()` or `rollback()`.
4. Identify how the FastAPI application obtains its dependencies.
5. Identify where the current tests point to the database file.

If the current code differs from the checkpoint report, adapt the exercise to the code that actually exists. Do not force the project to match the report.

## 6.5 Prefer the Smallest Useful Test Setup

The student correctly pushed back against premature complexity during Module 09. Preserve that pragmatic approach.

Do not introduce an elaborate Application Factory, dependency container, or test framework merely to make a few tests easier. First investigate whether the existing construction approach can support a small, safe test fixture. Refactor only when the need is demonstrated and explain the cost of the change.

A simple setup is acceptable if it is deterministic, isolated, and easy to understand. However, never use the working application database as a test database.

---

# 7. Learning Sequence

The module consists of six learning blocks and a final integration task. The mentor should proceed in order unless the student demonstrates that a block is already independently mastered.

Recommended effort:

| Block | Topic | Estimated time |
|---|---|---:|
| 1 | The purpose and anatomy of tests | 2–3 h |
| 2 | pytest fixtures and parametrization | 3–4 h |
| 3 | Test doubles and Use Case unit tests | 5–7 h |
| 4 | Transactions and SQLite integration tests | 4–6 h |
| 5 | FastAPI API tests and test isolation | 4–5 h |
| 6 | Test quality and systematic debugging | 2–3 h |
| Final | Integration task and checkpoint | 2 h |
| **Total** |  | **22–30 h** |

Time is an estimate, not a deadline. Understanding and independent application matter more than finishing within a fixed number of days.

---

# 8. Block 1 — The Purpose and Anatomy of Tests

## 8.1 Mental Model: A Test Is an Executable Promise

A test describes a promise the software makes.

For example:

```text
Given: an estimate exists and has one item
When: the user removes that item
Then: the item is no longer present
And: the estimate total reflects the remaining items
```

This is more useful than a test named `test_remove_item` that only checks whether a method returned without raising an exception.

A test should make three things clear:

- the relevant starting conditions;
- the action being performed;
- the observable outcome that proves the expected behavior.

## 8.2 Arrange–Act–Assert

Use the Arrange–Act–Assert (AAA) structure as a default mental model:

```text
ARRANGE
Prepare the object, dependencies, and initial state.

ACT
Perform one meaningful operation.

ASSERT
Verify the externally meaningful result.
```

AAA is a guide, not a formatting law. A test may have several assertions when they describe one coherent outcome. Avoid turning one test into a long script that verifies many unrelated behaviors.

## 8.3 Test Behavior, Not Private Implementation

A robust test usually checks observable behavior:

- returned result;
- changed state;
- persisted data;
- emitted or returned error;
- calls to a dependency when the interaction itself is part of the contract.

Avoid assertions that depend unnecessarily on:

- private method names;
- the exact order of internal helper calls;
- incidental local variables;
- SQL formatting when the purpose is to test business behavior;
- implementation details that may change without changing behavior.

Testing implementation details often makes refactoring harder without improving confidence.

## 8.4 One Test, One Behavioral Claim

A test should have one primary reason to fail. It may need multiple assertions to establish that claim, but it should not combine unrelated scenarios.

Prefer descriptive names that state an outcome. Examples of naming style:

```text
test_add_item_rejects_unknown_sku
test_change_quantity_updates_estimate_total
test_delete_estimate_removes_its_items
```

The names are examples of intent, not required names. Adapt them to the project's actual API.

## 8.5 Exercise 1 — Turn Requirements into Test Cases

Do not write code at first. Use the current QR Warehouse behavior and write test-case descriptions for these operations:

1. Creating an estimate with valid data.
2. Attempting to retrieve an estimate that does not exist.
3. Adding a catalog item to an existing estimate.
4. Attempting to add an item that does not exist.
5. Attempting to reserve more equipment than is available.
6. Changing an item's quantity.
7. Deleting an item from an estimate.

For each operation, describe at least one successful path and one relevant failure path where applicable.

For every test case, record:

- initial state;
- action;
- expected result;
- expected state changes;
- whether the case belongs in a unit test, an integration test, or an API test.

The student should identify any ambiguity in current business rules rather than inventing a rule silently. Ask the mentor to clarify only when the existing project behavior or requirements do not answer the question.

### Block 1 Completion Criteria

The student can explain AAA, distinguish behavior from implementation details, and produce a small, meaningful test plan before writing tests.

---

# 9. Block 2 — pytest Fixtures and Parametrization

## 9.1 Why Fixtures Exist

A fixture prepares a known context for a test. It may create an object, prepare data, provide a dependency, or guarantee cleanup.

The goal is to avoid repeating fragile setup while keeping dependencies visible.

Conceptually:

```text
Test requests a fixture
          ↓
pytest prepares the fixture
          ↓
Test receives the prepared object
          ↓
Cleanup runs when the fixture scope ends
```

Fixtures should make tests clearer, not hide important behavior behind layers of indirection.

## 9.2 Fixture Scope

Understand the practical difference between common scopes:

- `function`: a fresh fixture for each test; the safest default for mutable test state;
- `class`: shared within a test class;
- `module`: shared within a test module;
- `session`: shared for the whole test run.

Do not choose a broad scope merely to make tests faster. A shared mutable database or repository can cause order-dependent tests. Start with function-scoped fixtures unless a clear reason justifies another scope.

## 9.3 Cleanup and `yield`

Some test setup creates resources that must be released: temporary files, database connections, or application resources.

Understand the setup/teardown pattern and how a fixture using `yield` can perform cleanup after the test finishes. Cleanup must still happen when the test fails.

Avoid manual cleanup at the end of every test when a fixture can express it more safely and clearly.

## 9.4 Parametrization

Parametrization runs the same behavioral test against several input cases. It is useful when the rule is the same but values differ.

Possible QR Warehouse examples:

- quantities that should be rejected: zero and negative values;
- several invalid estimate durations;
- different unknown identifiers;
- combinations of valid and invalid request fields.

Do not parametrize unrelated scenarios merely to reduce the number of test functions. A readable test suite is more important than a small test count.

## 9.5 Exception Assertions

Use `pytest.raises(ExpectedException)` when the contract of a unit under test is to raise a specific exception.

Do not use `pytest.raises(Exception)` as a universal assertion. It can allow unrelated programming errors to make a test pass. Assert the narrowest meaningful exception type and, when appropriate, inspect its message or attributes without overfitting to incidental wording.

Remember that a business failure represented by a `Result` object is not the same as a raised exception. Test the behavior that the current application actually promises.

## 9.6 Exercise 2 — Make Setup Reliable

Using a small existing test or a simple disposable exercise:

1. Identify repeated setup that genuinely belongs in a fixture.
2. Extract only that setup into a fixture.
3. Make the fixture return a fresh object or state for each test unless sharing is intentional.
4. Add cleanup if the fixture creates a resource that needs it.
5. Introduce parametrization for one repeated validation rule.
6. Demonstrate that the tests pass regardless of their execution order.

Do not refactor the entire test suite at once.

### Block 2 Completion Criteria

The student can explain fixture setup and teardown, select a sensible scope, parametrize a repeated rule, and avoid shared mutable state between tests.

---

# 10. Block 3 — Test Doubles and Use Case Unit Tests

## 10.1 The Three Common Test Doubles

A test double is a replacement for a real dependency used to make a test more controlled or focused.

For this module, distinguish three common forms:

**Stub**  
Provides predefined responses. It is useful when a test only needs a dependency to return a known value.

**Fake**  
A lightweight working implementation with simplified behavior. An in-memory repository that stores objects in a dictionary can be a fake.

**Mock**  
A test double used to verify interactions, such as whether a dependency was called with specific arguments. Use interaction assertions only when that interaction is an important part of the behavior.

The words are sometimes used loosely in everyday discussion. The student should understand the practical distinction, not spend time arguing over labels.

## 10.2 Why Test Use Cases with Fakes?

A Use Case should be testable without starting the HTTP server or opening the production database.

A fake repository can provide a controlled initial state and allow the student to inspect resulting state. This makes business behavior easier to test and failure cases easier to reproduce.

The conceptual flow is:

```text
Unit test
   ↓
Use Case under test
   ↓
Fake repository or other controlled dependency
   ↓
Assertion about result and state
```

The real SQLite repositories are intentionally absent from a pure Use Case unit test. That is what makes the test focused.

## 10.3 Inspect the Existing Contracts First

Before creating any fakes, inspect the current QR Warehouse repository interfaces and the Use Cases that depend on them.

The mentor should ask the student to identify:

- methods each Use Case actually calls;
- values returned by repository methods;
- business outcomes returned by Use Cases;
- state that must change on success;
- state that must remain unchanged on failure;
- transaction responsibilities and any dependency shared between repositories.

Do not create a large fake repository with every method in the production interface if each test needs only a small, clear subset. On the other hand, a fake must implement the contract required by the Use Case it is testing.

## 10.4 Select a Small Set of Use Cases

Start with the following candidates, adapting names to the actual project:

1. `CreateEstimate` — creates an estimate with valid values and rejects invalid business input where that validation belongs.
2. `AddItemToEstimate` — verifies the successful path and relevant failures involving missing estimates, missing equipment, and insufficient stock.
3. `ChangeItemQuantity` — verifies the updated quantity and total, including invalid changes.
4. `DeleteItemFromEstimate` — verifies removal and the expected updated estimate state.
5. `DeleteEstimate` — verifies the intended deletion behavior and any relevant missing-resource case.

Do not attempt to test every possible detail in every Use Case. Begin with the business behavior that would be expensive or dangerous to break.

## 10.5 Assert Results and State

Where relevant, test both the returned outcome and the resulting state.

For a successful add-item operation, the test might verify that:

- the result represents success;
- the estimate contains the expected item;
- the requested quantity is correct;
- the total is recalculated according to the current business rule;
- inventory availability reflects the expected reservation behavior, if this operation owns that behavior.

For a rejected operation, verify that:

- the result or exception matches the documented contract;
- the state remains unchanged where the operation is expected to be atomic;
- no unrelated resource is modified.

Avoid asserting fields that are not part of the relevant contract.

## 10.6 Test Historical Snapshot Behavior

The Module 08 design established that estimate data may preserve values from the time an item was added, even if the catalog changes later.

Write at least one behavioral test for the relevant snapshot rule that exists in the current project. For example, after adding an item to an estimate, changing the catalog price must not silently rewrite the already stored estimate price if the current business rule says the estimate preserves its original price.

First inspect the current implementation and confirm exactly which values are snapshotted. Do not assume that all fields are historical snapshots.

## 10.7 Keep Fakes Honest

A fake exists to make a particular test easier. It should not pretend to prove behavior it does not implement.

For example:

- a fake repository can help verify how a Use Case reacts when an item is missing;
- a fake can record whether a save operation was requested;
- a fake cannot prove that SQLite enforces a foreign key;
- a fake cannot prove that an actual database transaction rolls back correctly unless it faithfully models the relevant transaction behavior—and even then, the real database still requires an integration test.

Avoid writing a complex miniature database inside the tests. Test doubles should be simpler than the real dependency.

## 10.8 Exercise 3 — Test a Use Case Independently

Choose one Use Case that has a meaningful success path and at least one failure path.

The student should:

1. Read the Use Case and its repository contracts.
2. Describe its behavior in plain language before coding.
3. Create the smallest suitable fake dependencies.
4. Write one test for a successful operation.
5. Write at least two tests for meaningful failure cases.
6. Assert the returned result and important state changes.
7. Run the tests and explain any failures.
8. Ask the mentor to review whether the tests would still pass if the internal implementation changed but the behavior remained the same.

Then repeat the pattern for a second Use Case that coordinates more than one repository.

### Block 3 Completion Criteria

The student can create a suitable fake for a real repository contract, test a Use Case without FastAPI or SQLite, and explain why an in-memory fake does not prove database correctness.

---

# 11. Block 4 — Transactions and SQLite Integration Tests

## 11.1 Unit Tests Cannot Prove Real Transaction Atomicity

This distinction is essential.

A Use Case unit test with fake repositories can verify the Use Case's decisions and the calls it makes. It does not prove that a real SQLite connection rolls back actual database changes.

To test database behavior, use an integration test with the real SQLite repositories and an isolated test database.

```text
Use Case unit test
  → business behavior with fakes

SQLite integration test
  → real repositories + real database

API test
  → HTTP boundary + application behavior
```

These layers complement one another; they are not competing alternatives.

## 11.2 Reconfirm the Transaction Boundary

Before writing the tests, map the current transaction lifecycle:

- Where is the connection created?
- Which repositories share it?
- Which component begins or controls the transaction?
- Which component commits on success?
- Which component rolls back on failure?
- What happens if an exception occurs after the first database write but before the second?

The project previously adopted a Unit of Work approach in which one business operation coordinates changes and commits once. Confirm that this is still how the code works. Do not rely on memory or the report alone.

The test should protect the actual intended contract. If the code reveals an ambiguous or incorrect transaction boundary, stop and discuss it before hiding the issue behind a passing test.

## 11.3 Isolated SQLite Database

Integration tests must never point to the student's working `warehouse.db`.

Prefer a temporary database created for the test run. pytest's `tmp_path` fixture can provide a unique temporary directory. The test setup should initialize the schema using the project's actual initialization path where practical, then create repositories and Use Cases connected to that test database.

An in-memory database is also possible, but remember that separate SQLite connections opened with `":memory:"` normally receive separate independent databases. If the application uses multiple connections, choose a setup that accurately represents the behavior being tested.

For tests using SQLite, confirm that foreign-key enforcement is enabled on the connection when the schema depends on it. Do not assume that declaring a foreign key alone proves that the running connection enforces it.

## 11.4 Transaction Scenarios

Test a meaningful multi-step operation that changes more than one piece of persistent state.

At minimum, cover:

**Success path**

- the operation completes;
- all expected changes are committed;
- a fresh read from the test database observes the committed state.

**Failure before any write**

- the operation returns or raises the documented failure;
- persistent state remains unchanged.

**Failure after an earlier write**

- arrange a controlled failure after the first database mutation but before the operation is complete;
- verify that the transaction does not leave a partial result;
- verify the expected state by reading from the database after the operation.

Do not introduce an artificial production feature solely to force a failure. Use the simplest legitimate test seam available. If a controlled failure cannot be introduced cleanly, discuss options with the mentor and explain the trade-offs before changing architecture.

## 11.5 What Exactly Should Be Verified?

For a transaction that coordinates inventory and estimate data, the important invariant may be:

```text
Either all required changes are committed,
or none of them are committed.
```

The test should verify data, not merely observe that `rollback()` was called. A call to `rollback()` is an implementation detail; the externally meaningful guarantee is that persistent state is not left partially updated.

Also test that a successful operation does not accidentally discard valid changes.

## 11.6 SQLite Version and Transaction Configuration

The behavior of Python's `sqlite3` transaction controls has evolved. Do not change transaction configuration blindly or copy configuration from an unrelated tutorial.

For this module:

- inspect the Python version and current `sqlite3` connection settings;
- preserve the project's current transaction contract while testing it;
- understand whether transactions are implicit or explicitly controlled in the existing implementation;
- avoid combining a transaction redesign with the first round of tests unless the tests reveal a concrete defect;
- document any intentional configuration change and why it is required.

The goal is to test and understand the current system before redesigning it.

## 11.7 Exercise 4 — Prove Atomicity with SQLite

Create one isolated integration test for a Use Case that coordinates multiple repositories or multiple writes.

The student should demonstrate:

1. the test cannot access the working database;
2. the schema and seed data are deterministic;
3. the successful path persists all expected changes;
4. a meaningful failure path leaves no partial persistent state;
5. test cleanup occurs even if an assertion fails;
6. the test suite can be run repeatedly without accumulating data.

The mentor should ask the student to explain which claim is proven by the unit test and which is proven by the integration test.

### Block 4 Completion Criteria

The student can distinguish fake-based business tests from real SQLite integration tests and can demonstrate an important transaction guarantee against an isolated database.

---

# 12. Block 5 — FastAPI API Tests and Test Isolation

## 12.1 API Tests Verify the HTTP Contract

An API test should exercise the HTTP boundary, not simply call the endpoint function directly.

Use FastAPI's `TestClient` for the current synchronous API tests. Test the behavior a client can observe:

- response status code;
- response JSON and its structure;
- validation errors;
- not-found behavior;
- business conflicts;
- successful resource creation, retrieval, update, and deletion.

Do not duplicate every Use Case unit test as an API test. The purpose of an API test is to establish that HTTP input is translated correctly into application calls and that application outcomes are translated into the intended HTTP response.

## 12.2 Build a Small HTTP Contract Matrix

Inspect the existing routes and document a compact matrix. Adapt it to the actual endpoints and current domain rules.

| Scenario | What the test should verify |
|---|---|
| Valid create request | Documented creation status and response body |
| Invalid request body | Validation response and useful error structure |
| Existing resource | Correct response and representation |
| Missing specific resource | Documented not-found behavior |
| Empty collection | Valid empty collection response, not a missing-resource response |
| Valid update | Correct update response and persisted state |
| Business conflict | Appropriate conflict response without leaking internal or sensitive data |
| Successful delete | Documented deletion response and resource absence |

Do not treat this table as a rigid mapping for every possible API. The actual contract should reflect the semantics of the operation.

Remember the distinctions:

- `201 Created` means the request created a resource; it is not restricted solely by the HTTP method.
- `200 OK` is suitable when a successful response includes a representation.
- `204 No Content` is suitable when the operation succeeds and intentionally returns no body.
- `404 Not Found` concerns a missing target resource; an existing collection with zero elements is normally a successful empty response.
- `409 Conflict` is appropriate when a valid request conflicts with the current resource state.
- `422 Unprocessable Content` is commonly used by FastAPI for request validation failures.
- `500 Internal Server Error` should represent an unexpected server failure, not a normal business outcome.

The student should be able to justify each selected response code rather than merely repeat these examples.

## 12.3 Request and Response Assertions

Check that the API returns the documented shape, not only a status code.

For example, if the create endpoint returns an estimate identifier, verify that:

- the response contains the documented key;
- the value has the expected type;
- the created resource can subsequently be retrieved;
- fields that must not be exposed are absent.

Avoid asserting the exact wording of framework-generated validation messages unless that wording is intentionally part of the API contract. Framework wording may change between versions.

## 12.4 Validation Versus Business Errors

Keep these questions separate:

**Request validation:** Is the supplied representation structurally valid? Examples include a missing required field or a value of the wrong type.

**Business validation:** Is the requested operation permitted by the current business rules? Examples include insufficient stock or an estimate that cannot be modified in its current state.

**Unexpected failure:** Did the server encounter an error that was not an expected outcome of the request?

Test representative cases from each category. Ensure that business failures remain distinguishable from unexpected programming or infrastructure errors.

## 12.5 Test Database Isolation

API tests must not use the working `warehouse.db`.

Inspect how the FastAPI application receives the Application object, Use Cases, repositories, or database connection. Prefer the smallest reliable method to supply an isolated test environment.

If the current module-level application construction prevents safe isolation, first explain the problem. A small application factory or dependency override may be justified, but do not introduce a broad redesign automatically.

Do not rely exclusively on deleting resources at the end of a test. Cleanup code can be skipped by process termination, and one failed test can contaminate later tests. Use an isolated temporary database whenever practical.

Tests should not depend on execution order. They should pass when run individually and as part of the full suite.

## 12.6 Exercise 5 — Verify the Existing API

Choose a representative subset of endpoints across Equipment and Estimates. Add or improve API tests to cover:

1. a successful read;
2. a successful create;
3. a successful update or delete;
4. a missing-resource response;
5. invalid request data;
6. a business conflict, where the current API supports one;
7. an empty collection, if that state is possible.

For each test, state which part of the HTTP contract it protects. Ensure the tests use isolated data and that they remain repeatable.

### Block 5 Completion Criteria

The student can test a real HTTP request through `TestClient`, verify its contract, distinguish validation from business errors, and demonstrate that API tests do not modify working project data.

---

# 13. Block 6 — Test Quality and Systematic Debugging

## 13.1 A Passing Test Can Still Be a Bad Test

A test suite is useful only when its assertions correspond to meaningful expectations.

Examples of weak tests:

- a test checks only that a method did not crash;
- a test asserts a value that is already guaranteed by the test's own setup;
- a test uses an overly broad exception type and passes for the wrong reason;
- a test depends on another test having run first;
- a test checks private implementation details that are not part of the behavior;
- a test cleans up the wrong record or leaves persistent data behind;
- a test passes against a fake but makes claims about real SQLite behavior.

Review tests for their ability to fail when the relevant behavior is broken.

## 13.2 Read Failures as Evidence

When a test fails, do not immediately modify the assertion.

Use this sequence:

1. Read the test name and restate its behavioral claim.
2. Identify the exact failing assertion or exception.
3. Compare expected and actual values, including their types.
4. Inspect the setup and initial state.
5. Determine whether the test is wrong, the implementation is wrong, or the requirement is ambiguous.
6. Make the smallest justified change.
7. Rerun the focused test, then the relevant group, then the full suite.

A red test is information. It is not automatically proof that the implementation is broken.

## 13.3 Test Names and Diagnostic Value

A useful test failure should help the developer understand what behavior has regressed.

Prefer names and assertions that tell a story. When an assertion fails, make it easy to identify:

- the operation;
- the relevant initial condition;
- the expected behavior;
- the actual result.

Do not add large custom assertion helpers unless repeated complexity makes them worthwhile.

## 13.4 Coverage Is a Map, Not a Score

Code coverage can show which lines or branches executed during tests. It cannot establish that assertions are meaningful or that all relevant behavior is correct.

Do not set an arbitrary target such as 100% coverage for this module. Instead, create a behavioral coverage map for the critical Use Cases and API operations.

For each important operation, identify:

- at least one successful case;
- important expected failure cases;
- state that must change;
- state that must remain unchanged;
- the test layer responsible for verifying each claim.

Coverage tools may be introduced as optional diagnostic aids, not as the central objective.

## 13.5 Exercise 6 — Review the Test Suite

Review the tests written during Blocks 2–5. Identify at least three weaknesses or opportunities for improvement. Examples include duplicated setup, weak assertions, shared state, poor test naming, or a missing failure case.

For each finding:

1. explain the risk;
2. decide whether the change is worth making now;
3. improve the test if justified;
4. verify that the full suite remains stable.

Do not refactor tests only to make them look more sophisticated.

### Block 6 Completion Criteria

The student can diagnose test failures systematically, explain the limitations of coverage, and improve a test suite without creating unnecessary abstractions.

---

# 14. Final Integration Task — A Tested QR Warehouse Workflow

The final task combines the module's core ideas in one bounded scenario.

## Scenario

A manager creates an estimate and adds a catalog item. The requested quantity is either available or exceeds current stock. The operation must produce a consistent result, and the API must communicate that result through the expected HTTP contract.

Adapt the exact workflow to the real QR Warehouse business rules. Do not assume that the current project reserves stock at the same stage as a future commercial workflow.

## Required Work

The student must independently:

1. Describe the intended business behavior and relevant invariants.
2. Identify the Use Case and its repository dependencies.
3. Write fake-based unit tests for the Use Case's success and important failure paths.
4. Write at least one SQLite integration test for persistence and, where relevant, transaction atomicity.
5. Write API tests for the corresponding successful and failing HTTP requests.
6. Ensure all tests use isolated, deterministic data.
7. Run the focused tests and the entire project test suite.
8. Review the tests for meaningful assertions and explain what remains untested.

The task is complete when the student can demonstrate the workflow through the tests and explain what each test layer proves.

## Acceptance Criteria

- Tests are written by the student, not copied from a generated solution.
- A Use Case can be tested without starting FastAPI or using the real database.
- Real database behavior is tested against an isolated SQLite database.
- At least one meaningful failure scenario verifies that no invalid partial state remains.
- HTTP tests verify status codes and relevant response content.
- No test reads from or writes to the working QR Warehouse database.
- The focused tests and the complete test suite pass reproducibly.
- The student can explain the limits of the tests without claiming that the application is bug-free.

If an acceptance criterion cannot be met because the current architecture lacks a safe test seam, the mentor and student should document the obstacle and choose the smallest justified design change. The criterion must not be silently waived.

---

# 15. Suggested Repository Organization

Do not impose a new structure before inspecting the actual project. A possible organization is:

```text
tests/
    unit/
        test_create_estimate.py
        test_add_item_to_estimate.py
        test_change_item_quantity.py
        test_delete_item_from_estimate.py
    integration/
        test_estimate_transactions.py
        test_sql_repositories.py
    api/
        test_estimate_routes.py
        test_equipment_routes.py
```

This is an example, not a required layout. The student may keep a simpler structure if it remains clear and maintainable.

Use `conftest.py` only for fixtures that are genuinely shared. Avoid turning it into an opaque container for application construction and test behavior.

---

# 16. Common Traps to Watch For

The mentor should actively watch for these mistakes during code review:

## Test Design

- Checking only that a function returns without raising.
- Combining many unrelated behaviors in one test.
- Writing tests that mirror implementation details instead of behavior.
- Using broad exception assertions.
- Making assertions whose expected values are derived from the same incorrect calculation as the implementation.

## State and Fixtures

- Sharing mutable fake repositories between tests unintentionally.
- Using the working database as a test database.
- Relying on test execution order.
- Forgetting cleanup when a fixture creates a resource.
- Assuming that a `":memory:"` SQLite database is automatically shared between independent connections.

## Use Cases and Test Doubles

- Testing a Use Case only through FastAPI and calling that sufficient unit coverage.
- Building a fake that is more complex than the real dependency.
- Verifying calls but forgetting to verify resulting business state.
- Assuming that fake repositories prove SQL or transaction correctness.
- Mocking every dependency even when a small fake would be clearer.

## Transactions

- Checking only that `rollback()` was called instead of verifying the persistent state.
- Testing only failures that occur before any write.
- Using separate connections accidentally when the test expects one transaction.
- Modifying transaction code and test setup simultaneously without isolating the cause of a failure.

## API Tests

- Treating an empty collection as a missing specific resource.
- Comparing numeric status codes to strings.
- Checking a dictionary value where key existence should be checked.
- Overfitting to exact validation error wording generated by the framework.
- Returning or asserting sensitive internal details in error responses.
- Assuming every `PATCH` must return `200`, or that every `POST` must return `201`, without considering the operation's semantics.

These are review prompts, not a checklist to mechanically apply without understanding the context.

---

# 17. Assessment and Competency Calibration

Evaluate demonstrated behavior, not confidence or speed. Use the following scale consistently:

**Level 1 — Conceptual / Guided**  
The student can explain the idea or complete a test with substantial step-by-step guidance.

**Level 2 — Guided Application**  
The student can implement a familiar test after hints, examples, or help identifying the next step.

**Level 3 — Independent Application**  
The student independently writes and debugs tests for familiar project behavior, explains the assertions, and makes reasonable design choices.

**Level 4 — Transfer and Justification**  
The student independently applies the skill to a less familiar scenario, compares reasonable approaches, explains trade-offs, and avoids unnecessary complexity.

A Level 4 in this educational framework means independent transfer within the demonstrated scope. It must not be described as professional or senior-level expertise.

## Competencies to Evaluate

| Competency | Evidence Required |
|---|---|
| TEST-001 Test Anatomy | Clear Arrange–Act–Assert structure and meaningful behavioral claims |
| TEST-002 pytest Fixtures | Reliable setup and cleanup; appropriate fixture scope |
| TEST-003 Parametrization | Appropriate reuse of a behavioral test across multiple cases |
| TEST-004 Test Doubles | A suitable fake or stub that keeps a unit test focused |
| TEST-005 Use Case Testing | Independent tests for success and business failure paths |
| TEST-006 Transaction Verification | Real SQLite integration test demonstrating an important transaction guarantee |
| TEST-007 API Contract Testing | Tests verify status codes, response shape, validation, and error behavior |
| TEST-008 Test Isolation | Reproducible tests that do not touch working project data |
| TEST-009 Failure Diagnosis | Systematic explanation and correction of a failing test |
| TEST-010 Test Quality Judgment | Ability to identify brittle tests and justify whether refactoring is worthwhile |

For each competency, record:

- current level;
- concrete evidence from the student's own work;
- how much guidance was needed;
- confidence in the assessment (low / medium / high);
- one next step, if needed.

Do not assign Level 3 or Level 4 solely because the final code works. The mentor should look at the student's reasoning and degree of independence.

---

# 18. Checkpoint Report Requirements

After completion, create a Module 10 Checkpoint Report using the APMF report format.

The report should include:

1. **General Information** — module, date, project, and mentor.
2. **Summary** — what was actually completed, without inflated claims.
3. **Completed Learning Areas** — concepts demonstrated in practice.
4. **Competency Evaluation** — the competencies from Section 17, with evidence and confidence.
5. **Project Integration** — tests and any code changes made to QR Warehouse.
6. **Testing Evidence** — which tests were run, what they verified, and whether the complete suite passed.
7. **Difficulties** — recurring mistakes and unresolved uncertainties.
8. **Independent Decisions** — decisions made by the student, noting whether they were made independently or after guidance.
9. **Recommended Next Steps** — only the most relevant follow-up topics.
10. **Student Reflection** — the questions below.

A report must not claim that tests passed unless the mentor has seen the actual run output or the student has supplied it. Distinguish code review from executed verification.

## Student Reflection Questions

Ask the student to answer in their own words:

- Which test type became clearer, and why?
- What was the most difficult test to design or debug?
- Did fake repositories make the Use Case easier to understand? What did they fail to prove?
- What did the SQLite integration test reveal that a unit test could not reveal?
- Which test assertion turned out to be weak or misleading?
- How confident do you feel about test isolation and why?
- What remains confusing?
- Which part of the module should be revisited before moving on?

---

# 19. Integration with APMF Knowledge Documents

After Module 10, update the relevant knowledge documents without rewriting history.

## Programming Handbook

Add or revise concise reference sections for:

```text
Test Pyramid / Test Layers
Arrange–Act–Assert
pytest Fixtures
Fixture Scope and Teardown
Parametrization
pytest.raises
Fakes, Stubs, and Mocks
Use Case Unit Testing
SQLite Integration Testing
Transaction Verification
FastAPI TestClient
API Contract Tests
Test Isolation
Test Coverage Limitations
```

Store reusable technical explanations, not the full learning narrative.

## Learning Journal

Append an entry that records:

- the student's most important insight about testing;
- a difficult test or debugging moment;
- a misconception that changed;
- the difference between what felt clear conceptually and what was difficult in code;
- a useful lesson about test quality or isolation.

Do not turn the journal into a copy of the Checkpoint Report.

## Questions

Update existing questions when Module 10 genuinely resolves them, especially:

- Q-0026 — testing thick Use Cases and multi-repository coordination;
- any open questions about reliable API testing or test isolation.

Do not mark a question as Mastered merely because the topic was discussed. Require demonstrated application.

Add new questions only when they emerge naturally from the work.

## Development Log

Record:

- what improved in the student's testing and reliability practices;
- which recurring difficulties remained;
- how independent the student was;
- what the module revealed about the teaching methodology;
- which adjustments would make the next module more effective.

Avoid copying broad praise from the Checkpoint Report. Prefer concrete observations and changes in the learning process.

---

# 20. Recommended Learning Resources

Use official documentation as a reference, not as a substitute for practical work.

- [pytest — How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest — How to parametrize tests](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [pytest — Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [FastAPI — Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Python — sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [SQLite — In-Memory Databases](https://www.sqlite.org/inmemorydb.html)

When documentation behavior depends on a library version, check the version installed in the student's project. Do not assume that a tutorial written for a different version matches the current environment.

---

# 21. Final Principle

Do not leave Module 10 thinking:

> “I know pytest.”

A more meaningful outcome is:

> **“I can describe the behavior my application promises, write focused tests for that behavior, choose the right test layer, isolate test data, verify important transaction guarantees, and explain what my tests do—and do not—prove.”**

The purpose of this module is not to make QR Warehouse look more sophisticated. It is to make its important behavior easier to trust and safer to change.

The student should leave this module with a stronger foundation for the next stage: building a client that relies on a stable API and evolving the backend without losing confidence in the existing functionality.
