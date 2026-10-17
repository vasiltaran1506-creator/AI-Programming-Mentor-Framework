# Module 11 — Home Server, Linux, Docker & Deployment

**Framework:** AI Programming Mentor Framework (APMF)  
**Version:** 0.1 — proposed module  
**Stage:** Application Delivery / Infrastructure Foundations  
**Prerequisites:** Modules 00–10; Module 10 closed at Minimum Viable Completion  
**Primary project:** QR Warehouse  
**Communication language:** Russian  
**Curriculum language:** English  
**Estimated effort:** 25–40 focused hours, depending on hardware, installation state, and database migration complexity  
**Module type:** Guided infrastructure practice with a real project  
**Primary outcome:** A reproducible, testable QR Warehouse deployment on a home server, initially reachable only from the trusted local network

---

## 1. Why Module 11 Exists

QR Warehouse has evolved beyond an isolated Python exercise. It contains an application structure with Domain, Application, Infrastructure, and Presentation concerns; repository implementations; SQLite persistence; a FastAPI HTTP API; and an initial set of automated tests. Module 10 provided useful testing practice and was deliberately closed as **Minimum Viable Completion**.

The next bottleneck is no longer adding more tests merely to increase their number. The next bottleneck is learning how software is run, maintained, and delivered outside the development environment.

Module 11 moves QR Warehouse from “a program that runs on the developer's machine” toward “a service that can be started, observed, updated, backed up, and tested in a repeatable way.”

The central question is:

> **How do I turn a Python web application into a service that I can reliably operate on a Linux server?**

The learning process must remain incremental. Do not attempt to design a production platform, expose the application to the public internet, or rewrite the project before the first local deployment works.

## 2. Evidence-Based Starting Point

Use the latest Module 10 checkpoint report as the transition note. It records that:

- Module 10 is complete at Minimum Viable Completion, not full mastery of testing.
- The student practised pytest, test doubles/fakes, fixtures, parametrization, Use Case tests, and a SQLite rollback scenario as reported by the original checkpoint.
- The supplied API test snippet demonstrates basic FastAPI `TestClient` checks for successful creation, not-found responses, and validation errors.
- The complete test suite and all underlying source were not independently verified in that checkpoint. Do not overstate test coverage or claim all test isolation is proven.
- Some testing gaps are intentionally deferred until there is a concrete reason to revisit them, especially CI setup or a feature/bug that calls for another test.
- The recommended next focus is Linux/home-server setup, Docker, PostgreSQL as a deployment exercise, and CI/CD that runs existing tests on pushes.

Treat these as checkpoint-reported evidence, not a guarantee that every implementation is correct. At the beginning of the module, inspect the current repository and test run before making changes.

## 3. Student Context and Constraints

The student is learning Linux administration alongside Python backend development and does not yet have a strong mental model of Linux filesystems, services, permissions, or server operations. The student knows basic terminal commands such as `cd`, `pwd`, `mkdir`, and `ls`.

The student has a Kubuntu desktop environment and has been considering a separate home-server machine assembled from existing components. The known parts discussed include an Asus B85M-K motherboard, Intel Xeon E3-1231 v3, 8 GB DDR3 RAM, and a 120 GB SSD; a discrete GPU may be available but is not expected to be necessary for a headless server. Confirm actual hardware and current installation state before relying on these details. A previously replaced AeroCool VX550 Plus PSU was associated with crashes under combined CPU/GPU load; do not recommend it for unattended server use without proper independent verification. Prefer stable, known-good power hardware.

The student has a gray/non-public home WAN address and has previously considered using a VPS with a public IP as a secure access point. That remote-access topology is **not part of the first deployment milestone**. Start with local-network access, verify the service is stable, and establish a security baseline before planning any external access.

The student prefers understanding decisions rather than blindly copying commands or accepting generated code. Explain the purpose and trade-offs of each major choice.

## 4. Guiding Principles

