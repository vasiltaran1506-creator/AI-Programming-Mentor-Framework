# Module 12 — PostgreSQL, Async Persistence & Database Migration

**Framework:** AI Programming Mentor Framework (APMF)  
**Version:** 0.1 Alpha  
**Status:** Proposed next module after Module 11  
**Stage:** Backend Foundations → Persistent Data & Database Migration  
**Primary project:** QR Warehouse  
**Primary language:** Python 3  
**Teaching language:** Russian  
**Estimated effort:** 23–36 focused hours (flexible; not a deadline)  
**Primary outcome:** Replace QR Warehouse's SQLite persistence with PostgreSQL while preserving business behavior and making the database integration understandable, testable, and maintainable.

---

# 1. Why Module 12 Exists

Module 11 moved QR Warehouse beyond the development computer. The application now has a first deployment on a physical Linux server, runs in Docker, keeps its SQLite data in persistent storage, and has a basic GitHub Actions CI workflow.

That is a meaningful operational milestone. It also makes the persistence layer the next useful place to learn.

The current application uses SQLite and a synchronous database interface. PostgreSQL is a separate database server: the application must connect to it, manage connections, execute queries, handle transactions, and deal with failures across a network boundary. Because the existing repositories contain SQLite-specific SQL and connection behavior, this transition is expected to require a real persistence-adapter refactor.

The purpose is **not** to replace technology for its own sake. The purpose is to learn how a backend application owns data access, transactions, database lifecycle, and reliable changes to a schema.

> **Central question:** How can QR Warehouse replace its database implementation without rewriting its domain rules or losing control of data integrity?

This module also provides a concrete and justified place to apply the student's existing knowledge of `async` / `await`. It must not turn into an abstract asyncio course: asynchronous code is introduced where the selected database interface actually requires it.

---

# 2. The Target State

At the end of this module, the intended development/deployment shape is:

```text
HTTP Client / existing CLI
          |
          v
     Presentation
          |
          v
    Application
      Use Cases
          |
          v
  Repository Contracts
          |
          v
 PostgreSQL Repository Adapter
          |
          v
 PostgreSQL service
          |
          v
 Persistent Docker volume
```

The intended container arrangement is:

```text
Docker Compose project
  ├── qr-warehouse application
  └── postgres database
           |
           └── named persistent volume
```

The exact implementation must be verified against the actual repository. Do not assume current filenames, table names, constructor signatures, or transaction boundaries without inspecting the code.

## What should remain stable

- Domain concepts and business invariants, unless the audit finds a real defect.
- The meaning and expected behavior of existing Use Cases.
- HTTP request/response contracts where no intentional API change is needed.
- Separation between Presentation, Application, Domain, and Infrastructure.
- Existing meaningful tests, with changes only when a test depends on SQLite-specific behavior rather than the intended contract.

## What may need to change

- Repository implementations and their database-specific SQL.
- Database connection and pool lifecycle.
- Repository method signatures if database operations become asynchronous.
- Use Cases that await asynchronous repository operations.
- FastAPI endpoint functions and application startup/shutdown handling.
- CLI entry-point orchestration if the CLI is retained and calls asynchronous Use Cases.
- Schema creation and upgrade process.
- Docker Compose configuration and CI environment.
- Tests and test fixtures that currently create SQLite connections directly.

A change is not justified merely because the new stack makes it possible. Each change should have a stated reason.

---

# 3. Learning Outcomes

By the end of Module 12, the student should be able to:

1. Explain the practical differences between SQLite and PostgreSQL for this application.
2. Explain the difference between a database server, a database, a connection, and a connection pool.
3. Inspect the current repositories and identify where SQLite-specific details have leaked into other layers.
4. Explain how PostgreSQL constraints and transactions help protect data integrity.
5. Choose a Python database interface deliberately, based on the project and learning objectives.
6. Implement PostgreSQL repository adapters without moving SQL into endpoints or Domain objects.
7. Understand why introducing async database I/O can require changes to the full call chain.
8. Use `async` / `await` correctly at the boundary between the application and database driver.
9. Manage connections and transactions without creating a new connection for every trivial operation or sharing one unsafe connection across unrelated concurrent requests.
10. Track schema changes with a repeatable migration process.
11. Test repository behavior and important Use Case invariants against a real, isolated PostgreSQL database.
12. Run PostgreSQL alongside the application through Docker Compose.
13. Configure CI to start a temporary test database and run the test suite against it.
14. Explain how to migrate existing data, verify the result, and retain a rollback path.
15. Identify which production concerns remain after the module rather than claiming the application is production-hardened.

