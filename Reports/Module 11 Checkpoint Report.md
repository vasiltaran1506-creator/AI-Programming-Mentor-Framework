# Checkpoint Report

**Framework:** AI Programming Mentor Framework (APMF)

**Version:** 0.1 Alpha

**Status:** Active

---

# 1. General Information

```text
Student: alabardam_
Date: 2026-06-03
Checkpoint: Module 11 — Home Server, Linux, Docker, CI/CD
Module / Stage: Deployment and Infrastructure
Teacher: AI Programming Mentor
```

---

# 2. Summary

The student successfully completed their first real deployment of a Python web application to a physical Linux server. This module marked a significant transition from local development to operating a service on a separate machine.

**Overall progress:** The student demonstrated the ability to follow a guided deployment pipeline end-to-end: server preparation → SSH access → code delivery → environment setup → Docker containerization → persistent storage → CI/CD pipeline → service recovery after reboot.

**Major achievements:**
- Independently diagnosed CI/CD branch mismatch failure
- Correctly identified stale dependencies caused by unpushed requirements.txt
- Made deliberate, reasoned decisions to defer PostgreSQL migration and backups
- Understood the critical distinction between images, containers, and volumes
- Verified data persistence through explicit testing

**Current challenges:**
- Initial misconceptions about Docker concepts required correction
- Local vs remote state synchronization remains a recurring issue
- Test authorship motivation is low despite understanding CI's purpose
- Limited independent operational experience (all work was guided)

**General recommendation:** Proceed to PostgreSQL migration module as planned. Increase independent operational tasks and reduce guidance gradually.

---

# 3. Completed Learning Areas

```text
Completed:

- Linux server administration basics (SSH, sudo, package management)
- Network configuration (IP addressing, DHCP reservation, port mapping)
- SSH key-based authentication for GitHub
- Git-based code delivery between machines
- Python virtual environments on remote servers
- Docker fundamental concepts (images, containers, layers)
- Dockerfile authoring (FROM, WORKDIR, COPY, RUN, CMD)
- .dockerignore and build context
- Docker volumes for persistent data
- Docker Compose for declarative infrastructure
- Port mapping and network exposure (0.0.0.0 vs 127.0.0.1)
- Restart policies and service recovery
- GitHub Actions CI pipeline setup
- Workflow triggers and branch filters
- Build-time vs run-time configuration separation
- Scope management and deliberate deferral decisions
```

---

# 4. Competency Evaluation

```text
Competency:
DEP-001 Server Administration

Current Level:
Level 2 — Guided Application

Evidence:
Student can connect via SSH, run basic commands, install packages, and check system state. Required guidance for diagnosing broken package dependencies (amneziawg-dkms).

Confidence:
Medium

Notes:
Student can follow instructions but does not yet independently navigate unfamiliar system failures. The broken apt package diagnosis was guided, not self-discovered.
```

```text
Competency:
DEP-002 Network Configuration

Current Level:
Level 2 — Guided Application

Evidence:
Student understood DHCP reservation concept, connected to server via IP, and verified connectivity. Did not independently configure network settings.

Confidence:
Medium

Notes:
Conceptual understanding is present. Practical network troubleshooting remains undeveloped.
```

```text
Competency:
DEP-003 Code Delivery

Current Level:
Level 3 — Assisted Application

Evidence:
Student successfully cloned repository via SSH, created feature branches, and pushed changes. Independently diagnosed the branch filter mismatch in CI/CD.

Confidence:
High

Notes:
The unpushed requirements.txt incident revealed a recurring gap: student does not systematically verify remote state before assuming deployment correctness.
```

```text
Competency:
DEP-004 Docker Containerization

Current Level:
Level 2 — Guided Application

Evidence:
Student understood image vs container distinction after correction, authored a Dockerfile following guidance, and ran containers successfully. Initial misconceptions included describing an image as "a snapshot of a container" and a volume as "a separate container."

Confidence:
Medium

Notes:
Conceptual models were corrected through dialogue. Student can now predict behavior (data loss on container deletion, persistence via volume) but has not independently designed a Docker setup from scratch.
```

```text
Competency:
DEP-005 Persistent Storage

Current Level:
Level 3 — Assisted Application

Evidence:
Student correctly reasoned that container-local data is disposable, understood volume mount points, and verified data survival through a controlled experiment. However, the volume was later reset during exploration, and the student initially expected data to persist after that reset.

Confidence:
Medium

Notes:
The student demonstrated understanding of the persistence model but confused it with the separate volume reset event. This shows the mental model is present but not yet fully stable under changing conditions.
```

