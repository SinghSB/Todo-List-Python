from todo import addtask, deletetask

def test_add_then_delete():
    # Test adding a task
    tasklist = []
    newtask = "Test Task"
    add_result = addtask(tasklist, newtask)
    assert add_result == "proceed", f"Expected 'proceed', but got {add_result}"
    assert tasklist == ["Test Task"], f"Expected ['Test Task'], but got {tasklist}"

    # Test deleting the task
    delete_result = deletetask(tasklist, 1)
    assert delete_result == "success", f"Expected 'success', but got {delete_result}"
    assert tasklist == [], f"Expected [], but got {tasklist}"

def add_duplicate_task():
    #Test adding a duplicate task
    tasklist = ["Task 1"]
    newtask = "Task 1"
    result = addtask(tasklist, newtask)
    assert result == "duplicate", f"Expected 'duplicate', but got {result}"
    assert tasklist == ["Task 1"], f"Expected ['Task 1'], but got {tasklist}"

def add_empty_task():
    #Test adding an empty task
    tasklist = []
    newtask = ""
    result = addtask(tasklist, newtask)
    assert result == "empty", f"Expected 'empty', but got {result}"
    assert tasklist == [], f"Expected [], but got {tasklist}"

def delete_task_out_of_range():
    #Test deleting a task with an invalid index which is out of range
    tasklist = ["Task 1", "Task 2"]
    result = deletetask(tasklist, 3)
    assert result == "invalid", f"Expected 'invalid', but got {result}"
    assert tasklist == ["Task 1", "Task 2"], f"Expected ['Task 1', 'Task 2'], but got {tasklist}"

def delete_task_zero():
    #Test deleting a task with an index of 0 (which is invalid)
    tasklist = ["Task 1", "Task 2"]
    result = deletetask(tasklist, 0)
    assert result == "invalid", f"Expected 'invalid', but got {result}"
    assert tasklist == ["Task 1", "Task 2"], f"Expected ['Task 1', 'Task 2'], but got {tasklist}"

def delete_task_negative():
    #Test deleting a task with a negative index
    tasklist = ["Task 1", "Task 2"]
    result = deletetask(tasklist, -1)
    assert result == "invalid", f"Expected 'invalid', but got {result}"
    assert tasklist == ["Task 1", "Task 2"], f"Expected ['Task 1', 'Task 2'], but got {tasklist}"

def delete_task_from_empty_list():
    #Test deleting a task from an empty list
    tasklist = []
    result = deletetask(tasklist, 1)
    assert result == "invalid", f"Expected 'invalid', but got {result}"
    assert tasklist == [], f"Expected [], but got {tasklist}"