---

# 4. Scope and Non-Goals

## In scope

- PostgreSQL fundamentals needed by QR Warehouse.
- Database roles, credentials, connection configuration, and least-privilege basics.
- A Python PostgreSQL interface and connection pooling.
- Async repository access if the chosen interface is asynchronous.
- Transactions, rollback, constraints, and multi-repository workflows.
- Schema migrations and development data migration where required.
- Docker Compose networking, health/readiness checks, and persistent storage.
- PostgreSQL-backed repository and integration tests.
- CI changes required to test the new persistence adapter.

## Explicitly out of scope for this module

- Building the desktop client or a full frontend.
- Implementing authentication and role-based authorization for users.
- Public internet exposure, HTTPS, reverse proxy, or domain setup.
- Kubernetes, microservices, distributed transactions, or high availability.
- Deep query optimization, replication, partitioning, or advanced PostgreSQL administration.
- Rewriting every part of QR Warehouse for stylistic consistency.
- Adding an ORM merely because it is popular.
- Converting every function in the repository to `async def` without a demonstrated need.

These topics may be relevant later, but they should not obscure the main goal: a correct, understandable database migration.

---

# 5. Prerequisites and Preflight

Before editing the persistence layer, the mentor must inspect the actual current project and verify the following:

- [ ] The current branch and working tree are known.
- [ ] A clean checkpoint or feature branch exists for the migration.
- [ ] The latest intended commit is present on the remote repository.
- [ ] The current tests have been run and their actual results recorded.
- [ ] The current SQLite schema and repository implementations have been inspected.
- [ ] The current transaction flow has been traced through at least one Use Case that writes data.
- [ ] The role of the CLI is clarified: preserve it, adapt it, or explicitly defer it.
- [ ] It is known whether the deployed SQLite database contains data worth preserving.
- [ ] There is no accidental access to the production/deployed database from tests.
- [ ] The server's disk space and memory constraints have been considered before adding another service.

If a prerequisite is not satisfied, resolve or document it before beginning the migration. Do not infer successful tests from the presence of test files or a green CI badge alone.

---

# 6. Phase A — Audit the Existing Persistence Boundary

**Goal:** Understand what must change before choosing implementation details.

## Topics

- What a repository contract promises to the Application Layer.
- Which details belong only to Infrastructure.
- The current SQLite connection lifecycle.
- Where `commit()` and `rollback()` happen today.
- How multiple repositories participate in one Use Case.
- How SQL parameters, rows, identifiers, booleans, and missing records are represented.
- Whether the API creates connections/repositories at import time and whether that complicates lifecycle and test isolation.

## Practical task A1: Trace a complete write workflow

Choose one representative operation that writes related data—for example, adding an item to an estimate. Trace:

```text
HTTP request or CLI command
  -> endpoint / CLI entry point
  -> Use Case
  -> repository contract
  -> SQLite repository
  -> SQL and transaction
  -> returned result / error
```

Write down which component owns each decision and which component performs each side effect.

## Practical task A2: Write a migration-impact map

Create a compact table in the module notes:

| Component | Current SQLite-specific knowledge | Expected change | Must business behavior remain the same? |
|---|---|---|---|
| Domain | Inspect actual code | Usually none | Yes |
| Application / Use Cases | Inspect calls and transaction flow | Possibly async call chain / transaction coordination | Yes, unless a defect is demonstrated |
| Repository contracts | Inspect signatures | Possibly async signatures | Same meaning; signature can change |
| SQLite adapter | SQL, connection, row conversion | Replace or retire | No SQLite detail should leak outward |
| FastAPI / CLI composition roots | Lifecycle and object creation | Adapt to pool and async lifecycle | External behavior should remain intentional |
| Tests | SQLite fixtures and assertions | Split unit vs PostgreSQL integration tests | Preserve meaningful contracts |

This map is a planning tool, not a requirement to create new architecture layers.

## Phase A exit condition

The student can explain, using actual project code, why the migration affects more than connection settings and can identify the smallest vertical slice to migrate first.

---

