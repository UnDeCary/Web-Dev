from models import TaskManager
from storage import load_tasks, save_tasks

FILENAME: str = "data.json"

def show_menu():
    print("\n=== Task Manager ===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

def show_tasks(manager: TaskManager):
    tasks = manager.list_tasks()

    if not tasks:
        print("\nNo tasks yet")
        return


    print(f"\nYour tasks:")
    for task in tasks:
        print(task)

def add_task(manager: TaskManager) -> bool:
    title = input("\nEnter task title: ").strip()

    if not title:
        print("Task title is required")
        return False

    manager.add_task(title)
    print(f"Task added: {manager.tasks[-1]}")
    return True


def complete_task(manager: TaskManager) -> bool:
    try:
        task_id = int(input("\nEnter task ID to complete: "))
    except ValueError:
        print("Invalid task id")
        return False

    if manager.complete_task(task_id):
        print(f"Task completed!")
    else:
        print(f"Task not found!")
    return True

def delete_task(manager: TaskManager) -> bool:
    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Invalid task id")
        return False

    if manager.delete_task(task_id):
        print(f"Task deleted successfully!")
    else:
        print(f"Task not found!")
    return True


def main():
    tasks = load_tasks(FILENAME)
    manager = TaskManager(tasks)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                show_tasks(manager)

            case "2":
                if add_task(manager):
                    save_tasks(FILENAME, manager.tasks)

            case "3":
                if complete_task(manager):
                    save_tasks(FILENAME, manager.tasks)

            case "4":
                if delete_task(manager):
                    save_tasks(FILENAME, manager.tasks)

            case "5":
                print("Goodbye!")
                save_tasks(FILENAME, manager.tasks)
                break

            case _:
                print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()