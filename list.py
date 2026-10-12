
tasks = []

while True:
    print("\n----- TODO APP -----")
    print("1. Add an item")
    print("2. Delete an item at index")
    print("3. Remove the last item")
    print("4. Sort the list")
    print("5. Print the list")
    print("6. Exit the app")

    option = input("Choose an option: ")

    if option == "1":
        while True:
            task = input("Enter a task (-1 to go back): ")

            if task == "-1":
                break

            tasks.append(task)
            print("Task added!")

    elif option == "2":
        print("Your tasks:", tasks)

        if len(tasks) == 0:
            print("The list is empty.")
        else:
            index_input = input("Enter index to delete: ")

            if index_input.isdigit():
                index = int(index_input)

                if index < len(tasks):
                    del tasks[index]
                    print("Updated list:", tasks)
                else:
                    print("Invalid index!")
            else:
                print("Please enter a valid number!")

    elif option == "3":
        if len(tasks) > 0:
            tasks.pop()
            print("Updated list:", tasks)
        else:
            print("The list is empty.")
    elif option == "4":
        tasks.sort()
        print("Sorted list:", tasks)
    elif option == "5":
        print("Your tasks:", tasks)
    elif option == "6":
        print("Exiting Todo App. Goodbye!")
        break
    else:
        print("Invalid option! Choose from 1 to 6.")
