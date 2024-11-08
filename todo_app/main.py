import todo_Operation
import utils

tasks = []
print("--- To-Do List ---")
def menu():
    print("Select an operation")
    print("\n1. Add a New Task \n2. View All Tasks \n3. Delete a Task by Index \n4. Clear Screen \n5. Exit")

def main():
    while True:
        menu()
        choice = input("Please enter your choice : ")

        if choice == '1':
            task = input("Enter the new task: ")
            todo_Operation.add_task(tasks, task)
        elif choice == '2':
            todo_Operation.view_tasks(tasks)
        elif choice == '3':
            try:
                index = int(input("Enter the index of the task to delete: "))
                todo_Operation.delete_task(tasks, index)
            except ValueError:
                print("Input is invalid.")
        elif choice == '4':
            utils.clear_screen()
        elif choice == '5':
            print("Exited from the app")
            break
        else:
            print("Invalid Choice. Please select an option from above.")

if __name__ == "__main__":
    main()
