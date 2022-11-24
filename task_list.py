tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# As a user, to manage my task list I would like a program that allows me to:

# # 1. Print a list of uncompleted tasks
# # make an empty list of uncompleted tasks find those where completed == false and then add the uncompleted tasks to the uncompleted task list,  print the uncompleted task list 
def uncompleted(list_of_tasks):
    for task in list_of_tasks:
        if task["completed"] == False:
            print(task["description"])
            
uncompleted(tasks)

# # # # 2. Print a list of completed tasks
def completed(list_of_tasks):
    for task in list_of_tasks:
        if task["completed"] == True:
            print(task["description"])

completed(tasks)


# # # # 3. Print a list of all task descriptions
def task_description(list_of_tasks):
    for task in list_of_tasks:
        print(task["description"])

task_description(tasks)


# # 4. Print a list of tasks where time_taken is at least a given time
# least_time = int(input("What's the minimum amount of time you want to spend doing tasks, in munutes? "))

def time_taken(list_of_tasks, time):
    for task in list_of_tasks:
        if task["time_taken"] >= time:
            print(task["description"])

time_taken(tasks, 5)


# 5. Print any task with a given description
user_input = input("Please type a task name ")

def print_description(list_of_tasks):
    for task in list_of_tasks:
        if task["description"] == user_input:
            print(task)

print_description(tasks)