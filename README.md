According to the [requirement](https://roadmap.sh/projects/task-tracker), this project is for simple task management in CLI.

# Usage - Example
```zsh
# Adding a new task
./task-cli add "Buy groceries"

# Updating and deleting tasks
./task-cli update 1 "Buy groceries and cook dinner"
./task-cli delete 1

# Marking a task as in progress or done
./task-cli mark-in-progress 1
./task-cli mark-done 1

# Listing all tasks
./task-cli list

# Listing tasks by status
./task-cli list done
./task-cli list todo
./task-cli list deleted
./task-cli list in-progress
```