1. **Make one change at a time.** Preserve a known-working state after each milestone.
2. **Deploy locally before exposing remotely.** The initial goal is LAN-only access.
3. **Prefer reversible operations.** Back up existing data before changing schemas, volumes, configuration, or OS installation.
4. **Keep the project architecture intact.** Infrastructure work must not become an excuse for a full rewrite.
5. **Use tests as a practical safety net.** Run the current tests before and after meaningful changes; add tests only when they protect a real behavior or operational risk.
6. **Avoid cargo-cult DevOps.** Use Docker Compose and a small CI workflow only where they solve an actual problem.
7. **No secrets in source control.** Credentials belong in local environment/configuration mechanisms that are excluded from Git.
8. **Document only what is needed.** The module file is the plan. Do not create a parallel administrative framework or demand a large report.
9. **Be transparent about evidence.** Distinguish verified behavior from assumed behavior, and verified tests from tests merely described in previous reports.
10. **Teach the operating model.** A command is not understood merely because it ran successfully.

## 5. Learning Outcomes

By the end of Module 11, the student should be able to:

- explain the difference between a development environment, a server OS, a process, a service, a container image, a container, a port, and a persistent volume;
- administer the server using a non-root account and SSH;
- inspect service status and logs using appropriate Linux tools;
- describe the minimum firewall/network rules needed for local access;
- build and run QR Warehouse's API in a Docker container;
- use Docker Compose to define the application and its runtime configuration;
- preserve application data outside a disposable container layer and explain the backup implications;
- configure the app without committing secrets or environment-specific settings;
- evaluate whether the existing SQLite implementation should remain for the first deployment or be migrated to PostgreSQL;
- if the PostgreSQL migration is feasible within the module, run the database as a separate service, apply a deliberate schema/data migration, and verify application behavior;
- configure CI to run the project's available tests automatically on pushes or pull requests;
- troubleshoot a failed deployment by checking exit status, container status, logs, ports, configuration, and data persistence;
- perform and verify a basic backup/restore exercise;
- explain which remote-access and production-hardening tasks are deliberately deferred.

## 6. Explicit Scope Boundaries

### In scope

- safe preparation of the server machine;
- supported Ubuntu Server LTS installation or verification of an existing suitable server OS;
- user account, updates, SSH, basic firewall, system logs, and service inspection;
- Docker fundamentals, image builds, container lifecycle, port mapping, volumes, and Docker Compose;
- local deployment of QR Warehouse API;
- running and integrating existing tests into a basic CI workflow;
- a careful, evidence-based decision about PostgreSQL migration;
- backup/restore and operational documentation sufficient for one person to maintain the service.

### Deliberately out of scope for the first milestone

- directly exposing the API or database to the public internet;
- complex VPS tunnelling / remote-access topology;
- authentication and authorization for multiple real users, unless the current application already has it and it is required for safe LAN use;
- Kubernetes, multi-node orchestration, microservices, service meshes, elaborate observability stacks, and infrastructure-as-code;
- a full redesign of the Domain/Application architecture;
- asynchronous database migration merely to use `async` everywhere;
- chasing an arbitrary test-coverage percentage;
- implementing all future QR Warehouse product features.

These may become later modules or separate tasks. Do not quietly expand Module 11 to include all of them.

## 7. Phase 0 — Establish the Current State

Before installation or refactoring:

1. Ask the student which machine is intended to become the server and whether an OS is already installed.
2. Confirm whether its data can be erased; do not assume it is safe to repartition a disk.
3. Confirm the current repository location, active branch, working-tree status, and how the app is run today.
4. Inspect `README`/run instructions, dependency files, API entry point, database configuration, schema creation, data/catalog files, and the current test commands.
5. Run the available tests and record the exact result. If tests fail before changes, diagnose or document the baseline rather than hiding the failure.
6. Verify dependency completeness. For example, if FastAPI/Uvicorn are imported but absent from the intended installation requirements, resolve how the project actually installs/runs them before creating a container.
7. Check for mismatches between configuration paths and files present in the repository. Do not assume an apparent mismatch is a bug until usage is traced.
8. Make a backup or commit before operational changes.

### Mentor rule

Do not dump a massive audit report on the student. Present the most consequential findings first, verify them against the current repository, then agree on the next small step. Do not treat old source snippets or checkpoint reports as proof of the current state of the codebase.

## 8. Phase 1 — Server Fundamentals and Safe Preparation

### Concepts

Introduce the concepts needed to understand the work:

- server as a role a machine performs, not necessarily a special type of hardware;
- headless operation and why a server usually does not need a graphical desktop;
- local IP address, router, LAN, hostname, SSH, and firewall at a basic level;
- users, groups, root, `sudo`, updates, and least privilege;
- service vs interactive process;
- logs as the record used to investigate what happened.

