task_variable = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(task_variable + " is a " + task_priority + " priority task that requires immediate attention today!")
        else:
            print(task_variable + " is a " + task_priority + " priority task that requires attention soon.")
    case "medium":
        if time_bound == "yes":
            print(task_variable + " is a " + task_priority + " priority task that requires immediate attention!")
        else:
            print(task_variable + " is a " + task_priority + " priority task that requires attention soon.")
    case "low":
        if time_bound == "yes":
            print(task_variable + "is a " + task_priority + " priority task that requires immediate attention later!.")
        else:
            print(task_variable + " is a " + task_priority + " priority task. Consider completing it when you have free time.")
