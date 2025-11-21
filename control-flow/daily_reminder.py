task = input("Enter your task: ")


while True:
    priority = input("priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("please enter a valid priority: high, medium, or low.")

        time_bound = input("Is it time-bound? (yes/no): ").lower()

        immediate = time_bound == "yes"
        
match priority:
    case "high":
        if immediate:
            print(f"Reminder: '{task}' is a high-priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if immediate:
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!") 
        else:
            print(f"Note: '{task}' is a medium priority task. Schedule time to complete it soon.")
    case "low":
        if immediate:
           print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
           print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")  
