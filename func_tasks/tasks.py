import os
from dotenv import load_dotenv

load_dotenv()

data_path = ".task/taskchampion.sqlite3"
cmd3 = "task list"

# - As a user, I want to be able to create task
def create_tasks():
    print('------------------CREATED TASKS-----------------')
    test_plan_tasks=[ 
        "task add Requirement gathering",
        "task add Test Planning",
        "task add Test case creation or development",
        "task add Test environment setup",
        "task add Test execution",
        "task add Test report",
        "task add Test closure"
    ]
    
    try: 
        for x in test_plan_tasks:
            os.system(x)
    except:
        print("Something went wrong")
    

# As a user, I want to be able to group task
def group_task():
    print('-----------------GROUP THE TASKS----------------')
    group_1 = [
        "task 1 modify project:phase_one",
        "task 2 modify project:phase_one",
        "task 3 modify project:phase_one"
    ]

    group_2 = [
        "task 4 modify project:phase_two",
        "task 5 modify project:phase_two"    
    ]

    group_3 = [
        "task 6 modify project:phase_three",
        "task 7 modify project:phase_three"
    ]

    group_total = group_1 + group_2 + group_3

    try: 
        for x in group_total:
            os.system(x)
    except:
        print("Something went wrong")

# - As a user, I want to be able to priorities task
def task_priority():
    print('----------------PRIORITISE TASK-----------------')
    task_priority = "task 1 modify priority:H"
    
    try:
        os.system(task_priority)
    except:
        print("Something went wrong")

# - As a user, I want to be able to add dependency from task to task
def task_dependency():
    print('-------------------TASK DEPENDENCY--------------')
    dep_1 = [
        "task 5 modify depends:4",
        "task 6 modify depends:5"
    ]

    try:
        for x in dep_1:
            os.system(x)
    except:
        print("Something went wrong")

# - As a user, I want to be able to add due date to my task
def task_delivery():
    print('-------------------TASK DELIVERY----------------')
    due_date = [
        "task 1 modify due:Monday",
        "task 2 modify due:Tuesday",
        "task 3 modify due:Tuesday",
        "task 4 modify due:Thursday",
        "task 5 modify due:Thursday",
        "task 6 modify due:Friday",
        "task 7 modify due:Friday",
    ]

    try:
        for x in due_date:
            os.system(x)
    except:
        print("Something went wrong")

# - As a user, I want to be able to see a list of my task
def list_task():
    print('-------------------LIST TASK--------------------')
    
    try:
        os.system(cmd3)
    except:
        print("Something went wrong")

# - As a user, I want to be able to see the number of my pending task
def task_count():
    print('----------------COUNT PENDING TASK--------------')

    try:
        os.system("task status:pending count")
    except:
        print("Something went wrong")
    
# -  As a user, I want to be able to mark done task
def task_done():
    print('-------------------TASK DONE--------------------')
    task_done = [
        "task 1 done",
        "task 2 done",
        "task 3 done",
        "task 4 done"
    ]
    
    try:
        for x in task_done:
            os.system(x)
        os.system("task 5 done",)
        os.system("task 6 done",)
        os.system("task 7 done",)
    except:
        print("Something went wrong")

def print_list_task():
    list_task()

def print_count_task():
    task_count()

# delete data file
def delete_data_file():
    if os.path.exists(data_path):
        os.remove(data_path)
    else:
        print("Data file does not exist")