task_variable = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match task_priority:
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
            print(task_variable + "is a " + task_priority + " priority task that can wait.")
        else:
            print(task_variable + " is a " + task_priority + " priority task. Consider completing it when you have free time.")
