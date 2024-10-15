from sys import argv
import lib

# handle different counts
script, action = argv

if action == "add" or action == '1' :
    print("Task added successfully (ID: {})")
elif action == "update" or action == '2' :
    print("Task updated successfully: {}")
elif action == "delete" or action == '3' :
    print("Task deleted successfully (ID: {})")
elif action == "mark-in-progress" or action == '4' :
    print("Task marked in progress (ID: {})")
elif action == "mark-done" or action == '5' :
    print("Task marked done (ID: {})")
elif action == "list" or action == '0' :
    print("1 - {}: {}")
    print("2 - {}: {}")
    print("3 - {}: {}")
else:
    print("Invalid action, re-type please!")
