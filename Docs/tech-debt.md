# Technical Debt Register

## Project: Python Task Manager App

---

## What is Technical Debt?

Technical debt refers to shortcuts or suboptimal decisions made during development
that need to be addressed later. Ignoring technical debt leads to slower development,
more bugs, and harder-to-maintain code.

---

## Technical Debt Items

### TD-001 — In-Memory Storage (No Persistence)
- **Description:** All tasks are stored in a Python dictionary in memory. Data is lost when the app restarts.
- **Impact:** High — users lose all data on every restart
- **Effort to Fix:** Medium
- **Plan:** Replace in-memory storage with SQLite using Python's built-in sqlite3 module

### TD-002 — No Input Sanitization Beyond Title Validation
- **Description:** Only task title was validated originally. Other fields had no validation.
- **Impact:** Medium — invalid data could be stored silently
- **Effort to Fix:** Low
- **Plan:** Add validation functions for all input fields

### TD-003 — No Logging System
- **Description:** The app had no logging. Errors and events were not recorded anywhere.
- **Impact:** Medium — debugging production issues is very difficult without logs
- **Effort to Fix:** Low
- **Plan:** Integrate Python's logging module for key events

### TD-004 — No User Authentication
- **Description:** There is no login system. All tasks belong to a single unnamed user.
- **Impact:** High — cannot be used as a multi-user system
- **Effort to Fix:** High
- **Plan:** Implement user registration and login with hashed passwords using bcrypt

### TD-005 — Hardcoded Task ID Counter
- **Description:** The _next_id counter in TaskManager resets on every restart.
- **Impact:** Medium — will cause ID collisions when database is introduced
- **Effort to Fix:** Low
- **Plan:** Use database-generated auto-increment IDs or UUIDs

---

## Debt Fixed This Sprint

### TD-002 — Input Validation and TD-003 — Logging

**Why selected:** Low effort, high impact on data integrity and observability.

**Changes made:**
- Added ValueError for empty or whitespace-only task titles
- Added ValueError for invalid due date format
- Added Python logging for task create, complete, and delete operations

**Before:**
```python
def add_task(self, title, description="", due_date=None):
    task = Task(self._next_id, title, description, due_date)
```

**After:**
```python
def add_task(self, title, description="", due_date=None):
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")
    if due_date:
        try:
            datetime.fromisoformat(due_date)
        except ValueError:
            raise ValueError("due_date must be a valid ISO format date string (YYYY-MM-DD).")
    task = Task(self._next_id, title.strip(), description, due_date)
    logger.info(f"Task created: ID={task.task_id}, title='{task.title}'")
```

**Status:** Fixed and tested — tagged as v0.8
