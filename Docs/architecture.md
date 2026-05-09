# System Architecture

## Project: Python Task Manager App — v1.0

---

## Architecture Overview

The Task Manager App follows a simple 3-layer architecture:

```
+------------------------------------------+
|          PRESENTATION LAYER              |
|   CLI output / Flask routes (future)     |
|   User interacts here via terminal       |
+--------------------+---------------------+
                     |
                     v
+------------------------------------------+
|         BUSINESS LOGIC LAYER            |
|   src/task_manager.py                   |
|   TaskManager class — core operations   |
|   Input validation, status management   |
|   Logging of key events                 |
+--------------------+---------------------+
                     |
                     v
+------------------------------------------+
|            DATA LAYER                   |
|   In-memory Python dict (v0.5 - v1.0)   |
|   SQLite planned for v1.1               |
+------------------------------------------+
```

---

## Component Diagram

```
GitHub Repository
       |
       | git push main
       v
GitHub Actions (CI/CD)
       |
       +-- pip install requirements.txt
       +-- pytest tests/ -v
       +-- Smoke test
       +-- Deploy to Render.com
                  |
                  v
         Render.com (Cloud Host)
                  |
                  v
         Python App (demo.py)
                  |
         +--------+--------+
         |                 |
   src/task_manager.py   docs/
   (core business logic)  (all documentation)
```

---

## Technology Stack

| Layer        | Technology                    | Reason                               |
|--------------|-------------------------------|--------------------------------------|
| Language     | Python 3.10+                  | Course requirement; widely used      |
| Web framework| Flask 3.0.3                   | Lightweight, easy to learn and deploy|
| Testing      | Pytest 9.0.3                  | Industry standard for Python testing |
| CI/CD        | GitHub Actions                | Free, integrates directly with GitHub|
| Hosting      | Render.com                    | Free tier supports Python apps       |
| Storage      | In-memory dict (v1.0)         | Simple, no setup required for MVP    |
| Version ctrl | Git + GitHub                  | Industry standard                    |

---

## Key Design Decisions

1. **In-memory storage first** — Keeps complexity low for the MVP; SQLite added in v1.1
2. **TaskManager class** — All business logic in one place, easy to unit test
3. **Pytest for testing** — Fast, readable unit tests with reusable fixtures
4. **GitHub Actions for CI/CD** — Automatically tests and deploys on every push to main
5. **Render.com for hosting** — Free tier supports Python/Flask with minimal configuration
6. **Logging added early** — Makes debugging easier in production from the start
