# Product Backlog

## Project: Python Task Manager App

---

## User Stories

### US-001 | User Registration
**As a** new user,
**I want to** register an account,
**So that** I can save and manage my tasks securely.

- **Priority:** High
- **Story Points:** 3
- **Acceptance Criteria:**
  - User can register with username, email, and password
  - System validates email format and password length (min 8 chars)
  - Success message shown after registration
  - Duplicate email registration is rejected

---

### US-002 | User Login
**As a** registered user,
**I want to** log in to my account,
**So that** I can access my personal task list.

- **Priority:** High
- **Story Points:** 3
- **Acceptance Criteria:**
  - User can log in with email and password
  - Invalid credentials show an error message
  - Successful login redirects to the task dashboard

---

### US-003 | Create a Task
**As a** logged-in user,
**I want to** create a new task,
**So that** I can track things I need to do.

- **Priority:** High
- **Story Points:** 2
- **Acceptance Criteria:**
  - User can enter a task title and optional description
  - Task is saved and appears in the task list
  - Task creation timestamp is recorded

---

### US-004 | View All Tasks
**As a** logged-in user,
**I want to** view all my tasks in a list,
**So that** I can see what needs to be done.

- **Priority:** High
- **Story Points:** 2
- **Acceptance Criteria:**
  - All tasks are listed with title, status, and due date
  - Tasks are sorted by creation date by default
  - Empty state message shown when no tasks exist

---

### US-005 | Mark Task as Complete
**As a** logged-in user,
**I want to** mark a task as complete,
**So that** I can track my progress.

- **Priority:** High
- **Story Points:** 1
- **Acceptance Criteria:**
  - User can click a checkbox or button to mark task complete
  - Completed tasks show a visual distinction
  - Completion timestamp is recorded

---

### US-006 | Delete a Task
**As a** logged-in user,
**I want to** delete a task,
**So that** I can remove tasks I no longer need.

- **Priority:** Medium
- **Story Points:** 1
- **Acceptance Criteria:**
  - User can delete a task with a delete button
  - Confirmation prompt before deletion
  - Task is removed from the list immediately

---

### US-007 | Edit a Task
**As a** logged-in user,
**I want to** edit a task's title or description,
**So that** I can update task details as they change.

- **Priority:** Medium
- **Story Points:** 2
- **Acceptance Criteria:**
  - User can click edit on any task
  - Title and description fields are pre-filled
  - Changes are saved and reflected in the task list

---

### US-008 | Set Task Due Date
**As a** logged-in user,
**I want to** set a due date on a task,
**So that** I know when things need to be finished.

- **Priority:** Medium
- **Story Points:** 2
- **Acceptance Criteria:**
  - User can pick a due date via date picker
  - Overdue tasks are highlighted in red
  - Tasks can be sorted by due date

---

### US-009 | Filter Tasks by Status
**As a** logged-in user,
**I want to** filter tasks by status (pending/completed),
**So that** I can focus on what is not done yet.

- **Priority:** Medium
- **Story Points:** 2
- **Acceptance Criteria:**
  - Filter buttons for All, Pending, Completed
  - Task list updates instantly when filter is applied
  - Active filter is highlighted

---

### US-010 | Search Tasks
**As a** logged-in user,
**I want to** search tasks by keyword,
**So that** I can quickly find a specific task.

- **Priority:** Low
- **Story Points:** 3
- **Acceptance Criteria:**
  - Search bar filters tasks in real time
  - Search matches task title and description
  - No results message if nothing matches

---

## Backlog Summary

| ID     | Story                  | Priority | Points |
|--------|------------------------|----------|--------|
| US-001 | User Registration      | High     | 3      |
| US-002 | User Login             | High     | 3      |
| US-003 | Create a Task          | High     | 2      |
| US-004 | View All Tasks         | High     | 2      |
| US-005 | Mark Task as Complete  | High     | 1      |
| US-006 | Delete a Task          | Medium   | 1      |
| US-007 | Edit a Task            | Medium   | 2      |
| US-008 | Set Task Due Date      | Medium   | 2      |
| US-009 | Filter Tasks by Status | Medium   | 2      |
| US-010 | Search Tasks           | Low      | 3      |

**Total Story Points:** 21
