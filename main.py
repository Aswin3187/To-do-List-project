import os
import json

FILE_NAME = 'todo_list.json'

# Initialize file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file)

initialize_file()

# Add a task
def add_task():
    task = input("Enter a task: ")
    with open(FILE_NAME, 'r+') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
        tasks.append({"task": task, "completed": False})
        file.seek(0)
        file.truncate()
        json.dump(tasks, file)
    print(f"Task '{task}' added.")

# View tasks
def view_tasks():
    with open(FILE_NAME, 'r') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
        print("\nTo-Do List:")
        if not tasks:
            print("No tasks found.")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} [{status}]")

# Mark task as complete
def mark_task_complete():
    view_tasks()
    task_num = int(input("Enter the task number to mark as complete: "))
    with open(FILE_NAME, 'r+') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            file.seek(0)
            file.truncate()
            json.dump(tasks, file)
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")

# Delete a task
def delete_task():
    view_tasks()
    task_num = int(input("Enter the task number to delete: "))
    with open(FILE_NAME, 'r+') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
        if 0 < task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            file.seek(0)
            file.truncate()
            json.dump(tasks, file)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")

# Menu
def menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
