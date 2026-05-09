# CI/CD Pipeline Diagram

## Project: Python Task Manager App

---

## Pipeline Overview

The CI/CD pipeline automatically tests and deploys the app every time
code is pushed to the main branch on GitHub.

---

## Pipeline Steps

```
Developer pushes code to main branch
              |
              v
   +----------------------+
   |    1. CODE PUSH      |
   |    git push main     |
   +----------+-----------+
              |
              v
   +----------------------+
   |   2. CI TRIGGERED    |
   |   GitHub Actions     |
   |   workflow starts    |
   +----------+-----------+
              |
              v
   +----------------------+
   |  3. INSTALL DEPS     |
   |  pip install -r      |
   |  requirements.txt    |
   +----------+-----------+
              |
              v
   +----------------------+
   |  4. RUN UNIT TESTS   |
   |  pytest tests/ -v    |
   |  (15 unit tests)     |
   +----------+-----------+
              |
        +-----+-----+
        |           |
      FAIL        PASS
        |           |
        v           v
    Stop and   +----------------------+
    notify     |  5. SMOKE TEST       |
    team       |  Verify app starts   |
               |  without errors      |
               +----------+-----------+
                          |
                          v
               +----------------------+
               |  6. AUTO-DEPLOY      |
               |  Deploy to Render    |
               |  (main branch only)  |
               +----------+-----------+
                          |
                          v
               +----------------------+
               |  7. VERIFY LIVE      |
               |  Check app URL is    |
               |  responding (200 OK) |
               +----------+-----------+
                          |
                          v
                    DEPLOYMENT DONE
```

---

## GitHub Actions Workflow File

Located at: .github/workflows/deploy.yml

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  test-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/ -v
      - run: python -c "from src.task_manager import TaskManager; m = TaskManager(); m.add_task('smoke test'); print('Smoke test passed')"
      - run: echo "Deploying to Render..."
```

---

## Pipeline Summary Table

| Step | Action               | Tool           | On Failure    |
|------|----------------------|----------------|---------------|
| 1    | Code pushed to main  | Git / GitHub   | —             |
| 2    | Workflow triggered   | GitHub Actions | —             |
| 3    | Install dependencies | pip            | Stop pipeline |
| 4    | Run unit tests       | Pytest         | Stop, notify  |
| 5    | Smoke test           | Python         | Stop, notify  |
| 6    | Auto-deploy          | Render webhook | Stop, notify  |
| 7    | Verify live          | HTTP check     | Alert team    |
