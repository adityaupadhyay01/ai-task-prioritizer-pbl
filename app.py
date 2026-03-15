from flask import Flask, render_template, request
from utils import importance_weight, urgency_score, priority_score
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        tasks = request.form.getlist("task[]")
        deadlines = request.form.getlist("deadline[]")
        importances = request.form.getlist("importance[]")

        results = []

        for i in range(len(tasks)):

            today = datetime.today().date()
            deadline = datetime.strptime(deadlines[i], "%Y-%m-%d").date()

            # Past date validation
            if deadline < today:
                results.append((tasks[i], 0, "Invalid deadline (past date)"))
                continue

            iw = importance_weight(importances[i])
            us = urgency_score(deadlines[i])
            score = priority_score(iw, us)

            # Smart suggestion logic
            if iw == 3 and us == 3:
                reason = "Very urgent and highly important"
            elif iw == 3:
                reason = "High importance task"
            elif us == 3:
                reason = "Deadline is very close"
            else:
                reason = "Lower urgency task"

            results.append((tasks[i], score, reason))

        # Sort by score
        results.sort(key=lambda x: x[1], reverse=True)

        return render_template("result.html", results=results)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)