# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate and immediately print reminder using the expected format
match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task.", end="")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task.", end="")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task.", end="")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority level.", end="")

# Add time-bound note
if time_bound == "yes":
    print(" This task requires immediate attention today!")
else:
    print(" Consider completing it when you have free time.")
print()
