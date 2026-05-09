# Release Notes

## Python Task Manager App

---

## v0.5 — Sprint 1 Release
**Release Date:** April 24, 2026
**Tag:** v0.5

### New Features
- Task Creation — create tasks with title and optional description
- View All Tasks — retrieve full list of all tasks
- Complete Tasks — mark tasks as completed with timestamp
- Delete Tasks — remove tasks by ID
- Search Tasks — search by keyword across title and description
- Filter by Status — filter tasks by pending or completed

### Bug Fixes
- BUG-01: Fixed empty/whitespace task titles being accepted

### Testing
- 15 unit tests written using Pytest — all passing

---

## v0.8 — Refactoring Release
**Release Date:** May 8, 2026
**Tag:** v0.8

### Improvements
- Added due date input validation (raises ValueError for invalid format)
- Added Python logging to task_manager.py for all key operations
- Refactored add_task() for cleaner, more defensive code

### Documentation Added
- docs/tech-debt.md
- docs/performance.md
- docs/security-checklist.md

---

## v1.0 — Capstone Final Release
**Release Date:** May 9, 2026
**Tag:** v1.0

### Features Complete
- All Sprint 1 stories delivered
- CI/CD pipeline live via GitHub Actions
- Full documentation suite complete
- Demo script prepared (demo.py)

### All Files in This Release

| File                              | Description                        |
|-----------------------------------|------------------------------------|
| src/task_manager.py               | Core Task and TaskManager classes  |
| tests/test_task_manager.py        | 15 unit tests using Pytest         |
| demo.py                           | Capstone demo script               |
| requirements.txt                  | Project dependencies               |
| LICENSE                           | MIT License                        |
| .github/workflows/deploy.yml      | CI/CD pipeline                     |
| docs/backlog.md                   | 10 user stories                    |
| docs/sprint-1-plan.md             | Sprint 1 plan                      |
| docs/team-roles.md                | Team roles                         |
| docs/risk-register.md             | 10 risks with mitigation           |
| docs/qa-plan.md                   | QA strategy                        |
| docs/defect-log.md                | Bug tracking log                   |
| docs/release-notes.md             | This file                          |
| docs/deployment-plan.md           | Deployment strategy                |
| docs/support-plan.md              | Support and issue process          |
| docs/tech-debt.md                 | Technical debt register            |
| docs/performance.md               | Performance analysis               |
| docs/cicd-diagram.md              | CI/CD pipeline diagram             |
| docs/security-checklist.md        | Security measures                  |
| docs/ethics-impact.md             | Ethics assessment                  |
| docs/privacy-note.md              | Privacy policy                     |
| docs/ip-and-attribution.md        | Licenses and attribution           |
| docs/kpis.md                      | 5 KPIs with measurements           |
| docs/metrics-report.md            | Metrics and analysis               |
| docs/cost-benefit.md              | Cost-benefit and ROI               |
| docs/architecture.md              | System architecture                |
| docs/devops-practices.md          | DevOps practices applied           |
