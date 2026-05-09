# Ethics Impact Assessment

## Project: Python Task Manager App

---

## 1. Project Description

The Python Task Manager App allows users to create, manage, and track personal tasks.
It stores task titles, descriptions, due dates, and completion status.

---

## 2. Stakeholders

| Stakeholder          | Interest / Concern                                       |
|----------------------|----------------------------------------------------------|
| End Users            | Privacy of personal task data; ease of use              |
| Development Team     | Building a secure, reliable, and ethical system         |
| Academic Institution | Compliance with academic integrity policies             |
| Third-party Services | Data shared with deployment platforms (e.g., Render.com)|

---

## 3. Ethical Risks Identified

| Risk                            | Description                                                              | Mitigation                                              |
|---------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------|
| User data privacy               | Task data may contain sensitive personal information                     | Data stored locally or on secure platform; no sharing   |
| Unauthorized data access        | Another user could access tasks if authentication is not implemented     | User authentication planned for v1.0                   |
| Data loss                       | Current in-memory storage loses all data on restart                      | Persistent SQLite storage planned for v1.0             |
| Over-collection of data         | Collecting more data than necessary                                      | Only collect title, description, due date, and status  |
| Algorithmic bias                | Not applicable for this task management application                      | N/A                                                     |

---

## 4. Ethical Principles Applied

- **Transparency:** Users know what data is stored and why
- **Data Minimization:** Only necessary data is collected; no tracking or analytics
- **Security:** Input validation and planned authentication protect user data
- **Fairness:** App is equally usable by all users; no discriminatory logic
- **Accountability:** Team members are assigned ownership of risks and issues

---

## 5. Conclusion

The Task Manager App poses low ethical risk. The main concern is user data privacy,
which will be addressed through user authentication and persistent secure storage
in future versions. All current data handling is transparent and minimal.
