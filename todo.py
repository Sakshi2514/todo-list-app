# To-Do List Application (Console-Based)
# File: todo.py

TASK_FILE = "tasks.txt"

# -----------------------------
# Load tasks from file
# -----------------------------
def load_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # If file doesn't exist, return empty list
    return tasks


# -----------------------------
# Save tasks to file
# -----------------------------
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# -----------------------------
# Show all tasks
# -----------------------------
def view_tasks(tasks):
    print("\n----- Your To-Do List -----")
    if not tasks:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("---------------------------\n")


# -----------------------------
# Add a new task
# -----------------------------
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!\n")
    else:
        print("Empty task cannot be added.\n")


# -----------------------------
# Remove task
# -----------------------------
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# -----------------------------
# Main Menu Loop
# -----------------------------
def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("===========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
if __name__ == "__main__":
    main()
