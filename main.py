from utils import importance_weight, urgency_score, priority_score

tasks = []

n = int(input("How many tasks? "))

for _ in range(n):
    name = input("\nTask name: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    importance = input("Importance (High/Medium/Low): ")

    iw = importance_weight(importance)
    us = urgency_score(deadline)
    score = priority_score(iw, us)

    tasks.append((name, score))

tasks.sort(key=lambda x: x[1], reverse=True)

print("\n--- Priority Order ---")
for i, t in enumerate(tasks, start=1):
    print(f"{i}. {t[0]} — Score {t[1]}")
