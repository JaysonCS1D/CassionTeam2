# Risk Register

## Project: Python Task Manager App

---

## Risk Scoring Guide

| Likelihood | Score | Impact | Score |
|------------|-------|--------|-------|
| Low        | 1     | Low    | 1     |
| Medium     | 2     | Medium | 2     |
| High       | 3     | High   | 3     |

**Risk Score = Likelihood x Impact**

---

## Risk Register Table

| ID   | Risk Description                                   | Likelihood | Impact | Score | Mitigation Plan                                           | Owner    | Status |
|------|----------------------------------------------------|------------|--------|-------|-----------------------------------------------------------|----------|--------|
| R-01 | Team member unavailable due to illness             | 2          | 3      | 6     | Cross-train team; redistribute tasks during standup       | Member A | Open   |
| R-02 | Scope creep from added features mid-sprint         | 3          | 2      | 6     | Strict sprint planning; new items go to backlog           | Member A | Open   |
| R-03 | Database corruption or data loss                   | 1          | 3      | 3     | Regular backups; use version-controlled migrations        | Member B | Open   |
| R-04 | Integration issues between frontend and backend    | 2          | 2      | 4     | Define API contracts early; integration tests in CI       | Member C | Open   |
| R-05 | Deployment failure on target platform              | 2          | 3      | 6     | Test deployment in staging before production              | Member D | Open   |
| R-06 | Security vulnerability in user authentication      | 2          | 3      | 6     | Use hashed passwords (bcrypt); follow OWASP guidelines    | Member B | Open   |
| R-07 | Low test coverage leads to undetected bugs         | 2          | 2      | 4     | Set minimum 80% code coverage; enforce in CI              | Member D | Open   |
| R-08 | Third-party library deprecation or breaking change | 1          | 2      | 2     | Pin dependency versions; review changelogs before updates | Member B | Open   |
| R-09 | Plaintext passwords stored                         | 1          | 3      | 3     | Use bcrypt hashing before any auth is built               | Member B | Open   |
| R-10 | Sensitive config values in source code             | 2          | 3      | 6     | Use environment variables and .gitignore                  | Member B | Open   |

---

## Risk Level Key

| Score Range | Level  |
|-------------|--------|
| 7 - 9       | High   |
| 4 - 6       | Medium |
| 1 - 3       | Low    |