# 7. Phase B — PostgreSQL Fundamentals Through the Project

**Goal:** Understand the database server model before connecting the application.

## Topics

- PostgreSQL server process vs database vs schema vs table.
- Database roles and credentials.
- TCP host/port and connection strings.
- Primary keys, foreign keys, `NOT NULL`, `UNIQUE`, and `CHECK` constraints.
- Transactions and atomicity.
- Identity/sequence behavior where applicable.
- Differences from SQLite that matter to the current schema and queries.
- Why PostgreSQL inside Compose is reached from the app container by service name rather than by `localhost`.

## Practical task B1: Run PostgreSQL in Docker Compose

Add PostgreSQL as a separate service in a development Compose configuration.

Requirements:

- [ ] Pin an intentional PostgreSQL major image version; avoid an unexamined floating tag.
- [ ] Use a named volume for database data.
- [ ] Use environment variables for initialization settings and credentials; do not commit real passwords.
- [ ] Configure a health check and distinguish container start from database readiness.
- [ ] Make the app connect through the Compose service name and internal port.
- [ ] Publish the database port to the host only if required for local development; do not expose it to the LAN/WAN by default.
- [ ] Document which data lives in the volume and what happens if the volume is deliberately deleted.
- [ ] Confirm that deleting/recreating the application container does not delete database data.

Use non-production development data and credentials in this phase.

## Practical task B2: Test data integrity deliberately

Use a small experiment to demonstrate:

1. a valid insert;
2. a foreign-key violation;
3. a constraint violation;
4. a transaction that is rolled back;
5. data surviving an app-container recreation;
6. data not being recoverable merely because a volume existed after that volume itself was deleted.

Record the observed result and explain it. Do not treat a successful command as sufficient evidence on its own.

## Phase B exit condition

The student can explain the database's lifecycle in Compose and why PostgreSQL must not be treated as a disposable part of the application container.

---

# 8. Phase C — Choose the Python Database Interface

**Goal:** Make one deliberate tooling decision before rewriting repositories.

Two reasonable paths exist. The mentor must compare them briefly against the actual codebase and select one primary path. Do not combine both in production repositories unless there is a specific reason.

## Path A — `asyncpg` directly

Potential advantages:

- Direct exposure to PostgreSQL queries and parameters.
- A relatively small application-level abstraction.
- Explicit control over connections, pools, transactions, and returned records.
- Good fit for learning how asynchronous database I/O works at the driver boundary.

Costs and design considerations:

- SQL and PostgreSQL-specific behavior remain explicit in repository code.
- Parameter syntax differs from SQLite's `?` placeholders; `asyncpg` normally uses `$1`, `$2`, and so on.
- A connection pool and its lifecycle must be designed deliberately.
- Schema migration tooling needs a clear, separate integration decision.

## Path B — SQLAlchemy Core with its async engine and PostgreSQL driver

Potential advantages:

- An established async connection/engine abstraction.
- A natural integration path with Alembic schema migrations.
- SQLAlchemy Core can be used without adopting the ORM or declarative model layer.

Costs and design considerations:

- Introduces another abstraction that must be understood.
- Requires learning its connection, result, and transaction APIs.
- May result in a wider change to query construction than a direct driver migration.

## Decision rule

The aim is not to select the option that looks most professional. Compare:

- the current SQL and repository structure;
- the desire to learn the actual async database boundary;
- migration and schema-versioning requirements;
- testability and debugging clarity;
- the amount of unnecessary abstraction introduced.

**Default recommendation for discussion:** because the current repositories already contain explicit SQL, investigate direct `asyncpg` first. Evaluate Alembic integration separately. If keeping the migration workflow simple requires SQLAlchemy Core as the application persistence interface, the mentor may recommend that instead, but must explain why before implementation. Do not introduce SQLAlchemy ORM unless a real project requirement justifies it.

## Practical task C1: Small isolated experiment

Before touching QR Warehouse, make a tiny program that:

- opens a connection or obtains one from a pool;
- inserts one row with parameterized SQL;
- reads it back;
- updates it;
- deliberately raises an error inside a transaction and confirms rollback;
- closes/releases resources correctly.

The student must be able to explain each `await`, context manager, and returned value. Do not proceed by copying an unexplained code block.

## Phase C exit condition

The tool choice is written down with reasons and acknowledged trade-offs. The tiny experiment passes and its behavior is understood.

