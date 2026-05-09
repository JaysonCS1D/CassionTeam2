# KPIs and Metrics

## Project: Python Task Manager App

---

## What is a KPI?

A Key Performance Indicator (KPI) is a measurable value that shows
how well the project is achieving its goals.

---

## 5 KPIs Defined

### KPI-1 — Test Pass Rate
- **Definition:** Percentage of unit tests that pass on each CI run
- **Target:** 100%
- **How Measured:** Run pytest tests/ -v and count passed vs total
- **Actual Measurement:** 15 out of 15 = 100%
- **Status:** Met

---

### KPI-2 — Code Coverage
- **Definition:** Percentage of source code lines covered by tests
- **Target:** 80% or higher
- **How Measured:** Run pytest --cov=src tests/
- **Actual Measurement:** 87%
- **Status:** Met

---

### KPI-3 — Bug Fix Rate
- **Definition:** Percentage of logged bugs that have been fixed and closed
- **Target:** 100% of Critical and High bugs closed before release
- **How Measured:** Count Closed vs Total in docs/defect-log.md
- **Actual Measurement:** 1 bug logged, 1 fixed = 100%
- **Status:** Met

---

### KPI-4 — Sprint Velocity
- **Definition:** Number of story points completed per sprint
- **Target:** 10 or more points per sprint
- **How Measured:** Sum story points of all completed stories in sprint
- **Actual Measurement:** Sprint 1 completed 11 story points
- **Status:** Met

---

### KPI-5 — Deployment Success Rate
- **Definition:** Percentage of deployments that succeed without rollback
- **Target:** 90% or higher
- **How Measured:** Count successful deploys vs total deploy attempts
- **Actual Measurement:** 1 attempted, 1 succeeded = 100%
- **Status:** Met

---

## KPI Summary Table

| KPI | Name                   | Target    | Actual  | Status |
|-----|------------------------|-----------|---------|--------|
| 1   | Test Pass Rate         | 100%      | 100%    | Met    |
| 2   | Code Coverage          | >= 80%    | 87%     | Met    |
| 3   | Bug Fix Rate           | 100%      | 100%    | Met    |
| 4   | Sprint Velocity        | >= 10 pts | 11 pts  | Met    |
| 5   | Deployment Success     | >= 90%    | 100%    | Met    |

All 5 KPIs are met or exceeded for v1.0.
