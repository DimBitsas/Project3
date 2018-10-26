from dates_handler import get_user_date
from log_csv import write_csv
TASK_NAME_PROMPT = "\nTitle of the task: "
TASK_TIME_PROMPT = "\nTime spent (minutes): "
TASK_NOTES_PROMPT = "\nNotes (Optional, you can leave this empty): "
ENTRY_ADDED = "\nThe entry has been add. Press enter to return to main menu\n"


class Task:
    def __init__(self):
        self.date = get_user_date()
        self.name = input(TASK_NAME_PROMPT)
        while True:
            time_input = input(TASK_TIME_PROMPT)
            if not time_input.isdigit():
                print("Error: Please provide a numeric value\n")
                continue
            self.time = time_input
            break
        self.notes = input(TASK_NOTES_PROMPT)
        write_csv(self.date, self.name, self.time, self.notes)
        input(ENTRY_ADDED)


