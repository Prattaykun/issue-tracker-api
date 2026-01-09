

```md
# Issue Tracker API

A backend Issue Tracker system built using **FastAPI** and **PostgreSQL**.  
The application supports issue management, comments, bulk operations, CSV imports, and reporting with transactional safety and optimistic concurrency control.

---

## 🚀 Features

- Create, update, and manage issues
- Optimistic concurrency control using versioning
- Add comments to issues with validation
- Transactional bulk status updates
- CSV import for bulk issue creation
- Aggregated reports (top assignees)
- Interactive API documentation (Swagger UI)

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Server:** Uvicorn
- **Language:** Python 3.10+

---

## 📁 Project Structure

```

issue-tracker-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│   └── routers/
│       ├── issues.py
│       └── reports.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt

````

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd issue-tracker-api
````

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/issue_tracker
```

---

## 🗄️ Database Setup

Create database in PostgreSQL:

```sql
CREATE DATABASE issue_tracker;
```

Tables are auto-created on application startup.

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Testing

### Create a User (manual)

```sql
INSERT INTO users (name) VALUES ('Test User');
```

### Example: Create Issue

```json
{
  "title": "Login Bug",
  "description": "Login fails with wrong password",
  "assignee_id": 1
}
```

### Example: Update Issue (with versioning)

```json
{
  "status": "in_progress",
  "version": 1
}
```

### Example: Add Comment

```json
{
  "body": "This issue needs urgent fixing",
  "author_id": 1
}
```

---

## 🔒 Concurrency Control

* Each issue contains a `version` field
* Updates require matching version
* Mismatch results in **409 Conflict**

---

## 🔄 Transactions

* Bulk status updates are atomic
* Any failure triggers a rollback

---

## 📊 Reports

### Top Assignees

```
GET /reports/top-assignees
```

Returns users with the highest number of assigned issues.

---

## ✅ Assignment Coverage

| Requirement        | Status |
| ------------------ | ------ |
| CRUD operations    | ✅      |
| Optimistic locking | ✅      |
| Comments           | ✅      |
| Transactions       | ✅      |
| CSV Import         | ✅      |
| Reports            | ✅      |
| Swagger docs       | ✅      |

---

## 📌 Future Enhancements

* Issue listing with pagination
* Label management
* Timeline endpoint
* Automated tests

---

## 👤 Author

**Prattay Roy Chowdhury**
Backend Developer – FastAPI & PostgreSQL

````

---

## ✅ What you should do next

1. Save `.gitignore` and `README.md`
2. Run:
   ```bash
   git status
````

3. Ensure `venv/` and `.env` are **NOT listed**
4. Commit:

   ```bash
   git add .
   git commit -m "Initial FastAPI Issue Tracker backend"
   ```

