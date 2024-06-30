# daily_reminder.py

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    reminder = f"Reminder: '{task}' is a "

    match priority:
        case 'high':
            reminder += "high priority task"
        case 'medium':
            reminder += "medium priority task"
        case 'low':
            reminder += "low priority task"
        case _:
            reminder = "Invalid priority entered. Please enter high, medium, or low."
            print(reminder)
            return

    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"
    elif time_bound == 'no':
        reminder += ". Consider completing it when you have free time."
    else:
        reminder = "Invalid time-bound entry. Please enter yes or no."
        print(reminder)
        return

    # Provide a customized reminder
    print(reminder)

if __name__ == "__main__":
    main()
