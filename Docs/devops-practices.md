# DevOps Practices

## Project: Python Task Manager App

---

## What is DevOps?

DevOps is a set of practices that combines software development (Dev) and IT operations (Ops).
The goal is to shorten the development cycle and deliver high-quality software continuously.

---

## DevOps Practices Applied in This Project

### Version Control — Git and GitHub
- All code is tracked using Git
- Feature branches used for every new feature
- Pull Requests required before merging to dev or main
- Commit messages follow a clear format: feat:, fix:, docs:, test:

### Continuous Integration (CI)
- GitHub Actions triggers automatically on every push to main
- Pipeline installs dependencies, runs all 15 unit tests, and runs a smoke test
- If any step fails, the pipeline stops and the team is notified
- No broken code can reach production

### Continuous Deployment (CD)
- On a successful CI run, the app is automatically deployed to Render.com
- No manual deployment steps are needed after the first setup
- Deployment takes under 2 minutes from push to live

### Automated Testing
- 15 unit tests written using Pytest
- Tests run on every commit via CI pipeline
- Minimum coverage target: 80%
- Current coverage: 87%

### Infrastructure as Code
- CI/CD pipeline is defined in .github/workflows/deploy.yml
- Environment is reproducible via requirements.txt
- No manual server configuration is needed

### Monitoring and Logging
- Python logging added to task_manager.py
- Logs key events: task created, task completed, task deleted
- Render.com provides live deployment and error logs

---

## CI/CD Pipeline Summary

```
Push to main branch
    -> Install dependencies (pip)
    -> Run unit tests (pytest)
    -> Run smoke test (python)
    -> Deploy to Render.com
    -> App is live
```

Full pipeline diagram: see docs/cicd-diagram.md

---

## Branching Strategy

| Branch   | Purpose                              |
|----------|--------------------------------------|
| main     | Production-ready code only           |
| dev      | Integration branch for all features  |
| feature/ | Individual feature development       |

Flow: feature/ branch -> Pull Request -> dev -> Pull Request -> main -> auto-deploy

---

## Release Strategy

Versions follow semantic versioning: vMAJOR.MINOR

| Version | Description                                    |
|---------|------------------------------------------------|
| v0.5    | Sprint 1 MVP — core task management            |
| v0.8    | Refactoring — input validation and logging     |
| v1.0    | Final capstone release — full documentation    |

---

## Emerging Trends Applied

| Trend                   | How Applied in This Project                         |
|-------------------------|-----------------------------------------------------|
| CI/CD Automation        | GitHub Actions pipeline for test and deploy         |
| Cloud Deployment        | Render.com free tier for hosting                    |
| Infrastructure as Code  | Pipeline in YAML, dependencies in requirements.txt  |
| Shift-Left Testing      | Tests written during development, not after         |
| Observability           | Logging added for runtime visibility                |
