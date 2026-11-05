# List starts off empty
todolist = []

# To save the list in a text file even after the user quits
def savetasks():
    with open("tasks.txt", "w") as file:
        for task in todolist:
            file.write(task + "\n")

# To load all the saved tasks even after quitting, added a try method if the user opens the app for the first time with an empty text file
def loadtasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                todolist.append(line.strip())
    except FileNotFoundError:
        pass

#Function to display all the tasks added so far
def showtasks(): 
    if (len(todolist) > 0):
        print("\n" + "Your tasks: \n")
        for tasknum, task in enumerate(todolist, start=1):
                print(f"{tasknum}. {task}")
    else:
        print("Your todo list is empty!")

#Function allowing the user to add new tasks
def addtask(tasklist, newtask):
    if newtask in tasklist:
        return "duplicate"
    elif len(newtask) == 0:
        return "empty"
    tasklist.append(newtask)
    savetasks()
    return "proceed"

#Function allowing the user to delete thier chosen task, and added a try method to manage the error if the user tries to delete a task that doesn't exist or if the list is empty
def deletetask(tasklist, tasknum):
    if tasknum < 1 or tasknum > len(tasklist):
        return "invalid"
    tasklist.pop(tasknum - 1)
    savetasks()
    return "success"
    

def cleartasks():
    confirmationmessage = input("Are you sure you want to clear ALL tasks? Enter 'yes' to confirm: ")
    if confirmationmessage.lower() == "yes":
        todolist.clear()
        savetasks()
        print("All tasks have been cleared!")
    else:
        print("Clear operation cancelled. Your tasks are safe. :)")

#To ensure the app reopens with saved tasks from the past session
loadtasks()

#While and if loops to ensure the app runs until the user prompts to quit, and so python can run commands based on user's inputs
def main():
    userinput = ""
    while userinput != "5":
        print("\nSingh's Todo List\n")
        print("Enter 1 to show all tasks\n" + 
            "Enter 2 to add a new task\n" + 
            "Enter 3 to delete a task\n" + 
            "Enter 4 to clear all tasks\n" + 
            "Enter 5 to quit the app")

        userinput = input("\n" + "Enter a number: ")

        if (userinput == "1"):
            showtasks()

        elif (userinput == "2"):
            taskinput = input("Enter a task: ").strip()
            result = addtask(todolist, taskinput)
            if result == "proceed":
                print("\nTask has been added!\n")
            elif result == "empty":
                print("\nError: Task cannot be empty!\n")
            elif result == "duplicate":
                print("\nTask already exists in the list!\n")

        elif (userinput == "3"):
            try:
                deletenum = int(input("Enter the task number you'd like to remove: "))
                result = deletetask(todolist, deletenum)
                if result == "invalid":
                    print("\nError: Task does not exist or the list is empty.\n")
                elif result == "success":
                    print("\nTask has been deleted!\n")
            except ValueError:
                    print("\nError: Please enter a valid number.\n")

        elif (userinput == "4"):
            cleartasks()
        elif (userinput == "5"):
            print("See you again!:)")
        else:
            print("Invalid input, please choose from the options below:")

#To ensure the app only runs when the user runs the file directly, and not when imported as a module
if __name__ == "__main__":
    main()