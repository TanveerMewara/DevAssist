import json
import os 
from datetime import datetime

FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "tasks.json"))

def load_tasks():
    try:
        with open(FILE_PATH,"r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return[]
    except:
        return[]

def save_tasks(tasks):
    with open (FILE_PATH,"w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task, deadline):
    tasks = load_tasks()

    new_task = {
        "task": task,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added with deadline!")

def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return
    
    #filter only valid tasks
    valid_tasks = [t for t in tasks if isinstance(t, dict) and "deadline" in t]

    #sort only valid tasks
    valid_tasks.sort(key=lambda t: datetime.strptime(t["deadline"], "%Y-%m-%d"))
    
    for i, t in enumerate(valid_tasks, start=1):
        status = "✔" if t.get("completed") else "✘"  
        print (f"{i}. {t['task']} | Due: {t['deadline']} | {status}")

    #handle broken / old tasks
    invalid_tasks = [t for t in tasks if not isinstance(t, dict) or "deadline" not in t]

    if invalid_tasks:
        print("\n Some old tasks found (no deadline):")
        for i, t in enumerate(invalid_tasks, start=1):
            print(f"{i}. {t}")

def mark_complete(index):
    tasks = load_tasks()

    if 0 < index <= len(tasks):
        if isinstance(tasks[index - 1], dict):
            tasks[index - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Cannot mark old format task.")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()

    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)

        if isinstance(removed, dict):
            print("Deleted:", removed.get("task"))
        else:
            print("Deleted:", removed)
    else:
        print("Invalid task number.")

#show only pending task
def show_pending_tasks():
    tasks = load_tasks()

    pending = [t for t in tasks if isinstance(t, dict) and not t.get("completed", False)]

    if not pending:
        print("No pending tasks.")
        return
    
    for i, t in enumerate(pending, start=1):
        deadline = t.get("deadline", "No deadline")
        print(f"{i}. {t.get('task')} | Due: {deadline} | ✘")

#show only completed tasks
def show_completed_tasks():
    tasks = load_tasks()

    completed = [t for t in tasks if isinstance(t, dict) and t.get("completed", False)]

    if not completed:
        print("No completed tasks.")
        return 
    
    for i, t in enumerate(completed, start=1):
        deadline = t.get("deadline", "No deadline")
        print(f"{i}. {t.get('task')} | Due: {deadline} | ✔")