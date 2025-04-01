import json
import datetime

class Task:
    id_counter = 0


    def __init__(self, name, date, status):
        Task.id_counter += 1
        self.id = Task.id_counter
        self.name = name
        self.date = date
        self.status = status



tasks = []  
check_point = True


def create_task(name, date, status):
    tasks.append(Task(name, date, status))
    print("Task created successfully")

def display_task():
    if len(tasks) == 0:
        print("There are no tasks created")
    for x in tasks:
        status_text = "Completed" if x.status else "Pending"
        print(f"{x.id}: {x.name} (Date created: {x.date} - {status_text})")

def update_task(id, name):
    task_id = int(id)
    for x in tasks:
        if x.id == task_id:
            x.name = name
            print("Updated")
            return
    print("Item Not Found ")


def delete_task(id, tasks_arr):
    global tasks
    task_id = int(id)
    tasks_arr = [task for task in tasks if task.id != task_id]
    display_task()

while check_point:
    display_task()

    print("\n<1. Create>")
    print("<2. Delete>")
    print("<3. Update>")
    print("<4. Complete Task>")

    task_options = input("\nWhat would you like to do?")

    if task_options == "1":
        print("Create a Task")
        task_name = input("Enter Task ")
        task_date = datetime.datetime.now().strftime("%d:%m:%Y")
        create_task(task_name, task_date, False)

    elif task_options == "2":
        task_del = input("Enter the number/id of the Task to delete")
        delete_task(task_del, tasks)

    elif task_options == "3":
        task_update_id = input("Enter the number/id of the Task to update")
        task_update_name = input("Enter the new name of the Task to update")
        update_task(task_update_id, task_update_name)

    else:
        task_completed = input("Enter the number/id of the Task you have completed")
        for x in tasks:
            if x.id == int(task_completed):
                x.status = True

    

    

    check = input("Would you like to continue(Y/N)")
    if check.upper() != "Y":
        check_point = False






