# Student Profile — AI Programming Mentor Framework

Version: 3.0 Last updated: 2026-10-02

## 1. General Information

The student is learning Python with the long-term goal of becoming a professional software developer capable of building and maintaining real-world applications.

Primary career objective: Junior Python Backend Developer.

Primary programming language: Python.

Primary learning framework: AI Programming Mentor Framework (APMF).

Primary practical project: QR Warehouse.

The student is pursuing a backend-oriented career and is particularly interested in application architecture, databases, APIs, and the development of software that solves practical problems.

The student does not have a formal computer science degree. Explanations should therefore focus on building a solid technical foundation without assuming extensive prior knowledge of computer science or advanced mathematics.

## 2. Learning History and Current Progress

The student has completed APMF Modules 00–09 and is currently working on Module 10.

The completed curriculum has covered the following areas:

* Python fundamentals and core language features.

* Object-oriented programming.

* Software architecture and separation of responsibilities.

* Domain, Application, Presentation, and Infrastructure layers.

* Repository contracts and implementations.

* Use Cases and application logic.

* Dependency injection and application composition.

* Relational databases and SQL using SQLite.

* FastAPI and REST API fundamentals.

* Automated testing and the integration of application components.

Completion of a module indicates that the student has worked through its learning objectives. It does not automatically establish independent mastery of every topic covered.

Use the Competency Matrix and module reports to determine the student's demonstrated level in individual areas.

## 3. Technical Knowledge and Skills

### 3.1. Python

The student has completed the foundational Python curriculum and has practical experience writing multi-module applications.

The student has encountered:

* Python's fundamental data types and control structures.

* Functions, modules, and packages.

* Object-oriented programming.

* Classes and objects.

* Exception handling.

* Working with structured data.

* Application-level organization of Python code.

The student has also worked with more advanced concepts as part of the APMF curriculum.

Do not assume that familiarity with a Python feature necessarily means the student can apply it independently in unfamiliar situations.

### 3.2. Software Architecture

The student has studied layered application architecture and applied it in QR Warehouse.

Relevant concepts include:

* Separation of concerns.

* Domain and application logic.

* Repository abstractions.

* Use Cases.

* Dependency injection.

* Composition roots.

* Separation between application logic and presentation interfaces.

The student has practical experience with these concepts but may still need guidance when evaluating architectural alternatives and their trade-offs.

Continue developing the ability to recognize when an abstraction is useful and when it introduces unnecessary complexity.

### 3.3. Databases and SQL

The student has completed the APMF module covering relational databases and SQL.

Practical experience includes SQLite and database-backed application functionality.

Continue developing the student's ability to:

* Design and reason about relational schemas.

* Write and understand SQL queries.

* Work with database constraints and relationships.

* Understand transactions and data integrity.

* Recognize the responsibilities of database repositories.

Do not assume that experience with SQLite automatically translates into proficiency with PostgreSQL or other database systems.

### 3.4. Backend Development and APIs

The student has implemented a FastAPI interface for QR Warehouse.

The current project includes:

* HTTP endpoints.

* Request and response handling.

* Pydantic-based data validation.

* Application logic shared between CLI and API interfaces.

* Repository and database integration.

* Automated API tests using `TestClient`.

The student has encountered the distinction between application logic and HTTP presentation logic.

Continue developing understanding of HTTP semantics, API design, validation, error handling, and the relationship between interfaces and application services.

### 3.5. Testing

The student has practical experience writing automated tests as part of QR Warehouse.

Testing knowledge includes:

* pytest.

* API tests.

* Database-backed tests.

* Test fixtures and parametrization.

* Test isolation and verification of application behavior.

Module 10 focuses on further developing testing skills, particularly unit testing, integration testing, and reliability.

Assess the student's testing proficiency using actual test implementations and their ability to explain what those tests verify.

## 4. Primary Project: QR Warehouse

QR Warehouse is the student's principal practical project and a central part of the learning process.

The project is intended to support equipment inventory and rental workflows, including equipment catalog management, estimates, orders, and warehouse operations.

The project originated from a real-world equipment rental workflow and is intended to provide practical experience in designing and implementing a useful backend application.

### Current Technical Direction

The project currently includes:

* A Python application.

* A CLI interface.

* A FastAPI interface.

* Shared application logic and Use Cases.

* Repository abstractions.

* SQLite persistence.

* Automated tests.

The project is being developed incrementally as the student progresses through the curriculum.

### Educational Priorities

Use QR Warehouse to reinforce:

* Practical Python development.

* Backend architecture.

* Database design.

* API implementation.

* Automated testing.

* Maintainability and software quality.

Avoid introducing production-scale complexity before the student understands the relevant fundamentals.

The project should remain a learning environment in which the student understands the code and architectural decisions, rather than merely integrating generated implementations.

## 5. Career Interests and Technical Priorities

The student's primary professional interest is Python backend development.

Areas of particular interest include:

* Backend application development.

* REST APIs.

* Relational databases.

* Software architecture.

* Application design.

* Practical automation.

* Development of software for real users.

The student is also interested in DevOps but currently has only introductory knowledge in this area.

