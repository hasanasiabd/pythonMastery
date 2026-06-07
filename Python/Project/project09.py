# Project 9: To-Do List App

import os

FILE_NAME = "todo_list.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is empty!")
    else:
        print("\nCurrent To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"Task '{new_task}' added successfully!")
            else:
                print("Task cannot be empty!")
        elif choice == '3':
            show_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"Removed task: '{removed}'")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':
            print("Saving your tasks... Exiting. Have a productive day!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()