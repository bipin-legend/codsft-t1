import hashlib
import random
import time


class SecretTask:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed


class UnusualToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        new_task = SecretTask(task_id, description)
        self.tasks.append(new_task)
        print(f'New task added with ID {task_id}: {description}')

    def view_tasks(self):
        print("\n--- Unusual To-Do List ---")
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f'{task.task_id}. {task.description} - Status: {status}')

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                print(f'Task {task_id} marked as completed.')
                return
        print(f'Task with ID {task_id} not found.')

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f'Task {task_id} removed.')
                return
        print(f'Task with ID {task_id} not found.')

def simple_main():
    todo_list = UnusualToDoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to remove: "))
            todo_list.remove_task(task_id)
        elif choice == '5':
            print("Exiting the Unusual To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    simple_main()