---

# 9. Phase D — Migrate the Repository Adapter

**Goal:** Replace persistence mechanics while preserving business rules.

## Implementation order

1. Start with one small, read-only repository operation.
2. Implement and test its PostgreSQL version.
3. Migrate one write path.
4. Migrate the smallest meaningful vertical slice through API → Use Case → repository → PostgreSQL.
5. Continue repository-by-repository, keeping working checkpoints.
6. Remove SQLite-specific implementation code only after the PostgreSQL path is verified and the fallback/rollback decision is clear.

## Required concepts

- Parameterized SQL. Never interpolate user-controlled values into SQL strings.
- Mapping database result rows to Domain/data-transfer structures deliberately.
- Handling “not found” as a defined repository/application result, not an accidental `None` or driver exception leaking into HTTP.
- Database exceptions versus application errors.
- Connection acquisition and release.
- Connection pool lifecycle.
- Transactions across a multi-step Use Case.
- Cancellation and exceptions in async code.
- Avoiding blocking synchronous database calls inside an async request path.

## Async rules

If the selected driver is asynchronous:

- Methods that perform async database operations must be declared and called appropriately; callers must `await` the result.
- The async call chain must be traced from the entry point to the database.
- Do not put `asyncio.run()` inside ordinary Use Cases or nested event-loop contexts.
- Create and close the pool at a clear application lifecycle boundary, not repeatedly for each query.
- Do not share a single connection among unrelated concurrent requests without a driver-supported design.
- Keep database-specific imports and record types inside Infrastructure.
- Do not change every endpoint to `async def` just for appearance; each change must follow the actual awaited call chain and framework behavior.

## Transaction ownership review

The current project has previously placed some `commit()` / `rollback()` behavior inside Use Cases through repository/connection access. Do not blindly reproduce this or perform a sweeping Unit of Work refactor at the same time.

First document the present transaction boundary. Then select the smallest design that correctly handles the chosen workflows:

- a Use Case that writes a single row;
- a Use Case that writes related rows through multiple repositories;
- a failure occurring after one of those writes.

All writes that must succeed or fail together must use the same database transaction. Introduce a Unit of Work or equivalent transaction abstraction only if it reduces real coupling or makes the transactional contract materially clearer. Explain its cost if you introduce it.

## Phase D exit condition

At least one end-to-end API operation uses PostgreSQL, returns the expected response, and preserves the existing business invariant. The implementation keeps SQL and driver-specific types out of Domain and Presentation.

---

# 10. Phase E — Schema Migrations and Existing Data

**Goal:** Make schema changes repeatable and avoid accidental data loss.

## Schema migration strategy

The project needs a versioned, repeatable way to create and evolve the PostgreSQL schema. Choose a migration tool and explain why. Alembic is a candidate, especially if SQLAlchemy Core/async engine is selected. If the application uses direct `asyncpg`, the mentor must explain how migration scripts are executed and tracked; do not pretend Alembic works without its SQLAlchemy-based migration environment.

Required concepts:

- schema creation vs schema migration;
- migration revision/order;
- applying migrations to an empty database;
- applying later migrations to an existing database;
- inspecting a migration before applying it;
- safe handling of destructive changes;
- why schema creation should not silently happen as a side effect of importing the application.

## Existing SQLite data decision

First establish whether the deployed SQLite database contains data worth preserving. If it contains only disposable learning/test data, an explicitly documented clean PostgreSQL initialization may be reasonable. If useful data exists, make a deliberate migration plan.

For a data migration, the plan must include:

1. a backup or immutable copy of the SQLite source;
2. an inventory of tables and relevant constraints;
3. a deterministic export/import method;
4. handling of primary keys and related foreign keys;
5. row-count checks and domain-level consistency checks;
6. verification of estimates and their item snapshots where relevant;
7. a clear statement of which database is authoritative during migration;
8. a rollback/recovery plan if verification fails.

Do not delete the original data source until the PostgreSQL result has been verified. Do not add dual writes or dual reads unless a real zero-downtime requirement exists.

## Phase E exit condition

A new empty database can be created from migrations in a repeatable way. If data transfer was required, the imported data is verified. If it was not required, that decision and the initialization procedure are documented.

---

# 11. Phase F — Tests Against Real PostgreSQL

