from datetime import datetime
import json

class Issues:
    def add(description):
        pass
        log("added", task_id)

    def mv(task_id, description):
        pass
        log("updated", task_id)

    def rm(task_id):
        pass
        log("deleted", task_id)

    def mark(task_id, status):
        if status == "done":
            pass
        else: # case: in-progress
            pass
        log(f"marked {status}", task_id)
    
    def ls(status):
        if status == "todo":
            pass
        elif status == "in-progress":
            pass
        else:
            pass

class Task:
    def __init__(self, description, task_id):
        self.id = task_id
        self.description = description
        self.status = "todo"
        self.createAt = now()
        self.updateAt = now()

def now():
    return datetime.now().strftime("%H-%M-%S")

def log(change, task_id):
    print(f"Task {change} (ID: {task_id})")
