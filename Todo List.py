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
    print("\n" + "Your tasks: " + "\n")
    for task in todolist:
        print(task)

#Function allowing the user to add new tasks
def addtask():
    newtask = input("Enter a task: ")
    todolist.append(newtask)
    savetasks()
    print("Task Added!" + "\n")

#Function allowing the user to delete thier chosen task
def deletetask():
     tasknum = int(input("Enter the task number you'd like to remove: "))
     todolist.pop(tasknum - 1)
     savetasks()
     print("Task has been deleted!")

#To ensure the app reopens with saved tasks from the past session
loadtasks()

#While and if loops to ensure the app runs until the user prompts to quit, and so python can run commands based on user's inputs
userinput = ""
while userinput != "4":
    print("\n" + "Singh's Todo List" + "\n")
    print("Enter 1 to show all tasks" + "\n" + "Enter 2 to add a new task" + "\n" + "Enter 3 to delete a task" + "\n" + "Enter 4 to quit the app")

    userinput = input("Enter a number: ")

    if (userinput == "1"):
        showtasks()
    elif (userinput == "2"):
        addtask()
    elif (userinput == "3"):
        deletetask()
    elif (userinput == "4"):
        print("See you again!:)")
    else:
        print("Invalid input, please choose from the options below")