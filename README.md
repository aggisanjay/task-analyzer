## Smart Task Analyzer 🧠

Smart Task Analyzer is a full-stack mini application that prioritizes user tasks using a weighted scoring algorithm.  
It helps users decide **what to work on first** by analyzing urgency, importance, effort, and task dependencies.

Built with:

 **Backend:** Django REST-style API
 **Frontend:** HTML, CSS, Vanilla JavaScript
 **Database:** SQLite (Django default)

## ✅ Features

- Task scoring algorithm with explainable weights
- REST API to analyze bulk tasks
- Priority-based sorting
- Client-side sorting strategies:
  - Priority Based
  - Fastest Wins
  - Deadline Driven
- Color-coded UI (Red → High, Orange → Medium, Green → Low)
- Handles real-world edge cases:
  - Overdue dates
  - Missing importance values
  - No due dates
  - Task dependencies

## 🧠 Scoring Algorithm

Every task receives a numeric **Priority Score**:

Score = Urgency + (Importance × 5) + Effort Bonus − Dependency Penalty


### 1️⃣ Urgency (Heaviest Weight)

| Due Status        | Points |
|-------------------|---------|
| Overdue           | +100 |
| Due ≤ 3 days      | +60 |
| Due ≤ 7 days      | +40 |
| Due > 7 days      | +20 |
| No due date       | +10 |

**Reason:** Missed deadlines cause the most real-world damage.


### 2️⃣ Importance

Importance × 5


| Level | Score |
|-------|--------|
| 1–10  | +5 to +50 |

If missing → default = **5**


### 3️⃣ Effort Bonus (Quick Wins)

| Estimated Hours | Bonus |
|-----------------|--------|
| ≤2 hours | +15 |
| 3–5 hours | +5 |
| >5 hours | +0 |

**Reason:** Smaller tasks improve momentum and productivity.

### 4️⃣ Dependencies

Penalty = 10 × number_of_dependencies


Blocked tasks are deprioritized because work cannot begin yet.



## 📊 Example Output

| Task | Score |
|------|--------|
| Overdue | 140 |
| Resume | 115 |
| ApplyJobs | 100 |
| No Importance Field | 60 |
| DSA Practice | 55 |
| Blocked Task | 40 |
| Someday Task | 35 |


## ⚙️ Installation & Setup

### 1️⃣ Clone Repository


git clone https://github.com/YOUR_USERNAME/task-analyzer.git

cd task-analyzer

2️⃣ Create Virtual Environment

Windows

python -m venv venv

venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

If requirements file is missing:

pip install django django-cors-headers


4️⃣ Run Database Migrations

python manage.py makemigrations

python manage.py migrate

5️⃣ Start Backend Server

python manage.py runserver

API will run at:

http://127.0.0.1:8000

6️⃣ Launch Frontend

Open directly:

frontend/index.html

Paste JSON tasks and click Analyze.

# 🔌 API Reference

POST /api/tasks/analyze/

Request:

[
  {
    "title":"Resume",
    "importance":8,
    "estimated_hours":2,
    "due_date":"2025-12-01"
  }
]

Response:

[
  {
    "title":"Resume",
    "importance":8,
    "estimated_hours":2,
    "due_date":"2025-12-01",
    "score":115
  }
]

# 🧪 Edge Case Handling

✔ Task due in the past → receives +100 urgency
✔ Missing importance → defaults to 5
✔ No due date → receives minimal urgency
✔ Blocked tasks → penalized by dependency count

## Screenshot

# Fastest wins

<img width="1298" height="1762" alt="image" src="https://github.com/user-attachments/assets/a0261d62-e077-4e94-a6da-750d11176d92" />

# Deadline Driven

<img width="1262" height="1759" alt="image" src="https://github.com/user-attachments/assets/f70cf9d3-3659-49e8-bafa-95014ca1dccb" />



🧑‍💻 Author
Sanjay Aggi
Full Stack MERN + Python Developer
