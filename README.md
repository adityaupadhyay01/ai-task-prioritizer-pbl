# AI Task Prioritizer

A modern web application that intelligently prioritizes tasks based on **importance** and **deadline urgency**.
The system helps users organize their workload by calculating a **priority score** and generating an **AI-like suggested task order**.

This project demonstrates a **full-stack web workflow** using **Python (Flask), HTML, CSS, and JavaScript** with a modern SaaS-style interface.

---

# 🚀 Features

### Intelligent Task Prioritization

The application calculates a **priority score** for each task based on:

* Task Importance (High / Medium / Low)
* Deadline Urgency (days remaining)

Tasks are automatically sorted in the **optimal execution order**.

---

### AI-Like Smart Suggestions

Each task includes an explanation such as:

* *Very urgent and highly important*
* *High importance task*
* *Deadline is very close*

This makes the system behave like a **decision-support assistant**.

---

### Dynamic Task Generation

Users can specify **how many tasks they want to add**, and the system dynamically generates input cards for each task.

---

### Modern SaaS UI

The interface is inspired by modern productivity tools like:

* Linear
* Notion
* Vercel

UI Features include:

* Dark mode dashboard
* Smooth hover animations
* Gradient action buttons
* Card-style layout
* Priority badges

---

### Smart Deadline Validation

* Past deadlines cannot be selected
* Backend validation prevents invalid submissions

---

### Local Storage Persistence

Tasks are stored in the browser using **localStorage**, so they remain visible even after page refresh.

---

### Task Management

Users can:

* Add multiple tasks
* Delete tasks instantly
* Modify tasks before prioritizing

---

# 🧠 Priority Calculation Logic

Priority score is computed using:

```
Priority Score = Importance Weight + Urgency Score
```

### Importance Weights

| Importance | Weight |
| ---------- | ------ |
| High       | 3      |
| Medium     | 2      |
| Low        | 1      |

### Urgency Score

| Days Remaining | Score |
| -------------- | ----- |
| ≤ 2 days       | 3     |
| ≤ 5 days       | 2     |

> 5 days | 1 |

The system sorts tasks in **descending order of priority score**.

---

# 🏗 Project Structure

```
AI-Task-Prioritizer
│
├── app.py
├── utils.py
├── requirements.txt
│
├── templates
│   ├── index.html
│   └── result.html
│
├── static
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙️ Technologies Used

Backend

* Python
* Flask

Frontend

* HTML
* CSS
* JavaScript

Design

* Inter font
* Modern dark SaaS UI
* CSS animations and gradients

---

# ▶️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/yourusername/ai-task-prioritizer.git
cd ai-task-prioritizer
```

### 2. Install dependencies

```
pip install flask
```

or

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

# 💡 Example Usage

User inputs:

```
Task: Exam Preparation
Deadline: 2026-03-15
Importance: High
```

System output:

```
1. Exam Preparation — Score 6
Reason: Very urgent and highly important
```

---

# 🔮 Future Improvements

Potential upgrades for production-level development:

* User authentication
* Database integration (SQLite / PostgreSQL)
* Task completion tracking
* Calendar view
* Notification reminders
* Analytics dashboard
* Mobile responsive UI
* API endpoints for mobile apps

---

# 🎯 Purpose of the Project

This project demonstrates how **rule-based AI decision logic** can be combined with **modern web technologies** to build a productivity tool that helps users manage their tasks efficiently.

---

# 📄 License

This project is open-source and available for educational and learning purposes.
