# # Prompt for a single task
# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

#     # Process the task based on priority and time sensitivity
# reminder = f"Reminder: '{task}' is a "
# match priority:
#     case 'high':
#         reminder += "high priority task"
#     case 'medium':
#         reminder += "medium priority task"
#     case 'low':
#         reminder += "low priority task"
#     case _:
#         reminder = "Invalid priority entered. Please enter high, medium, or low."
#         print(reminder)

# if time_bound == 'yes':
#     reminder += " that requires immediate attention today!"
# elif time_bound == 'no':
#     reminder += ". Consider completing it when you have free time."
# else:
#     reminder = "Invalid time-bound entry. Please enter yes or no."
#     print(reminder)

#     # Provide a customized reminder
# print(reminder)
# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity

match priority:
    case 'high':
        priority = "high"
    case 'medium':
        priority = "medium"
    case 'low':
        priority = "low"
    case _:
        reminder = "Invalid priority entered. Please enter high, medium, or low."
        print(reminder)

if time_bound == 'yes':
    time = "that requires immediate attention today!"
elif time_bound == 'no':
    time = ". Consider completing it when you have free time."
else:
    reminder = "Invalid time-bound entry. Please enter yes or no."
    print(reminder)

    # Provide a customized reminder
print(f"Reminder: '{task}' is a {priority} priority task ,{time}")