Frontend development is not a primary career objective. The student is open to using AI tools to generate frontend components, provided that they retain sufficient understanding of the integration with the backend.

The learning curriculum should prioritize backend fundamentals rather than requiring comprehensive frontend specialization.

## 6. Learning Preferences

The student benefits from structured, progressive learning.

Preferred teaching approaches include:

* Clear explanations of fundamental concepts.

* Logical progression from simple examples to more complex applications.

* Practical exercises connected to real software.

* Detailed explanations of architectural decisions.

* Code reviews that identify concrete issues.

* Gradual hints that encourage independent problem-solving.

* Explicit connections between new material and previously learned concepts.

The student values understanding why a particular solution works rather than simply receiving a working implementation.

When explaining complex subjects, break them into manageable parts and establish the necessary prerequisites.

Avoid introducing multiple unfamiliar abstractions simultaneously when doing so would make the material unnecessarily difficult to understand.

## 7. Learning Challenges and Considerations

### 7.1. Mathematical Background

The student has limited experience with advanced mathematics and has expressed difficulty with mathematical subjects.

When mathematical concepts are relevant to programming:

* Explain the practical meaning of the mathematics.

* Introduce necessary notation gradually.

* Use concrete examples.

* Avoid unnecessary mathematical formalism.

* Explain the relationship between a formula and its implementation.

Do not avoid useful technical concepts solely because they involve mathematics. Instead, provide the necessary foundations when they become relevant.

### 7.2. Architectural Reasoning

The student has identified software architecture and application design as areas where further understanding is desirable.

Pay particular attention to:

* Why architectural boundaries exist.

* How responsibilities should be distributed.

* When interfaces and abstractions are justified.

* How dependencies affect maintainability and testing.

* How architectural decisions influence future changes.

Encourage the student to justify architectural decisions independently instead of memorizing recommended structures.

### 7.3. Independent Implementation

The student is learning to move from understanding individual programming concepts to implementing complete application features.

Continue developing the ability to:

* Decompose requirements into manageable tasks.

* Design an implementation before writing code.

* Identify appropriate responsibilities for each component.

* Write meaningful tests.

* Diagnose and correct defects.

* Review the resulting implementation critically.

Do not interpret the need for occasional guidance as evidence of an inability to develop independently.

## 8. AI-Assisted Learning

The student actively uses AI tools as part of the learning process.

AI assistance is an important component of the student's workflow, but it should support the development of independent technical skills.

The mentor should encourage the student to:

* Ask specific technical questions.

* Provide relevant code and project context.

* Critically evaluate generated suggestions.

* Verify implementations through tests.

* Understand architectural consequences.

* Recognize incorrect or unjustified recommendations.

Avoid making the student dependent on complete AI-generated solutions.

The student should remain responsible for understanding and maintaining the software they develop, including code generated with AI assistance.

## 9. Learning and Assessment Strategy

Use the unified APMF competency scale when assessing the student's progress.

| Level | Description                                                                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------- |
| 0     | Not encountered or not yet assessed.                                                                                      |
| 1     | Conceptual familiarity: recognizes the concept and can describe its basic purpose with assistance.                        |
| 2     | Guided application: can apply the concept with meaningful guidance.                                                       |
| 3     | Independent application: can apply the concept independently in familiar situations.                                      |
| 4     | Independent transfer: can apply the concept in unfamiliar situations, justify decisions, and explain relevant trade-offs. |

Assess competencies individually rather than assigning a single overall programming skill level.

Record the amount of assistance required separately from the competency level.

Prefer evidence from practical exercises, project implementations, code reviews, and explanations provided by the student.

When assessing a competency, distinguish between:

* Understanding the concept.

* Applying it with guidance.

* Applying it independently.

* Transferring it to unfamiliar problems.

Use these distinctions to determine appropriate exercises and identify learning gaps.

## 10. Curriculum Priorities

The immediate priority is completing Module 10 and consolidating the student's understanding of testing, quality, and reliability.

Future curriculum development should build on the completed modules and the current state of QR Warehouse.

Potential areas for further study include:

* More advanced backend development.

* PostgreSQL.

* ORM technologies and database migrations.

* Authentication and authorization.

* Deployment and application operations.

* Deeper understanding of asynchronous programming.

* Algorithms and data structures.

* Python typing and code quality.

These topics should be introduced in a logical order, taking prerequisites and the student's demonstrated progress into account.

Avoid treating planned topics as completed competencies or fixed deadlines.

## 11. Long-Term Objective

The student's long-term objective is to become a developer capable of independently designing, implementing, testing, and maintaining practical software.

The desired outcome is not merely familiarity with Python syntax or the completion of a predefined curriculum.

The student should progressively develop the ability to:

* Translate real-world requirements into software.

* Design maintainable backend applications.

* Work confidently with databases and APIs.

* Write and maintain automated tests.

* Make informed architectural decisions.

* Debug unfamiliar problems.

* Learn new technologies independently.

* Collaborate effectively with AI tools without surrendering technical ownership.

QR Warehouse serves as a practical environment for developing these capabilities, while the APMF curriculum provides the structured learning process.
