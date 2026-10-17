# Checkpoint Report — Module 10: Testing, Quality & Reliability

**Framework:** AI Programming Mentor Framework (APMF)  
**Version:** 0.2 — revised after evidence review  
**Status:** Completed — Minimum Viable Completion  
**Review date:** 2026-10-17  
**Student:** Vasily  
**Stage:** Stage 8 — Application Development  
**Teacher:** AI Programming Mentor (Qwen)  
**Project context:** QR Warehouse

---

## 1. Executive summary

Module 10 is being closed as **Minimum Viable Completion**, not as full mastery of software testing.

The original checkpoint report describes substantial practice with `pytest`, test doubles, fixtures, parametrization, Use Case behavior, and a SQLite rollback scenario. The additional API test snippet reviewed for this revision demonstrates basic use of FastAPI's `TestClient` to check successful creation, not-found responses, and request validation.

The evidence supports moving on to the next learning focus—Linux, the home server, deployment, Docker, and CI/CD—while retaining testing as an ongoing engineering practice. It does **not** establish that every testing competency is mastered, that all tests are isolated from the application's normal database, or that the transaction test's assertions were independently verified against freshly queried database state.

**Decision:** Stop repetitive expansion of the Module 10 exercise set for now. Record the gaps accurately and revisit them when they serve a concrete purpose, especially during CI setup or when a new bug or feature calls for a test.

## 2. Scope and evidence reviewed

This assessment uses two sources:

1. The original Module 10 checkpoint report, which describes Unit and Integration tests written for `AddItemToEstimate`, fixtures and test doubles, a `SaboteurEquipmentRepository`, and a SQLite rollback test.
2. The additional API test snippet supplied for this review. It contains four tests: `test_create_estimate`, `test_get_estimate_not_found`, `test_add_item_to_nonexistent_estimate`, and `test_create_estimate_invalid_data`.

The source code for the underlying application, the complete test suite, the pytest run output, and the full transaction test were **not** included in this review. Claims about those parts are therefore retained as previously reported evidence, not independently verified findings.

## 3. Demonstrated work

### 3.1 Testing concepts and techniques reported in the original checkpoint

The original report records practice with:

- Arrange–Act–Assert (AAA) structure.
- In-memory fakes for equipment and estimate repositories.
- A stub for connection commit/rollback behavior.
- `pytest` fixtures, including a `@dataclass` fixture and `tmp_path`.
- `@pytest.mark.parametrize` for quantity boundary cases.
- A test seam using `SaboteurEquipmentRepository` to trigger a failure.
- Unit tests for several `AddItemToEstimate` outcomes.
- An integration test intended to verify SQLite transaction rollback.
- A test-driven fix for the `quantity <= 0` validation rule.

These are relevant testing exercises. The corresponding full test files were not part of the material reviewed here, so this report does not independently certify every assertion or implementation detail.

### 3.2 What the supplied API tests demonstrate

The supplied snippet shows the student can use `TestClient` to send HTTP requests to a FastAPI application and assert status codes and response fields.

| Test | What it checks | Assessment |
|---|---|---|
| `test_create_estimate` | `POST /estimates` returns `201`; response fields match the request; `estimate_id` is an integer; cleanup request returns `204` | Useful basic success-path contract check. Cleanup is attempted, but is not protected by `try/finally`; a failure before cleanup could leave data behind. |
| `test_get_estimate_not_found` | `GET /estimates/99999` returns `404` and `error == "estimate_not_found"` | Checks an error response, but the fixed ID is not guaranteed to remain nonexistent in every database state. |
| `test_add_item_to_nonexistent_estimate` | `POST /estimates/99999/items` returns `404` and the expected error code | Checks another error contract, with the same fixed-ID limitation. |
| `test_create_estimate_invalid_data` | Omitting required `days` returns `422` | Useful request-validation check for the shown invalid payload. It checks the status code, not the structure of validation details. |

**Conclusion from this snippet:** basic API contract testing has been practiced. The snippet does **not** demonstrate isolated API tests using dependency overrides or a dedicated test database. It imports `app` directly from `routes` and does not show an override or test-database setup, so isolation from the application's normal database cannot be confirmed from this code alone. Additional global setup may exist elsewhere, but it was not supplied.

### 3.3 Limits of the evidence

This review cannot confirm:

- Whether all tests pass in the current repository.
- Whether the transaction test reads persisted values back from SQLite after rollback, rather than only checking in-memory objects.
- Whether `routes.app` is configured elsewhere to use a test database.
- Whether cleanup and database state remain reliable when tests run repeatedly or in parallel.
- Whether the student can transfer the same techniques independently to an unfamiliar codebase.

