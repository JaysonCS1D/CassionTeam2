# Defect Log

## Project: Python Task Manager App

---

## Defect Log Table

| ID     | Title                        | Severity | Found By | Date Found | Status |
|--------|------------------------------|----------|----------|------------|--------|
| BUG-01 | Empty title accepted as task | High     | Member B | 2026-04-24 | Closed |

---

## BUG-01 — Empty title accepted as task

- **Severity:** High
- **Found By:** Member B (during unit testing)
- **Date Found:** 2026-04-24
- **Date Fixed:** 2026-04-24
- **Fixed By:** Member B

**Description:**
The add_task() method in TaskManager did not validate the task title input.
An empty string or whitespace-only string was accepted and stored as a valid task,
causing data integrity issues.

**Steps to Reproduce:**
1. Create a TaskManager instance
2. Call manager.add_task("") or manager.add_task("   ")
3. Observe that a task is created without raising an error

**Expected Behavior:**
A ValueError should be raised when the title is empty or contains only whitespace.

**Actual Behavior:**
No error raised; invalid task stored in the system.

**Fix Applied:**
```python
if not title or not title.strip():
    raise ValueError("Task title cannot be empty.")
```

**Verification:**
Unit tests test_add_task_empty_title_raises and test_add_task_whitespace_title_raises both pass.
All 15 unit tests pass after fix.

**Status:** Closed
