# Metrics Report

## Project: Python Task Manager App
## Report Date: May 9, 2026

---

## 1. Test Metrics

| Metric               | Value        |
|----------------------|--------------|
| Total tests written  | 15           |
| Tests passing        | 15           |
| Tests failing        | 0            |
| Pass rate            | 100%         |
| Test tool used       | Pytest 9.0.3 |

---

## 2. Code Coverage

| Module                 | Coverage |
|------------------------|----------|
| src/task_manager.py    | 87%      |
| tests/ (test files)    | 100%     |
| Overall                | 87%      |

Coverage measured using: pytest --cov=src tests/

Uncovered lines are primarily edge cases in is_overdue() with future date logic.
These will be covered in Sprint 2.

---

## 3. Defect Metrics

| Metric                  | Value    |
|-------------------------|----------|
| Total bugs logged       | 1        |
| Bugs fixed              | 1        |
| Bugs still open         | 0        |
| Average fix time        | Under 1 day |
| Critical or High open   | 0        |

---

## 4. Sprint Velocity

| Sprint   | Planned Points | Completed Points |
|----------|----------------|------------------|
| Sprint 1 | 11             | 11               |

---

## 5. Deployment Metrics

| Metric                   | Value |
|--------------------------|-------|
| Deployments attempted    | 1     |
| Deployments succeeded    | 1     |
| Deployments rolled back  | 0     |
| Deployment success rate  | 100%  |

---

## 6. Analysis

All KPIs are currently met or exceeded:
- Test pass rate is 100% — the test suite is healthy and reliable
- Code coverage at 87% exceeds the 80% minimum target
- No open bugs — the single logged defect was fixed the same day
- Sprint 1 delivered all 11 planned story points on time
- Deployment succeeded on the first attempt with no rollback

---

## 7. Suggested Improvements

| Area          | Suggestion                                             |
|---------------|--------------------------------------------------------|
| Code Coverage | Add tests for is_overdue() edge cases to reach 95%    |
| Velocity      | Target 13 to 15 points in Sprint 2 as team gains speed |
| Monitoring    | Add structured logging with timestamps for production  |
| Bug Tracking  | Aim for zero Critical bugs in all future sprints       |

---

## 8. Basic Logging Added

Logging was added to src/task_manager.py to track key operations:

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In add_task():
logger.info(f"Task created: ID={task.task_id}, title='{task.title}'")

# In complete_task():
logger.info(f"Task completed: ID={task_id}")

# In delete_task():
logger.info(f"Task deleted: ID={task_id}")
```

This allows developers to monitor task operations and trace errors in production.
