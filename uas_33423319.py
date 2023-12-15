# File: main_program.py

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})

def view_tasks():
    print("\nCurrent Tasks:")
    for i, task_info in enumerate(tasks, start=1):
        status = "Done" if task_info["done"] else "Pending"
        print(f"{i}. {task_info['task']} ({status})")

def mark_task_as_done():
    task_index = int(input("Enter the task index to mark as done: "))
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task index.")

def calculate_golden_ratio():
    result = 1.618033988749895
    print(f"Golden Ratio: {result}")

def main():
    while True:
        print("\nMenu:")
        print("1. tambah tugas")
        print("2. lihat tugas")
        print("3. tandai tugas sudah selesai")
        print("4. menghitung Golden Ratio")
        print("5. keluar")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_as_done()
        elif choice == '4':
            calculate_golden_ratio()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