These are evidence gaps, not proof that the tests are incorrect.

## 4. Competency assessment

Levels use the APMF scale:

- **0 — Not encountered / not assessed**
- **1 — Conceptual familiarity**
- **2 — Guided application**
- **3 — Independent application in a familiar context**
- **4 — Independent transfer and justified trade-offs**

The level describes the current evidence, not a permanent label. Confidence indicates how strongly the reviewed material supports the assessment.

| Competency | Provisional level | Confidence | Evidence and limits |
|---|---:|---|---|
| TEST-001 — Test Anatomy | 3 — Independent application in familiar context | Medium | The original report describes AAA tests with result/state assertions. Full test files were not independently reviewed in this pass. |
| TEST-002 — pytest Fixtures | 3 — Independent application in familiar context | Medium | The original report describes `@dataclass`, `tmp_path`, `yield`, cleanup, and `conn.close()`. The fixture implementation was not included in the supplied API snippet. |
| TEST-003 — Parametrization | 3 — Independent application in familiar context | Medium | The original report describes quantity boundary tests using `@pytest.mark.parametrize`; the corresponding code was not supplied for this review. |
| TEST-004 — Test Doubles | 3 — Independent application in familiar context | Medium | Fakes, a connection stub, and a saboteur are described in the original report. Their complete implementations were not re-reviewed here. |
| TEST-005 — Use Case Testing | 3 — Independent application in familiar context | Medium | The original report lists several `AddItemToEstimate` outcomes. Other Use Cases have not been demonstrated in the reviewed evidence. |
| TEST-006 — Transaction Verification | 2–3 — Provisional; verify evidence | Low–Medium | The original report describes a failure between writes and a rollback assertion. To confirm the test's strength, inspect whether persisted state is re-read from SQLite after the failed transaction. |
| TEST-007 — API Contract Testing | 2 — Basic application demonstrated | Medium–High | The supplied code checks success, not-found responses, and validation status with `TestClient`. Dependency-override isolation is not shown. |
| TEST-008 — Test Isolation | 2 — Partial evidence | Medium | The original report describes `tmp_path` for integration tests. The supplied API snippet does not show database isolation and may use the application's configured database. Do not generalize isolation across all test types yet. |
| TEST-009 — Failure Diagnosis | 2–3 — Provisional | Medium | The original report lists concrete Python and pytest mistakes and subsequent corrections. The complete troubleshooting history was not independently reviewed in this pass. |
| TEST-010 — Test Quality Judgment | Not yet assessed as Level 4 | Low | Choosing to stop repetitive work can be a reasonable scope decision, but by itself it does not demonstrate independent transfer of test-quality judgment across different systems. |

### Calibration note

The earlier report assigned Level 4 with high confidence to TEST-010 because the student chose to stop expanding tests. That claim has been revised. The decision may be sensible and aligned with the student's learning priorities, but it is evidence of a **scope and motivation decision**, not sufficient proof of Level 4 testing expertise.

Likewise, Level 3 ratings above are provisional where the original report—not the complete code—was the evidence source. Ratings should be updated if the teacher later inspects the actual tests or observes the student writing comparable tests with less assistance.

## 5. Strengths supported by the available material

- The student has worked with multiple test types rather than only checking that code runs manually.
- The original report describes tests focused on observable behavior and state invariants.
- The reported use of fakes, fixtures, parametrization, and a failure-injection seam covers several useful testing techniques.
- The supplied API snippet demonstrates checks of response status codes and selected response fields.
- The student has identified recurring Python and pytest mistakes, including dictionary-versus-attribute access, object-versus-collection confusion, control-flow placement, mismatched fake signatures, and the difference between raised exceptions and returned error results.
- The student has identified a motivation problem with repetitive test expansion and wants to redirect effort toward a practical infrastructure project.

The last point is a valid learning-planning consideration. It should not be overstated as proof of broad engineering maturity or mastery.

## 6. Remaining gaps and risks

### API test isolation

The supplied snippet creates `TestClient(app)` directly and does not show dependency overrides, a test database, or a fixture that swaps the application's persistence dependency. The successful creation test deletes the created estimate afterward, but this is not guaranteed to run if an earlier assertion fails. The other tests use a fixed ID (`99999`), which is not guaranteed to remain unused.

**Later improvement:** configure a dedicated test database or override the application's database/repository dependency. Make setup and cleanup deterministic. If cleanup is necessary, use a fixture or `try/finally` so it also runs when assertions fail.

