TASK_TIME_PROMPT = "Time Spent (minutes): "


def task_minutes():
    """Prompt user for task time and return user input"""
    while True:
        time_input = input(TASK_TIME_PROMPT)
        if not time_input.isdigit():
            print("Error: Please provide a numeric value\n")
            continue
        return time_input