**Goal:** Test database-specific behavior without turning the module into a coverage contest.

SQLite and PostgreSQL are not identical. A passing SQLite test suite does not prove PostgreSQL-specific SQL, constraints, transactions, or type conversion are correct.

## Test layers

### Unit tests

Keep fast tests for business behavior using small fakes where they give a useful signal. They should not require a running PostgreSQL server.

### Repository integration tests

Use a dedicated test database/service. Verify actual SQL and database semantics. Do not point test fixtures at the deployed database or any database containing data worth keeping.

### API integration tests

Use the FastAPI TestClient or the project's chosen test approach to verify a small set of important contracts while the API uses the PostgreSQL adapter.

## Minimum meaningful scenarios

- [ ] Valid repository insert and read-back.
- [ ] Not-found behavior.
- [ ] Invalid quantity or other important domain boundary.
- [ ] Foreign-key or uniqueness constraint behavior, where applicable to the real schema.
- [ ] A multi-step Use Case succeeds atomically.
- [ ] A deliberately induced failure rolls back all writes in the transaction.
- [ ] Important historical snapshot data remains correct after the related catalog value changes, if that invariant exists in the current project.
- [ ] Tests are isolated from each other and use a dedicated test database.
- [ ] Tests do not rely on execution order or manually cleaned deployed state.

Do not add tests solely to reach an arbitrary number or coverage percentage. Select them because they protect real behavior or expose a database-specific risk.

## CI integration

Update GitHub Actions so it can start a temporary PostgreSQL service, wait for it to become ready, prepare the test schema through the chosen migration process, and run the relevant tests. Use disposable CI credentials and never pass production credentials to the workflow.

The CI result should make clear whether it tested unit behavior, PostgreSQL integration behavior, or both. A green result is useful evidence, not a guarantee that every production failure mode has been covered.

## Phase F exit condition

The new persistence layer is covered by a small, relevant test set that exercises real PostgreSQL behavior and runs reliably in CI.

---

# 12. Phase G — Deployment Integration and Verification

**Goal:** Make the migrated application work with PostgreSQL in the existing deployment model.

Verify, rather than assume:

- [ ] The application and PostgreSQL run as distinct Compose services.
- [ ] The application uses the internal Compose service name to connect to the database.
- [ ] PostgreSQL data is stored in a named volume.
- [ ] Database credentials are configuration, not committed secrets or baked into the image.
- [ ] Application startup handles database readiness and connection failure clearly.
- [ ] A restart of the application container does not reset the database.
- [ ] A restart/recreation of the PostgreSQL container preserves data when its intended volume is retained.
- [ ] Migrations are applied through an explicit and documented procedure.
- [ ] Logs give enough information to diagnose connection and startup failures without printing secrets.
- [ ] The application passes its intended smoke test after deployment.
- [ ] CI uses a separate database from the deployed instance.

A production-style backup-and-restore system is not a compulsory deliverable of this module, but its need must remain visible. The existence of a volume is not a backup strategy.

## Phase G exit condition

The deployed QR Warehouse uses PostgreSQL, the expected core workflow succeeds, data persists across the tested restart scenarios, and CI validates the new database adapter using an isolated database.

---

# 13. Mentor Teaching Protocol

The mentor should preserve the student's preferred learning sequence:

```text
Real problem
    ↓
Mental model
    ↓
Concept and trade-offs
    ↓
Small isolated experiment
    ↓
Guided implementation
    ↓
Independent implementation
    ↓
Integration into QR Warehouse
    ↓
Verification and reflection
```

## Guidance level

Start with a guided audit and one small experiment. Then reduce assistance progressively.

When a failure occurs, do not immediately supply a complete fix. Ask the student to identify:

1. what was expected;
2. what actually happened;
3. which layer the error belongs to;
4. what evidence would distinguish plausible causes;
5. what the smallest safe experiment would be.

The mentor must not generate the entire migration at once. Work in vertical slices and preserve working checkpoints.

## Scope discipline

The student is interested in the long-term commercial product. Respect that goal, but distinguish:

- a correctness issue that blocks this migration;
- an architectural decision that must be made now;
- a production concern that is real but belongs to a later module;
- an interesting topic that can be recorded without being implemented now.

A simpler solution is preferred when it satisfies the current requirements and keeps the next change understandable.

---

