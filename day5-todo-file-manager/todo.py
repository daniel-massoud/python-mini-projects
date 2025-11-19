# To-do list with file storage

def load_tasks(file_name):
    tasks = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # Do nothing if file not found; tasks remains empty
    return tasks  # Always return tasks, whether loaded or empty

def save_tasks(tasks, file_name):
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main program:
file_name = "tasks.txt"
tasks = load_tasks(file_name)

while True:
    print("1. view tasks\n2. add task\n3. remove task\n4. exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            show_tasks(tasks)
            print("\n")
        case "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks, file_name)
            print("Task added!")
        case "3":
            show_tasks(tasks)
            task_index = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                save_tasks(tasks, file_name)  # Save the updated tasks list, not the removed_task
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        case "4":
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")