### Practical tasks

- Verify hardware health and available storage before installation.
- Choose a currently supported Ubuntu Server LTS release at the time of installation; verify the supported release from official Ubuntu sources rather than assuming a version.
- Install or verify the OS only after the student explicitly confirms the target disk can be erased.
- Create/use a normal administrative account; avoid working as root for routine operations.
- Update the system and verify the result.
- Set a hostname and check the network configuration.
- Configure SSH for trusted LAN access. Prefer key-based authentication where practical; keep private keys private.
- Apply a basic firewall policy allowing only the required management connection from the appropriate network. Explain every rule and verify that SSH access remains possible before ending the session.
- Practise checking system and service state using tools such as `systemctl`, `journalctl`, `ip`, `ss`, and `df`, but explain each before use.

### Safety gate

Do not configure unattended remote SSH/firewall changes in a way that can lock the student out without an alternative access path. Do not publish the server's IPs, keys, or sensitive configuration in chat. Do not forward ports on the router in this module.

## 9. Phase 2 — Docker Mental Model

Teach the concepts before asking the student to write a Dockerfile:

- image vs container;
- build-time vs run-time configuration;
- container filesystem vs persistent storage;
- bind mounts vs named volumes;
- published ports vs internal container ports;
- environment variables and configuration;
- Docker Compose as a repeatable description of a small multi-service application;
- container logs, restart behavior, and graceful shutdown.

Use a small harmless sample container first if that would make the concepts easier. Then move to QR Warehouse. Avoid unnecessary base-image optimization, multi-stage build tricks, or production-hardening detail before the simple model works.

## 10. Phase 3 — Containerize QR Warehouse

### Target architecture for the first deployment

```text
Client on trusted LAN
        |
        | HTTP to a LAN address and chosen port
        v
Home server
  └── Docker Compose
        └── QR Warehouse API container
              └── Existing application layers
                    └── Existing persistence strategy
```

Start with the simplest architecture that fits the actual repository. The first successful deployment may retain SQLite if that is the lowest-risk way to prove the runtime/deployment path. Make the SQLite data location explicit and persistent outside the container's disposable layer.

### Work sequence

1. Determine the true ASGI application import path and current run command from the repository.
2. Check dependencies and select a suitable Python base image. Use a supported, explicit image tag; avoid relying on the `latest` tag as an unexamined default.
3. Create a minimal `.dockerignore` so local caches, virtual environments, Git metadata, secret files, and unrelated development data do not enter the build context.
4. Write a minimal Dockerfile that installs the declared dependencies, copies only required project files, and starts the actual application.
5. Build and run the image locally. Inspect logs and confirm the API responds.
6. Define the runtime in Compose. Keep configuration explicit and secrets out of the YAML file committed to Git.
7. Configure the intended port mapping for LAN testing. Do not publish database ports to the LAN unless there is a concrete, justified need.
8. Store database state in a persistent volume or a carefully chosen bind mount. Explain ownership/permissions and back up the data before testing volume changes.
9. Recreate/restart the container and prove that important data survives container replacement.
10. Test failure cases: invalid configuration, missing dependency, port conflict, app startup error. Learn to diagnose from `docker compose ps`, logs, and exit status rather than repeatedly rebuilding at random.
11. Run the existing test suite from a clean, documented environment and address any concrete failures.

### Architecture guardrails

- Do not put SQL inside HTTP endpoints.
- Do not make Application/Domain layers import FastAPI, Docker-specific libraries, or PostgreSQL driver details.
- Do not rewrite the current synchronous SQLite path into async code merely because FastAPI supports `async def`.
- Reuse the existing app structure unless a verified deployment blocker requires a focused change.
- Keep code changes and host/server changes as separate as practical so failures can be localized.

## 11. Phase 4 — Persistence and PostgreSQL Decision

The Module 10 checkpoint recommends a PostgreSQL migration as part of deployment practice. Treat it as a substantive engineering task, not a guaranteed one-line database swap.

Before deciding:

1. Inspect the current repository implementation and identify direct `sqlite3` coupling, SQL dialect assumptions, schema initialization, row mapping, generated identifiers, transactions, and constraints.
2. Explain what differs between SQLite and PostgreSQL at the application boundary and in operations.
3. Estimate the changes required from verified evidence.
4. Preserve a known-working SQLite deployment and a separate backup before migration.

