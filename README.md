AI Task Prioritizer (PBL)

AI Task Prioritizer is a simple rule-based AI prototype that helps users decide which task should be completed first based on importance and deadline urgency.
This project was developed as part of a B.Tech 1st Year Project Based Learning (PBL) assignment.

---

Problem Statement

Students often struggle to manage multiple tasks such as assignments, exams, and projects.
Without a clear prioritization system, important tasks may be delayed or missed.

This project provides a basic AI assistant that analyzes task details and automatically ranks tasks by priority.

---

Objective

- Design a simple AI-based task prioritization assistant
- Implement rule-based decision logic
- Help users organize and prioritize tasks efficiently
- Demonstrate basic Artificial Intelligence concepts

---

AI Logic Used

The system uses Rule-Based Artificial Intelligence.

Importance Weight

Importance| Weight
High| 3
Medium| 2
Low| 1

Urgency Score (based on deadline)

Days Remaining| Urgency Score
1–2 days| 3
3–5 days| 2
More than 5 days| 1

Final Priority Score

Priority Score = Importance Weight + Urgency Score

Tasks with higher scores are given higher priority.

---

Example

Task: Exam Preparation
Importance: High
Deadline: 2 days

Importance Weight = 3
Urgency Score = 3

Final Priority Score = 6

This task will appear at the top of the priority list.

---

Technologies Used

- Python
- datetime module
- VS Code

---

Project Structure

ai-task-prioritizer-pbl
│
├── main.py        # Main program (task input & output)
├── utils.py       # AI logic and scoring functions
├── test_cases.txt # Sample test inputs
├── README.md      # Project documentation

---

Features

- Accepts multiple tasks from the user
- Calculates urgency based on deadline
- Converts importance into weighted values
- Automatically ranks tasks by priority
- Beginner-friendly AI prototype

---

How to Run the Project

1. Clone the repository

git clone https://github.com/adityaupadhyay01/ai-task-prioritizer-pbl.git

2. Navigate to the project folder

cd ai-task-prioritizer-pbl

3. Run the program

python main.py

---

Future Improvements

- Graphical User Interface (GUI)
- Web-based version
- Task reminders and notifications
- Machine Learning based prioritization

---

Author

Aditya Upadhyay
B.Tech CSE – PBL Project