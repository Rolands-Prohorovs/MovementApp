tasks = []
def show_menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
def view_tasks():
    if tasks:
        print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    else:
        print("No tasks available.")
def remove_task():
    view_tasks()
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

show_menu()
add_task()