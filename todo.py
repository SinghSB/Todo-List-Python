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
        print("\n" + "Your tasks: " + "\n")
        for tasknum, task in enumerate(todolist, start=1):
                print(f"{tasknum}. {task}")
    else:
        print("Your todo list is empty!")

#Function allowing the user to add new tasks
def addtask():
    newtask = input("Enter a task: ")
    todolist.append(newtask)
    savetasks()
    print("Task Added!" + "\n")

#Function allowing the user to delete thier chosen task, and added a try method to manage the error if the user tries to delete a task that doesn't exist or if the list is empty
def deletetask():
    try:
        tasknum = int(input("Enter the task number you'd like to remove: "))
        if tasknum < 1 or tasknum > len(todolist):
            print("Error: Task number does not exist.")
        else:
            todolist.pop(tasknum - 1)
            print("Task has been deleted!")
        savetasks()
    except IndexError:
        print("Error: Task number does not exist or the list is empty.")
    except ValueError:
        print("Error: Please enter a valid number.")

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
userinput = ""
while userinput != "5":
    print("\n" + "Singh's Todo List" + "\n")
    print("Enter 1 to show all tasks" + "\n" + 
          "Enter 2 to add a new task" + "\n" + 
          "Enter 3 to delete a task" + "\n" + 
          "Enter 4 to clear all tasks" + "\n" + 
          "Enter 5 to quit the app")

    userinput = input("\n" + "Enter a number: ")

    if (userinput == "1"):
        showtasks()
    elif (userinput == "2"):
        addtask()
    elif (userinput == "3"):
        deletetask()
    elif (userinput == "4"):
        cleartasks()
    elif (userinput == "5"):
        print("See you again!:)")
    else:
        print("Invalid input, please choose from the options below")