```text
Competency:
DEP-006 CI/CD Pipeline

Current Level:
Level 2 — Guided Application

Evidence:
Student created GitHub Actions workflow, understood trigger mechanics, and independently diagnosed branch filter mismatch. Did not independently author the workflow YAML from scratch.

Confidence:
Medium

Notes:
The branch mismatch diagnosis was the strongest independent reasoning moment in this module. The student identified the cause without being told the answer.
```

```text
Competency:
DEP-007 Service Recovery

Current Level:
Level 2 — Guided Application

Evidence:
Student verified automatic startup after reboot and checked logs. Did not independently configure restart policies without guidance.

Confidence:
Medium

Notes:
The final reboot verification was successful, but the volume reset during exploration means data survival was not fully verified in the final test. Service recovery was confirmed; data recovery was not.
```

```text
Competency:
DEP-008 Scope Management

Current Level:
Level 3 — Assisted Application

Evidence:
Student made deliberate decisions to defer PostgreSQL migration, backups, and coverage thresholds. Each decision was reasoned rather than lazy.

Confidence:
High

Notes:
This is an emerging strength. The student distinguished between "will be needed" and "is needed now" with increasing clarity.
```

---

# 5. Strengths

**Conceptual reasoning**

The student consistently asks "why" before "how." Questions about daemon etymology, volume mechanics, and port mapping show genuine curiosity about underlying mechanisms rather than surface-level command memorization.

**Independent diagnosis**

The branch filter mismatch in CI/CD was identified without being told the answer. The student observed that the workflow did not trigger, hypothesized a branch mismatch, and confirmed it. This is the strongest evidence of independent operational reasoning in this module.

**Honest self-assessment**

The student explicitly stated uncertainty when present ("Я пока не знаю, как устроена файловая система докера изнутри") and admitted disliking test authorship. This calibration is valuable and should be preserved.

**Scope discipline**

Decisions to defer PostgreSQL, backups, and coverage thresholds were reasoned and explicit. The student did not attempt to do everything at once, which prevented scope creep.

**Transfer of existing models**

The student reused previously learned mental models (class vs object → image vs container; isolated kitchen → virtual environment) to approach unfamiliar infrastructure. When these models broke, they were corrected through dialogue.

---

# 6. Weaknesses and Knowledge Gaps

**Local vs remote state synchronization**

Two separate incidents occurred because the student assumed remote state matched local state:
1. Unpushed requirements.txt led to stale dependencies on the server
2. CI workflow branch filter did not match the working branch

This is a procedural gap, not a conceptual one. It is trainable through explicit verification habits.

**Docker mental model stability**

Initial misconceptions included:
- Describing an image as "a snapshot of a container"
- Describing a volume as "a separate container"
- Assuming the base image should mirror the server's operating system

These were corrected through dialogue but indicate that the Docker model is not yet fully stable. The student can now predict behavior correctly, but the mental model was recently reconstructed.

**Test authorship motivation**

The student explicitly stated they dislike writing tests and that existing tests were written formally. While the CI context helped reframe tests as contracts with future maintainers, this has not yet produced autonomous test authorship.

**Operational independence**

All deployment work was guided. The student has not yet:
- Deployed independently from an empty machine
- Configured a multi-service system
- Performed a real backup-and-restore cycle
- Diagnosed a system failure without guidance

---

# 7. Common Mistakes Pattern

```text
- Assumes remote state matches local state without verification.
  (Unpushed requirements.txt, CI branch mismatch)

- Confuses build-time configuration with run-time configuration.
  (Required explicit explanation of Dockerfile vs docker run flags)

- Over-generalizes from local development to server deployment.
  (Expected server to have pip, venv, and dependencies pre-installed)

- Does not systematically verify state after destructive operations.
  (Volume reset during exploration destroyed data used for later verification)
```

---

# 8. Independence Assessment

**Current Level: Assisted**

The student can solve problems with hints and can independently diagnose certain categories of failures (branch mismatch, unpushed files). However, the student cannot yet:

- Deploy a service from scratch without dialogue
- Design a Docker setup independently for an unfamiliar application
- Perform operational troubleshooting without guidance
- Author CI/CD pipelines from scratch

The progression toward Semi-Independent requires:
1. At least one independent deployment without step-by-step guidance
2. Successful diagnosis of a system failure without hints
3. Authorship of a Docker configuration for a new project

---

# 9. AI Usage Assessment

**Prompting Ability**

The student describes technical problems clearly and provides sufficient context. They ask specific questions rather than vague requests for help.

**Code Evaluation**

