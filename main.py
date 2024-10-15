from sys import argv
from lib import issues

# todo: handle errors
script, action, description = argv

if action == "add":
    Issues.add(description)
elif action == "update":
    Issues.mv(task_id, description)
elif action == "delete":
    Issues.rm(task_id)
elif action == "mark-in-progress":
    Issues.mark(task_id, "in progress")
elif action == "mark-done":
    Issues.mark(task_id, "done")
elif action == "list":
    status = description
    Issues.ls(status)
else:
    print("Invalid action, re-type please!")
