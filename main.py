from task_manager import add_task, view_tasks, mark_complete, delete_task, show_pending_tasks, show_completed_tasks
from notes import add_note, view_notes, search_notes, edit_note, delete_note
from file_search import search_files
from colorama import Fore, Style, init

init(autoreset=True)

def print_header():
    print(Fore.CYAN + "=" * 40)
    print(Fore.CYAN + "        DEVASSIST CLI")
    print(Fore.CYAN + "=" * 40)

def print_menu():
        print(Fore.YELLOW + "\n[  TASKS  ]")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")

        print(Fore.YELLOW + "\n[  NOTES  ]")
        print("5. Add Note")
        print("6. View Notes")
        print("7. Search Notes")
        print("9. Edit Note")
        print("10. Delete Note")

        print(Fore.YELLOW + "\n[  TOOLS  ]")
        print("8. Search Files")

        print(Fore.YELLOW + "\n[  FILTERS  ]")
        print("11. Show Pending Tasks")
        print("12. Show Completed Tasks")

        print(Fore.RED + "13. Exit")

def main():
    while True:
        print_header()
        print_menu()

        choice = input(Fore.CYAN + "\nEnter your choice > ").strip()

        print(Fore.MAGENTA + "\n" + "-" * 40)

        if choice == "1":
            task = input("Enter task: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            add_task(task, deadline)
            print(Fore.GREEN + "✔ Task added successfully!")

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            try:
                num = int(input("Enter task number:"))
                mark_complete(num)
                print(Fore.GREEN + "✔ Task marked complete!")
            except:
                print(Fore.RED + "Invalid input! Please enter a number.")

        elif choice == "4":
            try:
                num = int(input("Enter task number:"))
                delete_task(num)
                print(Fore.GREEN + "✔ Task deleted!")
            except:
                print(Fore.RED + "Invalid input! Please enter a number.")

        elif choice =="5":
            note = input("Enter note:")
            add_note(note)
            print(Fore.GREEN + "✔ Note added!")

        elif choice =="6":
            view_notes()

        elif choice =="7":
            keyword = input("Enter keyword:")
            search_notes(keyword)

        elif choice =="8":
            keyword = input("Enter file name or keyword: ")
            path = input("Enter folder path: ")
            search_files(keyword, path)

        elif choice == "9":
            try:
                view_notes()
                idx = int(input("Enter note number to edit: "))
                new_text = input("Enter new note text: ")
                edit_note(idx, new_text)
                print(Fore.GREEN + "✔ Note updated!")
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter a valid number.")

        elif choice == "10":
            try:
                view_notes()
                idx = int(input("Enter note number to delete: "))
                delete_note(idx)
                print(Fore.GREEN + "✔ Note deleted!")
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter a valid number.")

        elif choice == "11":
            show_pending_tasks()

        elif choice == "12":
            show_completed_tasks()

        elif choice == "13":
            print(Fore.RED + "Exiting DevAssist...")
            break

        else:
            print(Fore.RED + "Invalid choice. Try again.") 

if __name__ == "__main__":
    main()      
    
