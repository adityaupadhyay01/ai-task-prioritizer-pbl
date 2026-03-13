from flask import Flask, render_template, request
from utils import importance_weight, urgency_score, priority_score

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        tasks = request.form.getlist("task[]")
        deadlines = request.form.getlist("deadline[]")
        importances = request.form.getlist("importance[]")

        results = []

        for i in range(len(tasks)):

            iw = importance_weight(importances[i])
            us = urgency_score(deadlines[i])
            score = priority_score(iw, us)

            results.append((tasks[i], score))

        results.sort(key=lambda x: x[1], reverse=True)

        return render_template("result.html", results=results)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)