If the current code structure can support a focused migration within a reasonable learning scope, proceed in small steps:

- add the PostgreSQL driver and configuration through the project's dependency mechanism;
- define PostgreSQL service credentials through uncommitted environment configuration;
- add a database readiness strategy that does not rely on a fixed arbitrary sleep;
- port schema creation/migrations deliberately;
- update the repository implementation and row/result handling as needed;
- ensure transactions and rollback are intentional;
- migrate any data that matters, or use a fresh development dataset if the student explicitly accepts that choice;
- run unit/API/integration checks and verify results by querying the database independently;
- test restart persistence and a backup/restore path.

Do not keep an abandoned SQLite implementation and PostgreSQL implementation in parallel without a real compatibility/testing plan. If the migration is too broad for this module, document the blocker accurately and complete the first stable deployment using SQLite, then split PostgreSQL into a focused follow-up module. That is a legitimate Minimum Viable Completion decision, not a failure.

## 12. Phase 5 — Continuous Integration (CI)

The first CI goal is small: every push or pull request to the repository should install the project dependencies, run the available automated tests, and show a clear pass/fail result.

### Steps

1. Verify the test command and dependencies locally.
2. Ensure tests do not depend on a developer-specific absolute path or a production data file.
3. Check how the API application creates its database/repositories and whether tests can run against an isolated test database or temporary state. If isolation is incomplete, fix only what is necessary for safe repeatable CI.
4. Add a small GitHub Actions workflow to install a supported Python version, install dependencies, and run tests.
5. Open a branch/commit and verify that the workflow actually ran. A YAML file in the repository is not proof that CI works.
6. Introduce one deliberate failure on a temporary branch or by temporarily changing a test expectation to prove that CI catches a failing suite; restore the correct code immediately afterward.
7. Confirm that secrets are not required for ordinary unit tests. If a later integration test needs credentials, use repository secrets appropriately and avoid printing them in logs.

### CI vs CD

Explain the difference:
- **CI:** automatically checks changes, including running tests.
- **CD:** automates delivery or deployment of accepted changes.

A successful CI pipeline is the core outcome. Automatic public deployment to the home server is not required in this module. If a simple, safe deployment step becomes appropriate later, implement it only after manual deployment, rollback, and access-control decisions are understood.

## 13. Phase 6 — Operations, Backup, and Recovery

A service is not operationally reliable merely because a browser loaded it once.

The student should practise:

- checking Compose status and container logs;
- restarting the service and distinguishing application failure from host/network failure;
- verifying which port is listening and which interface it is bound to;
- updating the application without accidentally deleting persistent data;
- backing up the database to a separate location;
- restoring the backup into a test location and verifying that the restored data is usable;
- recording a minimal recovery sequence: where configuration lives, how to start the service, where data persists, and how to restore it.

Do not treat a copied file as a verified backup until a restore test has succeeded.

## 14. Security Baseline and Deferred Remote Access

The first deployment should be reachable only from a trusted local network. Do not expose the API or database directly to the public internet. Do not configure router port forwarding or VPS tunnels as an early shortcut.

Before a later remote-access module, establish:

- what data the API exposes and whether it has authentication/authorization;
- which interfaces and ports are listening;
- the firewall policy;
- how secrets are stored and rotated;
- whether HTTPS is required for the chosen remote path;
- how access will be revoked and logs checked;
- backup and recovery procedures.

When external access is addressed, compare safer options such as a VPN or a private tunnel with a VPS rather than treating public exposure as the default. Do not assume that an app is safe to expose merely because it is running in Docker.

## 15. Practical Deliverables

The module should aim for these concrete artifacts, in the repository where appropriate:

- a documented server setup and safe access method;
- a minimal Dockerfile;
- a Compose file defining the application runtime and any approved database service;
- a `.dockerignore`;
- an example environment file containing placeholders only, plus a real local environment file excluded from Git if needed;
- a verified test command;
- a working CI workflow;
- a brief operations note with start/stop/log/backup/restore commands;
- a tested backup and restore procedure.

Avoid creating additional process documents merely to prove that the work occurred. The artifacts and observed results are the evidence.