### Transaction rollback evidence

The original report says the rollback test proves SQLite atomicity by checking that the estimate has no items and equipment availability is unchanged. This is strong evidence only if the test exercises the real transaction and verifies persisted state after the failure. The full test was not supplied here, so the claim should remain provisional until that implementation is checked.

### Breadth of Use Case testing

The original report says `AddItemToEstimate` received the most detailed coverage, while `ChangeItemQuantity` and `DeleteItemFromEstimate` were deferred. That is acceptable for this checkpoint if the goal is to learn core testing concepts rather than achieve comprehensive coverage. It does mean the report should not imply that the application's Use Cases are broadly covered.

### Transfer to unfamiliar systems

The available evidence is primarily from the familiar QR Warehouse codebase. Transfer to an unfamiliar codebase has not been demonstrated and should remain a future learning objective, not an assumed competency.

## 7. Decision on Module 10

**Recommendation: close Module 10 as Minimum Viable Completion and move on.**

The decision is based on the learning plan and the evidence already described—not on a claim that every testing competency has been mastered.

The student does not need to write repetitive tests for every Use Case merely to satisfy a coverage target before proceeding. At the same time, the existing tests should not be treated as finished, production-grade quality assurance without checking their isolation and behavior.

Testing should continue as part of ordinary development:

- Add tests when implementing meaningful new behavior or fixing a bug.
- Revisit API isolation when setting up CI.
- Inspect the transaction test when its full source is available.
- Add tests for other Use Cases when the risk or a concrete change justifies them.

## 8. Recommended next steps

1. **Proceed to the home-server and deployment learning track.** This aligns with the student's current interests and gives the existing application a practical deployment target.
2. **Keep the current tests in the repository.** Do not delete or dismiss them because the module is being closed.
3. **Use the existing test suite in CI.** Start with a pipeline that installs dependencies and runs `pytest`; treat failures as useful feedback.
4. **Address API isolation when it becomes relevant.** Configure a test database or dependency override before relying on API tests in a repeatable CI environment.
5. **Verify the rollback test when convenient.** Check that it reads persisted database state after the failure and confirms the intended transaction boundary.
6. **Avoid a forced test-expansion backlog.** Write tests for additional Use Cases when a concrete feature, defect, or risk makes them useful.

Docker, PostgreSQL migration, and deployment are potential future exercises—not prerequisites that must all be completed immediately in order to close Module 10.

## 9. Revised mentor assessment

The available evidence supports the conclusion that the student has gained **practical introductory experience with software testing** in the QR Warehouse project. The original checkpoint describes useful work with Unit and Integration tests, test doubles, fixtures, parametrization, and transaction failure simulation. The supplied API tests add evidence of basic FastAPI endpoint and validation testing.

The evidence does not yet establish comprehensive test isolation, broad Use Case coverage, or Level 4 transfer of testing judgment. Those gaps are documented rather than treated as failures.

The agreed next step is to close the module at Minimum Viable Completion and continue into Linux, the home server, deployment, Docker, and CI/CD. Testing will remain part of that work, with API isolation and rollback verification revisited when they have a concrete role.

## 10. Student reflection

These questions are optional and can be answered later:

1. Which type of test—Unit or Integration—became clearer, and why?
2. What did the SQLite integration test demonstrate that a Unit test with fakes could not?
3. How did testing help identify the `quantity <= 0` bug?
4. What was hardest in this module: the concepts, pytest syntax, or motivation to continue?
5. Does closing the module at Minimum Viable Completion feel like a useful scope adjustment?
6. Which testing topic would be most useful to revisit while configuring CI/CD?

## 11. Report usage

### For the AI teacher

- Avoid repeating test-expansion exercises that add little new learning value.
- Refer to this report when wiring the current tests into CI.
- Revisit API isolation and rollback verification when the relevant source code is available.
- Track assistance and transfer separately from the apparent correctness of the final code.

### For the student

- Treat this as a checkpoint of current evidence, not a claim that testing is “finished forever.”
- Keep the test suite and apply it when adding features or fixing bugs.
- Return to the listed gaps when they become relevant to deployment or CI.

### For curriculum planning

- Minimum Viable Completion can be used to preserve learning momentum when additional repetition has low expected value.
- Do not convert one scope decision into a high-level competency rating without further evidence.
- Prefer later practice in a meaningful project context over arbitrary coverage targets.

---

**End of Checkpoint Report v0.2**
