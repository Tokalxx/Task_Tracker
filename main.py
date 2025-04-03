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
def create_task(name, date, status):
    tasks = read_json()
    new_task = Task(name, date, status)
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
        print(f"{x["id"]}: {x["name"]} (Date created: {x["date"]} - {status_text})")

# Method 3 - Update the name of the tasks
def update_task(id, name):
    tasks = read_json()   
    task_id = int(id)
    for x in tasks:
        if x["id"] == task_id:
            x["name"] = name
            print("Updated")
            write_json(tasks)
            return
    print("Item Not Found ")


# Method 4 - delete tasks
def delete_task(id):
    tasks = read_json()
    task_id = int(id)
    tasks = [task for task in tasks if task["id"] != task_id]
    write_json(tasks)



while check_point:
    display_task()

    print("\n<1. Create>")
    print("<2. Delete>")
    print("<3. Update>")
    print("<4. Complete Task>")
    print("<5. Display Completed>")
    print("<6. Display Pending>")

    task_options = input("\nWhat would you like to do? ")

    if task_options == "1":
        print("Create a Task")
        task_name = input("Enter Task ")
        task_date = datetime.datetime.now().strftime("%d:%m:%Y")
        create_task(task_name, task_date, False)

    elif task_options == "2":
        task_del = input("Enter the number/id of the Task to delete ")
        delete_task(task_del)
    elif task_options == "3":
        task_update_id = input("Enter the number/id of the Task to update ")
        task_update_name = input("Enter the new name of the Task to update ")
        update_task(task_update_id, task_update_name)
    elif task_options == "4":
        task_completed = int(input("Enter the number/id of the Task you have completed "))
        tasks = read_json()
        for task in tasks:
            if task["id"]  == task_completed:
                task["status"] = True
                write_json(tasks)
    elif task_options == "5" or task_options == "6":
        tasks = read_json()
        for task in tasks:
            if task["status"] == True and task_options == "5":
                print(f"{task["id"]}: {task["name"]} (Date created: {task["date"]} - Completed)")
            else:
                print(f"{task["id"]}: {task["name"]} (Date created: {task["date"]} - Completed)")

        
        
       

    

    

    check = input("Would you like to continue(Y/N) ")
    if check.upper() != "Y":
        check_point = False






