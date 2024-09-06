import json
import datetime
import sys

path_name = "tasks.json"


class Tasks:
    def __init__(self, description, status="todo", createdAt=None, updatedAt=None):
        self.description = description
        self.status = status
        self.createdAt = createdAt or datetime.datetime.now().strftime("%b/%m/%Y")
        self.updatedAt = updatedAt or datetime.datetime.now().strftime("%b/%m/%Y")
    
    def to_dict(self, task_id):
        return {
            "id": task_id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

def load_file():
    try:
        with open(path_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_file(data):
    with open(path_name, 'w') as f:
        json.dump(data, f, indent=4)

def add_task(task):
    jsonTasks = load_file()  # Load current tasks from file
    jsonTasks.append(task)
    write_file(jsonTasks)

def updateTask(task_id, newDesc, status):
    jsonTasks = load_file()  # Always load the file before modifying
    found = False
    for task in jsonTasks:
        if task["id"] == task_id:
            if(status == "description"):
                task["description"] = newDesc
                task["updatedAt"] = datetime.datetime.now().strftime("%b/%m/%Y")  # Update timestamp
                write_file(jsonTasks)
                print("Task updated")
                found = True
                break
            else:
                task["status"] = newDesc
                task["updatedAt"] = datetime.datetime.now().strftime("%b/%m/%Y")  # Update timestamp
                write_file(jsonTasks)
                print("Task updated")
                found = True
                break
    if not found:
        print(f"Task with id {task_id} not found.")

def deleteTask(task_id):
    jsonTasks = load_file()  # Load current tasks from file
    found = False
    for task in jsonTasks:
        if task["id"] == task_id:
            jsonTasks.remove(task)
            write_file(jsonTasks)
            print(f"Task with id {task_id} deleted successfully.")
            found = True
            break
    if not found:
        print(f"Task with id {task_id} not found.")

def main():
    operations = ["add", "update", "delete", "mark", "list"]
    jsonTasks = load_file()  # Initialize with loaded tasks

    # Determine next available ID
    if jsonTasks:
        next_id = max(task['id'] for task in jsonTasks) + 1
    else:
        next_id = 1

    if (sys.argv[1] not in operations):
        print("Invalid command. Enter (add, update, delete, mark, list)")
    else:
        match sys.argv[1]:
            case 'add':
                task = Tasks(sys.argv[2]).to_dict(next_id)
                add_task(task)
            case 'update':
                updateTask(int(sys.argv[2]), sys.argv[3], "description")
            case 'delete':
                deleteTask(int(sys.argv[2]))
            case 'mark':
                status = sys.argv[2]
                if(status == 'done' or status == 'todo' or status == 'in-progress'):
                    updateTask(int(sys.argv[3]), sys.argv[2], "status")
                else:
                    print("Improper status")
            case 'list':
                if(len(sys.argv) == 3):
                    for task in jsonTasks:
                        if (task['status'] == sys.argv[2]):
                            print(f"{task['id']}: {task['description']} = {task['status']}")
                elif(len(sys.argv) == 2):
                            for task in jsonTasks:
                                print(f"{task['id']}: {task['description']} = {task['status']}")

if __name__ == "__main__":
    main()
