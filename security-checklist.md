# Security Checklist

## Project: Python Task Manager App

---

## 1. Input Validation (2 Places)

Input validation prevents bad or malicious data from entering the system.

### Place 1 — Task Title Validation
File: src/task_manager.py

```python
if not title or not title.strip():
    raise ValueError("Task title cannot be empty.")
```
- Rejects empty strings and whitespace-only titles
- Prevents blank or meaningless data from being stored
- Tested by: test_add_task_empty_title_raises, test_add_task_whitespace_title_raises

### Place 2 — Due Date Format Validation
File: src/task_manager.py

```python
if due_date:
    try:
        datetime.fromisoformat(due_date)
    except ValueError:
        raise ValueError("due_date must be a valid ISO format date string (YYYY-MM-DD).")
```
- Rejects invalid date strings like "not-a-date" or "31/12/2026"
- Prevents runtime crashes from bad date formats
- Tested by: demo.py validation demo section

---

## 2. Basic Authentication

- Passwords must be hashed before storage using bcrypt
- Never store plaintext passwords
- Planned implementation uses bcrypt.hashpw() and bcrypt.checkpw()
- Login attempts should be rate-limited to prevent brute force attacks

Status: Planned for v1.0

---

## 3. Protected Sensitive Values

- Secret keys, API tokens, and database credentials are never hardcoded in source code
- All sensitive values stored in environment variables using a .env file
- The .env file is listed in .gitignore and never committed to GitHub

Example .env file (never committed):
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///tasks.db
```

Loading safely in code:
```python
import os
SECRET_KEY = os.environ.get("SECRET_KEY")
```

---

## 4. Dependency Audit

Run the following commands to check for known vulnerabilities:

```bash
pip install pip-audit
pip-audit
```

Audit Result (May 2026):
- No known vulnerabilities found in current dependencies
- Dependencies: flask, pytest, pytest-cov
- All packages pinned to specific versions in requirements.txt

---

## 5. Security Risks in Risk Register

The following security risks are documented in docs/risk-register.md:

| ID   | Risk                                   | Score |
|------|----------------------------------------|-------|
| R-06 | Security vulnerability in auth         | 6     |
| R-09 | Plaintext passwords stored             | 3     |
| R-10 | Sensitive config values in source code | 6     |

---

## Security Checklist Summary

| Item                            | Status   |
|---------------------------------|----------|
| Input validation — title        | Done     |
| Input validation — due date     | Done     |
| Password hashing plan           | Planned  |
| Sensitive values in env vars    | Done     |
| Dependency audit run            | Done     |
| Security risks in risk register | Done     |