## 16. Mentor Protocol

The mentor must:

- teach in Russian and explain technical terms in context;
- work one milestone at a time and request observations/output only when needed;
- explain risks before commands that affect users, services, disks, firewalls, or data;
- prefer diagnosis over command dumps;
- avoid assuming the operating system version, hardware, network, repository layout, application command, dependency file, database path, or test coverage; verify these from the student's actual setup;
- keep a distinction between local development, the home server, and CI environments;
- not ask the student to paste private keys, passwords, tokens, or unrestricted configuration files;
- not silently replace architectural decisions or rewrite whole files when a small patch is enough;
- not reopen Module 10's repetitive test-expansion work unless a concrete issue requires it;
- bring testing back as an operational tool for containerization, database migration, and CI;
- stop and reassess when a phase reveals that its assumptions were wrong.

The student is expected to propose hypotheses, explain choices, run commands, inspect results, and evaluate suggestions—not merely copy commands generated by AI.

## 17. Knowledge Checks

Use short conversations after practical milestones. Possible questions include:

### Linux and operations
1. What is the difference between a process and a service?
2. Why should routine tasks not run as root?
3. What does a firewall rule permit, and how can you verify it?
4. Where would you look if a service starts and then exits?

### Docker
5. What is the difference between an image and a container?
6. Why can data disappear when a container is removed?
7. What is the difference between a port inside the container and a published host port?
8. What problems does Compose solve in this setup?

### Persistence and deployment
9. Why is a database migration not automatically a configuration-only change?
10. What evidence proves that a backup can actually be restored?
11. How would you distinguish an application error from a port, network, or database error?

### CI/CD
12. What does CI verify, and what does it not verify?
13. What evidence shows that the workflow ran successfully?
14. Why should CI tests not use a production database?

These are prompts for discussion, not an exam. Teach any concept that is not yet understood through a new example.

## 18. Completion Criteria — Minimum Viable Completion

Module 11 can be closed at Minimum Viable Completion when the student can demonstrate and explain the following:

```text
[ ] The target server OS and disk were verified before installation or modification.
[ ] The server is updated and accessible by a normal account using a safe management method.
[ ] The student can inspect basic network information, services, and logs.
[ ] The current QR Warehouse baseline and test result were recorded before major changes.
[ ] QR Warehouse can be built and started using a reproducible container definition.
[ ] The API responds from a trusted LAN client.
[ ] Persistent application data survives container replacement/restart.
[ ] The student can find logs and diagnose at least one intentionally reproduced deployment failure.
[ ] The existing automated tests run from a documented command.
[ ] CI automatically runs those tests and has been observed failing and passing as expected.
[ ] A backup has been created and a restore has been verified, or a precisely documented blocker remains.
[ ] The SQLite/PostgreSQL decision is justified by the current repository. If PostgreSQL is migrated, key workflows and persistence are verified against it.
[ ] The student can explain why external access is deferred until the security baseline is understood.
```

Not every item has to be completed to claim full mastery of Linux or DevOps; this module is only a first operational deployment. If PostgreSQL migration becomes unexpectedly broad, a safe SQLite deployment plus a justified migration plan may be accepted as MVP, with PostgreSQL explicitly carried forward.

## 19. Suggested Time Budget

This is a planning estimate, not a time limit:

| Area | Approximate effort |
|---|---:|
| Baseline, safety, server/OS and SSH | 3–6 h |
| Linux operations and troubleshooting | 3–5 h |
| Docker and Compose fundamentals | 3–5 h |
| Containerizing and testing QR Warehouse | 4–7 h |
| CI workflow and test isolation | 3–5 h |
| PostgreSQL decision/migration | 4–8 h if included |
| Backup, restore, review | 2–4 h |

The range depends heavily on the actual server and repository state. If work takes longer because the student is learning a foundational concept, slow down. If a section adds little value, simplify it instead of completing it mechanically.

## 20. Suggested Start Prompt for the Mentor

Begin the module by saying that Module 10 is closed at Minimum Viable Completion and that testing now becomes part of the delivery workflow rather than a repetitive standalone exercise. Then inspect the student's current state before prescribing commands.

Ask only the first necessary question: **Which physical machine will be the home server, and is an operating system already installed on it?** Use the answer to select the safest next step. Do not provide a long all-at-once setup script.
