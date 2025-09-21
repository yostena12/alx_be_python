# daily_reminder.py
"""
Ask the user for a single task, its priority (high/medium/low),
and whether it is time-bound (yes/no). Print a customized reminder
that includes the task, its priority, and whether it requires
immediate attention today.
"""

def get_priority():
    while True:
        p = input("Priority (high/medium/low): ").strip().lower()
        if p in ("high", "medium", "low"):
            return p
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")

def get_time_bound():
    while True:
        tb = input("Is it time-bound? (yes/no): ").strip().lower()
        if tb in ("yes", "y"):
            return True
        if tb in ("no", "n"):
            return False
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    task = input("Enter your task: ").strip()
    while not task:
        task = input("Task cannot be empty. Enter your task: ").strip()

    priority = get_priority()
    time_bound = get_time_bound()

    # Build a priority phrase with match-case
    match priority:
        case "high":
            priority_phrase = "a high priority task"
        case "medium":
            priority_phrase = "a medium priority task"
        case "low":
            priority_phrase = "a low priority task"
        case _:
            # fallback (shouldn't happen due to validation)
            priority_phrase = "a task with an unknown priority"

    # Final messages follow your examples exactly
    if time_bound:
        print(f"\nReminder: '{task}' is {priority_phrase} that requires immediate attention today!")
    else:
        print(f"\nNote: '{task}' is {priority_phrase}. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
