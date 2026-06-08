from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Title: ").strip()
            description = input("Description (optional): ").strip()
            due_date = input("Due date (YYYY-MM-DD): ").strip()
            ok, msg = add_task(title, description, due_date)
            print(msg)
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue
            for i, t in enumerate(tasks, 1):
                status = "✓" if t.get("completed") else " "
                print(f"{i}. [{status}] {t['title']} (due: {t['due_date']})")
            idx = input("Enter task number to mark complete: ")
            try:
                num = int(idx)
            except ValueError:
                print("Invalid number.")
                continue
            ok, msg = mark_task_as_complete(num)
            print(msg)
        elif choice == "3":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks. Great job!")
            else:
                for i, t in enumerate(pending, 1):
                    print(f"{i}. {t['title']} - due {t['due_date']}\n   {t['description']}")
        elif choice == "4":
            prog = calculate_progress()
            print(f"Progress: {prog}%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
