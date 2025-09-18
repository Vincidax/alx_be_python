task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
sensitivity = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if sensitivity == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif sensitivity == 'no':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    
    case "medium":
        if sensitivity == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif sensitivity == 'no':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    
    case "low":
        if sensitivity == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif sensitivity == 'no':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")