# 14. Completion Criteria

Module 12 reaches **Minimum Viable Completion** when all essential items are satisfied. It does not claim mastery of PostgreSQL administration or production database engineering.

```text
[ ] The student can explain why PostgreSQL is appropriate for the project's current direction.

[ ] The current SQLite persistence boundary and transaction flow were audited.

[ ] A Python database-interface choice was made and justified before the full migration.

[ ] PostgreSQL runs as a distinct service in Docker Compose.

[ ] The chosen connection/pool lifecycle is explicit and understood.

[ ] The PostgreSQL repository adapter implements the required existing contracts or their intentionally updated async equivalents.

[ ] Core Domain behavior and HTTP contracts remain stable unless an intentional change is documented.

[ ] SQL and driver-specific records remain inside Infrastructure.

[ ] At least one multi-step write workflow has an explicit, correct transaction boundary.

[ ] Schema changes can be applied repeatably to a new database.

[ ] Existing data was migrated and verified, or a justified decision was made that no data migration was needed.

[ ] Relevant PostgreSQL integration tests exercise the real database.

[ ] CI can provision an isolated test database and run the required tests.

[ ] The deployed application uses PostgreSQL and passes a smoke test.

[ ] Persistence is verified through controlled restart/recreation tests.

[ ] The student can explain the remaining risks and deferred production work.
```

If a nonessential element, such as complete CLI adaptation or full data migration, is deliberately deferred, it must be documented with a reason and a follow-up point. Do not silently mark incomplete work as completed.

---

# 15. Suggested Time Budget

These are planning estimates, not quotas.

```text
Audit current persistence and transaction flow     2–4 h
PostgreSQL fundamentals and Compose service        3–4 h
Driver/library decision and isolated async test    2–4 h
Repository migration in vertical slices            7–10 h
Schema migration / data-transfer decision          3–5 h
PostgreSQL tests and CI integration                4–6 h
Deployment verification and final review           2–3 h

Estimated total                                   25–36 h
```

If the actual code reveals greater migration risk, stop and reassess scope rather than rushing or performing a broad, unexplained rewrite.

---

# 16. Questions for the Student

Use these as discussion prompts throughout the module, not as a one-time exam.

1. Why might PostgreSQL be a better fit than SQLite for the planned QR Warehouse product? What does PostgreSQL cost in return?
2. Which parts of the application should remain unchanged during a database migration?
3. What is the difference between a database connection and a connection pool?
4. Why is `localhost` inside the application container not the PostgreSQL service in a separate Compose container?
5. What changes when a repository method becomes asynchronous? Which callers are affected?
6. Why should a connection pool belong to an application lifecycle rather than one individual query?
7. How can two repositories participate in one transaction without committing partial work?
8. Which tests must use real PostgreSQL, and which can stay as unit tests with fakes?
9. What does a schema migration record that a `CREATE TABLE IF NOT EXISTS` statement does not?
10. How would you verify that an SQLite-to-PostgreSQL data migration did not lose relationships or historical estimate values?
11. What evidence would demonstrate that a PostgreSQL test is isolated from the deployed database?
12. What is the difference between a persistent volume and a backup?
13. What would make an async database implementation more complex without providing value?
14. Which production concerns should be deferred until the core migration is correct?

---

# 17. References

Use official documentation as a reference, not as a replacement for guided explanations and experiments.

- PostgreSQL documentation: https://www.postgresql.org/docs/current/
- PostgreSQL `CREATE TABLE` and constraints: https://www.postgresql.org/docs/current/sql-createtable.html
- `asyncpg` documentation: https://magicstack.github.io/asyncpg/current/
- `asyncpg` transactions and connection pools: https://magicstack.github.io/asyncpg/current/usage.html#transactions and https://magicstack.github.io/asyncpg/current/usage.html#connection-pools
- Alembic documentation: https://alembic.sqlalchemy.org/en/latest/
- Alembic asyncio cookbook: https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic
- SQLAlchemy asyncio documentation (for the SQLAlchemy Core option): https://docs.sqlalchemy.org/en/21/orm/extensions/asyncio.html

---

# 18. Final Principle

> The purpose of Module 12 is not to make QR Warehouse use more technologies. It is to make the persistence boundary reliable and understandable, and to teach the student how to change an infrastructure component without losing control of the application.

**End of Module 12.**
