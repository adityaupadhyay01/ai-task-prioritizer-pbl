# 🚀 AI Task Prioritizer

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=flat-square)
![UI](https://img.shields.io/badge/UI-Dark%20SaaS%20Style-purple?style=flat-square)
![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)

A **modern web-based task prioritization system** that intelligently ranks tasks using **importance and deadline urgency**.
Designed with a **premium SaaS-style UI**, the application helps users organize their workflow and determine which tasks should be completed first.

The project combines **Python (Flask) backend logic** with a **modern dark dashboard interface** inspired by productivity tools like **Notion, Linear, and Vercel**.

---

# 🌐 Live Demo

Try the application live:

🔗 https://ai-task-prioritizer-pbl.onrender.com/

Experience the AI-powered task prioritization system directly in your browser without installing anything.

---

# ✨ Key Features

### 🧠 Intelligent Task Prioritization

Automatically calculates a **priority score** for tasks based on:

* Task Importance
* Deadline Urgency

Tasks are sorted in **optimal execution order**.

---

### 🤖 Smart AI-Like Suggestions

Each task includes a reasoning message such as:

* *Very urgent and highly important*
* *High importance task*
* *Deadline is very close*

This makes the system behave like a **decision-support assistant**.

---

### 🧾 Dynamic Task Generation

Users can specify **how many tasks they want to add**, and the system dynamically generates input cards for each task.

---

### 🎨 Premium SaaS-Style Interface

The UI is designed to look like a **modern startup product**.

Features include:

* Dark mode dashboard
* Card-based layout
* Smooth hover animations
* Gradient action buttons
* Priority badges
* Clean typography

---

### 🗓 Smart Deadline Validation

The application prevents invalid inputs:

* Past dates cannot be selected
* Backend validation ensures data integrity

---

### 💾 Persistent Tasks (Local Storage)

Tasks are automatically stored in the browser using **localStorage**, allowing them to remain visible even after refreshing the page.

---

### ❌ Task Management

Users can easily:

* Add multiple tasks
* Delete tasks instantly
* Modify tasks before prioritization

---

# 🧠 Priority Calculation Logic

The system calculates a **priority score** using:

```
Priority Score = Importance Weight + Urgency Score
```

---

### Importance Weights

| Importance | Weight |
| ---------- | ------ |
| High       | 3      |
| Medium     | 2      |
| Low        | 1      |

---

### Urgency Score (based on days remaining)

| Days Remaining | Score |
| -------------- | ----- |
| ≤ 2 days       | 3     |
| ≤ 5 days       | 2     |

> 5 days | 1 |

---

Tasks are then sorted in **descending order of priority score**.

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

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### UI Design

* Inter font
* Dark SaaS dashboard
* CSS animations and gradients

---

# ▶️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/ai-task-prioritizer.git
cd ai-task-prioritizer
```

---

### 2️⃣ Install dependencies

```
pip install flask
```

or

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```
python app.py
```

---

### 4️⃣ Open in browser

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

Potential upgrades for production-level systems:

* User authentication
* Database integration (SQLite / PostgreSQL)
* Task completion tracking
* Calendar view
* Reminder notifications
* Analytics dashboard
* Mobile responsive UI
* REST API support

---

# 🎯 Project Objective

The goal of this project is to demonstrate how **rule-based AI decision logic** can be combined with **modern web development technologies** to build an intelligent productivity tool.

---

# 📄 License

This project is available for **educational and learning purposes**.
