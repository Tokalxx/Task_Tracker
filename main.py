import os
import json
import sys
import datetime

class Task:
    id_counter = 0


    def __init__(self, name, date, status, task_id = None):
        self.id = task_id if task_id is not None else self.get_next_id()
        self.name = name
        self.date = date
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "status": self.status
        }
    
    @staticmethod
    def get_next_id():
        tasks = read_json()
        if not tasks:
            return 1
        return max(task["id"] for task in tasks) + 1


check_point = True
file_path = "tasks.json"

# JSON Function 1 - Ensure File Path:
def ensure_file_path():
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)  

# JSON Function 1 - Write onto Json:
def write_json(data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# JSON Function 2 - Read from JSON:
def read_json():
    ensure_file_path() 
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# Method 1: Create a Task
def create_task(name):
    tasks = read_json()
    new_task = Task(name, datetime.datetime.now().strftime("%d:%m:/%Y"), "todo")
    tasks.append(new_task.to_dict())
    write_json(tasks)
    print("Task created successfully")

# Method 2 - Display all Tasks
def display_task():
    tasks = read_json()
    if len(tasks) == 0:
        print("There are no tasks created")
    for x in tasks:
        status_text = "Completed" if x["status"] else "Pending"
        print(f"{x["id"]}: {x["name"]} (Date created: {x["date"]} - {x["status"]})")

# Method 3 - Update the name of the tasks
def update_task(id, name):
    tasks = read_json()   
    task_id = int(id)
    for x in tasks:
        if x["id"] == task_id:
            x["name"] = name
            print("Updated")
            write_json(tasks)
            print("Task updated successfully")
            return
    print("Item Not Found ")

# Method 4 - delete tasks
def delete_task(id):
    tasks = read_json()
    task_id = int(id)
    tasks = [task for task in tasks if task["id"] != task_id]
    write_json(tasks)
    print("Task deleted successfully")

# Method 5 - Complete tasks
def mark_tasks(id, status):
    tasks = read_json()
    task_id = int(id)
    if status == "pending":
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = status
                write_json(tasks)
                print("Task completed")
                return
        print("Task not found")
    elif status == "complete":
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = status
                write_json(tasks)
                print("Task completed")
                return
        print("Task not found")
    elif status == "todo":
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = status
                write_json(tasks)
                print("Task completed")
                return
        print("Task not found")

# Method 6 - Filter Tasks
def filter_tasks(status):
    tasks = read_json()
    for task in tasks:
        if task["status"] == "completed" and status == "done":
            print(f"{task["id"]}: {task["name"]} (Date created: {task["date"]} - {task["status"]})")
        elif task["status"] == "todo" == status:
            print(f"{task["id"]}: {task["name"]} (Date created: {task["date"]} - {task["status"]})")
        elif task["status"] == "pending" and status == "pending":
            print(f"{task["id"]}: {task["name"]} (Date created: {task["date"]} - {task["status"]})")




def command_handle(cmd, params):
    match cmd:
        case "add":
            create_task(params[0])
        case "delete":
            delete_task(params[0])
        case "update":
            update_task(params[0], params[1])
        case "mark-done":
            mark_tasks(params[0], "complete")
        case "mark-in-progress":
            mark_tasks(params[0], "pending")
        case "list":
            if len(params) == 0:
                display_task()
            elif len(params) >= 1:
                filter_tasks(params[0])



def main():
    if len(sys.argv) < 2:
        print("Please provide a command.")
        sys.exit(1)

    command = sys.argv[1]
    params = sys.argv[2:]

    command_handle(command, params)

if __name__ == "__main__":
    main()
