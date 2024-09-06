# Task Manager

A simple Python-based task manager that allows you to create, update, delete, and list tasks using a command-line interface. Tasks are stored in a JSON file, and each task has a description, status, creation date, and update date.

## Features
- **Add Tasks**: Create new tasks with descriptions and default status "todo."
- **Update Tasks**: Modify the description or status of existing tasks.
- **Delete Tasks**: Remove tasks by their ID.
- **List Tasks**: Display tasks based on their status or list all tasks.
- **Mark Tasks**: Update the status of tasks as completed, pending, etc.

## Installation

1. Clone or download the repository.
2. Make sure you have Python 3.x installed.
3. You do not need any external libraries since it only uses the standard Python libraries (`json`, `datetime`, `sys`).

## Usage

The task manager operates via the command line. Below are the commands you can use:

### 1. Add a Task
To add a task, run the following command:
```bash
python tasks.py add "Task Description"
```
Example:
```bash
python tasks.py add "Go to the mosque"
```

### 2. Update a Task
To update the description of an existing task:
```bash
python tasks.py update <task_id> "New Description"
```
Example:
```bash
python tasks.py update 1 "Go to the mosque and meet friends"
```

### 3. Delete a Task
To delete a task by its ID:
```bash
python tasks.py delete <task_id>
```
Example:
```bash
python tasks.py delete 1
```

### 4. Mark Task (Change Status)
To change the status of a task (e.g., from "todo" to "completed"):
```bash
python tasks.py mark <status> <task_id>
```
Example:
```bash
python tasks.py mark completed 1
```

### 5. List Tasks
To list tasks by status (e.g., "todo", "completed", "in-progress"):
```bash
python tasks.py list <status>
```
Example:
```bash
python tasks.py list completed
```

You can also list all tasks regardless of their status:
```bash
python tasks.py list
```

## Task JSON Structure

Tasks are stored in a `tasks.json` file with the following structure:
```json
{
    "id": 1,
    "description": "Go to the mosque",
    "status": "todo",
    "createdAt": "Sep/06/2024",
    "updatedAt": "Sep/06/2024"
}
```

## How It Works

- **Tasks Class**: Encapsulates the task object, which includes a description, status, creation date, and update date.
- **Functions**:
  - `load_file()`: Loads tasks from the `tasks.json` file.
  - `write_file(data)`: Writes updated tasks back to the JSON file.
  - `add_task(task)`: Adds a new task to the JSON file.
  - `updateTask(task_id, newDesc, status)`: Updates the description or status of a task by its ID.
  - `deleteTask(task_id)`: Deletes a task by its ID.
  
The JSON file is updated whenever you add, update, or delete tasks.

## License

This project is open-source and free to use.

---

Now you're ready to manage your tasks from the command line with ease!

url: https://github.com/Abdulahia-39/task-cli.git
