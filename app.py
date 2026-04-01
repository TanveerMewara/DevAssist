from flask import Flask, render_template, request, redirect
from task_manager import load_tasks, add_task, mark_complete, delete_task
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "add":
            task = request.form.get("task")
            deadline = request.form.get("deadline")

            if task and deadline:
                add_task(task, deadline)

        elif action == "complete":
            index = int(request.form.get("index"))
            mark_complete(index)

        elif action == "delete":
            index = int(request.form.get("index"))
            delete_task(index)

        return redirect("/")

    tasks = load_tasks()

    # 🔍 SEARCH FEATURE
    search_query = request.args.get("search")
    if search_query:
        tasks = [t for t in tasks if search_query.lower() in t.get("task", "").lower()]

    # 📊 STATS
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get("completed"))
    pending = total - completed

    # ⏰ OVERDUE CHECK
    today = datetime.today().date()
    for t in tasks:
        try:
            deadline = datetime.strptime(t.get("deadline", ""), "%Y-%m-%d").date()
            t["overdue"] = deadline < today and not t.get("completed")
        except:
            t["overdue"] = False

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        search_query=search_query
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)