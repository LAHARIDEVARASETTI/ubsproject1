import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file into a list."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save the list of tasks to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all the tasks."""
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Invalid input, task not added.")

def mark_done(tasks):
    """Mark a task as done by deleting it from the list."""
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a specific task from the list."""
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to handle the menu and user input."""
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