The student reviews AI-generated Dockerfiles and workflows before executing them. They asked clarifying questions about flags and syntax rather than blindly copying.

**Decision Making**

The student correctly identified when AI guidance was appropriate (Dockerfile syntax, CI/CD YAML) versus when they needed to reason independently (scope decisions, persistence strategy).

---

# 10. Project Integration

**Implemented features:**
- QR Warehouse deployed to home server via Docker
- Persistent SQLite database via Docker volume
- GitHub Actions CI pipeline running existing test suite
- Automatic service recovery after reboot

**Improved understanding:**
- Distinction between code, environment, and data
- Build-time vs run-time configuration
- Image vs container vs volume lifecycle
- Port mapping and network exposure

**Architectural changes:**
- No application code changes (deliberately kept intact to isolate infrastructure work)
- Added Dockerfile, .dockerignore, docker-compose.yml, and CI workflow

**Discovered problems:**
- Synchronous SQLite driver identified as a product limitation (motivation for PostgreSQL migration)
- Test suite is too shallow to provide meaningful CI value
- Backup mechanism not implemented (deferred)

---

# 11. Recommended Next Steps

**Next learning objectives:**
1. PostgreSQL migration module (Q-0039)
   - asyncpg and asynchronous database access
   - Connection pooling
   - Schema migrations with Alembic
   - Multi-container Docker Compose topology

2. Testing depth (Q-0026)
   - Use Case unit tests
   - Multi-repository coordination tests
   - Transaction and rollback tests

3. Operational independence
   - Deploy a service without step-by-step guidance
   - Diagnose a system failure independently
   - Author a Docker configuration for a new project

**Recommended exercises:**
- Deploy a second service (e.g., a static file server) independently
- Write 5 meaningful Use Case tests for QR Warehouse
- Create a backup script and verify restore procedure

**Concepts requiring reinforcement:**
- Docker layer caching and build optimization
- Multi-container networking
- Environment variable management
- Reverse proxy and HTTPS

---

# 12. Curriculum Adjustment Recommendation

**Continue as planned, with the following adjustments:**

1. **Increase independent operational tasks.** The student has demonstrated sufficient conceptual understanding to attempt independent deployment. Guidance should decrease progressively.

2. **Do not rush PostgreSQL.** The student explicitly deferred it to a dedicated module. This decision should be respected. PostgreSQL migration requires its own focused module with asyncpg, Alembic, and multi-container networking.

3. **Address test motivation before test depth.** The student understands CI's purpose but lacks motivation to author tests. Connecting test authorship to real change and real risk (rather than coverage quotas) may be more effective than imposing coverage thresholds.

4. **Verify remote state explicitly.** Add a verification step before every deployment instruction: "Which branch? What is on the remote? Which revision will the server receive?"

---

# 13. Final Mentor Assessment

```text
The student has crossed a significant boundary: from developing an application
on their own machine to operating a service on a machine they control.

The deployment was guided, not independent. The student can follow a pipeline
and diagnose certain categories of failures, but cannot yet design and execute
a deployment from scratch without dialogue.

The strongest evidence of progress is the CI branch mismatch diagnosis,
where the student identified the cause without being told the answer.

The most important development is not the number of tools learned.
It is the student's growing ability to reason about lifecycle, state,
and failure scenarios:
- What happens to this data when the container is deleted?
- What happens when the volume itself is deleted?
- What would you check first?

These questions indicate a shift from component-level reasoning
to system-level reasoning.

The next phase should reduce guidance and increase independent
operational responsibility. The student is ready for this transition.
```

---

# 14. Student Reflection

*To be completed by the student.*


What concepts became clearer?
> Стало понятно, как запускать контейнеры, что они из себя представляют и как с ними работать.

What remains confusing?
>

What was the most difficult part?
>

What would you like to explore further?
> Хочется уже приступать к рефакторингу программы и переводу ее на полноценную клиент-серверную архитектуру. По хорошему было бы начать с создания консольного приложения для компьютера, которое бы взаимодействовало с серверной частью. Ко всему прочему, безумно хочется перейти на PostgreSQL и наконец применить знания об async/await, которые на текущий момент попросту негде использовать. 


---

# 15. Report Usage

This checkpoint report should be used by:

**AI Teacher** — To adapt the PostgreSQL migration module toward increasing independent operational tasks and reducing step-by-step guidance.

**Student** — To understand that the deployment was successful but guided, and that the next phase requires more independent problem-solving.

**Educational Architect** — To evaluate whether the Docker/CI/CD curriculum should include a dedicated "independent deployment" exercise before moving to the next module.

---

**End of Checkpoint Report — Module 11**