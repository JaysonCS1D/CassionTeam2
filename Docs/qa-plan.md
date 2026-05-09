# QA Plan

## Project: Python Task Manager App

---

## 1. Objectives

- Ensure all features meet acceptance criteria
- Catch and fix bugs before release
- Maintain code quality through automated testing
- Achieve minimum 80% test coverage

---

## 2. Test Types

### Unit Testing
- **Tool:** Pytest
- **Scope:** Individual functions and methods in isolation
- **Who:** Developers write tests alongside code
- **When:** Before merging any feature branch

### Integration Testing
- **Tool:** Pytest with fixtures
- **Scope:** Interaction between modules (e.g., database + task logic)
- **Who:** QA Engineer (Member D)
- **When:** After unit tests pass; before deployment

---

## 3. Test Environment

| Environment | Purpose             | Details                  |
|-------------|---------------------|--------------------------|
| Local       | Developer testing   | Each developer's machine |
| CI          | Automated testing   | GitHub Actions pipeline  |
| Staging     | Pre-release testing | Mirror of production     |

---

## 4. Test Coverage Goals

| Area       | Minimum Coverage |
|------------|------------------|
| Core logic | 90%              |
| API/routes | 80%              |
| Utilities  | 75%              |
| Overall    | 80%              |

---

## 5. Entry and Exit Criteria

### Entry Criteria (before testing begins)
- Feature code is complete and committed
- Code has been peer-reviewed
- Unit tests written by developer

### Exit Criteria (before release)
- All unit tests pass
- All integration tests pass
- No critical or high bugs open
- Coverage threshold met

---

## 6. Defect Management

- All bugs logged in docs/defect-log.md
- Severity levels: Critical, High, Medium, Low
- Bugs fixed in same sprint if Critical or High
- Retested after fix; status updated in defect log

---

## 7. Test Schedule

| Activity            | Timing                     |
|---------------------|----------------------------|
| Write unit tests    | During feature development |
| Run unit tests      | On every commit (CI)       |
| Integration tests   | End of each sprint         |
| Regression testing  | Before each release        |
